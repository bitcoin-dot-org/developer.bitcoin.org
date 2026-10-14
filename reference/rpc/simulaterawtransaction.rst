.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

simulaterawtransaction
======================

``simulaterawtransaction ( ["rawtx",...] {"include_watchonly":bool,...} )``

Calculate the balance change resulting in the signing and broadcasting of the given transaction(s).

Argument #1 - rawtxs
~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

An array of hex strings of raw transactions.
       

::

     [
       "rawtx",    (string)
       ...
     ]

Argument #2 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, optional

Options object that can be used to pass named arguments, listed below.

Result
~~~~~~

::

  {                          (json object)
    "balance_change" : n     (numeric) The wallet balance change (negative means decrease).
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli simulaterawtransaction ["myhex"]

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "simulaterawtransaction", "params": [["myhex"]]}' -H 'content-type: application/json' http://127.0.0.1:8332/

