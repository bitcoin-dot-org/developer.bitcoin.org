Introduction
============

The following guide aims to provide examples to help you start building DigiByte-based applications. To make the best use of this document, you may want to install the current version of DigiByte Core, either from `source <https://github.com/digibyte-core/digibyte>`__ or from a `pre-compiled executable <https://digibyte.org/#downloads>`__.

Once installed, you’ll have access to three programs: ``digibyted``, ``digibyte-qt``, and ``digibyte-cli``.

-  ``digibyte-qt`` provides a combination full DigiByte peer and wallet frontend. From the Help menu, you can access a console where you can enter the `RPC <../reference/rpc/index.html>`__ commands used throughout this document.

-  ``digibyted`` is more useful for programming: it provides a full peer which you can interact with through `RPCs <../reference/rpc/index.html>`__ to port 12024 (or 12026 for testnet).

-  ``digibyte-cli`` allows you to send `RPC <../reference/rpc/index.html>`__ commands to ``digibyted`` from the command line. For example, ``digibyte-cli help``

All three programs get settings from ``digibyte.conf`` in the ``DigiByte`` application directory:

-  Windows: ``%APPDATA%\DigiByte\``

-  OSX: ``$HOME/Library/Application Support/DigiByte/``

-  Linux: ``$HOME/.digibyte/``

To use ``digibyted`` and ``digibyte-cli``, you will need to add a `RPC <../reference/rpc/index.html>`__ password to your ``digibyte.conf`` file. Both programs will read from the same file if both run on the same system as the same user, so any long random password will work:

::

   rpcpassword=change_this_to_a_long_random_password

You should also make the ``digibyte.conf`` file only readable to its owner. On Linux, Mac OSX, and other Unix-like systems, this can be accomplished by running the following command in the DigiByte application directory:

::

   chmod 0600 digibyte.conf

For development, it’s safer and cheaper to use DigiByte's test `network <../devguide/p2p_network.html>`__ (testnet) or regression test mode (regtest) described below.

Questions about DigiByte use are best sent to the `BitcoinTalk forum <https://bitcointalk.org/index.php?board=4.0>`__ and `IRC channels <https://en.bitcoin.it/wiki/IRC_channels>`__. Errors or suggestions related to documentation on DigiByte.org can be `submitted as an issue <https://github.com/bitcoin-dot-org/bitcoin.org/issues>`__ or posted to the `bitcoin-documentation mailing list <https://groups.google.com/forum/#!forum/bitcoin-documentation>`__.

In the following documentation, some strings have been shortened or wrapped: “[…]” indicates extra data was removed, and lines ending in a single backslash “\\” are continued below. If you hover your mouse over a paragraph, cross-reference links will be shown in blue. If you hover over a cross-reference link, a brief definition of the term will be displayed in a tooltip.
