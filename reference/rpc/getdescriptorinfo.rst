.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getdescriptorinfo
=================

``getdescriptorinfo "descriptor"``

Analyses a descriptor.

Argument #1 - descriptor
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The descriptor.

Result
~~~~~~

::

  {                                   (json object)
    "descriptor" : "str",             (string) The descriptor in canonical form, without private keys. For a multipath descriptor, only the first will be returned.
    "multipath_expansion" : [         (json array, optional) All descriptors produced by expanding multipath derivation elements. Only if the provided descriptor specifies multipath derivation elements.
      "str",                          (string)
      ...
    ],
    "checksum" : "str",               (string) The checksum for the input descriptor
    "isrange" : true|false,           (boolean) Whether the descriptor is ranged
    "issolvable" : true|false,        (boolean) Whether the descriptor is solvable
    "hasprivatekeys" : true|false     (boolean) Whether the input descriptor contained at least one private key
  }

Examples
~~~~~~~~


.. highlight:: shell

Analyse a descriptor::

  bitcoin-cli getdescriptorinfo "wpkh([d34db33f/84h/0h/0h]0279be667ef9dcbbac55a06295Ce870b07029Bfcdb2dce28d959f2815b16f81798)"

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "getdescriptorinfo", "params": ["wpkh([d34db33f/84h/0h/0h]0279be667ef9dcbbac55a06295Ce870b07029Bfcdb2dce28d959f2815b16f81798)"]}' -H 'content-type: application/json' http://127.0.0.1:8332/

