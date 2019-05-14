.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

unloadwallet
============

``unloadwallet ( "wallet_name" )``

Unloads the wallet referenced by the request endpoint otherwise unloads the wallet specified in the argument.

Specifying the wallet name on a wallet endpoint is invalid.

Argument #1 - wallet_name
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=the wallet name from the RPC request

The name of the wallet to unload.

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli unloadwallet wallet_name

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "unloadwallet", "params": [wallet_name] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

