
Security Policies
=================


Outbound Only Configuration
---------------------------

Unknown URL Category Profile Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  This adds additional protections with a more aggressive file blocking posture when the URL category is unknown. It is
  referenced in the gold security rules.


Security Rules
~~~~~~~~~~~~~~

  These are outbound-specific rules levering the IronSkillet security profile groups.

    + Block quic to force usage of SSL to assist URL-filtering category discovery

    + Aggressive file blocking including PE file types when URL category = `unknown`

    + Outbound access for all applications using 'application default' port requirements

    + Non-defaul SSL ports: allows bypass of app defaults for SSL traffic; tracking for non-standard ports

    + Non-default web ports: allows bypass of app defaults for web traffic; tracking for non-standard ports

    + Non-default application ports: allows bypass of app defaults for all traffic; tracking for non-standard ports


.. Warning::
        The non-default ports effectively allow all outbound traffic on any port. These are provided due to the variance
        of ports used and for SMB deployments to avoid rampant support calls. The explicit rules provide for hit counts
        to track and monitor out-of-bounds and suspicious applications.

