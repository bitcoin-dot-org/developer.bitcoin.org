This repository contains a tool to generate Bitcoin Core RPC documentation. It
requires a running `bitcoin-cli` client and puts out the documentation in
Markdown format as used on [bitcoin.org](https://github.com/saltedlolly/bitcoin.org/tree/master/_data/devdocs/en/bitcoin-core/rpcs).

Run `rpc-docs-helper` to get command line help. Run `rpc-docs-helper generate`
to generate the markdown. Run `pytest` to run the unit tests if you want to work
on the tool itself.
