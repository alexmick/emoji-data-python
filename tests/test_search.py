import unittest

from emoji_data_python import all_doublebyte, find_by_shortname, find_by_name


class SearchTestCase(unittest.TestCase):
    def test_all_double_bytes(self):
        self.assertEqual('HASH KEY', all_doublebyte()[0].name)  # HASH_KEY is the first double byte char

    def test_find_by_shortname(self):
        self.assertEqual(1, len(find_by_shortname('wave')))
        self.assertEqual('WAVING HAND SIGN', find_by_shortname('wave')[0].name)

    def test_find_by_shortname_unique(self):
        self.assertEqual(23, len(find_by_shortname('heart')))
        self.assertEqual(13, len(find_by_shortname('moon')))

    def test_find_by_name(self):
        self.assertEqual('BLACK HEART SUIT', find_by_name('heart')[0].name)
        self.assertEqual(3, len(find_by_name('earth')))
