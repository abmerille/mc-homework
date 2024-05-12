from unittest import TestCase, main
import os

from app.html_generator import HTMLGenerator

class RegexRulesTestCase(TestCase):
    """Test cases for defined regex."""
    def test_translate_file(self):
        cwd = os.getcwd()
        file_name = 'tests/test_files/sample1.md'
        file_location = f'{cwd}/{file_name}'
        expected_file_name = 'tests/test_files/sample1_expected.html'
        expected_file_location = f'{cwd}/{expected_file_name}'
        file_iter = (line for line in open(f'{file_location}', 'r'))
        with open(f'{expected_file_location}', 'r') as file:
            expected_file_str = file.read()
        # test_it = zip(file_iter, expected_iter)
        found_html = HTMLGenerator.create_html_from_lines(file_iter)
        self.assertEqual(expected_file_str, found_html)
        # for i, (value, expected) in enumerate(test_it):
        #     with self.subTest(value):
        #         tokenizer(line)
        #         self.assertEqual(expected, found, f'Index {i} is wrong.')
                