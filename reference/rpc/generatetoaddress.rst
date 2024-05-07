.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

generatetoaddress
=================

``generatetoaddress nblocks "address" ( maxtries )``

Mine blocks immediately to a specified address (before the RPC call returns)

Argument #1 - nblocks
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

How many blocks are generated immediately.

Argument #2 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The address to send the newly generated bitcoin to.

Argument #3 - maxtries
~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1000000

How many iterations to try.

Result
~~~~~~

::

  [           (json array) hashes of blocks generated
    "hex",    (string) blockhash
    ...
  ]

Examples
~~~~~~~~


.. highlight:: shell

Generate 11 blocks to myaddress::

  bitcoin-cli generatetoaddress 11 "myaddress"

If you are using the Bitcoin Core wallet, you can get a new address to send the newly generated bitcoin to with:::

  bitcoin-cli getnewaddress

