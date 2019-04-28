.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getblockhash
============

``getblockhash height``

Returns hash of block in best-block-chain at height provided.

Argument #1 - height
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

The height index

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hash
     - string
     - The block hash

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getblockhash 1000

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockhash", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

