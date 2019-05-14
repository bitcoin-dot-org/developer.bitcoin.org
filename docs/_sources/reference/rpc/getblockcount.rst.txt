.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getblockcount
=============

``getblockcount``

Returns the number of blocks in the longest blockchain.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - n
     - numeric
     - The current block count

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getblockcount

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockcount", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

