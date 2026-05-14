RPC Error Codes
===============

When a `JSON-RPC <https://www.jsonrpc.org/specification>`__ call to Bitcoin Core fails, the response contains an error object with a numeric code and a human-readable message. Understanding these error codes helps developers diagnose problems quickly and build robust applications.

Error Response Format
---------------------

A JSON-RPC error response has the following structure:

.. highlight:: json

::

   {
     "result": null,
     "error": {
       "code": <numeric code>,
       "message": "<human-readable description>"
     },
     "id": "<request id>"
   }

For example, calling an unknown RPC method:

.. highlight:: json

::

   > bitcoin-cli unknownmethod
   error code: -32601
   error message:
   Method not found

Standard JSON-RPC Errors
-------------------------

These errors are defined by the JSON-RPC 2.0 specification and indicate problems with the request itself rather than the application logic.

========== =================== ================================================== ====================================
Code       Name                Description                                        Resolution
========== =================== ================================================== ====================================
-32700     RPC_PARSE_ERROR     Failed to parse the request as valid JSON.         Check your JSON syntax for errors such as unquoted strings, trailing commas, or mismatched brackets.
-32600     RPC_INVALID_REQUEST The JSON sent is not a valid Request object.       Ensure the request includes ``"jsonrpc": "2.0"``, ``"method"``, and ``"id"`` fields.
-32601     RPC_METHOD_NOT_FOUND The method does not exist or is not available.   Verify the RPC method name; use ``bitcoin-cli help`` to list available methods.
-32602     RPC_INVALID_PARAMS  Invalid method parameters.                         Check the number and types of parameters against the method documentation (``bitcoin-cli help <method>``).
-32603     RPC_INTERNAL_ERROR  Internal error in ``bitcoind``.                    Check ``debug.log`` for details. This may indicate data corruption or a bug; consider reindexing with ``-reindex``.
========== =================== ================================================== ====================================

General Application Errors
--------------------------

These errors indicate problems with the data or state passed to RPC calls.

========== ============================ ================================================== ====================================
Code       Name                         Description                                        Resolution
========== ============================ ================================================== ====================================
-1         RPC_MISC_ERROR               General error; a ``std::exception`` was thrown.    Check ``debug.log`` for the specific error message.
-3         RPC_TYPE_ERROR               Unexpected type was passed as parameter.            Ensure parameter types match expectations (e.g., string vs. number).
-5         RPC_INVALID_ADDRESS_OR_KEY   Invalid address or key.                             Verify the address format or key is correct for the network (mainnet/testnet/regtest).
-7         RPC_OUT_OF_MEMORY            Ran out of memory during operation.                 Reduce ``dbcache`` or other memory-intensive settings, or add more RAM.
-8         RPC_INVALID_PARAMETER        Invalid, missing, or duplicate parameter.          Check parameter values against the method documentation.
-20        RPC_DATABASE_ERROR            Database error.                                     Check disk space and ``debug.log``. May require ``-reindex`` or ``-rescan``.
-22        RPC_DESERIALIZATION_ERROR     Error parsing or validating structure in raw format. Ensure the raw transaction or block hex is well-formed and complete.
-25        RPC_VERIFY_ERROR              General error during transaction or block submission. Check the error message for details; the transaction may be invalid or fail consensus rules.
-26        RPC_VERIFY_REJECTED           Transaction or block was rejected by network rules.  The transaction violates mempool policy (e.g., too low fee, missing inputs, non-standard).
-27        RPC_VERIFY_ALREADY_IN_UTXO_SET Transaction already exists in the UTXO set.       This input has already been spent; use a different UTXO.
-28        RPC_IN_WARMUP                 Client still warming up.                            Wait for ``bitcoind`` to finish loading; poll ``getblockchaininfo`` until ``initialblockdownload`` completes or ``getinfo`` succeeds.
-32        RPC_METHOD_DEPRECATED         RPC method is deprecated and will be removed.      Use the recommended replacement method (check release notes).
========== ============================ ================================================== ====================================

P2P Client Errors
------------------

These errors relate to the node's network connectivity and peer management.

========== =============================== ================================================== ====================================
Code       Name                            Description                                        Resolution
========== =============================== ================================================== ====================================
-9         RPC_CLIENT_NOT_CONNECTED         Bitcoin is not connected to the network.           Ensure the node has network connectivity; check firewall settings and ``-connect``/``-addnode`` configuration.
-10        RPC_CLIENT_IN_INITIAL_DOWNLOAD  Still downloading initial blocks (IBD).            Wait for initial block download to complete; check progress with ``getblockchaininfo``.
-23        RPC_CLIENT_NODE_ALREADY_ADDED   Node is already in the ``addnode`` list.           No action needed; the peer is already configured.
-24        RPC_CLIENT_NODE_NOT_ADDED       Node has not been added.                           Add the node first using ``addnode`` before attempting to remove it.
-29        RPC_CLIENT_NODE_NOT_CONNECTED   Node to disconnect was not found in connected peers. Check ``getpeerinfo`` for the list of currently connected peers.
-30        RPC_CLIENT_INVALID_IP_OR_SUBNET  Invalid IP address or subnet.                     Use valid IPv4, IPv6, or CIDR notation (e.g., ``192.168.0.0/24``).
-31        RPC_CLIENT_P2P_DISABLED         No valid connection manager found (``-connect`` mode without peers).  Add at least one peer with ``-connect`` or ``-addnode``, or remove ``-connect`` to use automatic peer discovery.
-34        RPC_CLIENT_NODE_CAPACITY_REACHED Max outbound connections already open.             Disconnect an existing peer or increase ``-maxconnections``.
========== =============================== ================================================== ====================================

Chain Errors
------------

========== ============================= ================================================== ====================================
Code       Name                          Description                                        Resolution
========== ============================= ================================================== ====================================
-33        RPC_CLIENT_MEMPOOL_DISABLED   No mempool instance found.                         Ensure the node is not running with ``-blocksonly``; mempool is required for transaction relay.
========== ============================= ================================================== ====================================

Wallet Errors
-------------

These errors occur when interacting with wallet-related RPCs.

========== ================================= ================================================== ====================================
Code       Name                              Description                                      Resolution
========== ================================= ================================================== ====================================
-4         RPC_WALLET_ERROR                  Unspecified wallet problem (e.g., key not found).  Check ``debug.log`` for specifics; may need to rescan or re-import keys.
-6         RPC_WALLET_INSUFFICIENT_FUNDS     Not enough funds in the wallet.                   Use smaller amounts, or use ``listunspent`` to check available UTXOs; consider coin selection or consolidating inputs.
-11        RPC_WALLET_INVALID_LABEL_NAME     Invalid label name.                               Label names must be non-empty and shorter than the maximum length; avoid using ``""`` as a label name in newer versions.
-12        RPC_WALLET_KEYPOOL_RAN_OUT        Keypool exhausted; cannot generate new addresses.   Call ``keypoolrefill`` to top up the keypool, or increase the ``-keypool`` setting.
-13        RPC_WALLET_UNLOCK_NEEDED          Wallet is encrypted and needs to be unlocked.     Call ``walletpassphrase`` with the wallet passphrase before performing this operation.
-14        RPC_WALLET_PASSPHRASE_INCORRECT   The wallet passphrase entered was incorrect.       Verify the passphrase; too many failed attempts will lock the wallet temporarily.
-15        RPC_WALLET_WRONG_ENC_STATE        Command given in wrong wallet encryption state.   If the wallet is already encrypted, you cannot encrypt it again. If unencrypted, ``walletpassphrase`` is not applicable.
-16        RPC_WALLET_ENCRYPTION_FAILED      Failed to encrypt the wallet.                     Check ``debug.log``; ensure the wallet file is not read-only and there is sufficient disk space.
-17        RPC_WALLET_ALREADY_UNLOCKED       Wallet is already unlocked.                       No action needed; the wallet passphrase has already been provided.
-18        RPC_WALLET_NOT_FOUND              Invalid wallet specified.                         Use ``listwallets`` or ``listwalletdir`` to see available wallets; specify the correct wallet name or path.
-19        RPC_WALLET_NOT_SPECIFIED          No wallet specified when multiple wallets are loaded.  Use the ``-rpcwallet=<wallet_name>`` parameter or specify the wallet in the RPC endpoint path.
-35        RPC_WALLET_ALREADY_LOADED         This wallet is already loaded.                    No action needed; the wallet is already available.
-36        RPC_WALLET_ALREADY_EXISTS         A wallet with the same name already exists.       Use a different name, or load the existing wallet instead.
========== ================================= ================================================== ====================================

Block Validation Reject Reasons
-------------------------------

When submitting blocks or transactions, Bitcoin Core may return an error with a reject reason string. These are not numeric error codes but descriptive messages that appear in the ``message`` field of RPC_VERIFY_REJECTED (code -26) or RPC_VERIFY_ERROR (code -25) responses. Below are common reject reasons you may encounter, especially in regtest mode.

============================================= ================================================== ====================================
Reject Reason                                 Description                                        Resolution
============================================= ================================================== ====================================
``bad-fork-prior-to-checkpoint`` (code 67)    The block chain forked before the last valid checkpoint. This commonly occurs in regtest mode when using ``generate`` after manual block manipulation.  Reset regtest by deleting the ``regtest`` subdirectory in the Bitcoin data directory and restarting ``bitcoind -regtest``.
``bad-proof-of-work``                         Block proof-of-work is invalid.                    Ensure the block header hash is below the target. In regtest mode, use ``generatetoaddress`` instead of manual block construction.
``bad-diffbits``                              Block difficulty bits are incorrect.               Check that ``nBits`` in the block header matches the expected target for the current chain.
``bad-version``                               Block version is not allowed.                      Use a valid block version number as determined by consensus rules.
``bad-cb-height``                             Coinbase transaction height is incorrect.          The coinbase script must encode the correct block height (BIP34).
``bad-cb-amount``                             Coinbase output value exceeds the block subsidy.   Reduce the coinbase output value to at most the block subsidy plus fees.
``bad-txns-duplicate``                        Block contains duplicate transactions.            Remove the duplicate transaction from the block.
``bad-txns-inputs-missingorspent``            Transaction inputs are missing or already spent.   Use valid, unspent UTXOs as transaction inputs.
``bad-txns-premature-spend-of-coinbase``      Coinbase output spent before 100 confirmations.    Wait for at least 100 confirmations before spending coinbase outputs.
``txn-already-in-mempool``                    Transaction is already in the mempool.             No action needed; the transaction has already been submitted.
``txn-already-known``                         Transaction is already known (in block or mempool). The transaction has already been included; do not resubmit.
``missing-inputs``                            Transaction inputs could not be found.             Ensure all referenced outputs exist and have not been spent.
``insufficient-fee``                          Transaction fee is too low.                        Increase the fee rate; use ``estimatesmartfee`` to determine an appropriate fee.
``txn-mempool-conflict``                      Transaction conflicts with one already in the mempool. Use ``bumpfee`` for RBF, or wait for the conflicting transaction to confirm or expire.
============================================= ================================================== ====================================

Regtest Troubleshooting
^^^^^^^^^^^^^^^^^^^^^^^

The following regtest-specific issues are commonly encountered:

**``bad-fork-prior-to-checkpoint (code 67)``**

This error appears when running ``generate`` or ``generatetoaddress`` on a regtest chain that has been manually modified or has become inconsistent:

.. highlight:: bash

::

   $ bitcoin-cli -regtest generatetoaddress 11 $(bitcoin-cli -regtest getnewaddress)
   error code: -25
   error message:
   CreateNewBlock: TestBlockValidity failed: bad-fork-prior-to-checkpoint (code 67)

**Resolution:** Delete the ``regtest`` subdirectory and restart:

.. highlight:: bash

::

   $ bitcoin-cli -regtest stop
   $ rm -rf ~/.bitcoin/regtest
   $ bitcoind -regtest -daemon

**``generate`` command not found**

The ``generate`` RPC was removed in Bitcoin Core 18.0. Use ``generatetoaddress`` instead:

.. highlight:: bash

::

   ## Bitcoin Core 18.0+
   $ bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)

**Wallet not found in regtest**

Wallets must be created or loaded explicitly in newer versions:

.. highlight:: bash

::

   $ bitcoin-cli -regtest createwallet "test"
   $ bitcoin-cli -regtest loadwallet "test"

**Insufficient funds in regtest**

Generate at least 101 blocks to make coinbase rewards spendable:

.. highlight:: bash

::

   $ bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)
