pymdown-lexers
==================

A package created to add additional lexers for use in Pygments.  This package was created to be used in the [PyMdown project](https://github.com/facelessuser/PyMdown), but it can be used by anyone who wants to add the contained styles to Pygments.

# Overview
The purpose of this package was to natively add the lexers to Pygments via a plugin.  This was so that PyMdown could use 3rd party and native lexers without having to directly modify a Pygments installation.

The idea was to add the custom Pygments lexers here, and build a package that specifies the correct entry points.  When it is installed, the custom lexers can be used as if they were native.

I don't actually imagine many lexers will be added to this, but they are not necessary to use PyMdown.

# Included Lexers

| Lexers | Description |
|-------|-------------|
| hex | A simple lexer to parse hex data in the form `address: 00 FF 00: ascii`. |
| criticmarkup | A simple lexer used in PyMdown documents to highlight CriticMarkup in a way that stands out in plain text. |

## Adding New Lexers
To add a new lexer, the lexer must be dropped into the `pymdown_lexers` folder.  The `__init__.py` file must be updated to expose the lexer.  Lastly, `setup.py` must be modified to setup the entry points for the new lexer.
