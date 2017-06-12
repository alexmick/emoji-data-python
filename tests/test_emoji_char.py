import unittest

from emoji_data_python import EmojiChar


class EmojiCharTestCase(unittest.TestCase):
    def setUp(self):
        self.emoji = EmojiChar({
            "name": "WHITE UP POINTING INDEX",
            "unified": "261D",
            "variations": [
                "261D-FE0F"
            ],
            "docomo": None,
            "au": "E4F6",
            "softbank": "E00F",
            "google": "FEB98",
            "image": "261d.png",
            "sheet_x": 1,
            "sheet_y": 2,
            "short_name": "point_up",
            "short_names": [
                "point_up"
            ],
            "text": None,
            "texts": None,
            "category": "People",
            "sort_order": 116,
            "added_in": "1.4",
            "has_img_apple": True,
            "has_img_google": True,
            "has_img_twitter": True,
            "has_img_emojione": False,
            "has_img_facebook": False,
            "has_img_messenger": False,
            "skin_variations": {
                "1F3FB": {
                    "unified": "261D-1F3FB",
                    "image": "261d-1f3fb.png",
                    "sheet_x": 1,
                    "sheet_y": 3,
                    "added_in": "6.0",
                    "has_img_apple": True,
                    "has_img_google": False,
                    "has_img_twitter": False,
                    "has_img_emojione": False,
                    "has_img_facebook": False,
                    "has_img_messenger": False
                },
            },
            "obsoletes": "ABCD-1234",
            "obsoleted_by": "5678-90EF"
        })

    def test_init(self):
        self.assertEqual("261D", self.emoji.unified)
        self.assertEqual("point_up", self.emoji.short_names[0])
        self.assertEqual("People", self.emoji.category)
        self.assertEqual("1.4", self.emoji.added_in)

    def test_skin_variations(self):
        self.assertEqual("261D-1F3FB", self.emoji.skin_variations['1F3FB'].unified)

    def test_char(self):
        self.assertEqual('☝', self.emoji.char)

    def test_all_variations(self):
        self.assertEqual(['261D', '261D-FE0F', '261D-1F3FB'], self.emoji.all_variations)

    def test_chars(self):
        self.assertEqual('☝', self.emoji.chars[0])
        self.assertEqual('☝️', self.emoji.chars[1])  # Not the same char, this is \u261D\uFE0F

    def test_doublebyte(self):
        self.assertEqual(False, self.emoji.is_doublebyte)

    def test_str(self):
        self.assertEqual('WHITE UP POINTING INDEX', self.emoji.__str__())

    def test_repr(self):
        self.assertEqual('EmojiChar("WHITE UP POINTING INDEX")', self.emoji.__repr__())

