.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

waitforblock
============

``waitforblock "blockhash" ( timeout )``

Waits for a specific new block and returns useful info about it.

Returns the current block on timeout or exit.

Make sure to use no RPC timeout (bitcoin-cli -rpcclienttimeout=0)

Argument #1 - blockhash
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

Block hash to wait for.

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

  bitcoin-cli waitforblock "0000000000079f8ef3d2c688c244eb7a4570b24c9ed7b4a8c619eb02596f8862" 1000

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "waitforblock", "params": ["0000000000079f8ef3d2c688c244eb7a4570b24c9ed7b4a8c619eb02596f8862", 1000]}' -H 'content-type: application/json' http://127.0.0.1:8332/

