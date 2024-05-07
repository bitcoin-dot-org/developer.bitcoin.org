.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

importprunedfunds
=================

``importprunedfunds "rawtransaction" "txoutproof"``

Imports funds without rescan. Corresponding address or script must previously be included in wallet. Aimed towards pruned wallets. The end-user is responsible to import additional transactions that subsequently spend the imported outputs or rescan after the point in the blockchain the transaction is included.

Argument #1 - rawtransaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

A raw transaction in hex funding an already-existing address in wallet

Argument #2 - txoutproof
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The hex output from gettxoutproof that contains the transaction

Result
~~~~~~

::

  null    (json null)

