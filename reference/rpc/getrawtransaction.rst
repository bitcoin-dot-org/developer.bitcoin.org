.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getrawtransaction
=================

``getrawtransaction "txid" ( verbose "blockhash" )``

Return the raw transaction data.

By default this function only works for mempool transactions. When called with a blockhash
argument, getrawtransaction will return the transaction if the specified block is available and
the transaction is found in that block. When called without a blockhash argument, getrawtransaction
will return the transaction if it is in the mempool, or if -txindex is enabled and the transaction
is in a block in the blockchain.

Hint: Use gettransaction for wallet transactions.

Note: A confirmed transaction *may* temporarily disappear, between leaving the mempool and entering
the txindex; these operations do not happen atomically.

If verbose is 'true', returns an Object with information about 'txid'.

If verbose is 'false' or omitted, returns a string that is serialized, hex-encoded data for 'txid'.

Argument #1 - txid
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The transaction id

Argument #2 - verbose
~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=false

If false, return a string, otherwise return a json object

Argument #3 - blockhash
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

The block in which to look for the transaction

Result (if verbose is not set or set to false)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - str
     - string
     - The serialized, hex-encoded data for 'txid'

Result (if verbose is set to true)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {                                    (json object)
    "in_active_chain" : true|false,    (boolean) Whether specified block is in the active chain or not (only present with explicit "blockhash" argument)
    "hex" : "hex",                     (string) The serialized, hex-encoded data for 'txid'
    "txid" : "hex",                    (string) The transaction id (same as provided)
    "hash" : "hex",                    (string) The transaction hash (differs from txid for witness transactions)
    "size" : n,                        (numeric) The serialized transaction size
    "vsize" : n,                       (numeric) The virtual transaction size (differs from size for witness transactions)
    "weight" : n,                      (numeric) The transaction's weight (between vsize*4-3 and vsize*4)
    "version" : n,                     (numeric) The version
    "locktime" : xxx,                  (numeric) The lock time
    "vin" : [                          (json array)
      {                                (json object)
        "txid" : "hex",                (string) The transaction id
        "vout" : n,                    (numeric) The output number
        "scriptSig" : {                (json object) The script
          "asm" : "str",               (string) asm
          "hex" : "hex"                (string) hex
        },
        "sequence" : n,                (numeric) The script sequence number
        "txinwitness" : [              (json array)
          "hex",                       (string) hex-encoded witness data (if any)
          ...
        ]
      },
      ...
    ],
    "vout" : [                         (json array)
      {                                (json object)
        "value" : n,                   (numeric) The value in BTC
        "n" : n,                       (numeric) index
        "scriptPubKey" : {             (json object)
          "asm" : "str",               (string) the asm
          "hex" : "str",               (string) the hex
          "reqSigs" : n,               (numeric) The required sigs
          "type" : "str",              (string) The type, eg 'pubkeyhash'
          "addresses" : [              (json array)
            "str",                     (string) bitcoin address
            ...
          ]
        }
      },
      ...
    ],
    "blockhash" : "hex",               (string) the block hash
    "confirmations" : n,               (numeric) The confirmations
    "blocktime" : xxx,                 (numeric) The block time expressed in UNIX epoch time
    "time" : n                         (numeric) Same as "blocktime"
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getrawtransaction "mytxid"

::

  bitcoin-cli getrawtransaction "mytxid" true

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getrawtransaction", "params": ["mytxid", true]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

::

  bitcoin-cli getrawtransaction "mytxid" false "myblockhash"

::

  bitcoin-cli getrawtransaction "mytxid" true "myblockhash"

