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

Error Codes
^^^^^^^^^^^

When Bitcoin Core commands fail, they return error messages that include both a human-readable description and a numeric error code. Understanding these error codes helps you debug issues during development.

**Format:** Error messages are returned as JSON-RPC responses with the format:

::

   {
     "result": null,
     "error": {
       "code": -XX,
       "message": "Description"
     }
   }

**Common Regtest Error Codes:**

**Block Generation Errors:**

``bitcoin-cli -regtest generate 11`` — When generating blocks, you may encounter validation errors if block chain rules are violated:

::

   CreateNewBlock: TestBlockValidity failed: bad-fork-prior-to-checkpoint (code 67)

This error occurs when attempting to create a block that violates consensus rules, such as creating a fork before a checkpoint height. In regtest mode, checkpoints are disabled by default, but other validation rules (such as coinbase maturity—spending transactions must wait 100 blocks) still apply.

To avoid this error, ensure your block generation follows regtest rules:

* The first 150 blocks pay a block reward of 50 bitcoins
* Coinbase transactions cannot be spent until 100 blocks after creation (maturity requirement)
* Do not attempt to generate blocks on a forked chain after switching to a newer height

**Example: Generating Blocks After Coinbase Maturity:**

::

   ## Bitcoin Core 18.0 and later
   bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)
   ## Wait 100 blocks for coinbase to mature (already satisfied in the 101 block generation above)

   ## Now subsequent block generation will work
   bitcoin-cli -regtest generatetoaddress 1 $(bitcoin-cli -regtest getnewaddress)

**RPC Error Codes Reference:**

- **-1** — Generic RPC error (e.g., unexpected exceptions)
- **-3** — Type mismatch error (argument wrong type)
- **-5** — Invalid address or key
- **-8** — Block height out of range
- **-10** — Bitcoin Core is shutting down
- **-32601** — Method not found
- **-32602** — Invalid method parameters
- **-32603** — Internal error

For a complete list of RPC error codes, see the `JSON-RPC error codes <https://developer.bitcoin.org/reference/rpc.html#RPCerrorcodes>`__ reference.
