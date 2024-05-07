:orphan:

Terms
=====

.. note:: This is a temporary page with references used as targets for links in the documentation. They should be replaced by adding proper labels inline in the respective pages. This is more easily be done manually so this page acts as a temporary placeholder for that until the automatic import and conversion to RST is completed.

.. _signature_script_modification_warning:

signature_script_modification_warning (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#signature_script_modification_warning>`__)

.. _term-bitcoin-uri:

term-bitcoin-uri (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-bitcoin-uri>`__): A URI which allows receivers to encode payment details so spenders don't have to manually enter addresses and other details.

.. _term-certificate-chain:

term-certificate-chain (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-certificate-chain>`__): A chain of certificates connecting a individual's leaf certificate to the certificate authority's root certificate.

.. _term-coinbase-block-height:

term-coinbase-block-height (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-coinbase-block-height>`__): The current block's height encoded into the first bytes of the coinbase field.

.. _term-fiat:

term-fiat (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-fiat>`__): National currencies such as the dollar or euro.

.. _term-intermediate-certificate:

term-intermediate-certificate (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-intermediate-certificate>`__): A intermediate certificate authority certificate which helps connect a leaf (receiver) certificate to a root certificate authority.

.. _term-key-index:

term-key-index (wallets-guide) (`original target <https://bitcoin.org/en/wallets-guide#term-key-index>`__): An index number used in the HD wallet formula to generate child keys from a parent key.

.. _term-key-pair:

term-key-pair (transactions-guide) (`original target <https://bitcoin.org/en/transactions-guide#term-key-pair>`__): A private key and its derived public key.

.. _term-label:

term-label (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-label>`__): The label parameter of a bitcoin: URI which provides the spender with the receiver's name (unauthenticated).

.. _term-leaf-certificate:

term-leaf-certificate (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-leaf-certificate>`__): The end-node in a certificate chain; in the payment protocol, it is the certificate belonging to the receiver of satoshis.

.. _term-merge:

term-merge (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-merge>`__): Spending, in the same transaction, multiple outputs which can be traced back to different previous spenders, leaking information about how many satoshis you control.

.. _term-merge-avoidance:

term-merge-avoidance (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-merge-avoidance>`__): A strategy for selecting which outputs to spend that avoids merging outputs with different histories that could leak private information.

.. _term-message:

term-message (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-message>`__): A parameter of bitcoin: URIs which allows the receiver to optionally specify a message to the spender.

.. _term-micropayment-channel:

term-micropayment-channel (contracts-guide) (`original target <https://bitcoin.org/en/contracts-guide#term-micropayment-channel>`__)

.. _term-msg_block:

term-msg_block (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-msg_block>`__): The block header hash data type identifier of an inventory on the P2P network.

.. _term-msg_cmpct_block:

term-msg_cmpct_block (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-msg_cmpct_block>`__): An alternative to the block header hash data type identifier of an inventory on the P2P network used to request a compact block.

.. _term-msg_filtered_witness_block:

term-msg_filtered_witness_block (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-msg_filtered_witness_block>`__): An alternative to the block header hash data type identifier of an inventory on the P2P network that is reserved for future use and unused.

.. _term-msg_tx:

term-msg_tx (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-msg_tx>`__): The TXID data type identifier of an inventory on the P2P network.

.. _term-msg_witness_block:

term-msg_witness_block (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-msg_witness_block>`__): An alternative to the block header hash data type identifier of an inventory on the P2P network used to request a block with witness serialization for SegWit.

.. _term-msg_witness_tx:

term-msg_witness_tx (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-msg_witness_tx>`__): An alternative of the transaction data type identifier of an inventory on the P2P network used to request a transaction with witness serialization for SegWit.

.. _term-op-checkmultisig:

term-op-checkmultisig (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-checkmultisig>`__): Opcode which returns true if one or more provided signatures (m) sign the correct parts of a transaction and match one or more provided public keys (n).

.. _term-op-checksig:

term-op-checksig (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-checksig>`__): Opcode which returns true if a signature signs the correct parts of a transaction and matches a provided public key.

.. _term-op-dup:

term-op-dup (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-dup>`__): Operation which duplicates the entry below it on the stack.

.. _term-op-equal:

term-op-equal (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-equal>`__): Operation which returns true if the two entries below it on the stack are equivalent.

.. _term-op-equalverify:

term-op-equalverify (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-equalverify>`__): Operation which terminates the script in failure unless the two entries below it on the stack are equivalent.

.. _term-op-hash160:

term-op-hash160 (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-hash160>`__): Operation which converts the entry below it on the stack into a RIPEMD(SHA256()) hashed version of itself.

.. _term-op-return:

term-op-return (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-return>`__): Operation which terminates the script in failure.

.. _term-op-verify:

term-op-verify (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-op-verify>`__): Operation which terminates the script if the entry below it on the stack is non-true (zero).

.. _term-output-index:

term-output-index (transactions-guide) (`original target <https://bitcoin.org/en/transactions-guide#term-output-index>`__): The sequentially-numbered index of outputs in a single transaction starting from 0.

.. _term-paymentdetails:

term-paymentdetails (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-paymentdetails>`__): The PaymentDetails of the payment protocol which allows the receiver to specify the payment details to the spender.

.. _term-paymentrequest:

term-paymentrequest (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-paymentrequest>`__): The PaymentRequest of the payment protocol which contains and allows signing of the PaymentDetails.

.. _term-pki:

term-pki (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pki>`__): Public Key Infrastructure; usually meant to indicate the X.509 certificate system used for HTTP Secure (https).

.. _term-point-function:

term-point-function (wallets-guide) (`original target <https://bitcoin.org/en/wallets-guide#term-point-function>`__): The ECDSA function used to create a public key from a private key.

.. _term-pp-amount:

term-pp-amount (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-amount>`__): Part of the Output part of the PaymentDetails part of a payment protocol where receivers can specify the amount of satoshis they want paid to a particular pubkey script.

.. _term-pp-expires:

term-pp-expires (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-expires>`__): The expires field of a PaymentDetails where the receiver tells the spender when the PaymentDetails expires.

.. _term-pp-memo:

term-pp-memo (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-memo>`__): The memo fields of PaymentDetails, Payment, and PaymentACK which allow spenders and receivers to send each other memos.

.. _term-pp-merchant-data:

term-pp-merchant-data (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-merchant-data>`__): The merchant_data part of PaymentDetails and Payment which allows the receiver to send arbitrary data to the spender in PaymentDetails and receive it back in Payments.

.. _term-pp-pki-data:

term-pp-pki-data (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-pki-data>`__): The pki_data field of a PaymentRequest which provides details such as certificates necessary to validate the request.

.. _term-pp-pki-type:

term-pp-pki-type (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-pki-type>`__): The PKI field of a PaymentRequest which tells spenders how to validate this request as being from a specific recipient.

.. _term-pp-script:

term-pp-script (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-script>`__): The script field of a PaymentDetails where the receiver tells the spender what pubkey scripts to pay.

.. _term-previous-block-header-hash:

term-previous-block-header-hash (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-previous-block-header-hash>`__): A field in the block header which contains the SHA256(SHA256()) hash of the previous block's header.

.. _term-r-parameter:

term-r-parameter (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-r-parameter>`__): The payment request parameter in a bitcoin: URI.

.. _term-receipt:

term-receipt (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-receipt>`__): A cryptographically-verifiable receipt created using parts of a payment request and a confirmed transaction.

.. _term-root-certificate:

term-root-certificate (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-root-certificate>`__):
A certificate belonging to a certificate authority (CA).

.. _term-ssl-signature:

term-ssl-signature (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-ssl-signature>`__): Signatures created and recognized by major SSL implementations such as OpenSSL.

.. _term-standard-block-relay:

term-standard-block-relay (p2p-network-guide) (`original target <https://bitcoin.org/en/p2p-network-guide#term-standard-block-relay>`__): The regular block relay method: announcing a block with an inv message and waiting for a response.

.. _term-transaction-version-number:

term-transaction-version-number (transactions-guide) (`original target <https://bitcoin.org/en/transactions-guide#term-transaction-version-number>`__): A version number prefixed to transactions to allow upgrading.

.. _term-unique-address:

term-unique-address (transactions-guide) (`original target <https://bitcoin.org/en/transactions-guide#term-unique-address>`__): Address which are only used once to protect privacy and increase security.

.. _term-unsolicited-block-push:

term-unsolicited-block-push (p2p-network-guide) (`original target <https://bitcoin.org/en/p2p-network-guide#term-unsolicited-block-push>`__): When a miner sends a block message without sending an inv message first.

.. _term-uri-qr-code:

term-uri-qr-code (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-uri-qr-code>`__): A QR code containing a bitcoin: URI.

.. _term-v2-block:

term-v2-block (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#term-v2-block>`__): The current version of Bitcoin blocks.

.. _term-x509certificates:

term-x509certificates (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-x509certificates>`__)

