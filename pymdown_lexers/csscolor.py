"""A Pygments lexer for hex data."""
from pygments.lexer import RegexLexer, bygroups
from pygments import token

__all__ = ("CSSColorLexer",)

class CSSColorLexer(RegexLexer):

    """Simple lexer to highlight colors for coloraide."""

    name = 'csscolor'
    aliases = ['css-color']
    filenames = ['*.csscolor']
    mimetypes = ['text/css-color']

    tokens = {
        'root': [
            (
                r'([a-zA-Z][a-zA-Z\d]*)(\()(\s*))',
                bygroups(token.Name.Function, token.Generic, token.Whitespace),
                'function'
            ),
            (r'(#)([a-fA-F0-9]{8}|[a-fA-F0-9]{6}|[a-fA-F0-9]{3,4})\b', bygroups(token.Keyword, token.Literal.Number)),
            (r'[a-zA-Z][-a-zA-Z0-9_]+(?!\()', token.Constant),
            (r'\s*', token.Whitespace)
        ],

        'function': [
            (r'([ \s]*)(\))', bygroups(token.Whitespace, token.Generic), '#pop'),
            (r"([+\-])?(?:(?:([0-9]*)(\.)([0-9]+))|([0-9]+))(?:(e[-+]?[0-9]*))?(%|deg|rad|turn|grad)?",
                bygroups(
                    token.Generic,
                    token.Literal.Number,
                    token.Generic,
                    token.Literal.Number,
                    token.Literal.Number,
                    token.Literal.Number,
                    token.Keyword
                )
            ),
            (r'[a-zA-Z][-a-zA-Z0-9_]+(?!\()', token.Constant),
            (r',', token.Generic),
            (r'\s*', token.Whitespace)
        ]
    }
