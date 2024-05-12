import argparse
import os

from app.html_generator import HTMLGenerator


def file_iter(*args, **kwargs):
    with open(*args, **kwargs) as file:
        yield from file

def main(file_name: str, to_file: bool=False):
    cwd = os.getcwd()
    file_location = f'{cwd}/{file_name}'
    file_lines = file_iter(f'{file_location}', 'r', encoding='utf-8')
    html_generator = HTMLGenerator()
    lines_out = html_generator.create_html_from_lines(file_lines)
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