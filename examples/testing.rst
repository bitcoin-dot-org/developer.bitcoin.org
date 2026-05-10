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

Regtest Troubleshooting
^^^^^^^^^^^^^^^^^^^^^^^

The following errors are common when creating the first blocks in a
regtest chain.

``Method not found (code -32601)``
   The block-generation RPC has changed between Bitcoin Core releases.
   Use the command that matches your Bitcoin Core version in the example
   above.  For Bitcoin Core 18.0 and later, use
   ``generatetoaddress`` instead of ``generate`` or ``setgenerate``.

``Requested wallet does not exist or is not loaded (code -18)``
   The ``getnewaddress`` command needs a loaded wallet.  Create or load a
   wallet before calling it, or provide ``generatetoaddress`` with another
   valid regtest address:

   ::

      bitcoin-cli -regtest createwallet "regtest-wallet"
      bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)

``Invalid address or key (code -5)``
   The address passed to ``generatetoaddress`` is not valid for the chain
   you are using.  Generate the address with the same regtest node, or
   confirm that every command uses the ``-regtest`` option.

``CreateNewBlock: TestBlockValidity failed: bad-fork-prior-to-checkpoint (code 67)``
   The node is trying to create a block that is invalid for the active
   chain.  This usually means the command is not being run against the
   regtest chain you intended, or the local regtest chain state is stale
   from earlier testing.  First check that both ``bitcoind`` and
   ``bitcoin-cli`` are using regtest:

   ::

      bitcoin-cli -regtest getblockchaininfo

   The result should include ``"chain": "regtest"``.  If you only need
   the private test chain and do not need any old regtest wallets or block
   data, stop Bitcoin Core, delete the ``regtest`` subdirectory in your
   Bitcoin Core data directory, restart ``bitcoind -regtest``, and
   regenerate the first 101 blocks.

``Insufficient funds``
   Coinbase transactions must mature before they can be spent.  Generate
   101 blocks before spending the first block reward, as shown above.

Regtest wallets and block chain state (chainstate) are saved in the ``regtest`` subdirectory of the Bitcoin Core configuration directory. You can safely delete the ``regtest`` subdirectory and restart Bitcoin Core to start a new regtest. (See the `Developer Examples Introduction <../examples/index.html>`__ for default configuration directory locations on various operating systems. Always back up mainnet wallets before performing dangerous operations such as deleting.)
