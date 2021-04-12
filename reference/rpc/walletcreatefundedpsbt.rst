.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

walletcreatefundedpsbt
======================

``walletcreatefundedpsbt ( [{"txid":"hex","vout":n,"sequence":n},...] ) [{"address":amount},{"data":"hex"},...] ( locktime options bip32derivs )``

Creates and funds a transaction in the Partially Signed Transaction format.

Implements the Creator and Updater roles.

Argument #1 - inputs
~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

Leave empty to add inputs automatically. See add_inputs option.

::

     [
       {                              (json object)
         "txid": "hex",               (string, required) The transaction id
         "vout": n,                   (numeric, required) The output number
         "sequence": n,               (numeric, optional, default=depends on the value of the 'locktime' and 'options.replaceable' arguments) The sequence number
       },
       ...
     ]

Argument #2 - outputs
~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, required

The outputs (key-value pairs), where none of the keys are duplicated.
       That is, each address can only appear once and there can only be one 'data' object.
       For compatibility reasons, a dictionary, which holds the key-value pairs directly, is also
       accepted as second parameter.

::

     [
       {                              (json object)
         "address": amount,           (numeric or string, required) A key-value pair. The key (string) is the bitcoin address, the value (float or string) is the amount in BTC
       },
       {                              (json object)
         "data": "hex",               (string, required) A key-value pair. The key must be "data", the value is hex-encoded data
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

"replaceable": bool,           (boolean, optional, default=wallet default) Marks this transaction as BIP125 replaceable.
       Allows this transaction to be replaced by a transaction with higher fees
       "conf_target": n,              (numeric, optional, default=wallet -txconfirmtarget) Confirmation target in blocks
       "estimate_mode": "str",        (string, optional, default=unset) The fee estimate mode, must be one of (case insensitive):
       "unset"
       "economical"
       "conservative"
       }

::

     {
       "add_inputs": bool,            (boolean, optional, default=false) If inputs are specified, automatically include more if they are not enough.
       "changeAddress": "hex",        (string, optional, default=pool address) The bitcoin address to receive the change
       "changePosition": n,           (numeric, optional, default=random) The index of the change output
       "change_type": "str",          (string, optional, default=set by -changetype) The output type to use. Only valid if changeAddress is not specified. Options are "legacy", "p2sh-segwit", and "bech32".
       "includeWatching": bool,       (boolean, optional, default=true for watch-only wallets, otherwise false) Also select inputs which are watch only
       "lockUnspents": bool,          (boolean, optional, default=false) Lock selected unspent outputs
       "fee_rate": amount,            (numeric or string, optional, default=not set, fall back to wallet fee estimation) Specify a fee rate in sat/vB.
       "feeRate": amount,             (numeric or string, optional, default=not set, fall back to wallet fee estimation) Specify a fee rate in BTC/kvB.
       "subtractFeeFromOutputs": [    (json array, optional, default=empty array) The outputs to subtract the fee from.
                                      The fee will be equally deducted from the amount of each specified output.
                                      Those recipients will receive less bitcoins than you enter in their corresponding amount field.
                                      If no outputs are specified here, the sender pays the fee.
         vout_index,                  (numeric) The zero-based output index, before a change output is added.
         ...
       ],

Argument #5 - bip32derivs
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

Include BIP 32 derivation paths for public keys if we know them

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

Create a transaction with no inputs::

  bitcoin-cli walletcreatefundedpsbt "[{\"txid\":\"myid\",\"vout\":0}]" "[{\"data\":\"00010203\"}]"

