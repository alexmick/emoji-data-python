import unittest

from emoji_data_python import unified_to_char, char_to_unified


class EmojiConversionTestCase(unittest.TestCase):
    def test_unified_to_char(self):
        self.assertEqual('\u261D', unified_to_char('261D'))

    def test_longer_unified(self):
        self.assertEqual('\U0001F1E6', unified_to_char('1F1E6'))

    def test_multiple_unified_to_char(self):
        self.assertEqual('👨‍🌾', unified_to_char('1F468-200D-1F33E'))
        self.assertEqual('👩🏼‍🌾', unified_to_char('1F469-1F3FC-200D-1F33E'))
        self.assertEqual('🇳🇬', unified_to_char('1F1F3-1F1EC'))
        self.assertEqual('\U0001F1F3\U0001F1EC', unified_to_char('1F1F3-1F1EC'))
        self.assertEqual('4⃣', unified_to_char('0034-20E3'))
        self.assertEqual('\u0034\u20E3', unified_to_char('0034-20E3'))

    def test_char_to_unified(self):
        self.assertEqual('261D', char_to_unified('\u261D'))

    def test_longer_char_to_unified(self):
        self.assertEqual('1F1E6', char_to_unified('\U0001F1E6'))

    def test_multiple_char_to_unified(self):
        self.assertEqual('1F469-1F3FC-200D-1F33E', char_to_unified('👩🏼‍🌾'))
        self.assertEqual('1F468-200D-1F33E', char_to_unified('👨‍🌾'))
        self.assertEqual('1F1F3-1F1EC', char_to_unified('🇳🇬'))
        self.assertEqual('1F1F3-1F1EC', char_to_unified('\U0001F1F3\U0001F1EC'))
        self.assertEqual('0034-20E3', char_to_unified('4⃣'))
