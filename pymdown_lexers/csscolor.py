"""A Pygments lexer for hex data."""
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("CSSColorLexer",)

class CSSColorLexer(RegexLexer):

    """Simple lexer to highlight colors for coloraide."""

    name = 'csscolor'
    aliases = ['css-color']
    filenames = ['*.csscolor']

    tokens = {
        'root': [
            (
                r'([a-zA-Z][a-zA-Z\d]*)(\()(\s*)',
                bygroups(Name.Function, Generic, Whitespace),
                'function'
            ),
            (r'(#)(?:([a-fA-F0-9]{8}|[a-fA-F0-9]{6}|[a-fA-F0-9]{3,4})\b)?', bygroups(Keyword, Number)),
            (r'[a-zA-Z][-a-zA-Z0-9_]+(?!\()', Keyword.Constant),
            (r'//.+?$', Comment.Single),
            (r'/\*[\s\S]*?\*/', Comment.Multiline),
            (r'\s+', Whitespace),
        ],

        'function': [
            (r'\)', Generic, '#pop'),
            (r"([+\-])?(?:(?:([0-9]*)(\.)([0-9]+))|([0-9]+))(?:(e[-+]?[0-9]*))?(%|deg|rad|turn|grad)?",
                bygroups(
                    Generic,
                    Number,
                    Generic,
                    Number,
                    Number,
                    Number,
                    Keyword
                )
            ),
            (r'[a-zA-Z][-a-zA-Z0-9_]*(?!\()', Keyword.Constant),
            (r'[,/]', Generic),
            (r'\s+', Whitespace),
            (r'$', Generic, '#pop')
        ]
    }
