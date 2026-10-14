.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

sendall
=======

``sendall ["address",{"address":amount,...},...] ( conf_target "estimate_mode" fee_rate options )``

EXPERIMENTAL warning: this call may be changed in future releases.

Spend the value of all (or specific) confirmed UTXOs and unconfirmed change in the wallet to one or more recipients.

Unconfirmed inbound UTXOs and locked UTXOs will not be spent. Sendall will respect the avoid_reuse wallet flag.

If your wallet contains many small inputs, either because it received tiny payments or as a result of accumulating change, consider using `send_max` to exclude inputs that are worth less than the fees needed to spend them.

Argument #1 - recipients
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, required

The sendall destinations. Each address may only appear once.
       Optionally some recipients can be specified with an amount to perform payments, but at least one address must appear without a specified amount.
       

::

     [
       "address",              (string, required) A bitcoin address which receives an equal share of the unspecified amount.
       {                       (json object)
         "address": amount,    (numeric or string, required) A key-value pair. The key (string) is the bitcoin address, the value (float or string) is the amount in BTC
         ...
       },
       ...
     ]

Argument #2 - conf_target
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=wallet -txconfirmtarget

Confirmation target in blocks

Argument #3 - estimate_mode
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
       

Argument #4 - fee_rate
~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric or string, optional, default=not set, fall back to wallet fee estimation

Specify a fee rate in sat/vB.

Argument #5 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, optional

Options object that can be used to pass named arguments, listed below.
       unset, economical, conservative 
       unset means no mode set (economical mode is used if the transaction is replaceable;
       otherwise, conservative mode is used). 
       economical estimates use a shorter time horizon, making them more
       responsive to short-term drops in the prevailing fee market. This mode
       potentially returns a lower fee rate estimate.
       conservative estimates use a longer time horizon, making them
       less responsive to short-term drops in the prevailing fee market. This mode
       potentially returns a higher fee rate estimate.
       
       Allows this transaction to be replaced by a transaction with higher fees
       Used for fee estimation during coin selection.
       "scripts": [        (json array, optional, default=[]) Scripts involved in this transaction.
       "script",         (string) A script
       ...
       ],
       "descriptors": [    (json array, optional, default=[]) Descriptors that provide solving data for this transaction.
       "descriptor",     (string) A descriptor
       ...
       ],
       }

::

     {
       "pubkeys": [        (json array, optional, default=[]) Public keys involved in this transaction.
         "pubkey",         (string) A public key
         ...
       ],

Result
~~~~~~

::

  {                             (json object)
    "complete" : true|false,    (boolean) If the transaction has a complete set of signatures
    "txid" : "hex",             (string, optional) The transaction id for the send. Only 1 transaction is created regardless of the number of addresses.
    "hex" : "hex",              (string, optional) If add_to_wallet is false, the hex-encoded raw transaction with signature(s)
    "psbt" : "str"              (string, optional) If more signatures are needed, or if add_to_wallet is false, the base64-encoded (partially) signed transaction
  }

Examples
~~~~~~~~


.. highlight:: shell

Spend all UTXOs from the wallet with a fee rate of 1 sat/vB using named arguments::

  bitcoin-cli -named sendall recipients='["bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl"]' fee_rate=1

Spend all UTXOs with a fee rate of 1.1 sat/vB using positional arguments::

  bitcoin-cli sendall '["bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl"]' null "unset" 1.1

Spend all UTXOs split into equal amounts to two addresses with a fee rate of 1.5 sat/vB using the options argument::

  bitcoin-cli sendall '["bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl", "bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3"]' null "unset" null '{"fee_rate": 1.5}'

Leave dust UTXOs in wallet, spend only UTXOs with positive effective value with a fee rate of 10 sat/vB using the options argument::

  bitcoin-cli sendall '["bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl"]' null "unset" null '{"fee_rate": 10, "send_max": true}'

Spend all UTXOs with a fee rate of 1.3 sat/vB using named arguments and sending a 0.25 BTC to another recipient::

  bitcoin-cli -named sendall recipients='[{"bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3": 0.25}, "bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl"]' fee_rate=1.3

