.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

addnode
=======

``addnode "node" "command"``

Attempts to add or remove a node from the addnode list.

Or try a connection to a node once.

Nodes added using addnode (or -connect) are protected from DoS disconnection and are not required to be
full nodes/support SegWit as other outbound peers are (though such peers will not be synced from).

Argument #1 - node
~~~~~~~~~~~~~~~~~~

**Type:** string, required

The node (see getpeerinfo for nodes)

Argument #2 - command
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

'add' to add a node to the list, 'remove' to remove a node from the list, 'onetry' to try a connection to the node once

Result
~~~~~~

::

  null    (json null)

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli addnode "192.168.0.6:8333" "onetry"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "addnode", "params": ["192.168.0.6:8333", "onetry"]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

