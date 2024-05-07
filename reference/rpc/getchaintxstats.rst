.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getchaintxstats
===============

``getchaintxstats ( nblocks "blockhash" )``

Compute statistics about the total number and rate of transactions in the chain.

Argument #1 - nblocks
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=one month

Size of the window in number of blocks

Argument #2 - blockhash
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=chain tip

The hash of the block that ends the window.

Result
~~~~~~

::

  {                                       (json object)
    "time" : xxx,                         (numeric) The timestamp for the final block in the window, expressed in UNIX epoch time
    "txcount" : n,                        (numeric) The total number of transactions in the chain up to that point
    "window_final_block_hash" : "hex",    (string) The hash of the final block in the window
    "window_final_block_height" : n,      (numeric) The height of the final block in the window.
    "window_block_count" : n,             (numeric) Size of the window in number of blocks
    "window_tx_count" : n,                (numeric) The number of transactions in the window. Only returned if "window_block_count" is > 0
    "window_interval" : n,                (numeric) The elapsed time in the window in seconds. Only returned if "window_block_count" is > 0
    "txrate" : n                          (numeric) The average rate of transactions per second in the window. Only returned if "window_interval" is > 0
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getchaintxstats

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getchaintxstats", "params": [2016]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

