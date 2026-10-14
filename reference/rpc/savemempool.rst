.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

savemempool
===========

``savemempool``

Dumps the mempool to disk. It will fail until the previous dump is fully loaded.

Result
~~~~~~

::

  {                        (json object)
    "filename" : "str"     (string) the directory and file where the mempool was saved
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli savemempool

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "savemempool", "params": []}' -H 'content-type: application/json' http://127.0.0.1:8332/

