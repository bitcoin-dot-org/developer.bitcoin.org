Introduction
============

The Developer Reference aims to provide technical details and API information to help you start building Bitcoin-based applications, but it is `not a specification <../reference/intro.html#not-a-specification>`__. To make the best use of this documentation, you may want to install the current version of Bitcoin Core, either from `source <https://github.com/bitcoin/bitcoin>`__ or from a `pre-compiled executable <https://bitcoin.org/en/download>`__.

Questions about Bitcoin development are best asked in one of the `Bitcoin development communities <https://bitcoin.org/en/development#devcommunities>`__. Errors or suggestions related to documentation on Bitcoin.org can be `submitted as an issue <https://github.com/bitcoin-dot-org/bitcoin.org/issues>`__ or posted to the `bitcoin-documentation mailing list <https://groups.google.com/forum/#!forum/bitcoin-documentation>`__.

In the following documentation, some strings have been shortened or wrapped: “[…]” indicates extra data was removed, and lines ending in a single backslash “\\” are continued below. If you hover your mouse over a paragraph, cross-reference links will be shown in blue. If you hover over a cross-reference link, a brief definition of the term will be displayed in a tooltip.

Not A Specification
^^^^^^^^^^^^^^^^^^^



The Bitcoin.org Developer Documentation describes how Bitcoin works to help educate new Bitcoin developers, but it is not a specification—and it never will be.

Bitcoin security depends on consensus. Should your program diverge from consensus, its security is weakened or destroyed. The cause of the divergence doesn’t matter: it could be a bug in your program, it could be an `error in this documentation <https://github.com/bitcoin-dot-org/bitcoin.org/issues?q=is%3Aissue+label%3A%22Dev+Docs%22>`__ which you implemented as described, or it could be you do everything right but other software on the |network| `behaves unexpectedly <https://bitcoin.org/en/alert/2013-03-11-chain-fork>`__. The specific cause will not matter to the users of your software whose wealth is lost.

The only correct specification of consensus behavior is the actual behavior of programs on the |network| which maintain consensus. As that behavior is subject to arbitrary inputs in a large variety of unique environments, it cannot ever be fully documented here or anywhere else.

However, the Bitcoin Core developers are working on making their consensus code portable so other implementations can use it. `Bitcoin Core 0.10.0 <https://bitcoin.org/en/release/v0.10.0>`__ provided ``libbitcoinconsensus``, as the first attempt at exporting some consensus code. Future versions of Bitcoin Core also provided consensus code that is more complete, more portable, and more consistent in diverse environments.

In addition, we also warn you that this documentation has not been extensively reviewed by Bitcoin experts and so likely contains numerous errors. At the bottom of the menu on the left, you will find links that allow you to report an issue or to edit the documentation on GitHub. Please use those links if you find any errors or important missing information.
