from unittest import TestCase
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

        with open(f'{file_location}', 'r') as input_file:
            input_file_lines = input_file.readlines()

        with open(f'{expected_file_location}', 'r') as file:
            expected_file_str = file.read()

        found_html = HTMLGenerator.create_html_from_lines(input_file_lines)
        self.assertEqual(expected_file_str, found_html)
