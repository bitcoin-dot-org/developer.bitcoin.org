.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

settxfee
========

``settxfee amount``

Set the transaction fee per kB for this wallet. Overrides the global -paytxfee command line parameter.

Argument #1 - amount
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric or string, required

The transaction fee in BTC/kB

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - Returns true if successful

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli settxfee 0.00001

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "settxfee", "params": [0.00001] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

