Getting Started
========

The site aims to provide the information you need to understand
Bitcoin and start building Bitcoin-based applications. To make the best use of
this documentation, `make sure you're running a node`_.

For technical support, we recommend `Bitcoin Stack Exchange`_. For errors or
suggestions related to this documentation, please open an issue on `GitHub`_.

A simple payment system
-----------------------

Unless a payment needs to be associated with automatic invoices, accepting money
is as simple as sending some bitcoin - just display an address or QR code. This
simple setup is within reach of almost all users and can fulfill the needs of
many clients. From an accounting perspective, it's especially suitable for
reducing overhead and adding transparency.

Many third-party APIs
---------------------

There are many third party payment processing services that provide APIs; you
don't need to store bitcoins on your server and handle the security that this
implies. Additionally, most of these APIs allow you to process invoices and
exchange your bitcoins into your local currency at competitive costs.

Be your own bank
----------------

If you don't use any third party APIs, you can integrate a Bitcoin node directly
into your applications allowing you to become your own bank and payment
processor. With all the responsibilities that this implies, you can build
amazing systems that process Bitcoin transactions however you would like.

Bitcoin addresses to track invoices
-----------------------------------

Bitcoin creates a unique address for each transaction. If you were to build a
payment system associated with an invoice, all you would need to do is generate
and monitor a Bitcoin address for each payment (you should never use the same
address for more than one transaction).

Client side security
--------------------

Most security is handled by the protocol, eliminating the need for PCI
compliance. Fraud prevention can be simplified down to monitoring a single
variable: the confirmation score. Beyond that, keeping your bitcoins secure is
mainly a matter of securing your wallet and using HTTPS or other secure
protocols to send payment requests to customers.

A new world of possibilities
----------------------------

Bitcoin allows you to design new and creative online services that couldn't
exist before due to financial limitations. This includes tipping systems,
automated payment solutions, distributed crowdfunding services, time locked
payment management, public asset tracking, low-trust escrow services,
micropayment channels and more.

Acknowledgments
========

This documentation would not be possible without the many contributions to the
Bitcoin project over the years from core developers and other people. A very
special thanks, however, goes to `David Harding`_ who in 2014 helped lead the
effort to compose and bring together a significant amount of the material found
here. Also, to `Cornelius Schumacher`_ for envisioning new ways to extend the
developer documentation that led to this site.

.. _make sure you're running a node: https://bitcoin.org/en/full-node
.. _Bitcoin Stack Exchange: https://bitcoin.stackexchange.com/
.. _GitHub: https://github.com/bitcoin-dot-org/developer.bitcoin.org/issues/new/choose
.. _David Harding: https://github.com/harding
.. _Cornelius Schumacher: https://github.com/cornelius

.. toctree::

  devguide/index
  reference/index
  examples/index
  glossary
