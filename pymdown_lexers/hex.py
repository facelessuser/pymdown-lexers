"""A Pygments lexer for hex data."""
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("HexLexer",)


class HexLexer(RegexLexer):

    """
    Simple lexer to highlight a specific hex format.

        00000000: 4578 616d 706c 6520 6865 7821 : Example hex!

    Byte grouping can differ from 2, and number of bytes per line can differ.
    """

    name = 'Hex'
    aliases = ['hex']
    filenames = ['*.hex']
    mimetypes = ['text/hex']

    tokens = {
        'root': [
            (r'^([a-f\d]{8}\:)([ \t]*)', bygroups(String, Whitespace), 'address'),
            (r'^(\s*)(::.*?)$', bygroups(Whitespace, Comment.Single)),
            (r'^.+?$', Error),  # invalid
            (r'.+?$', Comment.Single)
        ],

        'address': [
            (r'([ \t]*)(?:(\:)|$)', bygroups(Whitespace, String), '#pop'),
            (r'[\da-f]{1}', Number, 'byte'),
            (r'[ \t]', Whitespace),
            (r'.+$', Error, '#pop')  # invalid
        ],

        'byte': [
            (r'[\da-f]{1}', Text, '#pop'),
            (r'.', Error, '#pop')  # invalid
        ]
    }
