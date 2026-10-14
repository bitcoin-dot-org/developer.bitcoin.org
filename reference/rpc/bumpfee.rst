.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

bumpfee
=======

``bumpfee "txid" ( options )``

Bumps the fee of a transaction T, replacing it with a new transaction B.

A transaction with the given txid must be in the wallet.

The command will pay the additional fee by reducing change outputs or adding inputs when necessary.

It may add a new change output if one does not already exist.

All inputs in the original transaction will be included in the replacement transaction.

The command will fail if the wallet or mempool contains a transaction that spends one of T's outputs.

By default, the new fee will be calculated automatically using the estimatesmartfee RPC.

The user can specify a confirmation target for estimatesmartfee.

Alternatively, the user can specify a fee rate in sat/vB for the new transaction.

At a minimum, the new fee rate must be high enough to pay an additional new relay fee (incrementalfee
returned by getnetworkinfo) to enter the node's mempool.

\* WARNING: before version 0.21, fee_rate was in BTC/kvB. As of 0.21, fee_rate is in sat/vB. \*

Argument #1 - txid
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The txid to be bumped

Argument #2 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, optional

Options object that can be used to pass named arguments, listed below.
       
       Specify a fee rate in sat/vB instead of relying on the built-in fee estimator.
       Must be at least 0.100 sat/vB higher than the current transaction fee rate.
       WARNING: before version 0.21, fee_rate was in BTC/kvB. As of 0.21, fee_rate is in sat/vB.
       
       marked bip-125 replaceable. If true, the sequence numbers in the transaction will
       be set to 0xfffffffd. If false, any input sequence numbers in the
       transaction will be set to 0xfffffffe
       so the new transaction will not be explicitly bip-125 replaceable (though it may
       still be replaceable in practice, for example if it has unconfirmed ancestors which
       are replaceable).
       
       unset, economical, conservative 
       unset means no mode set (economical mode is used if the transaction is replaceable;
       otherwise, conservative mode is used). 
       economical estimates use a shorter time horizon, making them more
       responsive to short-term drops in the prevailing fee market. This mode
       potentially returns a lower fee rate estimate.
       conservative estimates use a longer time horizon, making them
       less responsive to short-term drops in the prevailing fee market. This mode
       potentially returns a higher fee rate estimate.
       
       Each key may only appear once, i.e. there can only be one 'data' output, and no address may be duplicated.
       At least one output of either type must be specified.
       Cannot be provided if 'original_change_index' is specified.

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

Result
~~~~~~

::

  {                    (json object)
    "txid" : "hex",    (string) The id of the new transaction.
    "origfee" : n,     (numeric) The fee of the replaced transaction.
    "fee" : n,         (numeric) The fee of the new transaction.
    "errors" : [       (json array) Errors encountered during processing (may be empty).
      "str",           (string)
      ...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

Bump the fee, get the new transaction's txid::

  bitcoin-cli bumpfee <txid>

