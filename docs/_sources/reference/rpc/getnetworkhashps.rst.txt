.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getnetworkhashps
================

``getnetworkhashps ( nblocks height )``

Returns the estimated network hashes per second based on the last n blocks.

Pass in [blocks] to override # of blocks, -1 specifies since last difficulty change.

Pass in [height] to estimate the network speed at the time when a certain block was found.

Argument #1 - nblocks
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=120

The number of blocks, or -1 for blocks since last difficulty change.

Argument #2 - height
~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=-1

To estimate at the time of the given height.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - x
     - numeric
     - Hashes per second estimated

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getnetworkhashps

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworkhashps", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

