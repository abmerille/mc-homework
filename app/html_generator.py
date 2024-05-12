from airium import Airium

from app.tokens import HeadingToken


class HTMLGenerator:

    def __init__(self) -> None:
        self.a = Airium()

    def generate_link_html(self, token):
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

    def generate_html(self, tokens):
        HEADER_LEVEL_MAPPING = {
            1: self.a.h1,
            2: self.a.h2,
            3: self.a.h3,
            4: self.a.h4,
            5: self.a.h5,
            6: self.a.h6,
        }
        for token in tokens:
            if not token:
                continue

            if isinstance(token, HeadingToken):
                airium_elem_func = HEADER_LEVEL_MAPPING[token.level]
                with airium_elem_func():
                    self.generate_link_html(token)   
            else:
                with self.a.p():
                    self.generate_link_html(token)

 
    def get_html(self):
        # return bytes(self.a)
        return str(self.a)

