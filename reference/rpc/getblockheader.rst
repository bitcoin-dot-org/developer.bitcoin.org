.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getblockheader
==============

``getblockheader "blockhash" ( verbose )``

If verbose is false, returns a string that is serialized, hex-encoded data for blockheader 'hash'.

If verbose is true, returns an Object with information about blockheader 'hash'.

Argument #1 - blockhash
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The block hash

Argument #2 - verbose
~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

true for a json object, false for the hex-encoded data

Result (for verbose = true)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {                                 (json object)
    "hash" : "hex",                 (string) the block hash (same as provided)
    "confirmations" : n,            (numeric) The number of confirmations, or -1 if the block is not on the main chain
    "height" : n,                   (numeric) The block height or index
    "version" : n,                  (numeric) The block version
    "versionHex" : "hex",           (string) The block version formatted in hexadecimal
    "merkleroot" : "hex",           (string) The merkle root
    "time" : xxx,                   (numeric) The block time expressed in UNIX epoch time
    "mediantime" : xxx,             (numeric) The median block time expressed in UNIX epoch time
    "nonce" : n,                    (numeric) The nonce
    "bits" : "hex",                 (string) The bits
    "difficulty" : n,               (numeric) The difficulty
    "chainwork" : "hex",            (string) Expected number of hashes required to produce the current chain
    "nTx" : n,                      (numeric) The number of transactions in the block
    "previousblockhash" : "hex",    (string) The hash of the previous block
    "nextblockhash" : "hex"         (string) The hash of the next block
  }

Result (for verbose=false)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hex
     - string
     - A string that is serialized, hex-encoded data for block 'hash'

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getblockheader "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getblockheader", "params": ["00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

