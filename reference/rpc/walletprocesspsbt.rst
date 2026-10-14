.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

walletprocesspsbt
=================

``walletprocesspsbt "psbt" ( sign "sighashtype" bip32derivs finalize )``

Update a PSBT with input information from our wallet and then sign inputs
that we can sign for.

Requires wallet passphrase to be set with walletpassphrase call if wallet is encrypted.

Argument #1 - psbt
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The transaction base64 string

Argument #2 - sign
~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

Also sign the transaction when updating (requires wallet to be unlocked)

Argument #3 - sighashtype
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default="DEFAULT for Taproot, ALL otherwise"

The signature hash type to sign with if not specified by the PSBT. Must be one of
       "DEFAULT"
       "ALL"
       "NONE"
       "SINGLE"
       "ALL|ANYONECANPAY"
       "NONE|ANYONECANPAY"
       "SINGLE|ANYONECANPAY"

Argument #4 - bip32derivs
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

Include BIP 32 derivation paths for public keys if we know them

Argument #5 - finalize
~~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

Also finalize inputs if possible

Result
~~~~~~

::

  {                             (json object)
    "psbt" : "str",             (string) The base64-encoded partially signed transaction
    "complete" : true|false,    (boolean) If the transaction has a complete set of signatures
    "hex" : "hex"               (string, optional) The hex-encoded network transaction if complete
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli walletprocesspsbt "psbt"

