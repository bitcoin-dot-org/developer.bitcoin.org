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

   ## Bitcoin Core 18.0 to 21.0
   bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)
   
   ## Bitcoin Core 21.0 and later
   bitcoin-cli -regtest createwallet "regtestwallet"
   bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)

Generate 101 blocks using a special `RPC <../reference/rpc/index.html>`__ which is only available in regtest mode. This takes less than a second on a generic PC. Because this is a new block chain using Bitcoin’s default rules, the first blocks pay a block reward of 50 bitcoins. Unlike mainnet, in regtest mode only the first 150 blocks pay a reward of 50 bitcoins. However, a block must have 100 confirmations before that reward can be spent, so we generate 101 blocks to get access to the coinbase transaction from block #1.

.. highlight:: bash

::

   bitcoin-cli -regtest getbalance
   50.00000000

Verify that we now have 50 bitcoins available to spend.

You can now use Bitcoin Core `RPCs <../reference/rpc/index.html>`__ prefixed with ``bitcoin-cli -regtest``.

Regtest wallets and block chain state (chainstate) are saved in the ``regtest`` subdirectory of the Bitcoin Core configuration directory. You can safely delete the ``regtest`` subdirectory and restart Bitcoin Core to start a new regtest. (See the `Developer Examples Introduction <../examples/index.html>`__ for default configuration directory locations on various operating systems. Always back up mainnet wallets before performing dangerous operations such as deleting.)
