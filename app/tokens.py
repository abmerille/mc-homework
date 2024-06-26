from dataclasses import dataclass
from typing import Optional


@dataclass
class Token:
    """Represents a portion of the input string.

    Subclasses may add additional attributes.

    Public attributes:
    - raw_content: Original input string.
    """
    raw_content: str

@dataclass
class BlankLineToken(Token):
    """Represents a string containing only a new line character.

    Decided to capture blank lines in case anything was to be done later.
    It also made the matching process easier.
    """
    pass

@dataclass
class LinkToken(Token):
    """Represents a string containing the link format.

    Public attributes:
    - url: String to be mapped to href.
    - linked_text: String which will be wrapped in the anchor tag.
    - pre_text: Text which comes before the link formatted substring.
    - post_text: Text which comes after the link formatted substring.
    """
    url: str
    linked_text: str
    pre_text: str = None
    post_text: str = None

@dataclass
class HeadingToken(Token):
    """Represents a string containing the heading format.

    Public attributes:
    - level: The heading level number (integer between 1 and 6).
    - text: The heading text.
    - link_tokens: LinkToken objects if the heading has links inline.
    """
    level: int
    text: str
    link_tokens: Optional[list[LinkToken]] = None

@dataclass
class ParagraphToken(Token):
    """Represents a string containing the paragraph format.

    Since unformatted text is mapped to this token there is no associated
    regex rule to match on. Instead, a match occurs if the other regex rules 
    do not apply.

    Public attributes:
    - text: The paragraph text.
    - link_tokens: LinkToken objects if the paragraph has links inline.
    """
    text: str
    link_tokens: Optional[list[LinkToken]] = None
