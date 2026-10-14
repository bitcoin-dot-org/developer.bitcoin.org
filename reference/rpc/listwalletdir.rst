.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

listwalletdir
=============

``listwalletdir``

Returns a list of wallets in the wallet directory.

Result
~~~~~~

::

  {                        (json object)
    "wallets" : [          (json array)
      {                    (json object)
        "name" : "str",    (string) The wallet name
        "warnings" : [     (json array, optional) Warning messages, if any, related to loading the wallet.
          "str",           (string)
          ...
        ]
      },
      ...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli listwalletdir

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "listwalletdir", "params": []}' -H 'content-type: application/json' http://127.0.0.1:8332/

