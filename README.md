#Markdown to HTML converter

## Requirements
Either docker or python 3.12

## Installation
#### Python via Command Line
From within the `mc-interview-homework` directory create a virtual environment:
e.g. `python -m venv .mcvenv`

Activate the virtual environment with `source <venv>/bin/activate`
(Or see https://docs.python.org/3/library/venv.html#how-venvs-work if not using bash/zsh terminal)

Once activated run `pip install -q --upgrade -r requirements.txt`

After running the script the virtal environment can be deactivated by typing `deactivate`

#### Docker and FastAPI Option
Run the following command within the top directory to create a docker image:
docker build -t <image_tag_name> .
e.g. `docker build -t mc-homework-image .`



## Usage
#### Python via Command Line
There are 2 options with the command line each with an option to write the output to a file otherwise the default is output via stdout.
Each requires creating a markdown file to be converted.

1) From within the `mc-interview-homework` directory run:
    `python -m app <path/to/markdown_file.md>`
2) From within the `app` directory run:
    `python md_to_html.py <markdown_file.md>`

The first option uses an object oriented programming approach and the second is a self contained more functional approach. The flag `-f` or `-to-file` can be added to output the results to a file. The outputed file will be `<markdown_filename>_output.html`

#### Docker and FastAPI Option
Run FastApi via Docker:
Use the same `<image_tag_name>` created during installation and run:
`docker run --rm --name <container_name> -p 8000:8000 <image_tag_name>`
e.g. `docker run --rm --name adam_merille-app -p 8000:8000 mc-homework-image`

## Tests
From mc-interview-homework directory run `python3 -m unittest tests.regex_test` for example

## Markdown Implemented

| Markdown                               | HTML                                              |
| -------------------------------------- | ------------------------------------------------- |
| `# Heading 1`                          | `<h1>Heading 1</h1>`                              | 
| `## Heading 2`                         | `<h2>Heading 2</h2>`                              | 
| `...`                                  | `...`                                             | 
| `###### Heading 6`                     | `<h6>Heading 6</h6>`                              | 
| `Unformatted text`                     | `<p>Unformatted text</p>`                         | 
| `[Link text](https://www.example.com)` | `<a href="https://www.example.com">Link text</a>` | 
| `Blank line`                           | `Ignored`                                         | 