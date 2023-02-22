Introduction
============

The following guide aims to provide examples to help you start building Bitcoin-based applications. To make the best use of this document, you may want to install the current version of Bitcoin Core, either from `source <https://github.com/bitcoin/bitcoin>`__ or from a `pre-compiled executable <https://bitcoin.org/en/download>`__.

Once installed, you’ll have access to three programs: ``bitcoind``, ``bitcoin-qt``, and ``bitcoin-cli``.

-  ``bitcoin-qt`` provides a combination full Bitcoin peer and wallet frontend. From the Help menu, you can access a console where you can enter the `RPC <../reference/rpc/index.html>`__ commands used throughout this document.

-  ``bitcoind`` is more useful for programming: it provides a full peer which you can interact with through `RPCs <../reference/rpc/index.html>`__ to port 8332 (or 18332 for testnet).

-  ``bitcoin-cli`` allows you to send `RPC <../reference/rpc/index.html>`__ commands to ``bitcoind`` from the command line. For example, ``bitcoin-cli help``

All three programs get settings from ``bitcoin.conf`` in the ``Bitcoin`` application directory:

-  Windows: ``%APPDATA%\Bitcoin\``

-  OSX: ``$HOME/Library/Application Support/Bitcoin/``

-  Linux: ``$HOME/.bitcoin/``

Note: ``bitcoin.conf`` may not exist at these locations. If you chose a custom location during the GUI setup it will be at this custom location. The file may also need to be created: in the custom data folder you chose, or in the locations above.

To use ``bitcoind`` and ``bitcoin-cli``, you will need to add a `RPC <../reference/rpc/index.html>`__ password to your ``bitcoin.conf`` file. Both programs will read from the same file if both run on the same system as the same user, so any long random password will work:

::

   rpcpassword=change_this_to_a_long_random_password

You should also make the ``bitcoin.conf`` file only readable to its owner. On Linux, Mac OSX, and other Unix-like systems, this can be accomplished by running the following command in the Bitcoin application directory:

::

   chmod 0600 bitcoin.conf

For development, it’s safer and cheaper to use Bitcoin’s test `network <../devguide/p2p_network.html>`__ (testnet) or regression test mode (regtest) described below.

Questions about Bitcoin use are best sent to the `BitcoinTalk forum <https://bitcointalk.org/index.php?board=4.0>`__ and `IRC channels <https://en.bitcoin.it/wiki/IRC_channels>`__. Errors or suggestions related to documentation on Bitcoin.org can be `submitted as an issue <https://github.com/bitcoin-dot-org/bitcoin.org/issues>`__ or posted to the `bitcoin-documentation mailing list <https://groups.google.com/forum/#!forum/bitcoin-documentation>`__.

In the following documentation, some strings have been shortened or wrapped: “[…]” indicates extra data was removed, and lines ending in a single backslash “\\” are continued below. If you hover your mouse over a paragraph, cross-reference links will be shown in blue. If you hover over a cross-reference link, a brief definition of the term will be displayed in a tooltip.
