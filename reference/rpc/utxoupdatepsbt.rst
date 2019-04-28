.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

utxoupdatepsbt
==============

``utxoupdatepsbt "psbt"``

Updates a PSBT with witness UTXOs retrieved from the UTXO set or the mempool.

Argument #1 - psbt
~~~~~~~~~~~~~~~~~~

**Type:** string, required

A base64 string of a PSBT

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli utxoupdatepsbt "psbt"

