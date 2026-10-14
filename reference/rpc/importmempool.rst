.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

importmempool
=============

``importmempool "filepath" ( options )``

Import a mempool.dat file and attempt to add its contents to the mempool.

Warning: Importing untrusted files is dangerous, especially if metadata from the file is taken over.

Argument #1 - filepath
~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The mempool file

Argument #2 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, optional

Options object that can be used to pass named arguments, listed below.
       Warning: Importing untrusted metadata may lead to unexpected issues and undesirable behavior.
       It will be added to any existing fee deltas.
       The fee delta can be set by the prioritisetransaction RPC.
       Warning: Importing untrusted metadata may lead to unexpected issues and undesirable behavior.
       Only set this bool if you understand what it does.
       Warning: Importing untrusted metadata may lead to unexpected issues and undesirable behavior.

Result
~~~~~~

::

  {}    (empty JSON object)
  
  Examples:
  > bitcoin-cli importmempool /path/to/mempool.dat
  > curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "importmempool", "params": [/path/to/mempool.dat]}' -H 'content-type: application/json' http://127.0.0.1:8332/

