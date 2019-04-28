.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

setlabel
========

``setlabel "address" "label"``

Sets the label associated with the given address.

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The bitcoin address to be associated with a label.

Argument #2 - label
~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The label to assign to the address.

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli setlabel "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" "tabby"

::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setlabel", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX", "tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

