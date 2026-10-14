.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

ping
====

``ping``

Requests that a ping be sent to all other nodes, to measure ping time.

Results are provided in getpeerinfo.

Ping command is handled in queue with all other commands, so it measures processing backlog, not just network ping.

Result
~~~~~~

::

  null    (json null)

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli ping

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "ping", "params": []}' -H 'content-type: application/json' http://127.0.0.1:8332/

