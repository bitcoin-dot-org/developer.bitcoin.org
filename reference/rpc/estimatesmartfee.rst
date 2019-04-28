.. This file is licensed under the MIT License (MIT) available on
   http://opensource.org/licenses/MIT.

estimatesmartfee
================

``estimatesmartfee conf_target ( "estimate_mode" )``

Estimates the approximate fee per kilobyte needed for a transaction to begin
confirmation within conf_target blocks if possible and return the number of blocks
for which the estimate is valid. Uses virtual transaction size as defined
in BIP 141 (witness data is discounted).

Argument #1 - conf_target
~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** numeric, required

Confirmation target in blocks (1 - 1008)

Argument #2 - estimate_mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type:** string, optional, default=CONSERVATIVE

The fee estimate mode.
       Whether to return a more conservative estimate which also satisfies
       a longer history. A conservative estimate potentially returns a
       higher feerate and is more likely to be sufficient for the desired
       target, but is not as responsive to short term drops in the
       prevailing fee market.  Must be one of:
       "UNSET"
       "ECONOMICAL"
       "CONSERVATIVE"

Result
~~~~~~

::

  {
    "feerate" : x.x,     (numeric, optional) estimate fee rate in BTC/kB
    "errors": [ str... ] (json array of strings, optional) Errors encountered during processing
    "blocks" : n         (numeric) block number where estimate was found
  }

Examples
~~~~~~~~


.. highlight:: shell

::

  bitcoin-cli estimatesmartfee 6

