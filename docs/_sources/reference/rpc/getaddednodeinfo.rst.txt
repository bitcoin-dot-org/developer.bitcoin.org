.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

getaddednodeinfo
================

``getaddednodeinfo ( "node" )``

Returns information about the given added node, or all added nodes
(note that onetry addnodes are not listed here)

Argument #1 - node
~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=all nodes

If provided, return information about this specific node, otherwise all nodes are returned.

Result
~~~~~~

::

  [
    {
      "addednode" : "192.168.0.201",   (string) The node IP address or name (as provided to addnode)
      "connected" : true|false,          (boolean) If connected
      "addresses" : [                    (list of objects) Only when connected = true
         {
           "address" : "192.168.0.201:8333",  (string) The bitcoin server IP and port we're connected to
           "connected" : "outbound"           (string) connection, inbound or outbound
         }
       ]
    }
    ,...
  ]

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli getaddednodeinfo "192.168.0.201"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddednodeinfo", "params": ["192.168.0.201"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

