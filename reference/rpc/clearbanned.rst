.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

clearbanned
===========

``clearbanned``

Clear all banned IPs.

Result
~~~~~~

::

  null    (json null)

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli clearbanned

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "clearbanned", "params": []}' -H 'content-type: application/json' http://127.0.0.1:8332/

