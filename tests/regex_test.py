import re
from unittest import TestCase, main

from app.constants import REGEX_RULES

# TODO: test for unicode characters, e.g. other language and emojis

class RegexRulesTestCase(TestCase):
    """Test cases for defined regex."""
    def test_heading_good(self):
        good_cases = [
            # (value, expected)
            # (value, (group1, group2))
            ('# heading', 
             ('#', ' heading')),
            ('## heading', 
             ('##', ' heading')),
            ('### heading',
             ('###', ' heading')),
            ('#### heading', 
             ('####', ' heading')),
            ('##### heading', 
             ('#####', ' heading')),
            ('###### heading', 
             ('######', ' heading')),
            ('###### [Link text](https://www.example.com) heading', 
             ('######', ' [Link text](https://www.example.com) heading')),
        ]
        for i, (value, expected) in enumerate(good_cases):
            with self.subTest(value):
                pattern = re.compile(REGEX_RULES['heading'])
                matches_it = iter(pattern.match(value).groups())
                test_it = zip(expected, matches_it)
                
                for expected_match, match in test_it:
                    self.assertEqual(expected_match, match, f'Index {i} is wrong.')

    
    def test_link_good(self):
        good_cases = [
            # (value, expected)
            # (value, (group1, group2))
            ('[link text](https://www.example.com)', 
             ('link text', 'https://www.example.com', '')),
            ('[link text](https://www.example.com) carry on', 
             ('link text', 'https://www.example.com', ' carry on')),
        ]
        for i, (value, expected) in enumerate(good_cases):
            with self.subTest(value):
                pattern = re.compile(REGEX_RULES['link'])
                matches_it = iter(pattern.match(value).groups())
                test_it = zip(expected, matches_it)
                
                for expected_match, match in test_it:
                    self.assertEqual(expected_match, match, f'Index {i} is wrong.')



if __name__ == '__main__':
    main()
