.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

sendmany
========

``sendmany "" {"address":amount} ( minconf "comment" ["address",...] replaceable conf_target "estimate_mode" )``

Send multiple times. Amounts are double-precision floating point numbers.

Argument #1 - dummy
~~~~~~~~~~~~~~~~~~~

**Type:** string, required

Must be set to "" for backwards compatibility.

Argument #2 - amounts
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, required

A json object with addresses and amounts

::

     {
       "address": amount,    (numeric or string, required) The bitcoin address is the key, the numeric amount (can be string) in BTC is the value
     }

Argument #3 - minconf
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1

Only use the balance confirmed at least this many times.

Argument #4 - comment
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

A comment

Argument #5 - subtractfeefrom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

A json array with addresses.
       The fee will be equally deducted from the amount of each selected address.
       Those recipients will receive less bitcoins than you enter in their corresponding amount field.
       If no addresses are specified here, the sender pays the fee.

::

     [
       "address",            (string) Subtract fee from this address
       ...
     ]

Argument #6 - replaceable
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=fallback to wallet's default

Allow this transaction to be replaced by a transaction with higher fees via BIP 125

Argument #7 - conf_target
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=fallback to wallet's default

Confirmation target (in blocks)

Argument #8 - estimate_mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=UNSET

The fee estimate mode, must be one of:
       "UNSET"
       "ECONOMICAL"
       "CONSERVATIVE"

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - txid
     - string
     - The transaction id for the send. Only 1 transaction is created regardless of 

Examples
~~~~~~~~


.. highlight:: shell

Send two amounts to two different addresses:::

  bitcoin-cli sendmany "" "{\"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX\":0.01,\"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}"

Send two amounts to two different addresses setting the confirmation and comment:::

  bitcoin-cli sendmany "" "{\"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX\":0.01,\"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}" 6 "testing"

Send two amounts to two different addresses, subtract fee from amount:::

  bitcoin-cli sendmany "" "{\"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX\":0.01,\"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}" 1 "" "[\"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX\",\"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\"]"

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["", {"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX":0.01,"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz":0.02}, 6, "testing"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

