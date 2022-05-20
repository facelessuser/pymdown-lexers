"""
Regular expression.

https://blog.matt.wf/regex-lexer-for-pygments/
"""
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ('RegexpLexer',)


class RegexpLexer(RegexLexer):
    name = 'regex'
    aliases = ['regex']
    filenames = []

    tokens = {
        'root': [
            (r'\w+', Name),
            (r'\d+', Number),
            (r'[\s\,\:\-\"\']+', Text),
            (r'[\$\^]', Token),
            (r'[\+\*\.\?]', Operator),
            (r'(\()([\?\<\>\!\=\:]{2,3}.+?)(\))', bygroups(Keyword.Namespace, Name.Function, Keyword.Namespace)),
            (r'(\()(\?\#.+?)(\))', bygroups(Comment, Comment, Comment)),
            (r'[\(\)]', Keyword.Namespace),
            (r'[\[\]]', Name.Class),
            (r'(\\[xX])([a-fA-F0-9]{2})', bygroups(Keyword, Number)),
            (r'(\\[u])([a-fA-F0-9]{4})', bygroups(Keyword, Number)),
            (r'(\\[U])([a-fA-F0-9]{8})', bygroups(Keyword, Number)),
            (r'(?i)(\\p)(c[cfnos]?|l[clmotu]?|m[cen]?|n[dlo]?|p[cdefios]?|s[ckmo]?|z[lps]?)', bygroups(Keyword, Name)),
            (r'\\\w', Keyword),
            (r'[\{\}]', Operator),
        ],
    }
