.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

walletcreatefundedpsbt
======================

``walletcreatefundedpsbt ( [{"txid":"hex","vout":n,"sequence":n,"weight":n},...] ) [{"address":amount,...},{"data":"hex"},...] ( locktime options bip32derivs version )``

Creates and funds a transaction in the Partially Signed Transaction format.

Implements the Creator and Updater roles.

All existing inputs must either have their previous output transaction be in the wallet
or be in the UTXO set. Solving data must be provided for non-wallet inputs.

Argument #1 - inputs
~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

Leave empty to add inputs automatically. See add_inputs option.

::

     [
       {                       (json object)
         "txid": "hex",        (string, required) The transaction id
         "vout": n,            (numeric, required) The output number
         "sequence": n,        (numeric, optional, default=depends on the value of the 'locktime' and 'options.replaceable' arguments) The sequence number
         "weight": n,          (numeric, optional, default=Calculated from wallet and solving data) The maximum weight for this input, including the weight of the outpoint and sequence number. Note that signature sizes are not guaranteed to be consistent, so the maximum DER signatures size of 73 bytes should be used when considering ECDSA signatures.Remember to convert serialized sizes to weight units when necessary.
       },
       ...
     ]

Argument #2 - outputs
~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, required

The outputs specified as key-value pairs.
       Each key may only appear once, i.e. there can only be one 'data' output, and no address may be duplicated.
       At least one output of either type must be specified.
       For compatibility reasons, a dictionary, which holds the key-value pairs directly, is also
       accepted as second parameter.

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

Argument #3 - locktime
~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=0

Raw locktime. Non-0 value also locktime-activates inputs

Argument #4 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, optional

Options object that can be used to pass named arguments, listed below.

Argument #5 - bip32derivs
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

Include BIP 32 derivation paths for public keys if we know them

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

  {                     (json object)
    "psbt" : "str",     (string) The resulting raw transaction (base64-encoded string)
    "fee" : n,          (numeric) Fee in BTC the resulting transaction pays
    "changepos" : n     (numeric) The position of the added change output, or -1
  }

Examples
~~~~~~~~


.. highlight:: shell

Create a PSBT with automatically picked inputs that sends 0.5 BTC to an address and has a fee rate of 2 sat/vB:::

  bitcoin-cli walletcreatefundedpsbt "[]" "[{\"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl\":0.5}]" 0 "{\"add_inputs\":true,\"fee_rate\":2}"

Create the same PSBT as the above one instead using named arguments:::

  bitcoin-cli -named walletcreatefundedpsbt outputs="[{\"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl\":0.5}]" add_inputs=true fee_rate=2

