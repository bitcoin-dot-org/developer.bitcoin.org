.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

signmessage
===========

``signmessage "address" "message"``

Sign a message with the private key of an address

Argument #1 - address
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The bitcoin address to use for the private key.

Argument #2 - message
~~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The message to create a signature of.

Result
~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - signature
     - string
     - The signature of the message encoded in base 64

Examples
~~~~~~~~


.. highlight:: shell

Unlock the wallet for 30 seconds::

  bitcoin-cli walletpassphrase "mypassphrase" 30

Create the signature::

  bitcoin-cli signmessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" "my message"

Verify the signature::

  bitcoin-cli verifymessage "1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX" "signature" "my message"

As a JSON-RPC call::

  curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "signmessage", "params": ["1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX", "my message"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

