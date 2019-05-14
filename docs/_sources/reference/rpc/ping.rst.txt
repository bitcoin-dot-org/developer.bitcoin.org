.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

ping
====

``ping``

Requests that a ping be sent to all other nodes, to measure ping time.

Results provided in getpeerinfo, pingtime and pingwait fields are decimal seconds.

Ping command is handled in queue with all other commands, so it measures processing backlog, not just network ping.

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli ping

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "ping", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

