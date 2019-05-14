.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

verifychain
===========

``verifychain ( checklevel nblocks )``

Verifies blockchain database.

Argument #1 - checklevel
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=3, range=0-4

How thorough the block verification is.

Argument #2 - nblocks
~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=6, 0=all

The number of blocks to check.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - Verified or not

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli verifychain

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "verifychain", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

