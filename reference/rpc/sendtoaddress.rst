.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

sendtoaddress
=============

``sendtoaddress "address" amount ( "comment" "comment_to" subtractfeefromamount replaceable conf_target "estimate_mode" )``

Send an amount to a given address.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The bitcoin address to send to.

Argument #2 - amount
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric or string, required

The amount in BTC to send. eg 0.1

Argument #3 - comment
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

A comment used to store what the transaction is for.
       This is not part of the transaction, just kept in your wallet.

Argument #4 - comment_to
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

A comment to store the name of the person or organization
       to which you're sending the transaction. This is not part of the 
       transaction, just kept in your wallet.

Argument #5 - subtractfeefromamount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=false

The fee will be deducted from the amount being sent.
       The recipient will receive less bitcoins than you enter in the amount field.

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
     - The transaction id.

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli sendtoaddress "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1

::

  bitcoin-cli sendtoaddress "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 "donation" "seans outpost"

::

  bitcoin-cli sendtoaddress "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 "" "" true

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": ["1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

