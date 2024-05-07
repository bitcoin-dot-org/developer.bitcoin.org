.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

testmempoolaccept
=================

``testmempoolaccept ["rawtx",...] ( maxfeerate )``

Returns result of mempool acceptance tests indicating if raw transaction (serialized, hex-encoded) would be accepted by mempool.

This checks if the transaction violates the consensus or policy rules.

See sendrawtransaction call.

Argument #1 - rawtxs
~~~~~~~~~~~~~~~~~~~~

**Type:** json array, required

An array of hex strings of raw transactions.
       Length must be one for now.

::

     [
       "rawtx",    (string)
       ...
     ]

Argument #2 - maxfeerate
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric or string, optional, default=0.10

Reject transactions whose fee rate is higher than the specified value, expressed in BTC/kB
       

Result
~~~~~~

::

  [                               (json array) The result of the mempool acceptance test for each raw transaction in the input array.
                                  Length is exactly one for now.
    {                             (json object)
      "txid" : "hex",             (string) The transaction hash in hex
      "allowed" : true|false,     (boolean) If the mempool allows this tx to be inserted
      "vsize" : n,                (numeric) Virtual transaction size as defined in BIP 141. This is different from actual serialized size for witness transactions as witness data is discounted (only present when 'allowed' is true)
      "fees" : {                  (json object) Transaction fees (only present if 'allowed' is true)
        "base" : n                (numeric) transaction fee in BTC
      },
      "reject-reason" : "str"     (string) Rejection string (only present when 'allowed' is false)
    },
    ...
  ]

Examples
~~~~~~~~


.. highlight:: shell

Create a transaction::

  bitcoin-cli createrawtransaction "[{\"txid\" : \"mytxid\",\"vout\":0}]" "{\"myaddress\":0.01}"

Sign the transaction, and get back the hex::

  bitcoin-cli signrawtransactionwithwallet "myhex"

Test acceptance of the transaction (signed hex)::

  bitcoin-cli testmempoolaccept '["signedhex"]'

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "testmempoolaccept", "params": [["signedhex"]]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

