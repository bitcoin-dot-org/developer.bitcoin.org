# Welcome to developer.bitcoin.org's codebase

Live site: [developer.bitcoin.org](https://developer.bitcoin.org)

Report problems or help improve the site by opening a [new
issue](https://github.com/bitcoin-dot-org/developer.bitcoin.org/issues) or [pull
request](https://github.com/bitcoin-dot-org/developer.bitcoin.org/compare).

## How to contribute

This repo hosts the sources for the Bitcoin developer documentation.

It is converted from Markdown to [reStructuredText
(RST)](http://docutils.sourceforge.net/rst.html) and rendered with
[Sphinx](http://www.sphinx-doc.org).

### Render the documentation locally

To render the documentation locally you first need to install Sphinx and the
required theme modules, e.g. by running

    pip install -r requirements.txt

from the root of this repo. Then you can execute Sphinx by calling

    make html

This will generate HTML from the RST sources in the directory `_build/html`.
It's all static HTML so you can just open the index.html file in your browser
locally to view the rendered documentation.

### Import from bitcoin.org

The RST is generated from the original Markdown sources from bitcoin.org using a
helper script, which resides in the [helpers](helpers) directory. Run the script
by calling

    helpers/import-docs <bitcoin-dot-org/bitcoin.org checkout>

with the path to a local checkout of
[bitcoin-dot-org/bitcoin.org](https://github.com/bitcoin-dot-org/bitcoin.org) as
argument. This will regenerate the RST files based on the content from the
bitcoin.org repository.

This is a temporary mechanism to port the documentation to RST. Once the import
is in a good shape and the original information is captured correctly in the
converted files, the RST files will become the original source, and the import
is not needed anymore. There is a
[milestone](https://github.com/bitcoin-documentation/website/milestone/1) to
track the necessary work to be done before detaching from the Markdown sources.

### Generation of RPC docs

The documentation of the RPC commands is automatically generated from the help
of a bitcoin client with another [helper
tool](https://github.com/cornelius/rpc-docs-helper). This is the content in the
[reference/rpc](reference/rpc) directory. Changes in these files need to be done
through the helper tool or at least backported to the helper tool after doing
them in this repo.

## Code of Conduct

Participation in this project is subject to a [Code of
Conduct](https://github.com/bitcoin-dot-org/developer.bitcoin.org/blob/master/CODE_OF_CONDUCT.md).

## Donations

This project, developer.bitcoin.org, is community supported:
[3FkenCiXpSLqD8L79intRNXUgjRoH9sjXa](bitcoin:3FkenCiXpSLqD8L79intRNXUgjRoH9sjXa)

## Questions?

Please contact Will Binns ([will@bitcoin.org](mailto:will@bitcoin.org)) if you
need help.
