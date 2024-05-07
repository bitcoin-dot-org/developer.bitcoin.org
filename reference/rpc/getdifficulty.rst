.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getdifficulty
=============

``getdifficulty``

Returns the proof-of-work difficulty as a multiple of the minimum difficulty.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - n
     - numeric
     - the proof-of-work difficulty as a multiple of the minimum difficulty.

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getdifficulty

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getdifficulty", "params": []}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

