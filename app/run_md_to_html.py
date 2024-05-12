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


@app.post('/create_html/', status_code=status.HTTP_201_CREATED)
async def create_html(markdown_request: MarkdownRequest):
    lines = markdown_request.model_dump()['markdown'].split('\n')
    html = HTMLGenerator.create_html_from_lines(lines)
    return {'response': html}
