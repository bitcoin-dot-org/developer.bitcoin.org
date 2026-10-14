.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

RPC API Reference
=================

Blockchain RPCs
---------------

.. toctree::
  :maxdepth: 1

  dumptxoutset
  getbestblockhash
  getblock
  getblockchaininfo
  getblockcount
  getblockfilter
  getblockfrompeer
  getblockhash
  getblockheader
  getblockstats
  getchainstates
  getchaintips
  getchaintxstats
  getdeploymentinfo
  getdescriptoractivity
  getdifficulty
  getmempoolancestors
  getmempooldescendants
  getmempoolentry
  getmempoolinfo
  getrawmempool
  gettxout
  gettxoutproof
  gettxoutsetinfo
  gettxspendingprevout
  importmempool
  loadtxoutset
  preciousblock
  pruneblockchain
  savemempool
  scanblocks
  scantxoutset
  verifychain
  verifytxoutproof
  waitforblock
  waitforblockheight
  waitfornewblock

Control RPCs
------------

.. toctree::
  :maxdepth: 1

  getmemoryinfo
  getrpcinfo
  help
  logging
  stop
  uptime

Generating RPCs
---------------

.. toctree::
  :maxdepth: 1

  generateblock
  generatetoaddress
  generatetodescriptor

Mining RPCs
-----------

.. toctree::
  :maxdepth: 1

  getblocktemplate
  getmininginfo
  getnetworkhashps
  getprioritisedtransactions
  prioritisetransaction
  submitblock
  submitheader

Network RPCs
------------

.. toctree::
  :maxdepth: 1

  addnode
  clearbanned
  disconnectnode
  getaddednodeinfo
  getaddrmaninfo
  getconnectioncount
  getnettotals
  getnetworkinfo
  getnodeaddresses
  getpeerinfo
  listbanned
  ping
  setban
  setnetworkactive

Rawtransactions RPCs
--------------------

.. toctree::
  :maxdepth: 1

  analyzepsbt
  combinepsbt
  combinerawtransaction
  converttopsbt
  createpsbt
  createrawtransaction
  decodepsbt
  decoderawtransaction
  decodescript
  descriptorprocesspsbt
  finalizepsbt
  fundrawtransaction
  getrawtransaction
  joinpsbts
  sendrawtransaction
  signrawtransactionwithkey
  submitpackage
  testmempoolaccept
  utxoupdatepsbt

Signer RPCs
-----------

.. toctree::
  :maxdepth: 1

  enumeratesigners

Util RPCs
---------

.. toctree::
  :maxdepth: 1

  createmultisig
  deriveaddresses
  estimatesmartfee
  getdescriptorinfo
  getindexinfo
  signmessagewithprivkey
  validateaddress
  verifymessage

Wallet RPCs
-----------

**Note:** the wallet RPCs are only available if Bitcoin Core was built
with wallet support, which is the default.

.. toctree::
  :maxdepth: 1

  abandontransaction
  abortrescan
  backupwallet
  bumpfee
  createwallet
  createwalletdescriptor
  encryptwallet
  getaddressesbylabel
  getaddressinfo
  getbalance
  getbalances
  gethdkeys
  getnewaddress
  getrawchangeaddress
  getreceivedbyaddress
  getreceivedbylabel
  gettransaction
  getwalletinfo
  importdescriptors
  importprunedfunds
  keypoolrefill
  listaddressgroupings
  listdescriptors
  listlabels
  listlockunspent
  listreceivedbyaddress
  listreceivedbylabel
  listsinceblock
  listtransactions
  listunspent
  listwalletdir
  listwallets
  loadwallet
  lockunspent
  migratewallet
  psbtbumpfee
  removeprunedfunds
  rescanblockchain
  restorewallet
  send
  sendall
  sendmany
  sendtoaddress
  setlabel
  settxfee
  setwalletflag
  signmessage
  signrawtransactionwithwallet
  simulaterawtransaction
  unloadwallet
  walletcreatefundedpsbt
  walletdisplayaddress
  walletlock
  walletpassphrase
  walletpassphrasechange
  walletprocesspsbt

