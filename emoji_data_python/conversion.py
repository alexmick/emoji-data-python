
def unified_to_char(code_point: str) -> str:
    """Renders a character from its hexadecimal codepoint

    :param code_point: Character code point ex: `'261D'`

    >>> emoji_data_python.unified_to_char('1F603')
    '😃'
    """
    return ''.join([chr(int(code, 16)) for code in code_point.split('-')])
