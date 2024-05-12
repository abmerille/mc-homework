"""
Run local FastAPI server.

A simple server with one endpoint accepting POST requests where the body
should be JSON like
{
    "markdown": "<markdown>"
}
"""
from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

from app.html_generator import HTMLGenerator

app = FastAPI()

class MarkdownRequest(BaseModel):
    markdown: str


@app.post('/create_html/', status_code=status.HTTP_201_CREATED)
async def create_html(markdown_request: MarkdownRequest):
    """POST endpoint which expects a JSON body.

    Used JSON in the body for quick development. The trade-off is that
    newline characters (\n) need to be explicit in the passed in value.
    An area for improvement could be to look into handling large inputs
    and accept files or query parameters instead of json.
    """
    lines = markdown_request.model_dump()['markdown'].split('\n')
    html = HTMLGenerator.create_html_from_lines(lines)
    return {'response': html}
