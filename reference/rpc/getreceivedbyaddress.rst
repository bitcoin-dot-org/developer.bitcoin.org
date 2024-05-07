.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getreceivedbyaddress
====================

``getreceivedbyaddress "address" ( minconf )``

Returns the total amount received by the given address in transactions with at least minconf confirmations.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The bitcoin address for transactions.

Argument #2 - minconf
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1

Only include transactions confirmed at least this many times.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - n
     - numeric
     - The total amount in BTC received at this address.

Examples
~~~~~~~~


.. highlight:: shell

The amount from transactions with at least 1 confirmation::

  bitcoin-cli getreceivedbyaddress "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl"

The amount including unconfirmed transactions, zero confirmations::

  bitcoin-cli getreceivedbyaddress "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" 0

The amount with at least 6 confirmations::

  bitcoin-cli getreceivedbyaddress "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" 6

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getreceivedbyaddress", "params": ["bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl", 6]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

