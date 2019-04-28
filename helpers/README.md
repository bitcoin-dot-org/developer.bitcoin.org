This directory contains a small helper to convert documentation from bitcoin.org
from markdown to reStructuredText (RST). It takes the markdown sources from
https://github.com/bitcoin/bitcoin.org, runs a bit of the original Jekyll
plugins and some custom code to process it, then runs pandoc to convert
markdown to rst.

The tool `import-docs` needs to be run from the root of the repo. You have to
pass the path to a checkout of the bitcoin.org git repo.
