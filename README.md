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

Once activated run:

```sh
pip install -q --upgrade -r requirements.txt
```

After running the script the virtal environment can be deactivated by typing 

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
There are 2 options with the command line each with an option to write the output to a file otherwise the default is output via stdout.
Each requires creating a markdown file to be converted.

1) From within the `mc-homework` directory run:
    ```sh
    python -m app <path/to/markdown_filename.md>
    ```
2) From within the `app` directory run:
    ```sh
    python md_to_html.py <markdown_filename.md>
    ```

The first option uses an object oriented programming approach and the second is a self contained more functional approach. The flag `-f` or `-to-file` can be added to output the results to a file. The outputed file will be named `<markdown_filename>_output.html`

#### OPTION 2: Docker and FastAPI Option
To run FastAPI via Docker, use the same `<image_tag_name>` created during installation and run:

```sh
docker run --rm --name <container_name> -p 8000:8000 <image_tag_name>
```
(e.g. `docker run --rm --name adam_merille_craft -p 8000:8000 mc-homework-image`)

## Tests
From mc-homework directory run 
```sh
python3 -m unittest tests.regex_test
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