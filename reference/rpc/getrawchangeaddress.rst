.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getrawchangeaddress
===================

``getrawchangeaddress ( "address_type" )``

Returns a new Bitcoin address, for receiving change.

This is for use with raw transactions, NOT normal use.

Argument #1 - address_type
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=set by -changetype

The address type to use. Options are "legacy", "p2sh-segwit", and "bech32".

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - str
     - string
     - The address

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getrawchangeaddress

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getrawchangeaddress", "params": []}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

