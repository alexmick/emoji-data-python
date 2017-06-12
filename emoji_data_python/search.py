from typing import List

from .emoji_char import EmojiChar


def find_by_shortname(name: str) -> List[EmojiChar]:
    """Finds all emoji with `name` in their short_names

    :param name: string to find in short names

    >>> emoji_data_python.find_by_shortname('moon')
    [
        EmojiChar("NEW MOON SYMBOL"),
        EmojiChar("WAXING CRESCENT MOON SYMBOL"),
        EmojiChar("FIRST QUARTER MOON SYMBOL"),
        EmojiChar("WAXING GIBBOUS MOON SYMBOL"),
        EmojiChar("FULL MOON SYMBOL"),
        EmojiChar("WANING GIBBOUS MOON SYMBOL"),
        EmojiChar("LAST QUARTER MOON SYMBOL"),
        EmojiChar("WANING CRESCENT MOON SYMBOL"),
        EmojiChar("CRESCENT MOON"),
        EmojiChar("NEW MOON WITH FACE"),
        EmojiChar("FIRST QUARTER MOON WITH FACE"),
        EmojiChar("LAST QUARTER MOON WITH FACE"),
        EmojiChar("FULL MOON WITH FACE"),
    ]
    """
    from emoji_data_python import emoji_short_names
    name = name.replace('-', '_')
    res_list = [emoji_short_names[key] for key in emoji_short_names.keys() if name in key]
    return list(set(res_list))  # Keep only unique values


def find_by_name(name: str) -> List[EmojiChar]:
    """Finds emoji with `name` in their full name

    :param name: string to find in full names
    """
    from emoji_data_python import emoji_data
    return [emoji for emoji in emoji_data if emoji.name and name.upper() in emoji.name]


def all_doublebyte() -> List[EmojiChar]:
    """Returns all emoji coded on two or more bytes"""
    from emoji_data_python import emoji_data
    return [emoji for emoji in emoji_data if emoji.is_doublebyte]

