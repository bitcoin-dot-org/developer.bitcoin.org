.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

walletpassphrase
================

``walletpassphrase "passphrase" timeout``

Stores the wallet decryption key in memory for 'timeout' seconds.

This is needed prior to performing transactions related to private keys such as sending bitcoins
Note:

Issuing the walletpassphrase command while the wallet is already unlocked will set a new unlock
time that overrides the old one.

Argument #1 - passphrase
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The wallet passphrase

Argument #2 - timeout
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

The time to keep the decryption key in seconds; capped at 100000000 (~3 years).

Examples
~~~~~~~~


.. highlight:: shell

Unlock the wallet for 60 seconds::

  bitcoin-cli walletpassphrase "my pass phrase" 60

Lock the wallet again (before 60 seconds)::

  bitcoin-cli walletlock

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "walletpassphrase", "params": ["my pass phrase", 60] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

