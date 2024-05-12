HEADING = 'heading'
LINK = 'link'
BLANK_LINE = 'blank_line'
PARAGRAPH = 'paragraph'


r""" Regex notes
. all characters except newline
\n newline
^ start of string or negate
* 0 or more
+ 1 or more
(?=...) Positive lookahead, non-capturing
(?:...) Non-capturing
(?!...) Negative lookahead, non-capturing (should not have this following)
\s whitespace
$ end of string or end of line
? after . or * makes it lazy search instead of greedy
"""
REGEX_RULES = {
    HEADING: r'^(#{1,6})(?=\s|$)(.*)(?:\n+|$)', # Get up to 6 #s and all other text
    LINK: r'^(.*?)\[(?!.*\] )(.+?)\]\((.*?)(?:\))(?!\))(.*)(?:\n+|$)',
    BLANK_LINE: r'^(\n)', 
    # 'paragraph': r'^([^\n]+(?:\n+(?!heading|link|blank_line)[^\n])*)' #TODO not any of the others
}