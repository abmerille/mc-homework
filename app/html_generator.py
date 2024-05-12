from typing import Iterable

from airium import Airium

from app.tokenizer import Tokenizer
from app.tokens import BlankLineToken, HeadingToken, Token


class HTMLGenerator:
    """
    HTMLGenerator class which converts Token objects or an iterable containing
    strings into an html string or file.

    The package Airium is used to create the html. The standard output is a
    minified version of html but can be output in a pretty format for easy reading.
    """
    def __init__(self, minify: bool = True) -> None:
        """Initiate Airium object and default to minified html.
        
        Args:
            minify: If set to False the output will be in pretty format.
        """
        self.a = Airium(source_minify=minify)

    def generate_inline_html(self, token: Token) -> None:
        """Updates Airium object with inline html.

        This function handles the case where a HeadingToken or ParagraphToken
        contain anchor tag markdown. 

        Args:
            token: root token which may contain inline tokens.
        """
        if not token.link_tokens:
            self.a(token.text)
        else:
            for link_token in token.link_tokens:
                if link_token.pre_text:
                    self.a(link_token.pre_text)
                with self.a.a(href=link_token.url):
                    self.a(link_token.linked_text)
                if link_token.post_text:
                    self.a(link_token.post_text)

    def generate_html(self, tokens: list[Token]):
        """Updates Airium object with token values.

        I split the path between a heading tag and everything else. I looked
        up some markdown generators to see the output from a line which only has
        an anchor tag and it still wrapped them in a paragraph tag. Combined with
        ignoring the blank lines it seemed the simplest path was to split on whether
        I was dealing with a heading tag.

        Args:
            tokens: All tokens to be used for html generation.
        """
        HEADER_LEVEL_MAPPING = {
            1: self.a.h1,
            2: self.a.h2,
            3: self.a.h3,
            4: self.a.h4,
            5: self.a.h5,
            6: self.a.h6,
        }
        for token in tokens:
            # Ignore blank lines for output.
            if isinstance(token, BlankLineToken):
                continue

            if isinstance(token, HeadingToken):
                airium_elem_func = HEADER_LEVEL_MAPPING[token.level]
                with airium_elem_func():
                    self.generate_inline_html(token)   
            else:
                with self.a.p():
                    self.generate_inline_html(token)

    @classmethod
    def create_html_from_lines(cls, lines_iter: Iterable, minify: bool=True) -> str:
        """Factory method to instantiate HTMLGenerator

        Since a call to create the html involved instantiating the HTMLGenerator 
        object in order to create the Airium object on the class follwoed by a call
        a call to then generate the html this classmethod allowed for a more 
        streamlined approach.
        
        Args:
            lines_iter: Lines from markdown input (can be an iterator).
            minify: Whether to output pretty or minified html.
        Returns:
            A string containing html output.
        """
        html_generator = cls(minify=minify)
        tokenizer = Tokenizer()
        tokens = []
        for line in lines_iter:
            tokens.append(tokenizer.tokenize_line(line))
        html_generator.generate_html(tokens)
        html = html_generator.get_html()
        return html
    
    def get_html(self) -> str:
        """Returns the current html.

        Originally, I was going to have a toggle in case there might be a 
        to handle unicode characters where I would use bytes(self.a). But I didn't 
        have time to dig too deep into this issue.
        """
        return str(self.a)

