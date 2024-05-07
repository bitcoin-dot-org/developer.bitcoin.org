.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

setwalletflag
=============

``setwalletflag "flag" ( value )``

Change the state of the given wallet flag for a wallet.

Argument #1 - flag
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The name of the flag to change. Current available flags: avoid_reuse

Argument #2 - value
~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

The new state.

Result
~~~~~~

::

  {                               (json object)
    "flag_name" : "str",          (string) The name of the flag that was modified
    "flag_state" : true|false,    (boolean) The new state of the flag
    "warnings" : "str"            (string) Any warnings associated with the change
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli setwalletflag avoid_reuse

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "setwalletflag", "params": ["avoid_reuse"]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

