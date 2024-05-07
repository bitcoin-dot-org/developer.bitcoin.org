.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

gettxoutsetinfo
===============

``gettxoutsetinfo ( "hash_type" )``

Returns statistics about the unspent transaction output set.

Note this call may take some time.

Argument #1 - hash_type
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=hash_serialized_2

Which UTXO set hash should be calculated. Options: 'hash_serialized_2' (the legacy algorithm), 'none'.

Result
~~~~~~

::

  {                                 (json object)
    "height" : n,                   (numeric) The current block height (index)
    "bestblock" : "hex",            (string) The hash of the block at the tip of the chain
    "transactions" : n,             (numeric) The number of transactions with unspent outputs
    "txouts" : n,                   (numeric) The number of unspent transaction outputs
    "bogosize" : n,                 (numeric) A meaningless metric for UTXO set size
    "hash_serialized_2" : "hex",    (string) The serialized hash (only present if 'hash_serialized_2' hash_type is chosen)
    "disk_size" : n,                (numeric) The estimated size of the chainstate on disk
    "total_amount" : n              (numeric) The total amount
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli gettxoutsetinfo

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "gettxoutsetinfo", "params": []}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

