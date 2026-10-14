.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

enumeratesigners
================

``enumeratesigners``

Returns a list of external signers from -signer.

Result
~~~~~~

::

  {                               (json object)
    "signers" : [                 (json array)
      {                           (json object)
        "fingerprint" : "hex",    (string) Master key fingerprint
        "name" : "str"            (string) Device name
      },
      ...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli enumeratesigners

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "enumeratesigners", "params": []}' -H 'content-type: application/json' http://127.0.0.1:8332/

