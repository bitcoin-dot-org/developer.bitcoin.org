



The Developer Guide aims to provide the information you need to understand
Bitcoin and start building Bitcoin-based applications, but it is [not a
specification][]. To make the best use of
this documentation, you may want to install the current version of Bitcoin
Core, either from [source][core git] or from a [pre-compiled executable][core executable].

Questions about Bitcoin development are best asked in one of the
[Bitcoin development communities][dev communities].
Errors or suggestions related to
documentation on Bitcoin.org can be [submitted as an issue][docs issue]
or posted to the [bitcoin-documentation mailing list][].

In the following documentation, some strings have been shortened or wrapped: "[...]"
indicates extra data was removed, and lines ending in a single backslash "\\"
are continued below. If you hover your mouse over a paragraph, cross-reference
links will be shown in blue.  If you hover over a cross-reference link, a brief
definition of the term will be displayed in a tooltip.






[bitcoin URI]: /en/developer-guide#term-bitcoin-uri "A URI which allows receivers to encode payment details so spenders don't have to manually enter addresses and other details."
[certificate chain]: /en/developer-examples#term-certificate-chain "A chain of certificates connecting a individual's leaf certificate to the certificate authority's root certificate."
[coinbase block height]: /en/developer-reference#term-coinbase-block-height "The current block's height encoded into the first bytes of the coinbase field."
[data-pushing opcode]: https://en.bitcoin.it/wiki/Script#Constants "Any opcode from 0x01 to 0x4e which pushes data on to the script evaluation stack."
[fiat]: /en/developer-guide#term-fiat "National currencies such as the dollar or euro."
[intermediate certificate]: /en/developer-examples#term-intermediate-certificate "A intermediate certificate authority certificate which helps connect a leaf (receiver) certificate to a root certificate authority."
[key index]: /en/developer-guide#term-key-index "An index number used in the HD wallet formula to generate child keys from a parent key."
[key pair]: /en/developer-guide#term-key-pair "A private key and its derived public key."
[label]: /en/developer-guide#term-label "The label parameter of a bitcoin: URI which provides the spender with the receiver's name (unauthenticated)."
[leaf certificate]: /en/developer-examples#term-leaf-certificate "The end-node in a certificate chain; in the payment protocol, it is the certificate belonging to the receiver of satoshis."
[merge]: /en/developer-guide#term-merge "Spending, in the same transaction, multiple outputs which can be traced back to different previous spenders, leaking information about how many satoshis you control."
[merge avoidance]: /en/developer-guide#term-merge-avoidance "A strategy for selecting which outputs to spend that avoids merging outputs with different histories that could leak private information."
[message]: /en/developer-guide#term-message "A parameter of bitcoin: URIs which allows the receiver to optionally specify a message to the spender."
[msg_tx]: /en/developer-reference#term-msg_tx "The TXID data type identifier of an inventory on the P2P network."
[msg_block]: /en/developer-reference#term-msg_block "The block header hash data type identifier of an inventory on the P2P network."
[msg_filtered_block]: /en/developer-reference#term-msg_block "An alternative to the block header hash data type identifier of an inventory on the P2P network used to request a merkle block."
[msg_cmpct_block]: /en/developer-reference#term-msg_cmpct_block "An alternative to the block header hash data type identifier of an inventory on the P2P network used to request a compact block."
[msg_witness_block]: /en/developer-reference#term-msg_witness_block "An alternative to the block header hash data type identifier of an inventory on the P2P network used to request a block with witness serialization for SegWit."
[msg_witness_tx]: /en/developer-reference#term-msg_witness_tx "An alternative of the transaction data type identifier of an inventory on the P2P network used to request a transaction with witness serialization for SegWit."
[msg_filtered_witness_block]: /en/developer-reference#term-msg_filtered_witness_block "An alternative to the block header hash data type identifier of an inventory on the P2P network that is reserved for future use and unused."
[network]: /en/developer-guide#term-network "The Bitcoin P2P network which broadcasts transactions and blocks"
[op_checkmultisig]: /en/developer-reference#term-op-checkmultisig "Opcode which returns true if one or more provided signatures (m) sign the correct parts of a transaction and match one or more provided public keys (n)."
[op_checksig]: /en/developer-reference#term-op-checksig "Opcode which returns true if a signature signs the correct parts of a transaction and matches a provided public key."
[op_dup]: /en/developer-reference#term-op-dup "Operation which duplicates the entry below it on the stack."
[op_equal]: /en/developer-reference#term-op-equal "Operation which returns true if the two entries below it on the stack are equivalent."
[op_equalverify]: /en/developer-reference#term-op-equalverify "Operation which terminates the script in failure unless the two entries below it on the stack are equivalent."
[op_hash160]: /en/developer-reference#term-op-hash160 "Operation which converts the entry below it on the stack into a RIPEMD(SHA256()) hashed version of itself."
[op_return]: /en/developer-reference#term-op-return "Operation which terminates the script in failure."
[op_verify]: /en/developer-reference#term-op-verify "Operation which terminates the script if the entry below it on the stack is non-true (zero)."
[output index]: /en/developer-guide#term-output-index "The sequentially-numbered index of outputs in a single transaction starting from 0."
[PaymentDetails]: /en/developer-examples#term-paymentdetails "The PaymentDetails of the payment protocol which allows the receiver to specify the payment details to the spender."
[PaymentRequest]: /en/developer-examples#term-paymentrequest "The PaymentRequest of the payment protocol which contains and allows signing of the PaymentDetails."
[PaymentRequests]: /en/developer-examples#term-paymentrequest "The PaymentRequest of the payment protocol which contains and allows signing of the PaymentDetails."
[PKI]: /en/developer-examples#term-pki "Public Key Infrastructure; usually meant to indicate the X.509 certificate system used for HTTP Secure (https)."
[point function]: /en/developer-guide#term-point-function "The ECDSA function used to create a public key from a private key."
[pp amount]: /en/developer-examples#term-pp-amount "Part of the Output part of the PaymentDetails part of a payment protocol where receivers can specify the amount of satoshis they want paid to a particular pubkey script."
[pp expires]: /en/developer-examples#term-pp-expires "The expires field of a PaymentDetails where the receiver tells the spender when the PaymentDetails expires."
[pp memo]: /en/developer-examples#term-pp-memo "The memo fields of PaymentDetails, Payment, and PaymentACK which allow spenders and receivers to send each other memos."
[pp merchant data]: /en/developer-examples#term-pp-merchant-data "The merchant_data part of PaymentDetails and Payment which allows the receiver to send arbitrary data to the spender in PaymentDetails and receive it back in Payments."
[pp PKI data]: /en/developer-examples#term-pp-pki-data "The pki_data field of a PaymentRequest which provides details such as certificates necessary to validate the request."
[pp pki type]: /en/developer-examples#term-pp-pki-type "The PKI field of a PaymentRequest which tells spenders how to validate this request as being from a specific recipient."
[pp script]: /en/developer-examples#term-pp-script "The script field of a PaymentDetails where the receiver tells the spender what pubkey scripts to pay."
[previous block header hash]: /en/developer-reference#term-previous-block-header-hash "A field in the block header which contains the SHA256(SHA256()) hash of the previous block's header."
[proper money handling]: /en/developer-reference#term-proper-money-handling "Bitcoin amounts need to be correctly processed without introducing rounding errors that could cause monetary loss."
[r]: /en/developer-guide#term-r-parameter "The payment request parameter in a bitcoin: URI."
[receipt]: /en/developer-guide#term-receipt "A cryptographically-verifiable receipt created using parts of a payment request and a confirmed transaction."
[recurrent rebilling]: /en/developer-guide#rebilling-recurring-payments "Billing a spender on a regular schedule"
[refund]: /en/developer-guide#issuing-refunds "A transaction which refunds some or all satoshis received in a previous transaction"
[root certificate]: /en/developer-examples#term-root-certificate "A certificate belonging to a certificate authority (CA)."
[ssl signature]: /en/developer-examples#term-ssl-signature "Signatures created and recognized by major SSL implementations such as OpenSSL."
[standard block relay]: /en/developer-guide#term-standard-block-relay "The regular block relay method: announcing a block with an inv message and waiting for a response."
[transaction]: /en/developer-guide#transactions "A transaction spending satoshis"
[transaction version number]: /en/developer-guide#term-transaction-version-number "A version number prefixed to transactions to allow upgrading."
[transactions]: /en/developer-guide#transactions "A transaction spending satoshis"
[unencrypted wallet]: /en/developer-reference#encryptwallet "A wallet that has not been encrypted with the encryptwallet RPC"
[unique addresses]: /en/developer-guide#term-unique-address "Address which are only used once to protect privacy and increase security."
[unlocked wallet]: /en/developer-reference#walletpassphrase "An encrypted wallet that has been unlocked with the walletpassphrase RPC"
[unsolicited block push]: /en/developer-guide#term-unsolicited-block-push "When a miner sends a block message without sending an inv message first."
[URI QR Code]: /en/developer-guide#term-uri-qr-code "A QR code containing a bitcoin: URI."
[v2 block]: /en/developer-reference#term-v2-block "The current version of Bitcoin blocks."
[verified payments]: /en/developer-guide#verifying-payment "Payments which the receiver believes won't be double spent"
[wallet support]: /en/developer-reference#term-wallet-support "A Bitcoin Core ./configure option that enables (default) or disables the wallet"
[prefilledtransaction]: /en/developer-reference#cmpctblock "A P2P Networking data structure used to represent a vector of a few transactions"
[headerandshortids]: /en/developer-reference#cmpctblock "A P2P Networking data structure used to relay a block header, the short transactions IDs used for matching already-available transactions, and a select few transactions which a peer may be missing"
[blocktransactionsrequest]: /en/developer-reference#getblocktxn "A P2P Networking data structure used to list transaction indexes in a block being requested by a peer"
[blocktransactions]: /en/developer-reference#blocktxn "A P2P Networking data structure used to provide some of the transactions in a block as requested"


[rpc abandontransaction]: /en/developer-reference#abandontransaction
[rpc addmultisigaddress]: /en/developer-reference#addmultisigaddress
[rpc addnode]: /en/developer-reference#addnode
[rpc addwitnessaddress]: /en/developer-reference#addwitnessaddress
[rpc backupwallet]: /en/developer-reference#backupwallet
[rpc bumpfee]: /en/developer-reference#bumpfee
[rpc clearbanned]: /en/developer-reference#clearbanned
[rpc createmultisig]: /en/developer-reference#createmultisig
[rpc createrawtransaction]: /en/developer-reference#createrawtransaction
[rpc decoderawtransaction]: /en/developer-reference#decoderawtransaction
[rpc decodescript]: /en/developer-reference#decodescript
[rpc disconnectnode]: /en/developer-reference#disconnectnode
[rpc dumpprivkey]: /en/developer-reference#dumpprivkey
[rpc dumpwallet]: /en/developer-reference#dumpwallet
[rpc encryptwallet]: /en/developer-reference#encryptwallet
[rpc estimatefee]: /en/developer-reference#estimatefee
[rpc estimatepriority]: /en/developer-reference#estimatepriority
[rpc fundrawtransaction]: /en/developer-reference#fundrawtransaction
[rpc generate]: /en/developer-reference#generate
[rpc generatetoaddress]: /en/developer-reference#generatetoaddress
[rpc getaccount]: /en/developer-reference#getaccount
[rpc getaccountaddress]: /en/developer-reference#getaccountaddress
[rpc getaddednodeinfo]: /en/developer-reference#getaddednodeinfo
[rpc getaddressesbyaccount]: /en/developer-reference#getaddressesbyaccount
[rpc getbalance]: /en/developer-reference#getbalance
[rpc getbestblockhash]: /en/developer-reference#getbestblockhash
[rpc getblock]: /en/developer-reference#getblock
[rpc getblockchaininfo]: /en/developer-reference#getblockchaininfo
[rpc getblockcount]: /en/developer-reference#getblockcount
[rpc getblockhash]: /en/developer-reference#getblockhash
[rpc getblockheader]: /en/developer-reference#getblockheader
[rpc getblocktemplate]: /en/developer-reference#getblocktemplate
[rpc getchaintips]: /en/developer-reference#getchaintips
[rpc getconnectioncount]: /en/developer-reference#getconnectioncount
[rpc getdifficulty]: /en/developer-reference#getdifficulty
[rpc getgenerate]: /en/developer-reference#getgenerate
[rpc gethashespersec]: /en/developer-reference#gethashespersec
[rpc getinfo]: /en/developer-reference#getinfo
[rpc getmemoryinfo]: /en/developer-reference#getmemoryinfo
[rpc getmempoolancestors]: /en/developer-reference#getmempoolancestors
[rpc getmempooldescendants]: /en/developer-reference#getmempooldescendants
[rpc getmempoolentry]: /en/developer-reference#getmempoolentry
[rpc getmempoolinfo]: /en/developer-reference#getmempoolinfo
[rpc getmininginfo]: /en/developer-reference#getmininginfo
[rpc getnettotals]: /en/developer-reference#getnettotals
[rpc getnetworkhashps]: /en/developer-reference#getnetworkhashps
[rpc getnetworkinfo]: /en/developer-reference#getnetworkinfo
[rpc getnewaddress]: /en/developer-reference#getnewaddress
[rpc getpeerinfo]: /en/developer-reference#getpeerinfo
[rpc getrawchangeaddress]: /en/developer-reference#getrawchangeaddress
[rpc getrawmempool]: /en/developer-reference#getrawmempool
[rpc getrawtransaction]: /en/developer-reference#getrawtransaction
[rpc getreceivedbyaccount]: /en/developer-reference#getreceivedbyaccount
[rpc getreceivedbyaddress]: /en/developer-reference#getreceivedbyaddress
[rpc gettransaction]: /en/developer-reference#gettransaction
[rpc gettxout]: /en/developer-reference#gettxout
[rpc gettxoutproof]: /en/developer-reference#gettxoutproof
[rpc gettxoutsetinfo]: /en/developer-reference#gettxoutsetinfo
[rpc getunconfirmedbalance]: /en/developer-reference#getunconfirmedbalance
[rpc getwalletinfo]: /en/developer-reference#getwalletinfo
[rpc getwork]: /en/developer-reference#getwork
[rpc help]: /en/developer-reference#help
[rpc importaddress]: /en/developer-reference#importaddress
[rpc importmulti]: /en/developer-reference#importmulti
[rpc importprivkey]: /en/developer-reference#importprivkey
[rpc importprunedfunds]: /en/developer-reference#importprunedfunds
[rpc importwallet]: /en/developer-reference#importwallet
[rpc keypoolrefill]: /en/developer-reference#keypoolrefill
[rpc listaccounts]: /en/developer-reference#listaccounts
[rpc listaddressgroupings]: /en/developer-reference#listaddressgroupings
[rpc listbanned]: /en/developer-reference#listbanned
[rpc listlockunspent]: /en/developer-reference#listlockunspent
[rpc listreceivedbyaccount]: /en/developer-reference#listreceivedbyaccount
[rpc listreceivedbyaddress]: /en/developer-reference#listreceivedbyaddress
[rpc listsinceblock]: /en/developer-reference#listsinceblock
[rpc listtransactions]: /en/developer-reference#listtransactions
[rpc listunspent]: /en/developer-reference#listunspent
[rpc lockunspent]: /en/developer-reference#lockunspent
[rpc move]: /en/developer-reference#move
[rpc ping]: /en/developer-reference#ping-rpc
[rpc preciousblock]: /en/developer-reference#preciousblock
[rpc pruneblockchain]: /en/developer-reference#pruneblockchain
[rpc prioritisetransaction]: /en/developer-reference#prioritisetransaction
[rpc removeprunedfunds]: /en/developer-reference#removeprunedfunds
[rpc sendfrom]: /en/developer-reference#sendfrom
[rpc sendmany]: /en/developer-reference#sendmany
[rpc sendrawtransaction]: /en/developer-reference#sendrawtransaction
[rpc sendtoaddress]: /en/developer-reference#sendtoaddress
[rpc setaccount]: /en/developer-reference#setaccount
[rpc setban]: /en/developer-reference#setban
[rpc setgenerate]: /en/developer-reference#setgenerate
[rpc setnetworkactive]: /en/developer-reference#setnetworkactive
[rpc settxfee]: /en/developer-reference#settxfee
[rpc signmessage]: /en/developer-reference#signmessage
[rpc signmessagewithprivkey]: /en/developer-reference#signmessagewithprivkey
[rpc signrawtransaction]: /en/developer-reference#signrawtransaction
[rpc stop]: /en/developer-reference#stop
[rpc submitblock]: /en/developer-reference#submitblock
[rpc validateaddress]: /en/developer-reference#validateaddress
[rpc verifychain]: /en/developer-reference#verifychain
[rpc verifymessage]: /en/developer-reference#verifymessage
[rpc verifytxoutproof]: /en/developer-reference#verifytxoutproof
[rpc walletlock]: /en/developer-reference#walletlock
[rpc walletpassphrase]: /en/developer-reference#walletpassphrase
[rpc walletpassphrasechange]: /en/developer-reference#walletpassphrasechange


[rest get block]: /en/developer-reference#get-block
[rest get block-notxdetails]: /en/developer-reference#get-blocknotxdetails
[rest get chaininfo]: /en/developer-reference#get-chaininfo
[rest get getutxos]: /en/developer-reference#get-getutxos
[rest get headers]: /en/developer-reference#get-headers
[rest get mempool-contents]: /en/developer-reference#get-mempoolcontents
[rest get mempool-info]: /en/developer-reference#get-mempoolinfo
[rest get tx]: /en/developer-reference#get-tx


[addr message]: /en/developer-reference#addr "The P2P network message which relays IP addresses and port numbers of active nodes to other nodes and clients, allowing decentralized peer discovery."
[alert message]: /en/developer-reference#alert "The P2P network message which sends alerts in case of major software problems."
[block message]: /en/developer-reference#block "The P2P network message which sends a serialized block"
[feefilter message]: /en/developer-reference#feefilter "The P2P network message which requests the receiving peer not relay any transactions below the specified fee rate"
[filteradd message]: /en/developer-reference#filteradd "A P2P protocol message used to add a data element to an existing bloom filter."
[filterclear message]: /en/developer-reference#filterclear "A P2P protocol message used to remove an existing bloom filter."
[filterload message]: /en/developer-reference#filterclear "A P2P protocol message used to send a filter to a remote peer, requesting that they only send transactions which match the filter."
[getaddr message]: /en/developer-reference#getaddr "A P2P protool message used to request an addr message containing connection information for other nodes"
[getblocks message]: /en/developer-reference#getblocks "A P2P protocol message used to request an inv message containing a range of block header hashes"
[getdata message]: /en/developer-reference#getdata "A P2P protocol message used to request one or more transactions, blocks, or merkle blocks"
[getheaders message]: /en/developer-reference#getheaders "A P2P protocol message used to request a range of block headers"
[headers message]: /en/developer-reference#headers "A P2P protocol message containing one or more block headers"
[inv message]: /en/developer-reference#inv "A P2P protocol message used to send inventories of transactions and blocks known to the transmitting peer"
[mempool message]: /en/developer-reference#mempool "A P2P protocol message used to request one or more inv messages with currently-unconfirmed transactions"
[merkleblock message]: /en/developer-reference#merkleblock "A P2P protocol message used to request a filtered block useful for SPV proofs"
[cmpctblock message]: /en/developer-reference#cmpctblock "A P2P protocol message used to request a compact block"
[sendcmpct message]: /en/developer-reference#sendcmpct "A P2P protocol message used to begin the receipt of a compact block between a peer and node"
[getblocktxn message]: /en/developer-reference#getblocktxn "A P2P protocol message used to request block transactions for the given block hash"
[blocktxn message]: /en/developer-reference#blocktxn "A P2P protocol message used to send available transaction data to requesting peers for a given block hash"
[notfound message]: /en/developer-reference#notfound "A P2P protocol message sent to indicate that the requested data was not available"
[ping message]: /en/developer-reference#ping "A P2P network message used to see if the remote host is still connected"
[pong message]: /en/developer-reference#pong "A P2P network message used to reply to a P2P network ping message"
[reject message]: /en/developer-reference#reject "A P2P network message used to indicate a previously-received message was rejected for some reason"
[sendheaders message]: /en/developer-reference#sendheaders "A P2P network message used to request new blocks be announced through headers messages rather than inv messages"
[tx message]: /en/developer-reference#tx "A P2P protocol message which sends a single serialized transaction"
[verack message]: /en/developer-reference#verack "A P2P network message sent in reply to a version message to confirm a connection has been established"
[version message]: /en/developer-reference#version "A P2P network message sent at the begining of a connection to allow protocol version negotiation"


[bandwidth sharing guide]: /en/full-node
[bcc contribute]: /en/bitcoin-core/contribute/
[bcc contribute documentation]: /en/bitcoin-core/contribute/documentation
[bcc contribute issues]: /en/bitcoin-core/contribute/issues
[bcc contribute support]: /en/bitcoin-core/contribute/support
[bcc contribute translations]: /en/bitcoin-core/contribute/translations
[bcc decentralized peer discovery]: /en/bitcoin-core/features/privacy#decentralized-peer-discovery
[bcc documentation]: /en/bitcoin-core/help#documentation
[bcc download]: /en/download
[bcc features]: /en/bitcoin-core/features/
[bcc forums]: /en/bitcoin-core/help#forums
[bcc help]: /en/bitcoin-core/help
[bcc live help]: /en/bitcoin-core/help#live
[bcc main]: /en/bitcoin-core/
[bcc network support]: /en/bitcoin-core/features/network-support
[bcc privacy]: /en/bitcoin-core/features/privacy
[bcc privacy data leaking]: /en/bitcoin-core/features/privacy#perfect-privacy-for-received-transactions
[bcc requirements]: /en/bitcoin-core/features/requirements
[bcc user interface]: /en/bitcoin-core/features/user-interface
[bcc user interface lightweight]: /en/bitcoin-core/features/user-interface#lightweight
[bcc validation]: /en/bitcoin-core/features/validation
[bcc validation decentralization]: /en/bitcoin-core/features/validation#help-protect-decentralization
[bcc validation do you validate]: /en/bitcoin-core/features/validation#do-you-validate
[bcc validation protection]: /en/bitcoin-core/features/validation#how-validation-protects-your-bitcoins
[bcc version history]: /en/version-history

[Bitcoin Core 0.6.0]: /en/release/v0.6.0
[Bitcoin Core 0.6.1]: /en/release/v0.6.1
[Bitcoin Core 0.7.0]: /en/release/v0.7.0
[Bitcoin Core 0.8.0]: /en/release/v0.8.0
[Bitcoin Core 0.9.0]: /en/release/v0.9.0
[Bitcoin Core 0.9.1]: /en/release/v0.9.1
[Bitcoin Core 0.9.2]: /en/release/v0.9.2
[Bitcoin Core 0.9.3]: /en/release/v0.9.3
[Bitcoin Core 0.10.0]: /en/release/v0.10.0
[Bitcoin Core 0.10.1]: /en/release/v0.10.1
[Bitcoin Core 0.10.2]: /en/release/v0.10.2
[Bitcoin Core 0.10.3]: /en/release/v0.10.3
[Bitcoin Core 0.11.0]: /en/release/v0.11.0
[Bitcoin Core 0.11.1]: /en/release/v0.11.1
[Bitcoin Core 0.11.2]: /en/release/v0.11.2
[Bitcoin Core 0.12.0]: /en/release/v0.12.0
[Bitcoin Core 0.12.1]: /en/release/v0.12.1
[Bitcoin Core 0.13.0]: /en/release/v0.13.0
[Bitcoin Core 0.13.1]: /en/release/v0.13.1
[Bitcoin Core 0.13.2]: /en/release/v0.13.2
[Bitcoin Core 0.14.0]: /en/release/v0.14.0
[Bitcoin Core 0.14.1]: /en/release/v0.14.1
[Bitcoin Core 0.14.2]: /en/release/v0.14.2
[bitcoin URI subsection]: /en/developer-guide#bitcoin-uri
[bitcoind initial setup]: /en/developer-examples
[bitcoinpdf]: https://bitcoin.org/en/bitcoin-paper
[choose your wallet]: /en/choose-your-wallet
[communities]: /en/community
[core executable]: /en/download
[dev communities]: /en/development#devcommunities
[developer documentation]: /en/developer-documentation
[devex complex raw transaction]: /en/developer-examples#complex-raw-transaction
[devex payment protocol]: /en/developer-examples#payment-protocol
[devexamples]: /en/developer-examples
[devguide]: /en/developer-guide
[devguide avoiding key reuse]: /en/developer-guide#avoiding-key-reuse
[devguide hardened keys]: /en/developer-guide#hardened-keys
[devguide payment processing]: /en/developer-guide#payment-processing
[devguide wallets]: /en/developer-guide#wallets
[devref]: /en/developer-reference
[devref wallets]: /en/developer-reference#wallets
[locktime parsing rules]: /en/developer-guide#locktime_parsing_rules
[Merge Avoidance subsection]: /en/developer-guide#merge-avoidance
[micropayment channel]: /en/developer-guide#term-micropayment-channel
[not a specification]: /en/developer-reference#not-a-specification
[raw transaction format]: /en/developer-reference#raw-transaction-format
[REST]: /en/developer-reference#http-rest
[RPC]: /en/developer-reference#remote-procedure-calls-rpcs
[RPCs]: /en/developer-reference#remote-procedure-calls-rpcs
[section block chain]: /en/developer-guide#block-chain
[section block header]: /en/developer-reference#block-headers
[section block versions]: /en/developer-reference#block-versions
[section creating a bloom filter]: /en/developer-examples#creating-a-bloom-filter
[section compactSize unsigned integer]: /en/developer-reference#compactsize-unsigned-integers
[section detecting forks]: /en/developer-guide#detecting-forks
[section getblocktemplate]: /en/developer-guide#getblocktemplate-rpc
[section hash byte order]: /en/developer-reference#hash-byte-order
[section merkle trees]: /en/developer-reference#merkle-trees
[section merkleblock example]: /en/developer-examples#parsing-a-merkleblock
[section message header]: /en/developer-reference#message-headers
[section p2p reference]: /en/developer-reference#p2p-network
[section protocol versions]: /en/developer-reference#protocol-versions
[section rpc quick reference]: /en/developer-reference#rpc-quick-reference
[section serialized blocks]: /en/developer-reference#serialized-blocks
[section simple raw transaction]: /en/developer-examples#simple-raw-transaction
[section verifying payment]: /en/developer-guide#verifying-payment
[secure your wallet]: /en/secure-your-wallet
[signature script modification warning]: /en/developer-reference#signature_script_modification_warning
[v0.8 chain fork]: /en/alert/2013-03-11-chain-fork
[Verification subsection]: /en/developer-guide#verifying-payment
[X509Certificates]: /en/developer-examples#term-x509certificates


[BIP9]: https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki
[BIP9 assignments]: https://github.com/bitcoin/bips/blob/master/bip-0009/assignments.mediawiki
[BIP14]: https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki
[BIP16]: https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki
[BIP21]: https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki
[BIP22]: https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki
[BIP23]: https://github.com/bitcoin/bips/blob/master/bip-0023.mediawiki
[BIP30]: https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki
[BIP31]: https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki
[BIP32]: https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki
[BIP34]: https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki
[BIP35]: https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki
[BIP37]: https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki
[BIP39]: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
[BIP50]: https://github.com/bitcoin/bips/blob/master/bip-0050.mediawiki
[BIP61]: https://github.com/bitcoin/bips/blob/master/bip-0061.mediawiki
[BIP62]: https://github.com/bitcoin/bips/blob/master/bip-0062.mediawiki
[BIP66]: https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki
[BIP70]: https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki
[BIP71]: https://github.com/bitcoin/bips/blob/master/bip-0071.mediawiki
[BIP72]: https://github.com/bitcoin/bips/blob/master/bip-0072.mediawiki
[BIP111]: https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki
[BIP112]: https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki
[BIP113]: https://github.com/bitcoin/bips/blob/master/bip-0113.mediawiki
[BIP125]: https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki
[BIP130]: https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki
[BIP133]: https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki
[BIP141]: https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki
[BIP144]: https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki
[BIP151]: https://github.com/bitcoin/bips/blob/master/bip-0151.mediawiki
[BIP152]: https://github.com/bitcoin/bips/blob/master/bip-0152.mediawiki
[CVE-2012-2459]: https://en.bitcoin.it/wiki/CVEs#CVE-2012-2459
[RFC5737]: http://tools.ietf.org/html/rfc5737
[secp256k1]: http://www.secg.org/sec2-v2.pdf


[#bitcoin]: https://webchat.freenode.net/?channels=bitcoin&uio=d4
[#bitcoin-dev]: https://webchat.freenode.net/?channels=bitcoin-dev&uio=d4
[#bitcoin-mining]: https://webchat.freenode.net/?channels=bitcoin-mining&uio=d4
[#bitcoin-wiki]: https://webchat.freenode.net/?channels=bitcoin-wiki&uio=d4
[0bin]: http://0bin.net/
[bcc automated testing]: https://github.com/bitcoin/bitcoin/blob/master/README.md#automated-testing
[bcc configuration]: https://en.bitcoin.it/wiki/Running_Bitcoin
[bcc data directory]: https://en.bitcoin.it/wiki/Data_directory
[bcc issues]: https://github.com/bitcoin/bitcoin/issues
[bcc new issue]: https://github.com/bitcoin/bitcoin/issues/new
[bcc pulls]: https://github.com/bitcoin/bitcoin/pulls
[bcc tor]: https://en.bitcoin.it/wiki/Tor
[bcc tor hs]: https://en.bitcoin.it/wiki/Tor#Hidden_services
[core github tag]: https://github.com/bitcoin-dot-org/bitcoin.org/labels/Core
[BFGMiner]: https://github.com/luke-jr/bfgminer
[Bitcoin beginners]: http://www.reddit.com/r/bitcoinbeginners
[Bitcoin Core]: https://bitcoin.org/en/download
[Bitcoin Core 0.1.6]: https://github.com/bitcoin/bitcoin/commit/cc0b4c3b62367a2aebe5fc1f4d0ed4b97e9c2ac9
[Bitcoin Core 0.2.9]: https://github.com/bitcoin/bitcoin/commit/42605ce8bcc9bd01b86491c74fee14de77960868
[Bitcoin Core 0.3.11]: https://github.com/bitcoin/bitcoin/commit/343328c6b8db85e58a1feea85f0d10e62967fa19
[Bitcoin Core 0.3.15]: https://github.com/bitcoin/bitcoin/commit/c891967b6fcab2e8dc4ce0c787312b36c07efa4d
[Bitcoin Core 0.3.18]: https://github.com/bitcoin/bitcoin/commit/82201801336f64ee77851b9eaab9383ee4e442f0
[Bitcoin Core build unix]: https://github.com/bitcoin/bitcoin/blob/master/doc/build-unix.md
[Bitcoin Core docs directory]: https://github.com/bitcoin/bitcoin/tree/master/doc
[bitcoin core fee drop commit]: https://github.com/bitcoin/bitcoin/commit/6a4c196dd64da2fd33dc7ae77a8cdd3e4cf0eff1
[Bitcoin Core issue #2381]: https://github.com/bitcoin/bitcoin/issues/2381
[Bitcoin Core master]: https://github.com/bitcoin/bitcoin
[Bitcoin Core pull #4468]: https://github.com/bitcoin/bitcoin/pull/4468
[Bitcoin core transifex]: https://www.transifex.com/projects/p/bitcoin/
[Bitcoin reddit]: http://www.reddit.com/r/Bitcoin
[Bitcoin reddit new]: http://www.reddit.com/r/Bitcoin/new
[Bitcoin Seeder]: https://github.com/sipa/bitcoin-seeder
[Bitcoin stackexchange]: http://bitcoin.stackexchange.com
[Bitcoin stackexchange tag bitcoin-qt]: http://bitcoin.stackexchange.com/questions/tagged/bitcoin-qt
[bitcoin-documentation mailing list]: https://groups.google.com/forum/#!forum/bitcoin-documentation
[BitcoinJ]: http://bitcoinj.github.io
[BitcoinJ documentation about pending transaction safety]: https://bitcoinj.github.io/security-model#pending-transactions
[bitcoinj micropayment tutorial]: https://bitcoinj.github.io/working-with-micropayments
[block170]: https://live.blockcypher.com/btc/block/00000000d1145790a8694403d4063f323d499e655c83426834d4ce2f8dd4a2ee/
[casascius address utility]: https://github.com/casascius/Bitcoin-Address-Utility
[core base58.h]: https://github.com/bitcoin/bitcoin/blob/master/src/base58.h
[core chainparams.cpp]: https://github.com/bitcoin/bitcoin/blob/master/src/chainparams.cpp
[core git]: https://github.com/bitcoin/bitcoin
[core paymentrequest.proto]: https://github.com/bitcoin/bitcoin/blob/master/src/qt/paymentrequest.proto
[core script.h]: https://github.com/bitcoin/bitcoin/blob/master/src/script/script.h
[creative commons attribution 3.0 license]: https://creativecommons.org/licenses/by/3.0/
[DER]: https://en.wikipedia.org/wiki/X.690#DER_encoding
[dig command]: https://en.wikipedia.org/wiki/Dig_%28Unix_command%29
[DNS A records]: http://tools.ietf.org/html/rfc1035#section-3.2.2
[DNS Seed Policy]: https://github.com/bitcoin/bitcoin/blob/master/doc/dnsseed-policy.md
[docs issue]: https://github.com/bitcoin-dot-org/bitcoin.org/issues
[ECDSA]: https://en.wikipedia.org/wiki/Elliptic_Curve_DSA
[edit bandwidth sharing guide]: https://github.com/bitcoin-dot-org/bitcoin.org/edit/master/en/full-node.md
[Electrum server]: https://github.com/spesmilo/electrum-server
[Eloipool]: https://github.com/luke-jr/eloipool
[errors in docs]: https://github.com/bitcoin-dot-org/bitcoin.org/issues?q=is%3Aissue+label%3A%22Dev+Docs%22
[fake satoshi transaction]: https://www.reddit.com/r/Bitcoin/comments/3fv42j/blockchaininfo_spoofed_transactions_problem_aug_4/
[forum tech support]: https://bitcointalk.org/index.php?board=4.0
[ghash betcoin double spend]: https://bitcointalk.org/index.php?topic=321630.msg3445371
[gitian sigs]: https://github.com/bitcoin/gitian.sigs
[high-speed block relay network]: https://www.mail-archive.com/bitcoin-development@lists.sourceforge.net/msg03189.html
[HMAC-SHA512]: https://en.wikipedia.org/wiki/HMAC
[HTTP basic authentication]: https://en.wikipedia.org/wiki/Basic_access_authentication
[HTTP longpoll]: https://en.wikipedia.org/wiki/Push_technology#Long_polling
[information theoretic security]: https://en.wikipedia.org/wiki/Information_theoretic_security
[inherit bitcoins]: http://bitcoin.stackexchange.com/q/38692/21052
[IP-to-IP payment protocol]: https://en.bitcoin.it/wiki/IP_Transactions
[IPv4-mapped IPv6 addresses]: http://en.wikipedia.org/wiki/IPv6#IPv4-mapped_IPv6_addresses
[irc channels]: https://en.bitcoin.it/wiki/IRC_channels
[JSON-RPC version 1.0]: http://json-rpc.org/wiki/specification
[JSON-RPC request batching]: http://www.jsonrpc.org/specification#batch
[july 2015 chain forks]: https://en.bitcoin.it/wiki/July_2015_chain_forks
[libblkmaker]: https://github.com/bitcoin/libblkmaker
[localhost]: https://en.wikipedia.org/wiki/Localhost
[lying consistently is hard]: https://groups.google.com/forum/#!msg/bitcoinj/Ys13qkTwcNg/9qxnhwnkeoIJ
[makeseeds script]: https://github.com/bitcoin/bitcoin/tree/master/contrib/seeds
[mozilla's bug reporting documentation]: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#Writing_precise_steps_to_reproduce
[murmur3]: https://en.wikipedia.org/wiki/MurmurHash
[man-in-the-middle]: https://en.wikipedia.org/wiki/Man-in-the-middle_attack
[MIME]: https://en.wikipedia.org/wiki/Internet_media_type
[MIT license]: http://opensource.org/licenses/MIT
[mozrootstore]: https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/
[native irc client]: https://en.wikipedia.org/wiki/List_of_IRC_clients
[netcat]: https://en.wikipedia.org/wiki/Netcat
[nop opcodes]: https://en.bitcoin.it/wiki/Script#Reserved_words
[offline transactions]: http://bitcoin.stackexchange.com/a/34122/21052
[open a pull request]: https://github.com/bitcoin-dot-org/bitcoin.org#working-with-github
[open an issue]: https://github.com/bitcoin-dot-org/bitcoin.org/issues/new
[open assets protocol]: https://github.com/OpenAssets/open-assets-protocol/blob/master/specification.mediawiki
[Payment Request Generator]: https://github.com/gavinandresen/paymentrequest/blob/master/php/demo_website/createpaymentrequest.php
[peter todd p2sh example]: https://github.com/petertodd/checklocktimeverify-demos/blob/master/lib/python-bitcoinlib/examples/publish-text.py
[Piotr Piasecki's testnet faucet]: https://tpfaucet.appspot.com/
[prime symbol]: https://en.wikipedia.org/wiki/Prime_%28symbol%29
[protobuf]: https://developers.google.com/protocol-buffers/
[python-bitcoinlib]: https://github.com/petertodd/python-bitcoinlib
[python-blkmaker]: https://gitorious.org/bitcoin/python-blkmaker
[Satoshi Nakamoto]: https://en.bitcoin.it/wiki/Satoshi_Nakamoto
[setup tor]: https://www.torproject.org/
[SHA256]: https://en.wikipedia.org/wiki/SHA-2
[Stratum mining protocol]: http://mining.bitcoin.cz/stratum-mining
[study of SPV privacy over tor]: http://arxiv.org/abs/1410.6079
[Tor]: https://en.wikipedia.org/wiki/Tor_%28anonymity_network%29
[transifex]: https://www.transifex.com/projects/p/bitcoinorg/
[unix epoch time]: https://en.wikipedia.org/wiki/Unix_time
[URI encoded]: https://tools.ietf.org/html/rfc3986
[wiki bitcoin core compatible devices arm]: https://en.bitcoin.it/wiki/Bitcoin_Core_compatible_devices#ARM-based_Chipsets
[wiki bitcoin core documentation]: https://en.bitcoin.it/wiki/Category:Bitcoin_Core_documentation
[wiki create account]: https://en.bitcoin.it/w/index.php?title=Special:UserLogin&type=signup
[wiki enable editing]: https://en.bitcoin.it/wiki/Bitcoin_Wiki:Editing_privileges
[wiki getblocktemplate]: https://en.bitcoin.it/wiki/Getblocktemplate
[wiki proper money handling]: https://en.bitcoin.it/wiki/Proper_Money_Handling_%28JSON-RPC%29
[wiki template bitcoin core documentation]: https://en.bitcoin.it/wiki/Template:Bitcoin_Core_documentation
[wiki script]: https://en.bitcoin.it/wiki/Script
[x509]: https://en.wikipedia.org/wiki/X.509


[core bloom.cpp hash]: https://github.com/bitcoin/bitcoin/blob/cbf28c6619fe348a258dfd7d08bdbd2392d07511/src/bloom.cpp#L46
[MAX_SIZE]: https://github.com/bitcoin/bitcoin/blob/60abd463ac2eaa8bc1d616d8c07880dc53d97211/src/serialize.h#L23
[rpcprotocol.h]: https://github.com/bitcoin/bitcoin/blob/f914f1a746d7f91951c1da262a4a749dd3ebfa71/src/rpcprotocol.h

[/en/glossary/51-percent-attack]: ../reference/glossary.html#51-percent-attack
[/en/glossary/address]: ../reference/glossary.html#address
[/en/glossary/base58check]: ../reference/glossary.html#base58check
[/en/glossary/block]: ../reference/glossary.html#block
[/en/glossary/block-chain]: ../reference/glossary.html#block-chain
[/en/glossary/block-header]: ../reference/glossary.html#block-header
[/en/glossary/block-height]: ../reference/glossary.html#block-height
[/en/glossary/block-reward]: ../reference/glossary.html#block-reward
[/en/glossary/block-size-limit]: ../reference/glossary.html#block-size-limit
[/en/glossary/blocks-first-sync]: ../reference/glossary.html#blocks-first-sync
[/en/glossary/bloom-filter]: ../reference/glossary.html#bloom-filter
[/en/glossary/chain-code]: ../reference/glossary.html#chain-code
[/en/glossary/change-address]: ../reference/glossary.html#change-address
[/en/glossary/child-key]: ../reference/glossary.html#child-key
[/en/glossary/coinbase]: ../reference/glossary.html#coinbase
[/en/glossary/coinbase-transaction]: ../reference/glossary.html#coinbase-transaction
[/en/glossary/compactsize]: ../reference/glossary.html#compactsize
[/en/glossary/compressed-public-key]: ../reference/glossary.html#compressed-public-key
[/en/glossary/confirmation-score]: ../reference/glossary.html#confirmation-score
[/en/glossary/consensus]: ../reference/glossary.html#consensus
[/en/glossary/consensus-rules]: ../reference/glossary.html#consensus-rules
[/en/glossary/cpfp]: ../reference/glossary.html#cpfp
[/en/glossary/denominations]: ../reference/glossary.html#denominations
[/en/glossary/difficulty]: ../reference/glossary.html#difficulty
[/en/glossary/dns-seed]: ../reference/glossary.html#dns-seed
[/en/glossary/double-spend]: ../reference/glossary.html#double-spend
[/en/glossary/escrow-contract]: ../reference/glossary.html#escrow-contract
[/en/glossary/extended-key]: ../reference/glossary.html#extended-key
[/en/glossary/fork]: ../reference/glossary.html#fork
[/en/glossary/genesis-block]: ../reference/glossary.html#genesis-block
[/en/glossary/hard-fork]: ../reference/glossary.html#hard-fork
[/en/glossary/hardened-extended-key]: ../reference/glossary.html#hardened-extended-key
[/en/glossary/hd-protocol]: ../reference/glossary.html#hd-protocol
[/en/glossary/hd-wallet-seed]: ../reference/glossary.html#hd-wallet-seed
[/en/glossary/header-chain]: ../reference/glossary.html#header-chain
[/en/glossary/headers-first-sync]: ../reference/glossary.html#headers-first-sync
[/en/glossary/high-priority-transaction]: ../reference/glossary.html#high-priority-transaction
[/en/glossary/initial-block-download]: ../reference/glossary.html#initial-block-download
[/en/glossary/input]: ../reference/glossary.html#input
[/en/glossary/internal-byte-order]: ../reference/glossary.html#internal-byte-order
[/en/glossary/inventory]: ../reference/glossary.html#inventory
[/en/glossary/locktime]: ../reference/glossary.html#locktime
[/en/glossary/mainnet]: ../reference/glossary.html#mainnet
[/en/glossary/malleability]: ../reference/glossary.html#malleability
[/en/glossary/masf]: ../reference/glossary.html#masf
[/en/glossary/master-chain-code-and-private-key]: ../reference/glossary.html#master-chain-code-and-private-key
[/en/glossary/merkle-block]: ../reference/glossary.html#merkle-block
[/en/glossary/merkle-root]: ../reference/glossary.html#merkle-root
[/en/glossary/merkle-tree]: ../reference/glossary.html#merkle-tree
[/en/glossary/message-header]: ../reference/glossary.html#message-header
[/en/glossary/minimum-relay-fee]: ../reference/glossary.html#minimum-relay-fee
[/en/glossary/mining]: ../reference/glossary.html#mining
[/en/glossary/multisig]: ../reference/glossary.html#multisig
[/en/glossary/nbits]: ../reference/glossary.html#nbits
[/en/glossary/node]: ../reference/glossary.html#node
[/en/glossary/null-data-transaction]: ../reference/glossary.html#null-data-transaction
[/en/glossary/op-code]: ../reference/glossary.html#op-code
[/en/glossary/orphan-block]: ../reference/glossary.html#orphan-block
[/en/glossary/outpoint]: ../reference/glossary.html#outpoint
[/en/glossary/output]: ../reference/glossary.html#output
[/en/glossary/p2pkh-address]: ../reference/glossary.html#p2pkh-address
[/en/glossary/p2sh-address]: ../reference/glossary.html#p2sh-address
[/en/glossary/p2sh-multisig]: ../reference/glossary.html#p2sh-multisig
[/en/glossary/parent-key]: ../reference/glossary.html#parent-key
[/en/glossary/payment-protocol]: ../reference/glossary.html#payment-protocol
[/en/glossary/private-key]: ../reference/glossary.html#private-key
[/en/glossary/proof-of-work]: ../reference/glossary.html#proof-of-work
[/en/glossary/pubkey-script]: ../reference/glossary.html#pubkey-script
[/en/glossary/public-key]: ../reference/glossary.html#public-key
[/en/glossary/rbf]: ../reference/glossary.html#rbf
[/en/glossary/redeem-script]: ../reference/glossary.html#redeem-script
[/en/glossary/regression-test-mode]: ../reference/glossary.html#regression-test-mode
[/en/glossary/rpc-byte-order]: ../reference/glossary.html#rpc-byte-order
[/en/glossary/sequence-number]: ../reference/glossary.html#sequence-number
[/en/glossary/serialized-block]: ../reference/glossary.html#serialized-block
[/en/glossary/serialized-transaction]: ../reference/glossary.html#serialized-transaction
[/en/glossary/sighash-all]: ../reference/glossary.html#sighash-all
[/en/glossary/sighash-anyonecanpay]: ../reference/glossary.html#sighash-anyonecanpay
[/en/glossary/sighash-none]: ../reference/glossary.html#sighash-none
[/en/glossary/sighash-single]: ../reference/glossary.html#sighash-single
[/en/glossary/signature]: ../reference/glossary.html#signature
[/en/glossary/signature-hash]: ../reference/glossary.html#signature-hash
[/en/glossary/signature-script]: ../reference/glossary.html#signature-script
[/en/glossary/simplified-payment-verification]: ../reference/glossary.html#simplified-payment-verification
[/en/glossary/soft-fork]: ../reference/glossary.html#soft-fork
[/en/glossary/stale-block]: ../reference/glossary.html#stale-block
[/en/glossary/standard-transaction]: ../reference/glossary.html#standard-transaction
[/en/glossary/start-string]: ../reference/glossary.html#start-string
[/en/glossary/testnet]: ../reference/glossary.html#testnet
[/en/glossary/token]: ../reference/glossary.html#token
[/en/glossary/transaction-fee]: ../reference/glossary.html#transaction-fee
[/en/glossary/txid]: ../reference/glossary.html#txid
[/en/glossary/uasf]: ../reference/glossary.html#uasf
[/en/glossary/unspent-transaction-output]: ../reference/glossary.html#unspent-transaction-output
[/en/glossary/wallet]: ../reference/glossary.html#wallet
[/en/glossary/wallet-import-format]: ../reference/glossary.html#wallet-import-format
[/en/glossary/watch-only-address]: ../reference/glossary.html#watch-only-address
