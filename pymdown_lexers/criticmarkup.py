"""Pygments lexer for critic markup."""
from pygments.lexer import RegexLexer, bygroups
from pygments import token

__all__ = ("CriticMarkupLexer",)


class CriticMarkupLexer(RegexLexer):

    """Simple lexer for CriticMarkup."""

    name = 'Critic Markup'
    aliases = ['critic-markup']
    filenames = ['*.critic-markup']
    mimetypes = ['text/critic-markup']

    tokens = {
        'root': [
            (r'(?s)(\{\+{2})(.*?)(\+{2}\})', bygroups(token.String, token.Comment, token.String)),
            (r'(?s)(\{\-{2})(.*?)(\-{2}\})', bygroups(token.String, token.Comment, token.String)),
            (r'(?s)(\{={2})(.*?)(={2}\})', bygroups(token.String, token.Comment, token.String)),
            (r'(?s)(\{>{2})(.*?)(<{2}\})', bygroups(token.String, token.Comment, token.String)),
            (
                r'(?s)(\{~{2})(.*?)(~>.)(*?)(~{2}\})',
                bygroups(token.String, token.Comment, token.String, token.String, token.Comment, token.String)
            ),
            (r' |\t', token.Whitespace),
            (r'.', token.Text)
        ]
    }
