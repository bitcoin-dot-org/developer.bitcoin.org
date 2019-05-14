Wallets
-------

Deterministic Wallet Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <!-- no subhead-links here -->

Type 1: Single Chain Wallets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <!-- no subhead-links here -->

Type 1 deterministic wallets are the simpler of the two, which can create a single series of keys from a single seed. A primary weakness is that if the seed is leaked, all funds are compromised, and wallet sharing is extremely limited.

Type 2: Hierarchical Deterministic (HD) Wallets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <!-- no subhead-links here -->

.. figure:: /img/dev/en-hd-overview.svg
   :alt: Overview Of Hierarchical Deterministic Key Derivation

   Overview Of Hierarchical Deterministic Key Derivation

For an overview of HD wallets, please see the `developer guide section </en/developer-guide#wallets>`__. For details, please see `BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__.
