.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getreceivedbylabel
==================

``getreceivedbylabel "label" ( minconf include_immature_coinbase )``

Returns the total amount received by addresses with <label> in transactions with at least [minconf] confirmations.

Argument #1 - label
~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The selected label, may be the default label using "".

Argument #2 - minconf
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1

Only include transactions confirmed at least this many times.

Argument #3 - include_immature_coinbase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=false

Include immature coinbase transactions.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - n
     - numeric
     - The total amount in BTC received for this label.

Examples
~~~~~~~~


.. highlight:: shell

Amount received by the default label with at least 1 confirmation::

  bitcoin-cli getreceivedbylabel ""

Amount received at the tabby label including unconfirmed amounts with zero confirmations::

  bitcoin-cli getreceivedbylabel "tabby" 0

The amount with at least 6 confirmations::

  bitcoin-cli getreceivedbylabel "tabby" 6

The amount with at least 6 confirmations including immature coinbase outputs::

  bitcoin-cli getreceivedbylabel "tabby" 6 true

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "getreceivedbylabel", "params": ["tabby", 6, true]}' -H 'content-type: application/json' http://127.0.0.1:8332/

