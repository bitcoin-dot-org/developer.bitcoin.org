.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getnodeaddresses
================

``getnodeaddresses ( count "network" )``

Return known addresses, after filtering for quality and recency.

These can potentially be used to find new peers in the network.

The total number of addresses known to the node may be higher.

Argument #1 - count
~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=1

The maximum number of addresses to return. Specify 0 to return all known addresses.

Argument #2 - network
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=all networks

Return only addresses of the specified network. Can be one of: ipv4, ipv6, onion, i2p, cjdns.

Result
~~~~~~

::

  [                         (json array)
    {                       (json object)
      "time" : xxx,         (numeric) The UNIX epoch time when the node was last seen
      "services" : n,       (numeric) The services offered by the node
      "address" : "str",    (string) The address of the node
      "port" : n,           (numeric) The port number of the node
      "network" : "str"     (string) The network (ipv4, ipv6, onion, i2p, cjdns) the node connected through
    },
    ...
  ]

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getnodeaddresses 8

::

  bitcoin-cli getnodeaddresses 4 "i2p"

::

  bitcoin-cli -named getnodeaddresses network=onion count=12

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "getnodeaddresses", "params": [8]}' -H 'content-type: application/json' http://127.0.0.1:8332/

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "getnodeaddresses", "params": [4, "i2p"]}' -H 'content-type: application/json' http://127.0.0.1:8332/

