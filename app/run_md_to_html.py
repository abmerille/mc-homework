import argparse
import os

from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

from app.tokenizer import Tokenizer
from app.html_generator import HTMLGenerator

app = FastAPI()

class MarkdownRequest(BaseModel):
    markdown: str

def create_html(lines_iter):
    for line in lines_iter:
        token_l.append(tokenizer.tokenize_line(line))
    html_generator = HTMLGenerator()
    html_generator.generate_html(token_l)
    html = html_generator.get_html()
    return html


@app.post('/create_html/', status_code=status.HTTP_201_CREATED)
async def create_todo(markdown_request: MarkdownRequest):
    tokenizer = Tokenizer()
    token_l = []
    # lines = bytes(markdown_request.model_dump()['markdown'], encoding='utf8').split(b'\n')
    lines = markdown_request.model_dump()['markdown'].split('\n')
    print(lines)
    for line in lines:
        token_l.append(tokenizer.tokenize_line(line))
    html_generator = HTMLGenerator()
    html_generator.generate_html(token_l)
    html = html_generator.get_html()
    return {'response': html}

def file_iter(*args, **kwargs):
    with open(*args, **kwargs) as file:
        yield from file


def main(file_name: str=None, to_file: bool=False):
    if not file_name:
        file_name = 'sample1.md'
    cwd = os.getcwd()
    file_location = f'{cwd}/{file_name}'
    file = file_iter(f'{file_location}', 'r', encoding='utf-8')
    lines_out = create_html(file)
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