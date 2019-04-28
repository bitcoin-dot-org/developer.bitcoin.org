.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

importwallet
============

``importwallet "filename"``

Imports keys from a wallet dump file (see dumpwallet). Requires a new wallet backup to include imported keys.

Argument #1 - filename
~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The wallet file

Examples
~~~~~~~~


.. highlight:: shell

Dump the wallet::

  bitcoin-cli dumpwallet "test"

Import the wallet::

  bitcoin-cli importwallet "test"

Import using the json rpc call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importwallet", "params": ["test"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

