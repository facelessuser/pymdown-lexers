"""Pygments lexer for critic markup."""
from pygments.lexer import RegexLexer
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
            (r'(?s)\{\+{2}.*?\+{2}\}', token.String),
            (r'(?s)\{\-{2}.*?\-{2}\}', token.String),
            (r'(?s)\{={2}.*?={2}\}', token.String),
            (r'(?s)\{>{2}.*?<{2}\}', token.String),
            (r'(?s)\{~{2}.*?~>.*?~{2}\}', token.String),
            (r' |\t', token.Whitespace),
            (r'.', token.Text)
        ]
    }
