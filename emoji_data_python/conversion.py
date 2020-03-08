def unified_to_char(code_point: str) -> str:
    """Renders a character from its hexadecimal codepoint

    :param code_point: Character code point ex: `'261D'`

    >>> emoji_data_python.unified_to_char('1F603')
    '😃'
    """
    return "".join([chr(int(code, 16)) for code in code_point.split("-")])


def char_to_unified(chars: str) -> str:
    """Returns a characters unified codepoint

    :param chars: Emoji character ex: `'🇿🇦'`

    >>> emoji_data_python.char_to_unified('🇿🇦')
    '1F1FF-1F1E6'
    """
    return "-".join([f"{ord(char):04x}".upper() for char in chars])
