import re

from app.constants import BLANK_LINE, HEADING, LINK, REGEX_RULES
from app.tokens import BlankLineToken, HeadingToken, LinkToken, ParagraphToken, Token


class Tokenizer:
    """
    Tokenizer class which converts a string into a Token object.

    This class is mostly a collection of functions which work together. It 
    provides a location where if there were going to be more markdown rules 
    the input string could be tokenized using this class.
    
    I originally had the thought that if there were a set of strings then they
    could be tokenized in parallel before needing to be synchronously put 
    together as an html document. However, I did not have time to implement 
    that.
    """
    def tokenize_blank_line(self, text: str) -> BlankLineToken:
        """Returns BlankLineToken."""
        return BlankLineToken(
            raw_content=text
        )

    def tokenize_link(self, text: str) -> list[LinkToken]:
        """Creates a list of one or more LinkTokens.
        
        Since a link exists only inline of a paragraph or heading, this 
        function always returns a list. The order of the token list returned
        is a representation of the input text.
    
        The link regex rule divides the matches into 4 groups. The last group
        could contain additional links so that is taken into account where the
        last group is passed back through the regex until exhausted.

        I chose to do a regex match on the text input within this function so 
        the caller function does not have to be concerned with link related 
        logic.

        Args:
            text: Input line string.
        Returns:
            LinkToken objects representing the input text.
        """
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
    
    def tokenize_heading(self, raw_string: str, 
                         matched_groups: tuple) -> HeadingToken:
        """Creates a HeadingToken and adds LinkeTokens if they exist.
        
        Args:
            raw_string: Text input which regex mapped to a heading.
            matched_groups: The output from a regex match function call.
        Returns:
            HeadingToken which may contain additional link tokens.
        """
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
        """Creates a ParagraphToken and adds LinkTokens if they exist.
        
        Args:
            raw_string: Text input.
        Returns:
            ParagraphToken which may contain additional link tokens.
        """
        # Remove ending new line character(s) from text.
        text = raw_string.rstrip()
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
        """Takes a string and converts it to a Token object.

        Args:
            line: Expected to be a line from markdown input.
        Returns:
            Token object which the string mapped to.
        """
        token = None
        heading_pattern = re.compile(REGEX_RULES[HEADING])
        blank_line_pattern = re.compile(REGEX_RULES[BLANK_LINE])
        blank_line_match = blank_line_pattern.match(line)
        if (match := heading_pattern.match(line)):
            token = self.tokenize_heading(line, match.groups())
        elif not (blank_line_match):
            token = self.tokenize_paragraph(line)
        else:
            token = self.tokenize_blank_line(blank_line_match.groups())

        return token
