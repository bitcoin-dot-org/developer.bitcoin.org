.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

signrawtransactionwithwallet
============================

``signrawtransactionwithwallet "hexstring" ( [{"txid":"hex","vout":n,"scriptPubKey":"hex","redeemScript":"hex","witnessScript":"hex","amount":amount},...] "sighashtype" )``

Sign inputs for raw transaction (serialized, hex-encoded).

The second optional argument (may be null) is an array of previous transaction outputs that
this transaction depends on but may not yet be in the block chain.

Argument #1 - hexstring
~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The transaction hex string

Argument #2 - prevtxs
~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

A json array of previous dependent transaction outputs

::

     [
       {                            (json object)
         "txid": "hex",             (string, required) The transaction id
         "vout": n,                 (numeric, required) The output number
         "scriptPubKey": "hex",     (string, required) script key
         "redeemScript": "hex",     (string) (required for P2SH) redeem script
         "witnessScript": "hex",    (string) (required for P2WSH or P2SH-P2WSH) witness script
         "amount": amount,          (numeric or string, required) The amount spent
       },
       ...
     ]

Argument #3 - sighashtype
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=ALL

The signature hash type. Must be one of
       "ALL"
       "NONE"
       "SINGLE"
       "ALL|ANYONECANPAY"
       "NONE|ANYONECANPAY"
       "SINGLE|ANYONECANPAY"

Result
~~~~~~

::

  {
    "hex" : "value",                  (string) The hex-encoded raw transaction with signature(s)
    "complete" : true|false,          (boolean) If the transaction has a complete set of signatures
    "errors" : [                      (json array of objects) Script verification errors (if there are any)
      {
        "txid" : "hash",              (string) The hash of the referenced, previous transaction
        "vout" : n,                   (numeric) The index of the output to spent and used as input
        "scriptSig" : "hex",          (string) The hex-encoded signature script
        "sequence" : n,               (numeric) Script sequence number
        "error" : "text"              (string) Verification or signing error related to the input
      }
      ,...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli signrawtransactionwithwallet "myhex"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "signrawtransactionwithwallet", "params": ["myhex"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

