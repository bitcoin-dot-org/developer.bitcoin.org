.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getrpcinfo
==========

``getrpcinfo``

Returns details of the RPC server.

Result
~~~~~~

::

  {
   "active_commands" (array) All active commands
    [
     {               (object) Information about an active command
      "method"       (string)  The name of the RPC command
      "duration"     (numeric)  The running time in microseconds
     },...
    ]
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getrpcinfo

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrpcinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

