.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

listreceivedbyaddress
=====================

``listreceivedbyaddress ( minconf include_empty include_watchonly "address_filter" )``

List balances by receiving address.

Argument #1 - minconf
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1

The minimum number of confirmations before payments are included.

Argument #2 - include_empty
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=false

Whether to include addresses that haven't received any payments.

Argument #3 - include_watchonly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true for watch-only wallets, otherwise false

Whether to include watch-only addresses (see 'importaddress')

Argument #4 - address_filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

If present, only return information on this address.

Result
~~~~~~

::

  [                                        (json array)
    {                                      (json object)
      "involvesWatchonly" : true|false,    (boolean) Only returns true if imported addresses were involved in transaction
      "address" : "str",                   (string) The receiving address
      "amount" : n,                        (numeric) The total amount in BTC received by the address
      "confirmations" : n,                 (numeric) The number of confirmations of the most recent transaction included
      "label" : "str",                     (string) The label of the receiving address. The default label is ""
      "txids" : [                          (json array)
        "hex",                             (string) The ids of transactions received with the address
        ...
      ]
    },
    ...
  ]

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli listreceivedbyaddress

::

  bitcoin-cli listreceivedbyaddress 6 true

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "listreceivedbyaddress", "params": [6, true, true]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "listreceivedbyaddress", "params": [6, true, true, "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl"]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

