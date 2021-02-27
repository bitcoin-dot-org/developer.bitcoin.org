.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

sendtoaddress
=============

``sendtoaddress "address" amount ( "comment" "comment_to" subtractfeefromamount replaceable conf_target "estimate_mode" avoid_reuse fee_rate verbose )``

Send an amount to a given address.

Requires wallet passphrase to be set with walletpassphrase call if wallet is encrypted.

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

**Type:** boolean, optional, default=wallet default

Allow this transaction to be replaced by a transaction with higher fees via BIP 125

Argument #7 - conf_target
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=wallet -txconfirmtarget

Confirmation target in blocks

Argument #8 - estimate_mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=unset

The fee estimate mode, must be one of (case insensitive):
       "unset"
       "economical"
       "conservative"

Argument #9 - avoid_reuse
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

(only available if avoid_reuse wallet flag is set) Avoid spending from dirty addresses; addresses are considered
       dirty if they have previously been used in a transaction.

Result (if verbose is not set or set to false)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hex
     - string
     - The transaction id.

Result (if verbose is set to true)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {                          (json object)
    "txid" : "hex",          (string) The transaction id.
    "fee reason" : "str"     (string) The transaction fee reason.
  }

Examples
~~~~~~~~


.. highlight:: shell

Send 0.1 BTC::

  bitcoin-cli sendtoaddress "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" 0.1

Send 0.1 BTC with a confirmation target of 6 blocks in economical fee estimate mode using positional arguments::

  bitcoin-cli sendtoaddress "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" 0.1 "donation" "sean's outpost" false true 6 economical

Send 0.1 BTC with a fee rate of 1.1 sat/vB, subtract fee from amount, BIP125-replaceable, using positional arguments::

  bitcoin-cli sendtoaddress "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" 0.1 "drinks" "room77" true true null "unset" null 1.1

Send 0.2 BTC with a confirmation target of 6 blocks in economical fee estimate mode using named arguments::

  bitcoin-cli -named sendtoaddress address="bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" amount=0.2 conf_target=6 estimate_mode="economical"

Send 0.5 BTC with a fee rate of 25 sat/vB using named arguments::

  bitcoin-cli -named sendtoaddress address="bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" amount=0.5 fee_rate=25

::

  bitcoin-cli -named sendtoaddress address="bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl" amount=0.5 fee_rate=25 subtractfeefromamount=false replaceable=true avoid_reuse=true comment="2 pizzas" comment_to="jeremy" verbose=true

