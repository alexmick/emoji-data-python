import re
from typing import cast


def replace_colons(text: str, strip: bool = False) -> str:
    """Parses a string with colon encoded emoji and renders found emoji.
    Unknown emoji are left as is unless `strip` is set to `True`

    :param text: String of text to parse and replace
    :param strip: Whether to strip unknown codes or to leave them as `:unknown:`

    >>> emoji_data_python.replace_colons('Hello world ! :wave::skin-tone-3: :earth_africa: :exclamation:')
    'Hello world ! 👋🏼 🌍 ❗'
    """
    # pylint: disable=import-outside-toplevel
    from emoji_data_python import emoji_short_names, EmojiChar

    def emoji_repl(matchobj) -> str:
        emoji_match = matchobj.group(1)
        base_emoji = emoji_short_names.get(emoji_match.strip(":").replace("-", "_"))

        if matchobj.lastindex == 2:
            skin_tone_match = matchobj.group(2)
            skin_tone = cast(EmojiChar, emoji_short_names.get(skin_tone_match.strip(":")))

            if base_emoji is None:
                return f'{emoji_match if strip is False else ""}{skin_tone.char}'

            emoji_with_skin_tone = base_emoji.skin_variations.get(skin_tone.unified)
            if emoji_with_skin_tone is None:
                return f"{base_emoji.char}{skin_tone.char}"
            return emoji_with_skin_tone.char

        if base_emoji is None:
            return f'{emoji_match if strip is False else ""}'
        return base_emoji.char

    return re.sub(r"(\:[a-zA-Z0-9-_+]+\:)(\:skin-tone-[2-6]\:)?", emoji_repl, text)


def get_emoji_regex():
    """Returns a regex to match any emoji

    >>> emoji_data_python.get_emoji_regex().findall('Hello world ! 👋🏼 🌍 ❗')
    ['👋', '🏼', '🌍', '❗']
    """
    from emoji_data_python import emoji_data  # pylint: disable=import-outside-toplevel

    # Sort emojis by length to make sure mulit-character emojis are
    # matched first

    emojis = sorted([emoji.char for emoji in emoji_data], key=len, reverse=True)
    pattern = "(" + "|".join(re.escape(u) for u in emojis) + ")"
    return re.compile(pattern)
