.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

backupwallet
============

``backupwallet "destination"``

Safely copies current wallet file to destination, which can be a directory or a path with filename.

Argument #1 - destination
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The destination directory or file

Result
~~~~~~

::

  null    (json null)

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli backupwallet "backup.dat"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "backupwallet", "params": ["backup.dat"]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

