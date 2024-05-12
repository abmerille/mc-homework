import argparse
import os
import re

from constants import BLANK_LINE, HEADING, LINK, REGEX_RULES


def generate_link(text: str) -> list:
    out = []
    link_pattern = re.compile(REGEX_RULES[LINK])
    cur_text = text
    match = link_pattern.match(cur_text)
    if match:
        while True:
            pre_text, linked_text, url, end_text = match.groups()
            out.append(pre_text)
            out.append(f'<a href={url}>{linked_text}</a>')
            match = link_pattern.match(end_text)
            if not match:
                out.append(end_text)
                break
    else:
        out.append(cur_text)

    return out


def generate_heading(matched_groups: tuple) -> list:
    heading_indicators, text = matched_groups
    out = [f'<h{len(heading_indicators)}>', ]
    out.extend(generate_link(text))
    out.append(f'</h{len(heading_indicators)}>')
    return out


def generate_paragraph(text: str) -> list:
    out = ['<p>', ]
    out.extend(generate_link(text))
    out.append('</p>')
    return out


def generate_html(lines_iter):
    lines_out = []
    for line in lines_iter:
        heading_pattern = re.compile(REGEX_RULES[HEADING])
        blank_line_pattern = re.compile(REGEX_RULES[BLANK_LINE])
        if (match := heading_pattern.match(line)):
            lines_out.extend(generate_heading(match.groups()))
        elif not (blank_line_pattern.match(line)):
            lines_out.extend(generate_paragraph(line))
    return lines_out


def file_iter(*args, **kwargs):
    with open(*args, **kwargs) as file:
        yield from file


def main(file_name: str=None, to_file: bool=False):
    if not file_name:
        file_name = 'sample1.md'
    cwd = os.getcwd()
    file_location = f'{cwd}/{file_name}'
    file = file_iter(f'{file_location}', 'r', encoding='utf-8')
    lines_out = generate_html(file)
    if to_file:
        output_file_name = f'{file_name.split('.')[0]}_output.html'
        with open(f'{output_file_name}', 'w', encoding="utf-8") as f:
            f.write(''.join(lines_out))
    else:
        print(''.join(lines_out))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown_file", help="The local file to convert to html")
    parser.add_argument("-f", "--to_file", help="Output results to file", action='store_true')
    args = parser.parse_args()

    main(args.markdown_file, to_file=args.to_file)
