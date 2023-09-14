# Welcome to developer.digibyte.org's codebase


# **!! IMPORTANT: This documentation is currently a work-in-progress. Do not rely on it at this stage.**


Live site: [developer.digibyte.org](https://developer.digibyte.org)

Report problems or help improve the site by opening a [new
issue](https://github.com/saltedlolly/developer.digibyte.org/issues) or [pull
request](https://github.com/saltedlolly/developer.digibyte.org/compare).

## How to contribute

This repo hosts the sources for the DigiByte developer documentation. One of the
easiest ways to get started contributing is by rereading the site and looking for
inconsistencies in terminology, style, etc., and also in any illustrations.

Prior to contributing, please review the [style
guide](https://github.com/saltedlolly/developer.digibyte.org/tree/master/docs/style-guide.md).

Much of the content displayed on the is converted from Markdown to
[reStructuredText (RST)](http://docutils.sourceforge.net/rst.html) and rendered
with [Sphinx](http://www.sphinx-doc.org).

### Render the documentation locally

To render the documentation locally you first need to install Sphinx and the
required theme modules, e.g. by running

    pip install -r requirements.txt

This should be done from the root of this repo. Then you can execute Sphinx by calling

    make html

This will generate HTML from the RST sources in the directory `_build/html`.
It's all static HTML so you can just open the index.html file in your browser
locally to view the rendered documentation.

### Generation of RPC docs

The documentation of the RPC commands is automatically generated from the help
of a digibyte client with a [helper
tool](https://github.com/saltedlolly/developer.digibyte.org/tree/master/helpers/rpc).
This is the content in the [reference/rpc](reference/rpc) directory. Changes in
these files need to be done through the helper tool or at least backported to
the helper tool after doing them in this repo.

## Code of Conduct

Participation in this project is subject to a [Code of
Conduct](https://github.com/saltedlolly/developer.digibyte.org/blob/master/CODE_OF_CONDUCT.md).
