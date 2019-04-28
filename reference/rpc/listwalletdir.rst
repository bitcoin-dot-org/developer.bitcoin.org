.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

listwalletdir
=============

``listwalletdir``

Returns a list of wallets in the wallet directory.

Result
~~~~~~

::

  {
    "wallets" : [                (json array of objects)
      {
        "name" : "name"          (string) The wallet name
      }
      ,...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli listwalletdir

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listwalletdir", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

