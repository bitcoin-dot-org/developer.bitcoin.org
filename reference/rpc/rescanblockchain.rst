.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

rescanblockchain
================

``rescanblockchain ( start_height stop_height )``

Rescan the local blockchain for wallet related transactions.

Note: Use "getwalletinfo" to query the scanning progress.

The rescan is significantly faster if block filters are available
(using startup option "-blockfilterindex=1").

Argument #1 - start_height
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=0

block height where the rescan should start

Argument #2 - stop_height
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

the last block height that should be scanned. If none is provided it will rescan up to the tip at return time of this call.

Result
~~~~~~

::

  {                        (json object)
    "start_height" : n,    (numeric) The block height where the rescan started (the requested height or 0)
    "stop_height" : n      (numeric) The height of the last rescanned block. May be null in rare cases if there was a reorg and the call didn't scan any blocks because they were already scanned in the background.
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli rescanblockchain 100000 120000

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "rescanblockchain", "params": [100000, 120000]}' -H 'content-type: application/json' http://127.0.0.1:8332/

