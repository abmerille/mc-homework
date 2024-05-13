# Markdown to HTML converter

## Requirements
* Docker or python 3.9+ (3.12 preferred)

## Installation
#### OPTION 1: Python via Command Line
From within the `mc-homework` directory create a virtual environment:

```sh
python -m venv <virtual_env_name>
``` 
(e.g. `python3 -m venv .venv`)

Activate the virtual environment:

```sh
source <venv>/bin/activate
```

(Or see https://docs.python.org/3/library/venv.html#how-venvs-work if not using bash/zsh terminal)

Once activated, install the required libraries with:

```sh
pip install -q --upgrade -r requirements.txt
```

After running the script or module, the virtual environment can be deactivated by typing: 

```sh
deactivate
```

#### OPTION 2: Docker and FastAPI Option
Run the following command within the top directory to create a docker image:

```sh
docker build -t <image_tag_name> .
``` 
(e.g. `docker build -t mc-homework-image .`)



## Usage
#### OPTION 1: Python via Command Line
The script requires a local markdown file. There is a `tests/test_files/` directory that can be used or anywhere in the directory is fine.

From within the `mc-homework` directory run:
```sh
python -m app <path/to/markdown_file.md>
```

The optional flag `-f` or `--to_file` can be added to output the results to a file instead of printed to the terminal. The outputted file will be named `<markdown_filename>_output.html` in the same location as the input file.

#### OPTION 2: Docker and FastAPI Option
To run FastAPI via Docker, use the same `<image_tag_name>` created during installation and run:

```sh
docker run --rm --name <container_name> -p 8000:8000 <image_tag_name>
```
(e.g. `docker run --rm --name adam_merille_craft -p 8000:8000 mc-homework-image`)

The output should show `Uvicorn running on http://0.0.0.0:8000`.

Do a POST request at `http://0.0.0.0:8000/create_html/` with a JSON request body of `{"markdown": "<markdown>"}` using curl, Postman, or FastAPI Swagger UI.

FastAPI uses Swagger UI to create interactive docs at `http://0.0.0.0:8000/docs`. This can be reached in your browser.

To use the interactive docs: 
* Click on the POST /create_html/ option.
* Click on 'Try it out` on the right.
* Replace "string" in the request example body with the markdown.
* Click execute and scroll down to see the response.

## Tests
From `mc-homework` directory run 
```sh
python -m unittest tests.regex_test
``` 

```sh
python -m unitttest tests.file_test
```

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