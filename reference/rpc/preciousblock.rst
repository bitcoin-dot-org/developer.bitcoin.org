.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

preciousblock
=============

``preciousblock "blockhash"``

Treats a block as if it were received before others with the same work.

A later preciousblock call can override the effect of an earlier one.

The effects of preciousblock are not retained across restarts.

Argument #1 - blockhash
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

the hash of the block to mark as precious

Result
~~~~~~

::

  null    (json null)

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli preciousblock "blockhash"

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "preciousblock", "params": ["blockhash"]}' -H 'content-type: application/json' http://127.0.0.1:8332/

