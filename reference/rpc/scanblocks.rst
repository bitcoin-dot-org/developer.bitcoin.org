.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

scanblocks
==========

``scanblocks "action" ( [scanobjects,...] start_height stop_height "filtertype" options )``

Return relevant blockhashes for given descriptors (requires blockfilterindex).

This call may take several minutes. Make sure to use no RPC timeout (bitcoin-cli -rpcclienttimeout=0)

Argument #1 - action
~~~~~~~~~~~~~~~~~~~~

**Type:** string, required

The action to execute
       "start" for starting a scan
       "abort" for aborting the current scan (returns true when abort was successful)
       "status" for progress report (in %) of the current scan

Argument #2 - scanobjects
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** json array, optional

Array of scan objects. Required for "start" action
       Every scan object is either a string descriptor or an object:

::

     [
       "descriptor",             (string) An output descriptor
       {                         (json object) An object with output descriptor and metadata
         "desc": "str",          (string, required) An output descriptor
         "range": n or [n,n],    (numeric or array, optional, default=1000) The range of HD chain indexes to explore (either end or [begin,end])
       },
       ...
     ]

Argument #3 - start_height
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=0

Height to start to scan from

Argument #4 - stop_height
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, optional, default=chain tip

Height to stop to scan

Argument #5 - filtertype
~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default="basic"

The type name of the filter

Argument #6 - options
~~~~~~~~~~~~~~~~~~~~~

**Type:** json object, optional

Options object that can be used to pass named arguments, listed below.

Result (when action=='status' and no scan is in progress - possibly already completed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  null    (json null)

Result (When action=='start'; only returns after scan completes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {                              (json object)
    "from_height" : n,           (numeric) The height we started the scan from
    "to_height" : n,             (numeric) The height we ended the scan at
    "relevant_blocks" : [        (json array) Blocks that may have matched a scanobject.
      "hex",                     (string) A relevant blockhash
      ...
    ],
    "completed" : true|false     (boolean) true if the scan process was not aborted
  }

Result (when action=='status' and a scan is currently in progress)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  {                          (json object)
    "progress" : n,          (numeric) Approximate percent complete
    "current_height" : n     (numeric) Height of the block currently being scanned
  }

Result (when action=='abort')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - true|false
     - boolean
     - True if scan will be aborted (not necessarily before this RPC returns), or false if there is no scan to abort

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli scanblocks start '["addr(bcrt1q4u4nsgk6ug0sqz7r3rj9tykjxrsl0yy4d0wwte)"]' 300000

::

  bitcoin-cli scanblocks start '["addr(bcrt1q4u4nsgk6ug0sqz7r3rj9tykjxrsl0yy4d0wwte)"]' 100 150 basic

::

  bitcoin-cli scanblocks status

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "scanblocks", "params": ["start", ["addr(bcrt1q4u4nsgk6ug0sqz7r3rj9tykjxrsl0yy4d0wwte)"], 300000]}' -H 'content-type: application/json' http://127.0.0.1:8332/

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "scanblocks", "params": ["start", ["addr(bcrt1q4u4nsgk6ug0sqz7r3rj9tykjxrsl0yy4d0wwte)"], 100, 150, "basic"]}' -H 'content-type: application/json' http://127.0.0.1:8332/

::

  curl --user myusername --data-binary '{"jsonrpc": "2.0", "id": "curltest", "method": "scanblocks", "params": ["status"]}' -H 'content-type: application/json' http://127.0.0.1:8332/

