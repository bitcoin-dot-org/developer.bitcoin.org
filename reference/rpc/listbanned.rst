.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

listbanned
==========

``listbanned``

List all manually banned IPs/Subnets.

Result
~~~~~~

::

  [                            (json array)
    {                          (json object)
      "address" : "str",       (string)
      "banned_until" : xxx,    (numeric)
      "ban_created" : xxx      (numeric)
    },
    ...
  ]

Result
~~~~~~
::

  [
    {
    "address": <address>,             (string) The banned address.
    "banned_until": <time>,           (numeric) The time (in seconds since Jan 1 1970 GMT) until the address is banned.
    "ban_created": <time>,            (numeric) The time (in seconds since Jan 1 1970 GMT) when the ban was created.
    }
  ]

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli listbanned

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "listbanned", "params": []}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

