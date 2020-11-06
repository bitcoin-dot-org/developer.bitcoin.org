Transactions
------------

Transaction Tutorial
~~~~~~~~~~~~~~~~~~~~

Creating transactions is something most Bitcoin applications do. This section describes how to use Bitcoin Core’s `RPC <../reference/rpc/index.html>`__ interface to create transactions with various attributes.

Your applications may use something besides Bitcoin Core to create transactions, but in any system, you will need to provide the same kinds of data to create transactions with the same attributes as those described below.

In order to use this tutorial, you will need to setup `Bitcoin Core <https://bitcoin.org/en/download>`__ and create a regression test mode environment with 50 BTC in your test wallet.

Simple Spending
^^^^^^^^^^^^^^^

Bitcoin Core provides several `RPCs <../reference/rpc/index.html>`__ which handle all the details of spending, including creating change outputs and paying appropriate fees. Even advanced users should use these `RPCs <../reference/rpc/index.html>`__ whenever possible to decrease the chance that satoshis will be lost by mistake.

.. highlight:: bash

::

   > bitcoin-cli -regtest getnewaddress
   mvbnrCX3bg1cDRUu8pkecrvP6vQkSLDSou

   > NEW_ADDRESS=mvbnrCX3bg1cDRUu8pkecrvP6vQkSLDSou

Get a new Bitcoin address and save it in the shell variable ``$NEW_ADDRESS``.

.. highlight:: bash

::

   > bitcoin-cli -regtest sendtoaddress $NEW_ADDRESS 10.00
   263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0

Send 10 bitcoins to the address using the `“sendtoaddress” RPC <../reference/rpc/sendtoaddress.html>`__. The returned hex string is the transaction identifier (txid).

The `“sendtoaddress” RPC <../reference/rpc/sendtoaddress.html>`__ automatically selects an unspent transaction output (UTXO) from which to spend the satoshis. In this case, it withdrew the satoshis from our only available UTXO, the coinbase transaction for block #1 which matured with the creation of block #101. To spend a specific UTXO, you could use the ``sendfrom`` `RPC <../reference/rpc/index.html>`__ instead.

.. highlight:: bash

::

   > bitcoin-cli -regtest listunspent
   [
   ]

Use the `“listunspent” RPC <../reference/rpc/listunspent.html>`__ to display the UTXOs belonging to this wallet. The list is empty because it defaults to only showing confirmed UTXOs and we just spent our only confirmed UTXO.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest listunspent 0

   .. highlight:: json

   ::

      [
          {
              "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
              "vout" : 0,
              "address" : "muhtvdmsnbQEPFuEmxcChX58fGvXaaUoVt",
              "scriptPubKey" : "76a9149ba386253ea698158b6d34802bb9b550f5ce36dd88ac",
              "amount" : 40.00000000,
              "confirmations" : 0,
              "spendable" : true,
              "solvable" : true
          },
          {
              "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
              "vout" : 1,
              "address" : "mvbnrCX3bg1cDRUu8pkecrvP6vQkSLDSou",
              "account" : "",
              "scriptPubKey" : "76a914a57414e5ffae9ef5074bacbe10a320bb2614e1f388ac",
              "amount" : 10.00000000,
              "confirmations" : 0,
              "spendable" : true,
              "solvable" : true
          }
      ]

Re-running the `“listunspent” RPC <../reference/rpc/listunspent.html>`__ with the argument “0” to also display unconfirmed transactions shows that we have two UTXOs, both with the same txid. The first UTXO shown is a change output that `“sendtoaddress” <../reference/rpc/sendtoaddress.html>`__ created using a new address from the key pool. The second UTXO shown is the spend to the address we provided. If we had spent those satoshis to someone else, that second transaction would not be displayed in our list of UTXOs.

.. highlight:: bash

::

   > bitcoin-cli -regtest generate 1

   > unset NEW_ADDRESS

Create a new block to confirm the transaction above (takes less than a second) and clear the shell variable.

Simple Raw Transaction
^^^^^^^^^^^^^^^^^^^^^^

The raw transaction `RPCs <../reference/rpc/index.html>`__ allow users to create custom transactions and delay broadcasting those transactions. However, mistakes made in raw transactions may not be detected by Bitcoin Core, and a number of raw transaction users have permanently lost large numbers of satoshis, so please be careful using raw transactions on mainnet.

This subsection covers one of the simplest possible raw transactions.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest listunspent

   .. highlight:: json

   ::

      [
          {
              "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
              "vout" : 0,
              "address" : "muhtvdmsnbQEPFuEmxcChX58fGvXaaUoVt",
              "scriptPubKey" : "76a9149ba386253ea698158b6d34802bb9b550f5ce36dd88ac",
              "amount" : 40.00000000,
              "confirmations" : 1,
              "spendable" : true,
              "solvable" : true
          },
          {
              "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
              "vout" : 1,
              "address" : "mvbnrCX3bg1cDRUu8pkecrvP6vQkSLDSou",
              "account" : "",
              "scriptPubKey" : "76a914a57414e5ffae9ef5074bacbe10a320bb2614e1f388ac",
              "amount" : 10.00000000,
              "confirmations" : 1,
              "spendable" : true,
              "solvable" : true
          },
          {
              "txid" : "3f4fa19803dec4d6a84fae3821da7ac7577080ef75451294e71f9b20e0ab1e7b",
              "vout" : 0,
              "address" : "mwJTL1dZG8BAP6X7Be3CNNcuVKi7Qqt7Gk",
              "scriptPubKey" : "210260a275cccf0f4b106220725be516adba2752db1bec8c5b7174c89c4c07891f88ac",
              "amount" : 50.00000000,
              "confirmations" : 101,
              "spendable" : true,
              "solvable" : true
          }
      ]

   .. highlight:: bash

   ::

      > UTXO_TXID=3f4fa19803dec4d6a84fae3821da7ac7577080ef75451294e71f[...]
      > UTXO_VOUT=0

Re-run `“listunspent” <../reference/rpc/listunspent.html>`__. We now have three UTXOs: the two transactions we created before plus the coinbase transaction from block #2. We save the txid and :ref:`output index <term-output-index>` number (vout) of that coinbase UTXO to shell variables.

.. highlight:: bash

::

   > bitcoin-cli -regtest getnewaddress
   mz6KvC4aoUeo6wSxtiVQTo7FDwPnkp6URG

   > NEW_ADDRESS=mz6KvC4aoUeo6wSxtiVQTo7FDwPnkp6URG

Get a new address to use in the raw transaction.

.. highlight:: bash

::

   ## Outputs - inputs = transaction fee, so always double-check your math!
   > bitcoin-cli -regtest createrawtransaction '''
       [
         {
           "txid": "'$UTXO_TXID'",
           "vout": '$UTXO_VOUT'
         }
       ]
       ''' '''
       {
         "'$NEW_ADDRESS'": 49.9999
       }'''
   01000000017b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de\
   0398a14f3f0000000000ffffffff01f0ca052a010000001976a914cbc20a7664\
   f2f69e5355aa427045bc15e7c6c77288ac00000000

   > RAW_TX=01000000017b1eabe0209b1fe794124575ef807057c77ada2138ae4[...]

Using two arguments to the `“createrawtransaction” RPC <../reference/rpc/createrawtransaction.html>`__, we create a new raw format transaction. The first argument (a JSON array) references the txid of the coinbase transaction from block #2 and the index number (0) of the output from that transaction we want to spend. The second argument (a JSON object) creates the output with the address (public key hash) and number of bitcoins we want to transfer. We save the resulting raw format transaction to a shell variable.

|Warning icon| **Warning:** `“createrawtransaction” <../reference/rpc/createrawtransaction.html>`__ does not automatically create change outputs, so you can easily accidentally pay a large transaction fee. In this example, our input had 50.0000 bitcoins and our output (``$NEW_ADDRESS``) is being paid 49.9999 bitcoins, so the transaction will include a fee of 0.0001 bitcoins. If we had paid ``$NEW_ADDRESS`` only 10 bitcoins with no other changes to this transaction, the transaction fee would be a whopping 40 bitcoins. See the Complex Raw Transaction subsection below for how to create a transaction with multiple outputs so you can send the change back to yourself.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest decoderawtransaction $RAW_TX

   .. highlight:: json

   ::

      {
          "txid" : "c80b343d2ce2b5d829c2de9854c7c8d423c0e33bda264c40138d834aab4c0638",
          "hash" : "c80b343d2ce2b5d829c2de9854c7c8d423c0e33bda264c40138d834aab4c0638",
          "size" : 85,
          "vsize" : 85,
          "version" : 1,
          "locktime" : 0,
          "vin" : [
              {
                  "txid" : "3f4fa19803dec4d6a84fae3821da7ac7577080ef75451294e71f9b20e0ab1e7b",
                  "vout" : 0,
                  "scriptSig" : {
                      "asm" : "",
                      "hex" : ""
                  },
                  "sequence" : 4294967295
              }
          ],
          "vout" : [
              {
                  "value" : 49.99990000,
                  "n" : 0,
                  "scriptPubKey" : {
                      "asm" : "OP_DUP OP_HASH160 cbc20a7664f2f69e5355aa427045bc15e7c6c772 OP_EQUALVERIFY OP_CHECKSIG",
                      "hex" : "76a914cbc20a7664f2f69e5355aa427045bc15e7c6c77288ac",
                      "reqSigs" : 1,
                      "type" : "pubkeyhash",
                      "addresses" : [
                          "mz6KvC4aoUeo6wSxtiVQTo7FDwPnkp6URG"
                      ]
                  }
              }
          ]
      }

Use the `“decoderawtransaction” RPC <../reference/rpc/decoderawtransaction.html>`__ to see exactly what the transaction we just created does.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest signrawtransaction $RAW_TX

   .. highlight:: json

   ::

      {
          "hex" : "01000000017b1eabe0209b1fe794124575ef807057c77ada[...]",
          "complete" : true
      }

   .. highlight:: bash

   ::

      > SIGNED_RAW_TX=01000000017b1eabe0209b1fe794124575ef807057c77ada[...]

Use the ``signrawtransaction`` `RPC <../reference/rpc/index.html>`__ to sign the transaction created by `“createrawtransaction” <../reference/rpc/createrawtransaction.html>`__ and save the returned “hex” raw format signed transaction to a shell variable.

Even though the transaction is now complete, the Bitcoin Core node we’re connected to doesn’t know anything about the transaction, nor does any other part of the `network <../devguide/p2p_network.html>`__. We’ve created a spend, but we haven’t actually spent anything because we could simply unset the ``$SIGNED_RAW_TX`` variable to eliminate the transaction.

.. highlight:: bash

::

   > bitcoin-cli -regtest sendrawtransaction $SIGNED_RAW_TX
   c7736a0a0046d5a8cc61c8c3c2821d4d7517f5de2bc66a966011aaa79965ffba

Send the signed transaction to the connected node using the `“sendrawtransaction” RPC <../reference/rpc/sendrawtransaction.html>`__. After accepting the transaction, the node would usually then broadcast it to other peers, but we’re not currently connected to other peers because we started in regtest mode.

.. highlight:: bash

::

   > bitcoin-cli -regtest generate 1

   > unset UTXO_TXID UTXO_VOUT NEW_ADDRESS RAW_TX SIGNED_RAW_TX

Generate a block to confirm the transaction and clear our shell variables.

Complex Raw Transaction
^^^^^^^^^^^^^^^^^^^^^^^

In this example, we’ll create a transaction with two inputs and two outputs. We’ll sign each of the inputs separately, as might happen if the two inputs belonged to different people who agreed to create a transaction together (such as a CoinJoin transaction).

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest listunspent

   .. highlight:: json

   ::

      [
          {
              "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
              "vout" : 0,
              "address" : "muhtvdmsnbQEPFuEmxcChX58fGvXaaUoVt",
              "scriptPubKey" : "76a9149ba386253ea698158b6d34802bb9b550f5ce36dd88ac",
              "amount" : 40.00000000,
              "confirmations" : 2,
              "spendable" : true,
              "solvable" : true
          },
          {
              "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
              "vout" : 1,
              "address" : "mvbnrCX3bg1cDRUu8pkecrvP6vQkSLDSou",
              "account" : "",
              "scriptPubKey" : "76a914a57414e5ffae9ef5074bacbe10a320bb2614e1f388ac",
              "amount" : 10.00000000,
              "confirmations" : 2,
              "spendable" : true,
              "solvable" : true
          },
          {
              "txid" : "78203a8f6b529693759e1917a1b9f05670d036fbb129110ed26be6a36de827f3",
              "vout" : 0,
              "address" : "n2KprMQm4z2vmZnPMENfbp2P1LLdAEFRjS",
              "scriptPubKey" : "210229688a74abd0d5ad3b06ddff36fa9cd8edd181d97b9489a6adc40431fb56e1d8ac",
              "amount" : 50.00000000,
              "confirmations" : 101,
              "spendable" : true,
              "solvable" : true
          },
          {
              "txid" : "c7736a0a0046d5a8cc61c8c3c2821d4d7517f5de2bc66a966011aaa79965ffba",
              "vout" : 0,
              "address" : "mz6KvC4aoUeo6wSxtiVQTo7FDwPnkp6URG",
              "account" : "",
              "scriptPubKey" : "76a914cbc20a7664f2f69e5355aa427045bc15e7c6c77288ac",
              "amount" : 49.99990000,
              "confirmations" : 1,
              "spendable" : true,
              "solvable" : true
          }
      ]

   .. highlight:: bash

   ::

      > UTXO1_TXID=78203a8f6b529693759e1917a1b9f05670d036fbb129110ed26[...]
      > UTXO1_VOUT=0
      > UTXO1_ADDRESS=n2KprMQm4z2vmZnPMENfbp2P1LLdAEFRjS
       
      > UTXO2_TXID=263c018582731ff54dc72c7d67e858c002ae298835501d80200[...]
      > UTXO2_VOUT=0
      > UTXO2_ADDRESS=muhtvdmsnbQEPFuEmxcChX58fGvXaaUoVt

For our two inputs, we select two UTXOs by placing the txid and :ref:`output index <term-output-index>` numbers (vouts) in shell variables. We also save the addresses corresponding to the public keys (hashed or unhashed) used in those transactions. We need the addresses so we can get the corresponding private keys from our wallet.

.. highlight:: bash

::

   > bitcoin-cli -regtest dumpprivkey $UTXO1_ADDRESS
   cSp57iWuu5APuzrPGyGc4PGUeCg23PjenZPBPoUs24HtJawccHPm

   > bitcoin-cli -regtest dumpprivkey $UTXO2_ADDRESS
   cT26DX6Ctco7pxaUptJujRfbMS2PJvdqiSMaGaoSktHyon8kQUSg

   > UTXO1_PRIVATE_KEY=cSp57iWuu5APuzrPGyGc4PGUeCg23PjenZPBPoUs24Ht[...]

   > UTXO2_PRIVATE_KEY=cT26DX6Ctco7pxaUptJujRfbMS2PJvdqiSMaGaoSktHy[...]

Use the `“dumpprivkey” RPC <../reference/rpc/dumpprivkey.html>`__ to get the private keys corresponding to the public keys used in the two UTXOs we will be spending. We need the private keys so we can sign each of the inputs separately.

|Warning icon| **Warning:** Users should never manually manage private keys on mainnet. As dangerous as raw transactions are (see warnings above), making a mistake with a private key can be much worse—as in the case of a HD wallet `cross-generational key compromise <../devguide/wallets.html#hardened-keys>`__. These examples are to help you learn, not for you to emulate on mainnet.

.. highlight:: bash

::

   > bitcoin-cli -regtest getnewaddress
   n4puhBEeEWD2VvjdRC9kQuX2abKxSCMNqN
   > bitcoin-cli -regtest getnewaddress
   n4LWXU59yM5MzQev7Jx7VNeq1BqZ85ZbLj

   > NEW_ADDRESS1=n4puhBEeEWD2VvjdRC9kQuX2abKxSCMNqN
   > NEW_ADDRESS2=n4LWXU59yM5MzQev7Jx7VNeq1BqZ85ZbLj

For our two outputs, get two new addresses.

.. highlight:: bash

::

   ## Outputs - inputs = transaction fee, so always double-check your math!
   > bitcoin-cli -regtest createrawtransaction '''
       [
         {
           "txid": "'$UTXO1_TXID'", 
           "vout": '$UTXO1_VOUT'
         }, 
         {
           "txid": "'$UTXO2_TXID'",
           "vout": '$UTXO2_VOUT'
         }
       ]
       ''' '''
       {
         "'$NEW_ADDRESS1'": 79.9999, 
         "'$NEW_ADDRESS2'": 10 
       }'''
   0100000002f327e86da3e66bd20e1129b1fb36d07056f0b9a117199e75939652\
   6b8f3a20780000000000fffffffff0ede03d75050f20801d50358829ae02c058\
   e8677d2cc74df51f738285013c260000000000ffffffff02f028d6dc01000000\
   1976a914ffb035781c3c69e076d48b60c3d38592e7ce06a788ac00ca9a3b0000\
   00001976a914fa5139067622fd7e1e722a05c17c2bb7d5fd6df088ac00000000

   > RAW_TX=0100000002f327e86da3e66bd20e1129b1fb36d07056f0b9a117199[...]

Create the raw transaction using `“createrawtransaction” <../reference/rpc/createrawtransaction.html>`__ much the same as before, except now we have two inputs and two outputs.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest signrawtransaction $RAW_TX '[]' '''
          [
            "'$UTXO1_PRIVATE_KEY'"
          ]'''

   .. highlight:: json

   ::

      {
          "hex" : "0100000002f327e86da3e66bd20e1129b1fb36d07[...]",
          "complete" : false
          "errors": [
          {
            "txid": "c53f8f5ac0b6b10cdc77f543718eb3880fee6cf9b5e0cbf4edb2a59c0fae09a4",
            "vout": 0,
            "scriptSig": "",
            "sequence": 4294967295,
            "error": "Operation not valid with the current stack size"
          }
        ]
      }

   .. highlight:: bash

   ::

      > PARTLY_SIGNED_RAW_TX=0100000002f327e86da3e66bd20e1129b1fb36d07[...]

Signing the raw transaction with ``signrawtransaction`` gets more complicated as we now have three arguments:

1. The unsigned raw transaction.

2. An empty array. We don’t do anything with this argument in this operation, but some valid JSON must be provided to get access to the later positional arguments.

3. The private key we want to use to sign one of the inputs.

The result is a raw transaction with only one input signed; the fact that the transaction isn’t fully signed is indicated by value of the ``complete`` JSON field. We save the incomplete, partly-signed raw transaction hex to a shell variable.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest signrawtransaction $PARTLY_SIGNED_RAW_TX '[]' '''
          [
            "'$UTXO2_PRIVATE_KEY'"
          ]'''

   .. highlight:: json

   ::

      {
          "hex" : "0100000002f327e86da3e66bd20e1129b1fb36d07[...]",
          "complete" : true
      }

To sign the second input, we repeat the process we used to sign the first input using the second private key. Now that both inputs are signed, the ``complete`` result is *true*.

.. highlight:: bash

::

   > unset PARTLY_SIGNED_RAW_TX RAW_TX NEW_ADDRESS1 [...]

Clean up the shell variables used. Unlike previous subsections, we’re not going to send this transaction to the connected node with `“sendrawtransaction” <../reference/rpc/sendrawtransaction.html>`__. This will allow us to illustrate in the Offline Signing subsection below how to spend a transaction which is not yet in the block chain or memory pool.

Offline Signing
^^^^^^^^^^^^^^^

We will now spend the transaction created in the Complex Raw Transaction subsection above without sending it to the local node first. This is the same basic process used by wallet programs for offline signing—which generally means signing a transaction without access to the current UTXO set.

Offline signing is safe. However, in this example we will also be spending an output which is not part of the block chain because the transaction containing it has never been broadcast. That can be unsafe:

|Warning icon| **Warning:** Transactions which spend outputs from unconfirmed transactions are vulnerable to transaction malleability. Be sure to read about transaction malleability and adopt good practices before spending unconfirmed transactions on mainnet.

.. highlight:: bash

::

   > OLD_SIGNED_RAW_TX=0100000002f327e86da3e66bd20e1129b1fb36d07[...]

Put the previously signed (but not sent) transaction into a shell variable.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest decoderawtransaction $OLD_SIGNED_RAW_TX

   .. highlight:: json

   ::

      {
          "txid" : "682cad881df69cb9df8f0c996ce96ecad758357ded2da03bad40cf18ffbb8e09",
          "hash" : "682cad881df69cb9df8f0c996ce96ecad758357ded2da03bad40cf18ffbb8e09",
          "size" : 340,
          "vsize" : 340,
          "version" : 1,
          "locktime" : 0,
          "vin" : [
              {
                  "txid" : "78203a8f6b529693759e1917a1b9f05670d036fbb129110ed26be6a36de827f3",
                  "vout" : 0,
                  "scriptSig" : {
                      "asm" : "3045022100fce442ec52aa2792efc27fd3ad0eaf7fa69f097fdcefab017ea56d1799b10b2102207a6ae3eb61e11ffaba0453f173d1792f1b7bb8e7422ea945101d68535c4b474801",
                      "hex" : "483045022100FCE442ec52aa2792efc27fd3ad0eaf7fa69f097fdcefab017ea56d1799b10b2102207a6ae3eb61e11ffaba0453f173d1792f1b7bb8e7422ea945101d68535c4b474801"
                  },
                  "sequence" : 4294967295
              },
              {
                  "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
                  "vout" : 0,
                  "scriptSig" : {
                      "asm" : "3045022100b77f935ff366a6f3c2fdeb83589c790265d43b3d2cf5e5f0047da56c36de75f40220707ceda75d8dcf2ccaebc506f7293c3dcb910554560763d7659fb202f8ec324b0102240d7d3c7aad57b68aa0178f4c56f997d1bfab2ded3c2f9427686017c603a6d6",
                      "hex" : "483045022100b77f935ff366a6f3c2fdeb83589c790265d43b3d2cf5e5f0047da56c36de75f40220707ceda75d8dcf2ccaebc506f7293c3dcb910554560763d7659fb202f8ec324b012102240d7d3c7aad57b68aa0178f4c56f997d1bfab2ded3c2f9427686017c603a6d6"
                  },
                  "sequence" : 4294967295
              }
          ],
          "vout" : [
              {
                  "value" : 79.99990000,
                  "n" : 0,
                  "scriptPubKey" : {
                      "asm" : "OP_DUP OP_HASH160 ffb035781c3c69e076d48b60c3d38592e7ce06a7 OP_EQUALVERIFY OP_CHECKSIG",
                      "hex" : "76a914ffb035781c3c69e076d48b60c3d38592e7ce06a788ac",
                      "reqSigs" : 1,
                      "type" : "pubkeyhash",
                      "addresses" : [
                          "n4puhBEeEWD2VvjdRC9kQuX2abKxSCMNqN"
                      ]
                  }
              },
              {
                  "value" : 10.00000000,
                  "n" : 1,
                  "scriptPubKey" : {
                      "asm" : "OP_DUP OP_HASH160 fa5139067622fd7e1e722a05c17c2bb7d5fd6df0 OP_EQUALVERIFY OP_CHECKSIG",
                      "hex" : "76a914fa5139067622fd7e1e722a05c17c2bb7d5fd6df088ac",
                      "reqSigs" : 1,
                      "type" : "pubkeyhash",
                      "addresses" : [
                          "n4LWXU59yM5MzQev7Jx7VNeq1BqZ85ZbLj"
                      ]
                  }
              }
          ]
      }

   .. highlight:: bash

   ::

      > UTXO_TXID=682cad881df69cb9df8f0c996ce96ecad758357ded2da03bad40[...]
      > UTXO_VOUT=1
      > UTXO_VALUE=10.00000000
      > UTXO_OUTPUT_SCRIPT=76a914fa5139067622fd7e1e722a05c17c2bb7d5fd6[...]

Decode the signed raw transaction so we can get its txid. Also, choose a specific one of its UTXOs to spend and save that UTXO’s :ref:`output index <term-output-index>` number (vout) and hex pubkey script (scriptPubKey) into shell variables.

.. highlight:: bash

::

   > bitcoin-cli -regtest getnewaddress
   mfdCHEFL2tW9eEUpizk7XLZJcnFM4hrp78

   > NEW_ADDRESS=mfdCHEFL2tW9eEUpizk7XLZJcnFM4hrp78

Get a new address to spend the satoshis to.

.. highlight:: bash

::

   ## Outputs - inputs = transaction fee, so always double-check your math!
   > bitcoin-cli -regtest createrawtransaction '''
       [
         {
           "txid": "'$UTXO_TXID'",
           "vout": '$UTXO_VOUT'
         }
       ]
       ''' '''
       {
         "'$NEW_ADDRESS'": 9.9999
       }'''
   0100000001098ebbff18cf40ad3ba02ded7d3558d7ca6ee96c990c8fdfb99cf6\
   1d88ad2c680100000000ffffffff01f0a29a3b000000001976a914012e2ba6a0\
   51c033b03d712ca2ea00a35eac1e7988ac00000000

   > RAW_TX=0100000001098ebbff18cf40ad3ba02ded7d3558d7ca6ee96c990c8[...]

Create the raw transaction the same way we’ve done in the previous subsections.

.. container:: multicode

   .. highlight:: bash

   ::

          > bitcoin-cli -regtest signrawtransaction $RAW_TX

   .. highlight:: json

   ::

          {
              "hex" : "0100000001098ebbff18cf40ad3ba02ded7d3558d7ca6ee96c990c8[...]",
              "complete" : false
          }

Attempt to sign the raw transaction without any special arguments, the way we successfully signed the the raw transaction in the Simple Raw Transaction subsection. If you’ve read the `Transaction section <../devguide/transactions.html>`__ of the guide, you may know why the call fails and leaves the raw transaction hex unchanged.

.. figure:: /img/dev/en-signing-output-to-spend.svg
   :alt: Old Transaction Data Required To Be Signed

   Old Transaction Data Required To Be Signed

As illustrated above, the data that gets signed includes the txid and vout from the previous transaction. That information is included in the `“createrawtransaction” <../reference/rpc/createrawtransaction.html>`__ raw transaction. But the data that gets signed also includes the pubkey script from the previous transaction, even though it doesn’t appear in either the unsigned or signed transaction.

In the other raw transaction subsections above, the previous output was part of the UTXO set known to the wallet, so the wallet was able to use the txid and :ref:`output index <term-output-index>` number to find the previous pubkey script and insert it automatically.

In this case, you’re spending an output which is unknown to the wallet, so it can’t automatically insert the previous pubkey script.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest signrawtransaction $RAW_TX '''
          [
            {
              "txid": "'$UTXO_TXID'", 
              "vout": '$UTXO_VOUT', 
              "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'",
              "value": '$UTXO_VALUE'
            }
          ]'''

   .. highlight:: json

   ::

      {
          "hex" : "0100000001098ebbff18cf40ad3ba02ded7d3558d7ca6ee96c990c8[...]",
          "complete" : true
      }

   .. highlight:: bash

   ::

      > SIGNED_RAW_TX=0100000001098ebbff18cf40ad3ba02ded7d3558d7ca6ee9[...]

Successfully sign the transaction by providing the previous pubkey script and other required input data.

This specific operation is typically what offline signing wallets do. The online wallet creates the raw transaction and gets the previous pubkey scripts for all the inputs. The user brings this information to the offline wallet. After displaying the transaction details to the user, the offline wallet signs the transaction as we did above. The user takes the signed transaction back to the online wallet, which broadcasts it.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest sendrawtransaction $SIGNED_RAW_TX

   .. highlight:: json

   ::

      {"error": {"code":-22,"message":"TX rejected"}}

Attempt to broadcast the second transaction before we’ve broadcast the first transaction. The node rejects this attempt because the second transaction spends an output which is not a UTXO the node knows about.

.. highlight:: bash

::

   > bitcoin-cli -regtest sendrawtransaction $OLD_SIGNED_RAW_TX
   682cad881df69cb9df8f0c996ce96ecad758357ded2da03bad40cf18ffbb8e09
   > bitcoin-cli -regtest sendrawtransaction $SIGNED_RAW_TX
   67d53afa1a8167ca093d30be7fb9dcb8a64a5fdecacec9d93396330c47052c57

Broadcast the first transaction, which succeeds, and then broadcast the second transaction—which also now succeeds because the node now sees the UTXO.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest getrawmempool

   .. highlight:: json

   ::

      [
          "67d53afa1a8167ca093d30be7fb9dcb8a64a5fdecacec9d93396330c47052c57",
          "682cad881df69cb9df8f0c996ce96ecad758357ded2da03bad40cf18ffbb8e09"
      ]

We have once again not generated an additional block, so the transactions above have not yet become part of the regtest block chain. However, they are part of the local node’s memory pool.

.. highlight:: bash

::

   > unset OLD_SIGNED_RAW_TX SIGNED_RAW_TX RAW_TX [...]

Remove old shell variables.

P2SH Multisig
^^^^^^^^^^^^^

In this subsection, we will create a P2SH multisig address, spend satoshis to it, and then spend those satoshis from it to another address.

Creating a multisig address is easy. Multisig outputs have two parameters, the *minimum* number of signatures required (*m*) and the *number* of public keys to use to validate those signatures. This is called m-of-n, and in this case we’ll be using 2-of-3.

.. highlight:: bash

::

       > bitcoin-cli -regtest getnewaddress
       mhAXF4Eq7iRyvbYk1mpDVBiGdLP3YbY6Dm
       > bitcoin-cli -regtest getnewaddress
       moaCrnRfP5zzyhW8k65f6Rf2z5QpvJzSKe
       > bitcoin-cli -regtest getnewaddress
       mk2QpYatsKicvFVuTAQLBryyccRXMUaGHP

       > NEW_ADDRESS1=mhAXF4Eq7iRyvbYk1mpDVBiGdLP3YbY6Dm
       > NEW_ADDRESS2=moaCrnRfP5zzyhW8k65f6Rf2z5QpvJzSKe
       > NEW_ADDRESS3=mk2QpYatsKicvFVuTAQLBryyccRXMUaGHP

Generate three new P2PKH addresses. P2PKH addresses cannot be used with the multisig redeem script created below. (Hashing each public key is unnecessary anyway—all the public keys are protected by a hash when the redeem script is hashed.) However, Bitcoin Core uses addresses as a way to reference the underlying full (unhashed) public keys it knows about, so we get the three new addresses above in order to use their public keys.

Recall from the Guide that the hashed public keys used in addresses obfuscate the full public key, so you cannot give an address to another person or device as part of creating a typical multisig output or P2SH multisig redeem script. You must give them a full public key.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest validateaddress $NEW_ADDRESS3

   .. highlight:: json

   ::

      {
          "isvalid" : true,
          "address" : "mk2QpYatsKicvFVuTAQLBryyccRXMUaGHP",
          "scriptPubKey" : "76a9143172b5654f6683c8fb146959d347ce303cae4ca788ac",
          "ismine" : true,
          "iswatchonly" : false,
          "isscript" : false,
          "pubkey" : "029e03a901b85534ff1e92c43c74431f7ce72046060fcf7a95c37e148f78c77255",
          "iscompressed" : true,
          "account" : ""
      }

   .. highlight:: bash

   ::

      > NEW_ADDRESS3_PUBLIC_KEY=029e03a901b85534ff1e92c43c74431f7ce720[...]

Use the `“validateaddress” RPC <../reference/rpc/validateaddress.html>`__ to display the full (unhashed) public key for one of the addresses. This is the information which will actually be included in the multisig redeem script. This is also the information you would give another person or device as part of creating a multisig output or P2SH multisig redeem script.

We save the address returned to a shell variable.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest createmultisig 2 '''
          [
            "'$NEW_ADDRESS1'",
            "'$NEW_ADDRESS2'", 
            "'$NEW_ADDRESS3_PUBLIC_KEY'"
          ]'''

   .. highlight:: json

   ::

      {
          "address" : "2N7NaqSKYQUeM8VNgBy8D9xQQbiA8yiJayk",
          "redeemScript" : "522103310188e911026cf18c3ce274e0ebb5f95b007f230d8cb7d09879d96dbeab1aff210243930746e6ed6552e03359db521b088134652905bd2d1541fa9124303a41e95621029e03a901b85534ff1e92c43c74431f7ce72046060fcf7a95c37e148f78c7725553ae"
      }

   .. highlight:: bash

   ::

      > P2SH_ADDRESS=2N7NaqSKYQUeM8VNgBy8D9xQQbiA8yiJayk
      > P2SH_REDEEM_SCRIPT=522103310188e911026cf18c3ce274e0ebb5f95b007[...]

Use the `“createmultisig” RPC <../reference/rpc/createmultisig.html>`__ with two arguments, the number (*n*) of signatures required and a list of addresses or public keys. Because P2PKH addresses can’t be used in the multisig redeem script created by this `RPC <../reference/rpc/index.html>`__, the only addresses which can be provided are those belonging to a public key in the wallet. In this case, we provide two addresses and one public key—all of which will be converted to public keys in the redeem script.

The P2SH address is returned along with the redeem script which must be provided when we spend satoshis sent to the P2SH address.

|Warning icon| **Warning:** You must not lose the redeem script, especially if you don’t have a record of which public keys you used to create the P2SH multisig address. You need the redeem script to spend any bitcoins sent to the P2SH address. If you lose the redeem script, you can recreate it by running the same command above, with the public keys listed in the same order. However, if you lose both the redeem script and even one of the public keys, you will never be able to spend satoshis sent to that P2SH address.

Neither the address nor the redeem script are stored in the wallet when you use `“createmultisig” <../reference/rpc/createmultisig.html>`__. To store them in the wallet, use the `“addmultisigaddress” RPC <../reference/rpc/addmultisigaddress.html>`__ instead. If you add an address to the wallet, you should also make a new backup.

.. highlight:: bash

::

   > bitcoin-cli -regtest sendtoaddress $P2SH_ADDRESS 10.00
   7278d7d030f042ebe633732b512bcb31fff14a697675a1fe1884db139876e175

   > UTXO_TXID=7278d7d030f042ebe633732b512bcb31fff14a697675a1fe1884[...]

Paying the P2SH multisig address with Bitcoin Core is as simple as paying a more common P2PKH address. Here we use the same command (but different variable) we used in the Simple Spending subsection. As before, this command automatically selects an UTXO, creates a change output to a new one of our P2PKH addresses if necessary, and pays a transaction fee if necessary.

We save that txid to a shell variable as the txid of the UTXO we plan to spend next.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest getrawtransaction $UTXO_TXID 1

   .. highlight:: json

   ::

      {
          "hex" : "0100000001f0ede03d75050f20801d50358829ae02c058e8677d2cc74df51f738285013c26010000006a47304402203c3759592bf608ab79c01596c4a417f3110dd6eb776270337e575cdafc699af20220317ef140d596cc255a4067df8125db7f349ad945212e9264a87fa8d777151937012102a92913b70f9fb15a7ea5c42df44637f0de26e2dad97d6d54957690b94cf2cd05ffffffff0100ca9a3b0000000017a9149af61346ce0aa2dffcf697352b4b704c84dcbaff8700000000",
          "txid" : "7278d7d030f042ebe633732b512bcb31fff14a697675a1fe1884db139876e175",
          "hash" : "7278d7d030f042ebe633732b512bcb31fff14a697675a1fe1884db139876e175",
          "size" : 189,
          "vsize" : 189,
          "version" : 1,
          "locktime" : 0,
          "vin" : [
              {
                  "txid" : "263c018582731ff54dc72c7d67e858c002ae298835501d80200f05753de0edf0",
                  "vout" : 1,
                  "scriptSig" : {
                      "asm" : "304402203c3759592bf608ab79c01596c4a417f3110dd6eb776270337e575cdafc699af20220317ef140d596cc255a4067df8125db7f349ad945212e9264a87fa8d7771519370102a92913b70f9fb15a7ea5c42df44637f0de26e2dad97d6d54957690b94cf2cd05",
                      "hex" : "47304402203c3759592bf608ab79c01596c4a417f3110dd6eb776270337e575cdafc699af20220317ef140d596cc255a4067df8125db7f349ad945212e9264a87fa8d777151937012102a92913b70f9fb15a7ea5c42df44637f0de26e2dad97d6d54957690b94cf2cd05"
                  },
                  "sequence" : 4294967295
              }
          ],
          "vout" : [
              {
                  "value" : 10.00000000,
                  "n" : 0,
                  "scriptPubKey" : {
                      "asm" : "OP_HASH160 9af61346ce0aa2dffcf697352b4b704c84dcbaff OP_EQUAL",
                      "hex" : "a9149af61346ce0aa2dffcf697352b4b704c84dcbaff87",
                      "reqSigs" : 1,
                      "type" : "scripthash",
                      "addresses" : [
                          "2N7NaqSKYQUeM8VNgBy8D9xQQbiA8yiJayk"
                      ]
                  }
              }
          ]
      }

   .. highlight:: bash

   ::

      > UTXO_VOUT=0
      > UTXO_OUTPUT_SCRIPT=a9149af61346ce0aa2dffcf697352b4b704c84dcbaff87

We use the `“getrawtransaction” RPC <../reference/rpc/getrawtransaction.html>`__ with the optional second argument (*true*) to get the decoded transaction we just created with `“sendtoaddress” <../reference/rpc/sendtoaddress.html>`__. We choose one of the outputs to be our UTXO and get its :ref:`output index <term-output-index>` number (vout) and pubkey script (scriptPubKey).

.. highlight:: bash

::

   > bitcoin-cli -regtest getnewaddress
   mxCNLtKxzgjg8yyNHeuFSXvxCvagkWdfGU

   > NEW_ADDRESS4=mxCNLtKxzgjg8yyNHeuFSXvxCvagkWdfGU

We generate a new P2PKH address to use in the output we’re about to create.

.. highlight:: bash

::

   ## Outputs - inputs = transaction fee, so always double-check your math!
   > bitcoin-cli -regtest createrawtransaction '''
       [
         {
           "txid": "'$UTXO_TXID'",
           "vout": '$UTXO_VOUT'
         }
      ]
      ''' '''
      {
        "'$NEW_ADDRESS4'": 9.998
      }'''

   010000000175e1769813db8418fea17576694af1ff31cb2b512b7333e6eb42f0\
   30d0d778720000000000ffffffff01c0bc973b000000001976a914b6f64f5bf3\
   e38f25ead28817df7929c06fe847ee88ac00000000

   > RAW_TX=010000000175e1769813db8418fea17576694af1ff31cb2b512b733[...]

We generate the raw transaction the same way we did in the Simple Raw Transaction subsection.

.. highlight:: bash

::

   > bitcoin-cli -regtest dumpprivkey $NEW_ADDRESS1
   cVinshabsALz5Wg4tGDiBuqEGq4i6WCKWXRQdM8RFxLbALvNSHw7
   > bitcoin-cli -regtest dumpprivkey $NEW_ADDRESS3
   cNmbnwwGzEghMMe1vBwH34DFHShEj5bcXD1QpFRPHgG9Mj1xc5hq

   > NEW_ADDRESS1_PRIVATE_KEY=cVinshabsALz5Wg4tGDiBuqEGq4i6WCKWXRQd[...]
   > NEW_ADDRESS3_PRIVATE_KEY=cNmbnwwGzEghMMe1vBwH34DFHShEj5bcXD1Qp[...]

We get the private keys for two of the public keys we used to create the transaction, the same way we got private keys in the Complex Raw Transaction subsection. Recall that we created a 2-of-3 multisig pubkey script, so signatures from two private keys are needed.

|Warning icon| **Reminder:** Users should never manually manage private keys on mainnet. See the warning in the `complex raw transaction section <../examples/transactions.html#complex-raw-transaction>`__.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest signrawtransaction $RAW_TX '''
          [
            {
              "txid": "'$UTXO_TXID'", 
              "vout": '$UTXO_VOUT', 
              "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'", 
              "redeemScript": "'$P2SH_REDEEM_SCRIPT'"
            }
          ]
          ''' '''
          [
            "'$NEW_ADDRESS1_PRIVATE_KEY'"
          ]'''

   .. highlight:: json

   ::

      {
          "hex" : "010000000175e1769813db8418fea17576694af1ff31cb2b512b733[...]",
          "complete" : false
      }

   .. highlight:: bash

   ::

      > PARTLY_SIGNED_RAW_TX=010000000175e1769813db8418fea17576694af1f[...]

We make the first signature. The input argument (JSON object) takes the additional redeem script parameter so that it can append the redeem script to the signature script after the two signatures.

.. container:: multicode

   .. highlight:: bash

   ::

      > bitcoin-cli -regtest signrawtransaction $PARTLY_SIGNED_RAW_TX '''
          [
            {
              "txid": "'$UTXO_TXID'",
              "vout": '$UTXO_VOUT',
              "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'", 
              "redeemScript": "'$P2SH_REDEEM_SCRIPT'"
            }
          ]
          ''' '''
          [
            "'$NEW_ADDRESS3_PRIVATE_KEY'"
          ]'''

   .. highlight:: json

   ::

      {
          "hex" : "010000000175e1769813db8418fea17576694af1ff31cb2b512b733[...]",
          "complete" : true
      }

   .. highlight:: bash

   ::

      > SIGNED_RAW_TX=010000000175e1769813db8418fea17576694af1ff31cb2b[...]

The ``signrawtransaction`` call used here is nearly identical to the one used above. The only difference is the private key used. Now that the two required signatures have been provided, the transaction is marked as complete.

.. highlight:: bash

::

   > bitcoin-cli -regtest sendrawtransaction $SIGNED_RAW_TX
   430a4cee3a55efb04cbb8718713cab18dea7f2521039aa660ffb5aae14ff3f50

We send the transaction spending the P2SH multisig output to the local node, which accepts it.

.. |Warning icon| image:: /img/icons/icon_warning.svg

