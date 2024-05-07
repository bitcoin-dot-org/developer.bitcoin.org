.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

unloadwallet
============

``unloadwallet ( "wallet_name" load_on_startup )``

Unloads the wallet referenced by the request endpoint otherwise unloads the wallet specified in the argument.

Specifying the wallet name on a wallet endpoint is invalid.

Argument #1 - wallet_name
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=the wallet name from the RPC endpoint

The name of the wallet to unload. Must be provided in the RPC endpoint or this parameter (but not both).

Argument #2 - load_on_startup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=null

Save wallet name to persistent settings and load on startup. True to add wallet to startup list, false to remove, null to leave unchanged.

Result
~~~~~~

::

  {                       (json object)
    "warning" : "str"     (string) Warning message if wallet was not unloaded cleanly.
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli unloadwallet wallet_name

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "unloadwallet", "params": [wallet_name]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

