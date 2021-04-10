.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getrpcinfo
==========

``getrpcinfo``

Returns details of the RPC server.

Result
~~~~~~

::

  {                          (json object)
    "active_commands" : [    (json array) All active commands
      {                      (json object) Information about an active command
        "method" : "str",    (string) The name of the RPC command
        "duration" : n       (numeric) The running time in microseconds
      },
      ...
    ],
    "logpath" : "str"        (string) The complete file path to the debug log
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getrpcinfo

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getrpcinfo", "params": []}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

