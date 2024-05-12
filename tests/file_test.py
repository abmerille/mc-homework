from unittest import TestCase, main

from app.utils import tokenizer

class RegexRulesTestCase(TestCase):
    """Test cases for defined regex."""
    def test_translate_file(self):
        file_location = 'test_files/sample1.md'
        expected_file_location = 'test_files/sample1_expected.html'
        file_iter = (line for line in open(f'{file_location}', 'r'))
        expected_iter = (line for line in open(f'{expected_file_location}', 'r'))
        test_it = zip(file_iter, expected_iter)

        for i, (value, expected) in enumerate(test_it):
            with self.subTest(value):
                tokenizer(line)
                self.assertEqual(expected, found, f'Index {i} is wrong.')
                