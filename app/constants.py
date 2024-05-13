"""Constants used within the module."""
HEADING = 'heading'
LINK = 'link'
BLANK_LINE = 'blank_line'
PARAGRAPH = 'paragraph'


r"""Regex notes
. all characters except newline
\n newline
^ start of string or negate
* 0 or more
+ 1 or more
(?=...) Positive lookahead, non-capturing
(?:...) Non-capturing
(?!...) Negative lookahead, non-capturing (should not have this following)
\s whitespace
$ end of string (or end of line in multiline mode)
? after . or * makes it a lazy search instead of a greedy search.
"""
REGEX_RULES = {
    HEADING: r'^(#{1,6})(?=\s|$)(.*)(?:\n+|$)',
    LINK: r'^(.*?)\[(?!.*\] )(.+?)\]\((.*?)(?:\))(?!\))(.*)(?:\n+|$)',
    BLANK_LINE: r'^(\n)',
}