.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

listbanned
==========

``listbanned``

List all banned IPs/Subnets.

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli listbanned

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listbanned", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

