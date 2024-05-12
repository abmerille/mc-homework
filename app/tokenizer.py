import re

from app.constants import BLANK_LINE, HEADING, LINK, REGEX_RULES
from app.tokens import HeadingToken, LinkToken, ParagraphToken, Token


class Tokenizer:

    def tokenize_link(self, text) -> LinkToken:
        tokens = []
        link_pattern = re.compile(REGEX_RULES[LINK])
        cur_text = text
        match = link_pattern.match(cur_text)
        if match:
            while True:
                pre_text, linked_text, url, post_text = match.groups()
                match = link_pattern.match(post_text)
                if not match:
                    tokens.append(LinkToken(
                        raw_content=cur_text,
                        pre_text=pre_text,
                        linked_text=linked_text,
                        url=url,
                        post_text=post_text
                    ))
                    break
                else:
                    tokens.append(LinkToken(
                        raw_content=cur_text,
                        pre_text=pre_text,
                        linked_text=linked_text,
                        url=url
                    ))

        return tokens
    
    def tokenize_heading(self, raw_string: str, matched_groups: tuple) -> HeadingToken:
        heading_indicators, text = matched_groups
        link_tokens = self.tokenize_link(text)
        if link_tokens:
            text = ''
        heading_token = HeadingToken(
            raw_content=raw_string,
            level=len(heading_indicators),
            text=text.strip(),
            link_tokens=link_tokens
        )
        return heading_token

    def tokenize_paragraph(self, raw_string: str) -> ParagraphToken:
        text = raw_string
        link_tokens = self.tokenize_link(text)
        if link_tokens:
            text = ''
        paragraph_token = ParagraphToken(
            raw_content=raw_string,
            text=text,
            link_tokens=link_tokens
        )
        return paragraph_token

    def tokenize_line(self, line: str) -> Token:
        """
        Takes a String and converts it to a Token object.
        """
        token = None
        heading_pattern = re.compile(REGEX_RULES[HEADING])
        blank_line_pattern = re.compile(REGEX_RULES[BLANK_LINE])
        if (match := heading_pattern.match(line)):
            token = self.tokenize_heading(line, match.groups())
        elif not (blank_line_pattern.match(line)):
            token = self.tokenize_paragraph(line)

        return token
