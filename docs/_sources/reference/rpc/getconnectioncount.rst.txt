.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getconnectioncount
==================

``getconnectioncount``

Returns the number of connections to other nodes.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - n
     - numeric
     - The connection count

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getconnectioncount

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getconnectioncount", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

