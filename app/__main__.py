"""
Markdown to HTML module script.

This can be run using `python -m app <markdwon_file>`
An optional `--to_file` flag can be passed in which outputs the results
to a file instead of printing them to stdout.
"""

import argparse
import os

from app.html_generator import HTMLGenerator


def file_iter(*args, **kwargs):
    """Iterator for reading each line in a file
    
    Used to read a file one line at a time without loading the entire file
    into memory at once. This is to handle if the file were to be extremely 
    large. The trade-off is that it will incur more Disk I/O.

    However, it appears that it improves performance due to pipelining and 
    disk cache so while one batch is being worked on the next one is being 
    read without the blocking which would occur with a full read of the file.
    """
    with open(*args, **kwargs) as file:
        yield from file

def main(file_name: str, to_file: bool=False):
    """Module script handler."""
    cwd = os.getcwd()
    file_location = f'{cwd}/{file_name}'
    file_lines = file_iter(f'{file_location}', 'r', encoding='utf-8')
    lines_out = HTMLGenerator.create_html_from_lines(file_lines)
    if to_file:
        output_file_name = f'{file_name.split('.')[0]}_output.html'
        with open(f'{output_file_name}', 'w', encoding="utf-8") as f:
            f.write(''.join(lines_out))
    else:
        print(''.join(lines_out))



parser = argparse.ArgumentParser()
parser.add_argument("markdown_file", help="The local file to convert to html")
parser.add_argument("-f", "--to_file", help="Output results to file", action='store_true')
args = parser.parse_args()

main(args.markdown_file, to_file=args.to_file)