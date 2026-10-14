.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

createwalletdescriptor
======================

``createwalletdescriptor "type" ( {"internal":bool,"hdkey":"str",...} )``

Creates the wallet's descriptor for the given address type. The address type must be one that the wallet does not already have a descriptor for.

Requires wallet passphrase to be set with walletpassphrase call if wallet is encrypted.

Argument #1 - type
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The address type the descriptor will produce. Options are "legacy", "p2sh-segwit", "bech32", "bech32m".

Argument #2 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, optional

Options object that can be used to pass named arguments, listed below.

Result
~~~~~~

::

  {                (json object)
    "descs" : [    (json array) The public descriptors that were added to the wallet
      "str",       (string)
      ...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli createwalletdescriptor bech32m

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "createwalletdescriptor", "params": [bech32m]}' -H 'content-type: application/json' http://127.0.0.1:8332/

