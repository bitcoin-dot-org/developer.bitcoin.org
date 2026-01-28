Testing Applications
--------------------

Bitcoin Core provides testing tools designed to let developers test their applications with reduced risks and limitations.

Testnet
~~~~~~~

When run with no arguments, all Bitcoin Core programs default to Bitcoin’s main `network <../devguide/p2p_network.html>`__ (:term:`mainnet <Mainnet>`). However, for development, it’s safer and cheaper to use Bitcoin’s test `network <../devguide/p2p_network.html>`__ (testnet) where the satoshis spent have no real-world value. Testnet also relaxes some restrictions (such as standard transaction checks) so you can test functions which might currently be disabled by default on mainnet.

To use testnet, use the argument ``-testnet`` with ``bitcoin-cli``, ``bitcoind`` or ``bitcoin-qt`` or add ``testnet=1`` to your ``bitcoin.conf`` file as `described earlier <../examples/index.html>`__. To get free satoshis for testing, use `Piotr Piasecki’s testnet faucet <https://tpfaucet.appspot.com/>`__. Testnet is a public resource provided for free by members of the community, so please don’t abuse it.

Regtest Mode
~~~~~~~~~~~~

For situations where interaction with random peers and blocks is unnecessary or unwanted, Bitcoin Core’s regression test mode (regtest mode) lets you instantly create a brand-new private block chain with the same basic rules as testnet—but one major difference: you choose when to create new blocks, so you have complete control over the environment.

Many developers consider regtest mode the preferred way to develop new applications. The following example will let you create a regtest environment after you first `configure bitcoind <../examples/index.html>`__.

.. highlight:: bash

::

   > bitcoind -regtest -daemon
   Bitcoin server starting

Start ``bitcoind`` in regtest mode to create a private block chain.

::

   ## Bitcoin Core 0.10.1 and earlier
   bitcoin-cli -regtest setgenerate true 101

   ## Bitcoin Core 17.1 and earlier
   bitcoin-cli -regtest generate 101

   ## Bitcoin Core 18.0 and later
   bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)

Generate 101 blocks using a special `RPC <../reference/rpc/index.html>`__ which is only available in regtest mode. This takes less than a second on a generic PC. Because this is a new block chain using Bitcoin’s default rules, the first blocks pay a block reward of 50 bitcoins. Unlike mainnet, in regtest mode only the first 150 blocks pay a reward of 50 bitcoins. However, a block must have 100 confirmations before that reward can be spent, so we generate 101 blocks to get access to the coinbase transaction from block #1.

.. highlight:: bash

::

   bitcoin-cli -regtest getbalance
   50.00000000

Verify that we now have 50 bitcoins available to spend.

You can now use Bitcoin Core `RPCs <../reference/rpc/index.html>`__ prefixed with ``bitcoin-cli -regtest``.

Regtest wallets and block chain state (chainstate) are saved in the ``regtest`` subdirectory of the Bitcoin Core configuration directory. You can safely delete the ``regtest`` subdirectory and restart Bitcoin Core to start a new regtest. (See the `Developer Examples Introduction <../examples/index.html>`__ for default configuration directory locations on various operating systems. Always back up mainnet wallets before performing dangerous operations such as deleting.)

Common Error Codes
~~~~~~~~~~~~~~~~~~

When developing and testing with Bitcoin Core, you may encounter various error codes. Understanding these errors and their resolutions can help you debug issues more efficiently.

Block Validation Errors
^^^^^^^^^^^^^^^^^^^^^^^

These errors occur when Bitcoin Core rejects a block during validation:

.. list-table::
   :widths: 15 30 55
   :header-rows: 1

   * - Code
     - Error Message
     - Resolution
   * - 16
     - ``bad-txns-vin-empty``
     - Transaction has no inputs. Ensure all transactions have at least one input.
   * - 17
     - ``bad-txns-vout-empty``
     - Transaction has no outputs. Ensure all transactions have at least one output.
   * - 18
     - ``bad-txns-oversize``
     - Transaction exceeds maximum allowed size. Split into smaller transactions.
   * - 26
     - ``bad-txns-vout-negative``
     - Output value is negative. Ensure all output values are non-negative.
   * - 27
     - ``bad-txns-vout-toolarge``
     - Output value exceeds maximum allowed (21 million BTC). Check output amounts.
   * - 64
     - ``bad-blk-length``
     - Block exceeds maximum size limit. In regtest, check your block generation parameters.
   * - 67
     - ``bad-fork-prior-to-checkpoint``
     - Block forks the chain before a checkpoint. In regtest mode, this typically means you're trying to reorganize past a hardcoded checkpoint. Solution: Delete the regtest data directory and start fresh, or ensure you're not mixing mainnet/testnet checkpoints with regtest.
   * - 68
     - ``bad-diffbits``
     - Block has incorrect difficulty bits. Verify proof-of-work calculation.

RPC Error Codes
^^^^^^^^^^^^^^^

These errors are returned by Bitcoin Core's JSON-RPC interface:

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Code
     - Error Message
     - Resolution
   * - -1
     - ``RPC_MISC_ERROR``
     - Generic error. Check the error message for details.
   * - -3
     - ``RPC_TYPE_ERROR``
     - Unexpected argument type. Verify parameter types match the RPC specification.
   * - -5
     - ``RPC_INVALID_ADDRESS_OR_KEY``
     - Invalid Bitcoin address or key. Verify the address format and network (mainnet vs testnet vs regtest).
   * - -6
     - ``RPC_OUT_OF_MEMORY``
     - Not enough memory. Increase available RAM or reduce Bitcoin Core memory usage with ``-dbcache``.
   * - -8
     - ``RPC_INVALID_PARAMETER``
     - Invalid or missing parameter. Check the RPC documentation for required parameters.
   * - -25
     - ``RPC_VERIFY_ERROR``
     - Transaction or block verification failed. Check transaction inputs and signatures.
   * - -26
     - ``RPC_VERIFY_REJECTED``
     - Transaction rejected by network rules. Common causes: insufficient fee, non-standard transaction, or double-spend attempt.
   * - -27
     - ``RPC_VERIFY_ALREADY_IN_CHAIN``
     - Transaction already in blockchain. This is informational, not an actual error.
   * - -28
     - ``RPC_IN_WARMUP``
     - Bitcoin Core is still starting. Wait for initialization to complete before making RPC calls.

Wallet Error Codes
^^^^^^^^^^^^^^^^^^

Errors specific to wallet operations:

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Code
     - Error Message
     - Resolution
   * - -4
     - ``RPC_WALLET_ERROR``
     - Generic wallet error. Check that wallet is loaded and not encrypted/locked.
   * - -12
     - ``RPC_WALLET_KEYPOOL_RAN_OUT``
     - Keypool is exhausted. Run ``keypoolrefill`` to generate new keys.
   * - -13
     - ``RPC_WALLET_UNLOCK_NEEDED``
     - Wallet is encrypted and locked. Use ``walletpassphrase`` to unlock.
   * - -14
     - ``RPC_WALLET_PASSPHRASE_INCORRECT``
     - Incorrect wallet passphrase. Verify the passphrase is correct.
   * - -17
     - ``RPC_WALLET_NOT_FOUND``
     - Wallet not found. Load the wallet with ``loadwallet`` or create a new one.
   * - -18
     - ``RPC_WALLET_NOT_SPECIFIED``
     - Multiple wallets loaded but none specified. Use the ``-rpcwallet`` option or specify wallet in the RPC URL.

Network Error Codes
^^^^^^^^^^^^^^^^^^^

Errors related to peer-to-peer networking:

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - Code
     - Error Message
     - Resolution
   * - -9
     - ``RPC_CLIENT_NOT_CONNECTED``
     - Bitcoin Core is not connected to any peers. Check network connectivity and firewall settings.
   * - -10
     - ``RPC_CLIENT_IN_INITIAL_DOWNLOAD``
     - Node is still syncing the blockchain. Wait for initial block download to complete.

Debugging Tips
^^^^^^^^^^^^^^

When encountering errors:

1. **Check the debug log**: Bitcoin Core writes detailed logs to ``debug.log`` in the data directory. This often contains more context about errors.

2. **Use ``-printtoconsole``**: Start bitcoind with this flag to see log output in real-time.

3. **Verify network mode**: Ensure you're using the correct network flag (``-regtest``, ``-testnet``, or mainnet) consistently across all commands.

4. **Reset regtest state**: For persistent regtest issues, delete the ``regtest`` subdirectory and start fresh::

       rm -rf ~/.bitcoin/regtest
       bitcoind -regtest -daemon

5. **Check RPC connectivity**: Verify RPC settings with ``bitcoin-cli -regtest getnetworkinfo``.
