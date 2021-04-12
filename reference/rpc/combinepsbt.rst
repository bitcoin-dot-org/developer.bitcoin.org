.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

combinepsbt
===========

``combinepsbt ["psbt",...]``

Combine multiple partially signed Bitcoin transactions into one transaction.

Implements the Combiner role.

Argument #1 - txs
~~~~~~~~~~~~~~~~~

**Type:** json array, required

The base64 strings of partially signed transactions

::

     [
       "psbt",    (string) A base64 string of a PSBT
       ...
     ]

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - str
     - string
     - The base64-encoded partially signed transaction

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli combinepsbt '["mybase64_1", "mybase64_2", "mybase64_3"]'

