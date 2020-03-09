from typing import Optional, List, Dict

from .conversion import unified_to_char


# pylint: disable=too-many-instance-attributes
class EmojiChar:
    """Represents an emoji character as parsed from the json data"""

    def __init__(self, data_blob: dict) -> None:
        """Parse data into EmojiChar

        :param data_blob: Dictionary of values loaded from the json format in `emoji.json`

        >>> emoji.__dict__
        {
            'name': 'BLACK HEART SUIT',
            'unified': '2665',
            'variations': ['2665-FE0F'],
            'docomo': 'E68D',
            'au': 'EAA5',
            'softbank': 'E20C',
            'google': 'FEB1A',
            'image': '2665.png',
            'sheet_x': 1,
            'sheet_y': 34,
            'short_name': 'hearts',
            'short_names': ['hearts'],
            'text': None,
            'texts': None,
            'category': 'Symbols',
            'sort_order': 245,
            'added_in': '1.1',
            'has_img_apple': True,
            'has_img_google': True,
            'has_img_twitter': True,
            'has_img_emojione': True,
            'has_img_facebook': True,
            'has_img_messenger': True,
            'skin_variations': {},
            'obsoletes': None,
            'obsoleted_by': None
        }
        """
        self.name = data_blob.get("name")  # type: Optional[str]
        self.unified = data_blob.get("unified")  # type: str
        self.variations = data_blob.get("variations", [])  # type: List[str]

        self.docomo = data_blob.get("docomo")  # type: Optional[str]
        # pylint: disable=invalid-name
        self.au = data_blob.get("au")  # type: Optional[str]
        self.softbank = data_blob.get("softbank")  # type: Optional[str]
        self.google = data_blob.get("google")  # type: Optional[str]
        self.image = data_blob.get("image")  # type: Optional[str]
        self.sheet_x = data_blob.get("sheet_x")  # type: int
        self.sheet_y = data_blob.get("sheet_y")  # type: int

        self.short_name = data_blob.get("short_name")  # type: Optional[str]
        self.short_names = data_blob.get("short_names")  # type: List[str]
        self.text = data_blob.get("text")  # type: Optional[str]
        self.texts = data_blob.get("texts")  # type: List[str]

        self.category = data_blob.get("category")  # type: Optional[str]
        self.sort_order = data_blob.get("sort_order")  # type: int
        self.added_in = data_blob.get("added_in")  # type: str

        self.has_img_apple = data_blob.get("has_img_apple")  # type: bool
        self.has_img_google = data_blob.get("has_img_google")  # type: bool
        self.has_img_twitter = data_blob.get("has_img_twitter")  # type: bool
        self.has_img_emojione = data_blob.get("has_img_emojione")  # type: bool
        self.has_img_facebook = data_blob.get("has_img_facebook")  # type: bool
        self.has_img_messenger = data_blob.get("has_img_messenger")  # type: bool

        variations = data_blob.get("skin_variations", {})
        self.skin_variations = {
            code: EmojiChar(variation) for code, variation in variations.items()
        }  # type: Dict[str, EmojiChar]

        self.obsoletes = data_blob.get("obsoletes")  # type: Optional[str]
        self.obsoleted_by = data_blob.get("obsoleted_by")  # type: Optional[str]

    @property
    def all_variations(self) -> List[str]:
        """Lists all possible codepoint variations for given emoji.

        See :mod:`emoji_data_python.EmojiChar.chars` for a rendered version

        >>> emoji.all_variations
        ['261D', '261D-FE0F', '261D-1F3FB']
        """
        return (
            [self.unified]
            + self.variations
            + [self.unified + "-" + variation for variation in self.skin_variations.keys()]
        )

    @property
    def char(self) -> str:
        """Returns rendered char for emoji

        >>> emoji.char
        '👋'
        """
        return unified_to_char(self.unified)

    @property
    def chars(self) -> List[str]:
        """Lists all possible *rendered* codepoint variations for given emoji.
        This is useful when trying to find this particular emoji in a string by looking for any variation.

        >>> emoji.chars
        ['👋', '👋🏻', '👋🏼', '👋🏽', '👋🏾', '👋🏿']
        """

        return list(map(unified_to_char, self.all_variations))

    @property
    def is_doublebyte(self) -> bool:
        """`True` if emoji is coded on two or more bytes"""
        return "-" in self.unified

    def __str__(self):
        return self.name or self.short_name or self.unified

    def __repr__(self):
        return f'EmojiChar("{self!s}")'
