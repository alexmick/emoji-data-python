import unittest

from emoji_data_python import replace_colons


class ReplaceColonsTestCase(unittest.TestCase):
    def test_replace_colons(self):
        self.assertEqual('😄', replace_colons(':smile:'))
        self.assertEqual('😗', replace_colons(':kissing:'))

    def test_skin_tone(self):
        self.assertEqual('👋🏼', replace_colons(':wave::skin-tone-3:'))

    def test_underscore_hyphenated_codes(self):
        self.assertEqual('😙', replace_colons(':kissing_smiling_eyes:'))
        self.assertEqual('😘', replace_colons(':kissing-heart:'))

    def test_main_shortname_precedence(self):
        """There are two emoji for the family shortcode, one as the main short_name and one in the short_names_list"""
        self.assertEqual('👪', replace_colons(':family:'))

    def test_zwj_emoji(self):
        """These emoji are joined by a Zero Width Joiner"""
        self.assertEqual('👨‍👩‍👦', replace_colons(':man-woman-boy:'))
        self.assertEqual('👨‍🌾', replace_colons(':male-farmer:'))

    def test_unknown_code(self):
        self.assertEqual('💩💩 :poo:🏼', replace_colons(':hankey::poop: :poo::skin-tone-3:'))

    def test_strip_unknown_code(self):
        self.assertEqual('💩💩 🏼', replace_colons(':hankey::poop: :poo::skin-tone-3:', strip=True))

    def test_multiline_sentence(self):
        self.assertEqual("""
Hello 👋 world 🌍 !
How are you ❓""",

            replace_colons("""
Hello :wave: world :earth_africa: !
How are you :question:""")
        )

