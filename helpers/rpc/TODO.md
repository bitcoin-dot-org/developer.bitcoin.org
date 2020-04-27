# RPC helper To do

* Add RST
  * Add basic renderer
  * Try rendered result
  * Add unit tests
  * Refactor (share between backends, abstract rst page)

* Fix description
  * gettxoutproof (first line cut off before "txids")

* Fix result
  * importmulti (include example output)

* Fix examples in description
  * deriveaddresses
  * scantxoutset

* Fix arguments
  * sighashtype parameter table
    * signrawtransactionwithwallet
    * walletprocesspsbt
  * multi-line argument description
    * listsinceblock (include_removed)

* Results of example commands
  (https://github.com/cornelius/rpc-docs-helper/issues/4)
  * Check how many commands have example results and how many are up to date
  * Recreate current state with manually edited annotations file
  * Look into auto-generating example results
