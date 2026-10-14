.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

generateblock
=============

``generateblock "output" ["rawtx/txid",...] ( submit )``

Mine a set of ordered transactions to a specified address or descriptor and return the block hash.

Argument #1 - output
~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The address or descriptor to send the newly generated bitcoin to.

Argument #2 - transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, required

An array of hex strings which are either txids or raw transactions.
       Txids must reference transactions currently in the mempool.
       All transactions must be valid and in valid order, otherwise the block will be rejected.

::

     [
       "rawtx/txid",    (string)
       ...
     ]

Argument #3 - submit
~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

Whether to submit the block before the RPC call returns or to return it as hex.

Result
~~~~~~

::

  {                    (json object)
    "hash" : "hex",    (string) hash of generated block
    "hex" : "hex"      (string, optional) hex of generated block, only present when submit=false
  }

Examples
~~~~~~~~


.. highlight:: shell

Generate a block to myaddress, with txs rawtx and mempool_txid::

  bitcoin-cli generateblock "myaddress" '["rawtx", "mempool_txid"]'

