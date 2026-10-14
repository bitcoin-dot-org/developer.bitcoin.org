.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

abortrescan
===========

``abortrescan``

Stops current wallet rescan triggered by an RPC call, e.g. by a rescanblockchain call.

Note: Use "getwalletinfo" to query the scanning progress.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - Whether the abort was successful

Examples
~~~~~~~~


.. highlight:: shell

Import a private key::

  bitcoin-cli rescanblockchain

Abort the running wallet rescan::

  bitcoin-cli abortrescan

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "abortrescan", "params": []}' -H 'content-type: application/json' http://127.0.0.1:8332/

