.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

waitforblockheight
==================

``waitforblockheight height ( timeout )``

Waits for (at least) block height and returns the height and hash
of the current tip.

Returns the current block on timeout or exit.

Make sure to use no RPC timeout (bitcoin-cli -rpcclienttimeout=0)

Argument #1 - height
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

Block height to wait for.

Argument #2 - timeout
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=0

Time in milliseconds to wait for a response. 0 indicates no timeout.

Result
~~~~~~

::

  {                    (json object)
    "hash" : "hex",    (string) The blockhash
    "height" : n       (numeric) Block height
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli waitforblockheight 100 1000

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "waitforblockheight", "params": [100, 1000]}' -H 'content-type: application/json' http://127.0.0.1:8332/

