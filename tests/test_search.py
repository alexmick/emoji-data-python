import unittest

from emoji_data_python import all_doublebyte, find_by_shortname, find_by_name, emoji_data


class SearchTestCase(unittest.TestCase):
    def test_all_emoji_length(self):
        self.assertEqual(1810, len(emoji_data))

    def test_all_double_bytes(self):
        self.assertEqual('HASH KEY', all_doublebyte()[0].name)  # HASH_KEY is the first double byte char

    def test_find_by_shortname(self):
        self.assertEqual(1, len(find_by_shortname('wave')))
        self.assertEqual('WAVING HAND SIGN', find_by_shortname('wave')[0].name)

    def test_find_by_shortname_unique(self):
        self.assertEqual(28, len(find_by_shortname('heart')))
        self.assertEqual(14, len(find_by_shortname('moon')))

    def test_find_by_name(self):
        self.assertEqual('COUPLE WITH HEART: MAN, MAN', find_by_name('heart')[0].name)
        self.assertEqual('SUNRISE OVER MOUNTAINS', find_by_name('sun')[0].name)
        self.assertEqual(3, len(find_by_name('earth')))
