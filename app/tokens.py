"""TODO
"""
from dataclasses import dataclass
from typing import Optional

from app.constants import BLANK_LINE, HEADING, LINK, PARAGRAPH


@dataclass
class Token:
    raw_content: str

@dataclass
class LinkToken(Token):
    url: str
    linked_text: str
    pre_text: str = None
    post_text: str = None

@dataclass
class HeadingToken(Token):
    level: int
    text: str
    link_tokens: Optional[list[LinkToken]] = None

@dataclass
class ParagraphToken(Token):
    text: str
    link_tokens: Optional[list[LinkToken]] = None
