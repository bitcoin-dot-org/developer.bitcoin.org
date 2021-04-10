.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

finalizepsbt
============

``finalizepsbt "psbt" ( extract )``

Finalize the inputs of a PSBT. If the transaction is fully signed, it will produce a
network serialized transaction which can be broadcast with sendrawtransaction. Otherwise a PSBT will be
created which has the final_scriptSig and final_scriptWitness fields filled for inputs that are complete.

Implements the Finalizer and Extractor roles.

Argument #1 - psbt
~~~~~~~~~~~~~~~~~~

**Type:** string, required

A base64 string of a PSBT

Argument #2 - extract
~~~~~~~~~~~~~~~~~~~~~

**Type:** boolean, optional, default=true

If true and the transaction is complete,
       extract and return the complete transaction in normal network serialization instead of the PSBT.

Result
~~~~~~

::

  {                             (json object)
    "psbt" : "str",             (string) The base64-encoded partially signed transaction if not extracted
    "hex" : "hex",              (string) The hex-encoded network transaction if extracted
    "complete" : true|false     (boolean) If the transaction has a complete set of signatures
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli finalizepsbt "psbt"

