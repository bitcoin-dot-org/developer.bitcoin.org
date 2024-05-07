# RPC helper To do

* Add command to add deprecation notice and deprecate getbalance, getunconfirmedbalance in 0.19

* Remove markdown support
  * Remove renderer
  * Remove helper subcommands which rely on markdown files

* Add command to add "see also" and add references, e.g. in importaddress, importmulti, importprivkey, importpubkey, importwallet, rescanblockchain, walletprocesspsbt

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
