from re import sub


def replace_colons(text: str, strip: bool=False) -> str:
    """Parses a string with colon encoded emoji and renders found emoji.
    Unknown emoji are left as is unless `strip` is set to `True`

    :param text: String of text to parse and replace
    :param strip: Whether to strip unknown codes or to leave them as `:unkown:`

    >>> emoji_data_python.replace_colons('Hello world ! :wave::skin-tone-3: :earth_africa: :exclamation:')
    'Hello world ! 👋🏼 🌍 ❗'
    """
    from emoji_data_python import emoji_short_names

    def emoji_repl(matchobj) -> str:
        match = matchobj.group(0)
        codes = match.split(':')
        res = ''
        for code in codes:
            if len(code) > 0:
                try:
                    res += emoji_short_names.get(code.replace('-', '_')).char
                except AttributeError:
                    if not strip:
                        res += f':{code}:'

        return res

    return sub(r'\:[a-zA-Z0-9-_+]+\:(\:skin-tone-[2-6]\:)?', emoji_repl, text)


