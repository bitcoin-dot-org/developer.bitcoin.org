.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

walletdisplayaddress
====================

``walletdisplayaddress "address"``

Display address on an external signer for verification.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

bitcoin address to display

Result
~~~~~~

::

  {                       (json object)
    "address" : "str"     (string) The address as confirmed by the signer
  }

