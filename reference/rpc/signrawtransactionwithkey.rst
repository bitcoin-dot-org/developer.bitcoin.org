.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

signrawtransactionwithkey
=========================

``signrawtransactionwithkey "hexstring" ["privatekey",...] ( [{"txid":"hex","vout":n,"scriptPubKey":"hex","redeemScript":"hex","witnessScript":"hex","amount":amount},...] "sighashtype" )``

Sign inputs for raw transaction (serialized, hex-encoded).

The second argument is an array of base58-encoded private
keys that will be the only keys used to sign the transaction.

The third optional argument (may be null) is an array of previous transaction outputs that
this transaction depends on but may not yet be in the block chain.

Argument #1 - hexstring
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The transaction hex string

Argument #2 - privkeys
~~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, required

The base58-encoded private keys for signing

::

     [
       "privatekey",                (string) private key in base58-encoding
       ...
     ]

Argument #3 - prevtxs
~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

The previous dependent transaction outputs

::

     [
       {                            (json object)
         "txid": "hex",             (string, required) The transaction id
         "vout": n,                 (numeric, required) The output number
         "scriptPubKey": "hex",     (string, required) script key
         "redeemScript": "hex",     (string) (required for P2SH) redeem script
         "witnessScript": "hex",    (string) (required for P2WSH or P2SH-P2WSH) witness script
         "amount": amount,          (numeric or string) (required for Segwit inputs) the amount spent
       },
       ...
     ]

Argument #4 - sighashtype
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=ALL

The signature hash type. Must be one of:
       "ALL"
       "NONE"
       "SINGLE"
       "ALL|ANYONECANPAY"
       "NONE|ANYONECANPAY"
       "SINGLE|ANYONECANPAY"
       

Result
~~~~~~

::

  {                             (json object)
    "hex" : "hex",              (string) The hex-encoded raw transaction with signature(s)
    "complete" : true|false,    (boolean) If the transaction has a complete set of signatures
    "errors" : [                (json array, optional) Script verification errors (if there are any)
      {                         (json object)
        "txid" : "hex",         (string) The hash of the referenced, previous transaction
        "vout" : n,             (numeric) The index of the output to spent and used as input
        "scriptSig" : "hex",    (string) The hex-encoded signature script
        "sequence" : n,         (numeric) Script sequence number
        "error" : "str"         (string) Verification or signing error related to the input
      },
      ...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli signrawtransactionwithkey "myhex" "[\"key1\",\"key2\"]"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "signrawtransactionwithkey", "params": ["myhex", "[\"key1\",\"key2\"]"]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

