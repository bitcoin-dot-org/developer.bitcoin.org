.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

send
====

``send [{"address":amount,...},{"data":"hex"},...] ( conf_target "estimate_mode" fee_rate options version )``

EXPERIMENTAL warning: this call may be changed in future releases.

Send a transaction.

Argument #1 - outputs
~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, required

The outputs specified as key-value pairs.
       Each key may only appear once, i.e. there can only be one 'data' output, and no address may be duplicated.
       At least one output of either type must be specified.
       For convenience, a dictionary, which holds the key-value pairs directly, is also accepted.

::

     [
       {                       (json object)
         "address": amount,    (numeric or string, required) A key-value pair. The key (string) is the bitcoin address,
                               the value (float or string) is the amount in BTC
         ...
       },
       {                       (json object)
         "data": "hex",        (string, required) A key-value pair. The key must be "data", the value is hex-encoded data that becomes a part of an OP_RETURN output
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

Argument #6 - version
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=2

Transaction version
       
       Warning: the resulting transaction may become invalid if one of the unsafe inputs disappears.
       If that happens, you will need to fund the transaction with different inputs and republish it.
       The fee will be equally deducted from the amount of each specified output.
       Those recipients will receive less bitcoins than you enter in their corresponding amount field.
       If no outputs are specified here, the sender pays the fee.
       Transaction building will fail if this can not be satisfied.
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
       "scripts": [          (json array, optional, default=[]) Scripts involved in this transaction.
       "script",           (string) A script
       ...
       ],
       "descriptors": [      (json array, optional, default=[]) Descriptors that provide solving data for this transaction.
       "descriptor",       (string) A descriptor
       ...
       ],
       }

::

     {
       "pubkeys": [          (json array, optional, default=[]) Public keys involved in this transaction.
         "pubkey",           (string) A public key
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

Send 0.1 BTC with a confirmation target of 6 blocks in economical fee estimate mode::

  bitcoin-cli send '{"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl": 0.1}' 6 economical

Send 0.2 BTC with a fee rate of 1.1 sat/vB using positional arguments::

  bitcoin-cli send '{"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl": 0.2}' null "unset" 1.1

Send 0.2 BTC with a fee rate of 1 sat/vB using the options argument::

  bitcoin-cli send '{"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl": 0.2}' null "unset" null '{"fee_rate": 1}'

Send 0.3 BTC with a fee rate of 25 sat/vB using named arguments::

  bitcoin-cli -named send outputs='{"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl": 0.3}' fee_rate=25

Create a transaction that should confirm the next block, with a specific input, and return result without adding to wallet or broadcasting to the network::

  bitcoin-cli send '{"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl": 0.1}' 1 economical '{"add_to_wallet": false, "inputs": [{"txid":"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0", "vout":1}]}'

