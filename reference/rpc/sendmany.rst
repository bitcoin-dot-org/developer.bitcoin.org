.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

sendmany
========

``sendmany ( "" ) {"address":amount,...} ( minconf "comment" ["address",...] replaceable conf_target "estimate_mode" fee_rate verbose )``

Send multiple times. Amounts are double-precision floating point numbers.

Requires wallet passphrase to be set with walletpassphrase call if wallet is encrypted.

Argument #1 - dummy
~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default="\"\""

Must be set to "" for backwards compatibility.

Argument #2 - amounts
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, required

The addresses and amounts

::

     {
       "address": amount,    (numeric or string, required) The bitcoin address is the key, the numeric amount (can be string) in BTC is the value
       ...
     }

Argument #3 - minconf
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional

Ignored dummy value

Argument #4 - comment
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional

A comment

Argument #5 - subtractfeefrom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

The addresses.
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

**Type:** boolean, optional, default=wallet default

Signal that this transaction can be replaced by a transaction (BIP 125)

Argument #7 - conf_target
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=wallet -txconfirmtarget

Confirmation target in blocks

Argument #8 - estimate_mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default="unset"

The fee estimate mode, must be one of (case insensitive):
       unset, economical, conservative 
       unset means no mode set (economical mode is used if the transaction is replaceable;
       otherwise, conservative mode is used). 
       economical estimates use a shorter time horizon, making them more
       responsive to short-term drops in the prevailing fee market. This mode
       potentially returns a lower fee rate estimate.
       conservative estimates use a longer time horizon, making them
       less responsive to short-term drops in the prevailing fee market. This mode
       potentially returns a higher fee rate estimate.
       

Argument #9 - fee_rate
~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric or string, optional, default=not set, fall back to wallet fee estimation

Specify a fee rate in sat/vB.

Result (if verbose is not set or set to false)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - hex
     - string
     - The transaction id for the send. Only 1 transaction is created regardless of

Result (if verbose is set to true)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {                          (json object)
    "txid" : "hex",          (string) The transaction id for the send. Only 1 transaction is created regardless of
                             the number of addresses.
    "fee_reason" : "str"     (string) The transaction fee reason.
  }

Examples
~~~~~~~~


.. highlight:: shell

Send two amounts to two different addresses:::

  bitcoin-cli sendmany "" "{\"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl\":0.01,\"bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3\":0.02}"

Send two amounts to two different addresses setting the confirmation and comment:::

  bitcoin-cli sendmany "" "{\"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl\":0.01,\"bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3\":0.02}" 6 "testing"

Send two amounts to two different addresses, subtract fee from amount:::

  bitcoin-cli sendmany "" "{\"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl\":0.01,\"bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3\":0.02}" 1 "" "[\"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl\",\"bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3\"]"

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "sendmany", "params": ["", {"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl":0.01,"bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3":0.02}, 6, "testing"]}' -H 'content-type: application/json' http://127.0.0.1:8332/

