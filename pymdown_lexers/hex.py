"""A Pygments lexer for hex data."""
from pygments.lexer import RegexLexer, bygroups
from pygments import token

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
            (r'^([a-f\d]{8}\:)([ \t]*)', bygroups(token.String, token.Whitespace), 'address'),
            (r'^(\s*)(::.*?)$', bygroups(token.Whitespace, token.Comment.Single)),
            (r'^.+?$', token.Error),  # invalid
            (r'.+?$', token.Comment.Single)
        ],

        'address': [
            (r'([ \t]*)(?:(\:)|$)', bygroups(token.Whitespace, token.String), '#pop'),
            (r'[\da-f]{1}', token.Number, 'byte'),
            (r'[ \t]', token.Whitespace),
            (r'.+$', token.Error, '#pop')  # invalid
        ],

        'byte': [
            (r'[\da-f]{1}', token.Text, '#pop'),
            (r'.', token.Error, '#pop')  # invalid
        ]
    }
