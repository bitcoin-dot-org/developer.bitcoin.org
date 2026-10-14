.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

waitfornewblock
===============

``waitfornewblock ( timeout "current_tip" )``

Waits for any new block and returns useful info about it.

Returns the current block on timeout or exit.

Make sure to use no RPC timeout (bitcoin-cli -rpcclienttimeout=0)

Argument #1 - timeout
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=0

Time in milliseconds to wait for a response. 0 indicates no timeout.

Argument #2 - current_tip
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

Method waits for the chain tip to differ from this.

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

  bitcoin-cli waitfornewblock 1000

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "waitfornewblock", "params": [1000]}' -H 'content-type: application/json' http://127.0.0.1:8332/

