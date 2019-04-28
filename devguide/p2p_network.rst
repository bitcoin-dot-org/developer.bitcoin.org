P2P Network
-----------

The Bitcoin `network </en/developer-guide#term-network>`__ protocol allows full nodes (peers) to collaboratively maintain a `peer-to-peer network </en/developer-guide#term-network>`__ for block and transaction exchange. Full nodes download and verify every block and transaction prior to relaying them to other nodes. Archival nodes are full nodes which store the entire blockchain and can serve historical blocks to other nodes. Pruned nodes are full nodes which do not store the entire blockchain. Many SPV clients also use the Bitcoin `network </en/developer-guide#term-network>`__ protocol to connect to full nodes.

Consensus rules do not cover networking, so Bitcoin programs may use alternative networks and protocols, such as the `high-speed block relay network <https://www.mail-archive.com/bitcoin-development@lists.sourceforge.net/msg03189.html>`__ used by some miners and the `dedicated transaction information servers <https://github.com/spesmilo/electrum-server>`__ used by some wallets that provide SPV-level security.

To provide practical examples of the Bitcoin `peer-to-peer network </en/developer-guide#term-network>`__, this section uses Bitcoin Core as a representative full node and `BitcoinJ <http://bitcoinj.github.io>`__ as a representative SPV client. Both programs are flexible, so only default behavior is described. Also, for privacy, actual IP addresses in the example output below have been replaced with `RFC5737 <http://tools.ietf.org/html/rfc5737>`__ reserved IP addresses.

Peer Discovery
~~~~~~~~~~~~~~

When started for the first time, programs don’t know the IP addresses of any active full nodes. In order to discover some IP addresses, they query one or more DNS names (called `DNS seeds <../reference/glossary.html#dns-seed>`__) hardcoded into Bitcoin Core and `BitcoinJ <http://bitcoinj.github.io>`__. The response to the lookup should include one or more `DNS A records <http://tools.ietf.org/html/rfc1035#section-3.2.2>`__ with the IP addresses of full nodes that may accept new incoming connections. For example, using the `Unix ``dig`` command <https://en.wikipedia.org/wiki/Dig_%28Unix_command%29>`__:

::

   ;; QUESTION SECTION:
   ;seed.bitcoin.sipa.be.      IN  A

   ;; ANSWER SECTION:
   seed.bitcoin.sipa.be.   60  IN  A  192.0.2.113
   seed.bitcoin.sipa.be.   60  IN  A  198.51.100.231
   seed.bitcoin.sipa.be.   60  IN  A  203.0.113.183
   [...]

The DNS seeds are maintained by Bitcoin community members: some of them provide dynamic DNS seed servers which automatically get IP addresses of active nodes by scanning the `network </en/developer-guide#term-network>`__; others provide static DNS seeds that are updated manually and are more likely to provide IP addresses for inactive nodes. In either case, nodes are added to the DNS seed if they run on the default Bitcoin ports of 8333 for mainnet or 18333 for testnet.

DNS seed results are not authenticated and a malicious seed operator or `network </en/developer-guide#term-network>`__ `man-in-the-middle <https://en.wikipedia.org/wiki/Man-in-the-middle_attack>`__ attacker can return only IP addresses of nodes controlled by the attacker, isolating a program on the attacker’s own `network </en/developer-guide#term-network>`__ and allowing the attacker to feed it bogus transactions and blocks. For this reason, programs should not rely on DNS seeds exclusively.

Once a program has connected to the `network </en/developer-guide#term-network>`__, its peers can begin to send it ``addr`` (address) messages with the IP addresses and port numbers of other peers on the `network </en/developer-guide#term-network>`__, providing a fully decentralized method of peer discovery. Bitcoin Core keeps a record of known peers in a persistent on-disk database which usually allows it to connect directly to those peers on subsequent startups without having to use DNS seeds.

However, peers often leave the `network </en/developer-guide#term-network>`__ or change IP addresses, so programs may need to make several different connection attempts at startup before a successful connection is made. This can add a significant delay to the amount of time it takes to connect to the `network </en/developer-guide#term-network>`__, forcing a user to wait before sending a transaction or checking the status of payment.

To avoid this possible delay, `BitcoinJ <http://bitcoinj.github.io>`__ always uses dynamic DNS seeds to get IP addresses for nodes believed to be currently active. Bitcoin Core also tries to strike a balance between minimizing delays and avoiding unnecessary DNS seed use: if Bitcoin Core has entries in its peer database, it spends up to 11 seconds attempting to connect to at least one of them before falling back to seeds; if a connection is made within that time, it does not query any seeds.

Both Bitcoin Core and `BitcoinJ <http://bitcoinj.github.io>`__ also include a hardcoded list of IP addresses and port numbers to several dozen nodes which were active around the time that particular version of the software was first released. Bitcoin Core will start attempting to connect to these nodes if none of the DNS seed servers have responded to a query within 60 seconds, providing an automatic fallback option.

As a manual fallback option, Bitcoin Core also provides several command-line connection options, including the ability to get a list of peers from a specific node by IP address, or to make a persistent connection to a specific node by IP address. See the ``-help`` text for details. `BitcoinJ <http://bitcoinj.github.io>`__ can be programmed to do the same thing.

**Resources:** `Bitcoin Seeder <https://github.com/sipa/bitcoin-seeder>`__, the program run by several of the seeds used by Bitcoin Core and `BitcoinJ <http://bitcoinj.github.io>`__. The Bitcoin Core `DNS Seed Policy <https://github.com/bitcoin/bitcoin/blob/master/doc/dnsseed-policy.md>`__. The hardcoded list of IP addresses used by Bitcoin Core and `BitcoinJ <http://bitcoinj.github.io>`__ is generated using the `makeseeds script <https://github.com/bitcoin/bitcoin/tree/master/contrib/seeds>`__.

Connecting To Peers
~~~~~~~~~~~~~~~~~~~

Connecting to a peer is done by sending a `“version” message </en/developer-reference#version>`__, which contains your version number, block, and current time to the remote node. The remote node responds with its own `“version” message </en/developer-reference#version>`__. Then both nodes send a `“verack” message </en/developer-reference#verack>`__ to the other node to indicate the connection has been established.

Once connected, the client can send to the remote node ``getaddr`` and `“addr” messages </en/developer-reference#addr>`__ to gather additional peers.

In order to maintain a connection with a peer, nodes by default will send a message to peers before 30 minutes of inactivity. If 90 minutes pass without a message being received by a peer, the client will assume that connection has closed.

Initial Block Download
~~~~~~~~~~~~~~~~~~~~~~

Before a full node can validate unconfirmed transactions and recently-mined blocks, it must download and validate all blocks from block 1 (the block after the hardcoded genesis block) to the current tip of the best block chain. This is the Initial Block Download (IBD) or initial sync.

Although the word “initial” implies this method is only used once, it can also be used any time a large number of blocks need to be downloaded, such as when a previously-caught-up node has been offline for a long time. In this case, a node can use the IBD method to download all the blocks which were produced since the last time it was online.

Bitcoin Core uses the IBD method any time the last block on its local best block chain has a block header time more than 24 hours in the past. `Bitcoin Core 0.10.0 </en/release/v0.10.0>`__ will also perform IBD if its local best block chain is more than 144 blocks lower than its local best header chain (that is, the local block chain is more than about 24 hours in the past).

Blocks-First
^^^^^^^^^^^^

Bitcoin Core (up until version `0.9.3 </en/release/v0.9.3>`__) uses a simple initial block download (IBD) method we’ll call *blocks-first*. The goal is to download the blocks from the best block chain in sequence.

.. figure:: /img/dev/en-blocks-first-flowchart.svg
   :alt: Overview Of Blocks-First Method

   Overview Of Blocks-First Method

The first time a node is started, it only has a single block in its local best block chain—the hardcoded genesis block (block 0). This node chooses a remote peer, called the sync node, and sends it the `“getblocks” message </en/developer-reference#getblocks>`__ illustrated below.

.. figure:: /img/dev/en-ibd-getblocks.svg
   :alt: First GetBlocks Message Sent During IBD

   First GetBlocks Message Sent During IBD

In the header hashes field of the `“getblocks” message </en/developer-reference#getblocks>`__, this new node sends the header hash of the only block it has, the genesis block (6fe2…0000 in internal byte order). It also sets the stop hash field to all zeroes to request a maximum-size response.

Upon `receipt </en/developer-guide#term-receipt>`__ of the `“getblocks” message </en/developer-reference#getblocks>`__, the sync node takes the first (and only) header hash and searches its local best block chain for a block with that header hash. It finds that block 0 matches, so it replies with 500 block inventories (the maximum response to a `“getblocks” message </en/developer-reference#getblocks>`__) starting from block 1. It sends these inventories in the `“inv” message </en/developer-reference#inv>`__ illustrated below.

.. figure:: /img/dev/en-ibd-inv.svg
   :alt: First Inv Message Sent During IBD

   First Inv Message Sent During IBD

Inventories are unique identifiers for information on the `network </en/developer-guide#term-network>`__. Each inventory contains a type field and the unique identifier for an instance of the object. For blocks, the unique identifier is a hash of the block’s header.

The block inventories appear in the `“inv” message </en/developer-reference#inv>`__ in the same order they appear in the block chain, so this first `“inv” message </en/developer-reference#inv>`__ contains inventories for blocks 1 through 501. (For example, the hash of block 1 is 4860…0000 as seen in the illustration above.)

The IBD node uses the received inventories to request 128 blocks from the sync node in the `“getdata” message </en/developer-reference#getdata>`__ illustrated below.

.. figure:: /img/dev/en-ibd-getdata.svg
   :alt: First GetData Message Sent During IBD

   First GetData Message Sent During IBD

It’s important to blocks-first nodes that the blocks be requested and sent in order because each block header references the header hash of the preceding block. That means the IBD node can’t fully validate a block until its parent block has been received. Blocks that can’t be validated because their parents haven’t been received are called orphan blocks; a subsection below describes them in more detail.

Upon `receipt </en/developer-guide#term-receipt>`__ of the `“getdata” message </en/developer-reference#getdata>`__, the sync node replies with each of the blocks requested. Each block is put into serialized block format and sent in a separate `“block” message </en/developer-reference#block>`__. The first `“block” message </en/developer-reference#block>`__ sent (for block 1) is illustrated below.

.. figure:: /img/dev/en-ibd-block.svg
   :alt: First Block Message Sent During IBD

   First Block Message Sent During IBD

The IBD node downloads each block, validates it, and then requests the next block it hasn’t requested yet, maintaining a queue of up to 128 blocks to download. When it has requested every block for which it has an inventory, it sends another `“getblocks” message </en/developer-reference#getblocks>`__ to the sync node requesting the inventories of up to 500 more blocks. This second `“getblocks” message </en/developer-reference#getblocks>`__ contains multiple header hashes as illustrated below:

.. figure:: /img/dev/en-ibd-getblocks2.svg
   :alt: Second GetBlocks Message Sent During IBD

   Second GetBlocks Message Sent During IBD

Upon `receipt </en/developer-guide#term-receipt>`__ of the second `“getblocks” message </en/developer-reference#getblocks>`__, the sync node searches its local best block chain for a block that matches one of the header hashes in the message, trying each hash in the order they were received. If it finds a matching hash, it replies with 500 block inventories starting with the next block from that point. But if there is no matching hash (besides the stopping hash), it assumes the only block the two nodes have in common is block 0 and so it sends an ``inv`` starting with block 1 (the same `“inv” message </en/developer-reference#inv>`__ seen several illustrations above).

This repeated search allows the sync node to send useful inventories even if the IBD node’s local block chain forked from the sync node’s local block chain. This fork detection becomes increasingly useful the closer the IBD node gets to the tip of the block chain.

When the IBD node receives the second `“inv” message </en/developer-reference#inv>`__, it will request those blocks using `“getdata” messages </en/developer-reference#getdata>`__. The sync node will respond with `“block” messages </en/developer-reference#block>`__. Then the IBD node will request more inventories with another `“getblocks” message </en/developer-reference#getblocks>`__—and the cycle will repeat until the IBD node is synced to the tip of the block chain. At that point, the node will accept blocks sent through the regular block broadcasting described in a later subsection.

Blocks-First Advantages & Disadvantages
'''''''''''''''''''''''''''''''''''''''



The primary advantage of blocks-first IBD is its simplicity. The primary disadvantage is that the IBD node relies on a single sync node for all of its downloading. This has several implications:

-  **Speed Limits:** All requests are made to the sync node, so if the sync node has limited upload bandwidth, the IBD node will have slow download speeds. Note: if the sync node goes offline, Bitcoin Core will continue downloading from another node—but it will still only download from a single sync node at a time.

-  **Download Restarts:** The sync node can send a non-best (but otherwise valid) block chain to the IBD node. The IBD node won’t be able to identify it as non-best until the initial block download nears completion, forcing the IBD node to restart its block chain download over again from a different node. Bitcoin Core ships with several block chain checkpoints at various block heights selected by developers to help an IBD node detect that it is being fed an alternative block chain history—allowing the IBD node to restart its download earlier in the process.

-  **Disk Fill Attacks:** Closely related to the download restarts, if the sync node sends a non-best (but otherwise valid) block chain, the chain will be stored on disk, wasting space and possibly filling up the disk drive with useless data.

-  **High Memory Use:** Whether maliciously or by accident, the sync node can send blocks out of order, creating orphan blocks which can’t be validated until their parents have been received and validated. Orphan blocks are stored in memory while they await validation, which may lead to high memory use.

All of these problems are addressed in part or in full by the headers-first IBD method used in `Bitcoin Core 0.10.0 </en/release/v0.10.0>`__.

**Resources:** The table below summarizes the messages mentioned throughout this subsection. The links in the message field will take you to the reference page for that message.

| **Message** \| `“getblocks” </en/developer-reference#getblocks>`__ \| `“inv” </en/developer-reference#inv>`__ \| `“getdata” </en/developer-reference#getdata>`__ \| `“block” </en/developer-reference#block>`__
| **From→To** \| IBD→Sync \| Sync→IBD \| IBD→Sync \| Sync→IBD
| **Payload** \| One or more header hashes \| Up to 500 block inventories (unique identifiers) \| One or more block inventories \| One serialized block

Headers-First
^^^^^^^^^^^^^

`Bitcoin Core 0.10.0 </en/release/v0.10.0>`__ uses an initial block download (IBD) method called *headers-first*. The goal is to download the headers for the best `header chain <../reference/glossary.html#header-chain>`__, partially validate them as best as possible, and then download the corresponding blocks in parallel. This solves several problems with the older blocks-first IBD method.

.. figure:: /img/dev/en-headers-first-flowchart.svg
   :alt: Overview Of Headers-First Method

   Overview Of Headers-First Method

The first time a node is started, it only has a single block in its local best block chain—the hardcoded genesis block (block 0). The node chooses a remote peer, which we’ll call the sync node, and sends it the `“getheaders” message </en/developer-reference#getheaders>`__ illustrated below.

.. figure:: /img/dev/en-ibd-getheaders.svg
   :alt: First getheaders message

   First getheaders message

In the header hashes field of the `“getheaders” message </en/developer-reference#getheaders>`__, the new node sends the header hash of the only block it has, the genesis block (6fe2…0000 in internal byte order). It also sets the stop hash field to all zeroes to request a maximum-size response.

Upon `receipt </en/developer-guide#term-receipt>`__ of the `“getheaders” message </en/developer-reference#getheaders>`__, the sync node takes the first (and only) header hash and searches its local best block chain for a block with that header hash. It finds that block 0 matches, so it replies with 2,000 header (the maximum response) starting from block 1. It sends these header hashes in the `“headers” message </en/developer-reference#headers>`__ illustrated below.

.. figure:: /img/dev/en-ibd-headers.svg
   :alt: First headers message

   First headers message

The IBD node can partially validate these block headers by ensuring that all fields follow consensus rules and that the hash of the header is below the target threshold according to the nBits field. (Full validation still requires all transactions from the corresponding block.)

After the IBD node has partially validated the block headers, it can do two things in parallel:

1. **Download More Headers:** the IBD node can send another `“getheaders” message </en/developer-reference#getheaders>`__ to the sync node to request the next 2,000 headers on the best header chain. Those headers can be immediately validated and another batch requested repeatedly until a `“headers” message </en/developer-reference#headers>`__ is received from the sync node with fewer than 2,000 headers, indicating that it has no more headers to offer. As of this writing, headers sync can be completed in fewer than 200 round trips, or about 32 MB of downloaded data.

   Once the IBD node receives a `“headers” message </en/developer-reference#headers>`__ with fewer than 2,000 headers from the sync node, it sends a `“getheaders” message </en/developer-reference#getheaders>`__ to each of its outbound peers to get their view of best header chain. By comparing the responses, it can easily determine if the headers it has downloaded belong to the best header chain reported by any of its outbound peers. This means a dishonest sync node will quickly be discovered even if checkpoints aren’t used (as long as the IBD node connects to at least one honest peer; Bitcoin Core will continue to provide checkpoints in case honest peers can’t be found).

2. **Download Blocks:** While the IBD node continues downloading headers, and after the headers finish downloading, the IBD node will request and download each block. The IBD node can use the block header hashes it computed from the header chain to create `“getdata” messages </en/developer-reference#getdata>`__ that request the blocks it needs by their inventory. It doesn’t need to request these from the sync node—it can request them from any of its full node peers. (Although not all full nodes may store all blocks.) This allows it to fetch blocks in parallel and avoid having its download speed constrained to the upload speed of a single sync node.

   To spread the load between multiple peers, Bitcoin Core will only request up to 16 blocks at a time from a single peer. Combined with its maximum of 8 outbound connections, this means headers-first Bitcoin Core will request a maximum of 128 blocks simultaneously during IBD (the same maximum number that blocks-first Bitcoin Core requested from its sync node).

.. figure:: /img/dev/en-headers-first-moving-window.svg
   :alt: Simulated Headers-First Download Window

   Simulated Headers-First Download Window

Bitcoin Core’s headers-first mode uses a 1,024-block moving download window to maximize download speed. The lowest-height block in the window is the next block to be validated; if the block hasn’t arrived by the time Bitcoin Core is ready to validate it, Bitcoin Core will wait a minimum of two more seconds for the stalling node to send the block. If the block still hasn’t arrived, Bitcoin Core will disconnect from the stalling node and attempt to connect to another node. For example, in the illustration above, Node A will be disconnected if it doesn’t send block 3 within at least two seconds.

Once the IBD node is synced to the tip of the block chain, it will accept blocks sent through the regular block broadcasting described in a later subsection.

**Resources:** The table below summarizes the messages mentioned throughout this subsection. The links in the message field will take you to the reference page for that message.

| **Message** \| `“getheaders” </en/developer-reference#getheaders>`__ \| `“headers” </en/developer-reference#headers>`__ \| `“getdata” </en/developer-reference#getdata>`__ \| `“block” </en/developer-reference#block>`__
| **From→To** \| IBD→Sync \| Sync→IBD \| IBD→\ *Many* \| *Many*\ →IBD
| **Payload** \| One or more header hashes \| Up to 2,000 block headers \| One or more block inventories derived from header hashes \| One serialized block

Block Broadcasting
~~~~~~~~~~~~~~~~~~

When a miner discovers a new block, it broadcasts the new block to its peers using one of the following methods:

-  `Unsolicited Block Push </en/developer-guide#term-unsolicited-block-push>`__\ **:** the miner sends a `“block” message </en/developer-reference#block>`__ to each of its full node peers with the new block. The miner can reasonably bypass the standard relay method in this way because it knows none of its peers already have the just-discovered block.

-  `Standard Block Relay </en/developer-guide#term-standard-block-relay>`__\ **:** the miner, acting as a standard relay node, sends an `“inv” message </en/developer-reference#inv>`__ to each of its peers (both full node and SPV) with an inventory referring to the new block. The most common responses are:

   -  Each blocks-first (BF) peer that wants the block replies with a `“getdata” message </en/developer-reference#getdata>`__ requesting the full block.

   -  Each headers-first (HF) peer that wants the block replies with a `“getheaders” message </en/developer-reference#getheaders>`__ containing the header hash of the highest-height header on its best header chain, and likely also some headers further back on the best header chain to allow fork detection. That message is immediately followed by a `“getdata” message </en/developer-reference#getdata>`__ requesting the full block. By requesting headers first, a headers-first peer can refuse orphan blocks as described in the subsection below.

   -  Each Simplified Payment Verification (SPV) client that wants the block replies with a `“getdata” message </en/developer-reference#getdata>`__ typically requesting a merkle block.

   The miner replies to each request accordingly by sending the block in a `“block” message </en/developer-reference#block>`__, one or more headers in a `“headers” message </en/developer-reference#headers>`__, or the merkle block and transactions relative to the SPV client’s bloom filter in a `“merkleblock” message </en/developer-reference#merkleblock>`__ followed by zero or more `“tx” messages </en/developer-reference#tx>`__.

-  `Direct Headers Announcement <../reference/glossary.html#block-header>`__\ **:** a relay node may skip the round trip overhead of an `“inv” message </en/developer-reference#inv>`__ followed by ``getheaders`` by instead immediately sending a `“headers” message </en/developer-reference#headers>`__ containing the full header of the new block. A HF peer receiving this message will partially validate the block header as it would during headers-first IBD, then request the full block contents with a `“getdata” message </en/developer-reference#getdata>`__ if the header is valid. The relay node then responds to the ``getdata`` request with the full or filtered block data in a ``block`` or `“merkleblock” message </en/developer-reference#merkleblock>`__, respectively. A HF node may signal that it prefers to receive ``headers`` instead of ``inv`` announcements by sending a special `“sendheaders” message </en/developer-reference#sendheaders>`__ during the connection handshake.

   This protocol for block broadcasting was proposed in BIP 130 and has been implemented in Bitcoin Core since version 0.12.

By default, Bitcoin Core broadcasts blocks using direct headers announcement to any peers that have signalled with `“sendheaders” </en/developer-reference#sendheaders>`__ and uses `standard block relay </en/developer-guide#term-standard-block-relay>`__ for all peers that have not. Bitcoin Core will accept blocks sent using any of the methods described above.

Full nodes validate the received block and then advertise it to their peers using the `standard block relay </en/developer-guide#term-standard-block-relay>`__ method described above. The condensed table below highlights the operation of the messages described above (Relay, BF, HF, and SPV refer to the relay node, a blocks-first node, a headers-first node, and an SPV client; *any* refers to a node using any block retrieval method.)

| **Message** \| `“inv” </en/developer-reference#inv>`__ \| `“getdata” </en/developer-reference#getdata>`__ \| `“getheaders” </en/developer-reference#getheaders>`__ \| `“headers” </en/developer-reference#headers>`__
| **From→To** \| Relay→\ *Any* \| BF→Relay \| HF→Relay \| Relay→HF
| **Payload** \| The inventory of the new block \| The inventory of the new block \| One or more header hashes on the HF node’s best header chain (BHC) \| Up to 2,000 headers connecting HF node’s BHC to relay node’s BHC
| **Message** \| `“block” </en/developer-reference#block>`__ \| `“merkleblock” </en/developer-reference#merkleblock>`__ \| `“tx” </en/developer-reference#tx>`__ \|
| **From→To** \| Relay→BF/HF \| Relay→SPV \| Relay→SPV \|
| **Payload** \| The new block in `serialized format </en/developer-reference#serialized-blocks>`__ \| The new block filtered into a merkle block \| Serialized transactions from the new block that match the bloom filter \|

Orphan Blocks
^^^^^^^^^^^^^

Blocks-first nodes may download orphan blocks—blocks whose `previous block header hash </en/developer-reference#term-previous-block-header-hash>`__ field refers to a block header this node hasn’t seen yet. In other words, orphan blocks have no known parent (unlike stale blocks, which have known parents but which aren’t part of the best block chain).

.. figure:: /img/dev/en-orphan-stale-definition.svg
   :alt: Difference Between Orphan And Stale Blocks

   Difference Between Orphan And Stale Blocks

When a blocks-first node downloads an orphan block, it will not validate it. Instead, it will send a `“getblocks” message </en/developer-reference#getblocks>`__ to the node which sent the orphan block; the broadcasting node will respond with an `“inv” message </en/developer-reference#inv>`__ containing inventories of any blocks the downloading node is missing (up to 500); the downloading node will request those blocks with a `“getdata” message </en/developer-reference#getdata>`__; and the broadcasting node will send those blocks with a `“block” message </en/developer-reference#block>`__. The downloading node will validate those blocks, and once the parent of the former orphan block has been validated, it will validate the former orphan block.

Headers-first nodes avoid some of this complexity by always requesting block headers with the `“getheaders” message </en/developer-reference#getheaders>`__ before requesting a block with the `“getdata” message </en/developer-reference#getdata>`__. The broadcasting node will send a `“headers” message </en/developer-reference#headers>`__ containing all the block headers (up to 2,000) it thinks the downloading node needs to reach the tip of the best header chain; each of those headers will point to its parent, so when the downloading node receives the `“block” message </en/developer-reference#block>`__, the block shouldn’t be an orphan block—all of its parents should be known (even if they haven’t been validated yet). If, despite this, the block received in the `“block” message </en/developer-reference#block>`__ is an orphan block, a headers-first node will discard it immediately.

However, orphan discarding does mean that headers-first nodes will ignore orphan blocks sent by miners in an `unsolicited block push </en/developer-guide#term-unsolicited-block-push>`__.

Transaction Broadcasting
~~~~~~~~~~~~~~~~~~~~~~~~

In order to send a transaction to a peer, an `“inv” message </en/developer-reference#inv>`__ is sent. If a ``getdata`` response message is received, the transaction is sent using ``tx``. The peer receiving this transaction also forwards the transaction in the same manner, given that it is a valid transaction.

Memory Pool
^^^^^^^^^^^

Full peers may keep track of unconfirmed transactions which are eligible to be included in the next block. This is essential for miners who will actually mine some or all of those transactions, but it’s also useful for any peer who wants to keep track of unconfirmed transactions, such as peers serving unconfirmed transaction information to SPV clients.

Because unconfirmed transactions have no permanent status in Bitcoin, Bitcoin Core stores them in non-persistent memory, calling them a memory pool or mempool. When a peer shuts down, its memory pool is lost except for any transactions stored by its wallet. This means that never-mined unconfirmed transactions tend to slowly disappear from the `network </en/developer-guide#term-network>`__ as peers restart or as they purge some transactions to make room in memory for others.

Transactions which are mined into blocks that later become stale blocks may be added back into the memory pool. These re-added transactions may be re-removed from the pool almost immediately if the replacement blocks include them. This is the case in Bitcoin Core, which removes stale blocks from the chain one by one, starting with the tip (highest block). As each block is removed, its transactions are added back to the memory pool. After all of the stale blocks are removed, the replacement blocks are added to the chain one by one, ending with the new tip. As each block is added, any transactions it confirms are removed from the memory pool.

SPV clients don’t have a memory pool for the same reason they don’t relay transactions. They can’t independently verify that a transaction hasn’t yet been included in a block and that it only spends UTXOs, so they can’t know which transactions are eligible to be included in the next block.

Misbehaving Nodes
~~~~~~~~~~~~~~~~~

Take note that for both types of broadcasting, mechanisms are in place to punish misbehaving peers who take up bandwidth and computing resources by sending false information. If a peer gets a banscore above the ``-banscore=<n>`` threshold, he will be banned for the number of seconds defined by ``-bantime=<n>``, which is 86,400 by default (24 hours).

Alerts
~~~~~~

*Removed in*\ `Bitcoin Core 0.13.0 </en/release/v0.13.0>`__

Earlier versions of Bitcoin Core allowed developers and trusted community members to issue `Bitcoin alerts <https://bitcoin.org/en/alerts>`__ to notify users of critical `network </en/developer-guide#term-network>`__-wide issues. This messaging system `was retired <https://bitcoin.org/en/alert/2016-11-01-alert-retirement>`__ in Bitcoin Core v0.13.0; however, internal alerts, partition detection warnings and the ``-alertnotify`` option features remain.
