
Internet Gateway Templates
==========================

The configuration snippet descriptions and the associated GitHub repository link for each xml snippet.

Panorama can be configured using shared elements and device-specific elements. The MSSP templates are based on a non-shared
model to isolate each customer configuration. Deployments requiring shared or mixed models will need to edit the templates
specific to their environment.


The templates are incremental to and reference the IronSkillet day one configurations. The details of the IronSkillet
templates can be found at:

|IronSkilletdocs|.

The .meta-cnc.yaml file in each configuration directory contains:

    + list of variables and default values

    + load order including the xpaths and snippet file names


HomeSkillet Gold Configuration
------------------------------

----------------------------------------------------------------------

This section provides templated configurations for network elements used.

The Internet gateway deployment is a 2-zone, 2-interface model with IP routing.



Interface settings
~~~~~~~~~~~~~~~~~~

:panosrepo:`interface.xml`

Sample interface configurations with one for external/untrust and one internal/trust.

    + untrust interface uses DHCP and provides default route inheritance to the internet

    + trust interface is uses a static IP configuration

    + the interface names and the trust IP address are variables to adjust as needed

Zones
~~~~~

:panosrepo:`zone.xml`


Two zones are provided in the template. The names are variables with default values set to trust and internet.


Virtual Router
~~~~~~~~~~~~~~

:panosrepo:`virtual_router.xml`


The internet gateway deployment uses L3 zones and interfaces so routing configuration is required.

    + adds each of the firewall interfaces

    + uses inheritance from the DHCP internet interface to create a default gateway route to the internet


Source NAT
~~~~~~~~~~

:panosrepo:`source_nat_to_untrust.xml`


Provides dynamic ip and port mapping using the public internet interface address.


DHCP Server
~~~~~~~~~~~

:panosrepo:`dhcp_server.xml`

Simple DHCP server mapped to the trust interface

    + use of IP address range located in the trust subnet

    + inherits DNS information from the untrust interface

.. Note::
        This skillet does not include Dynamic DNS (DDNS) although it is a supported feature in PAN-OS v9.0.
        DDNS is recommended if GlobalProtect other configurations using the public IP are used.


Network Profiles
~~~~~~~~~~~~~~~~

:panosrepo:`network_profiles.xml`


Interface management profiles

    + sets the interface interface for ping only

    + allows for configuration access from the trust interface

.. NOTE::
    Device management will vary by users. It is expected that these profiles will be updated specific to the user management
    model.



Unknown URL Category Profile Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:panosrepo:`profile_group_unknown_url.xml`

This adds additional protections with a more aggressive file blocking posture when the URL category is unknown. It is
referenced in the gold security rules.


Security Rules
~~~~~~~~~~~~~~

:panosrepo:`security_rules_gold.xml`

These are outbound-specific rules levering the IronSkillet security profile groups.

    + Aggressive file blocking including PE file types when URL category = `unknown`

    + Outbound access for all applications using 'application default' port requirements

    + Non-defaul SSL ports: allows bypass of app defaults for SSL traffic; tracking for non-standard ports

    + Non-default web ports: allows bypass of app defaults for web traffic; tracking for non-standard ports

    + Non-default application ports: allows bypass of app defaults for all traffic; tracking for non-standard ports


.. Warning::
        The non-default ports effectively allow all outbound traffic on any port. These are provided due to the variance
        of ports used and for SMB deployments to avoid rampant support calls. The explicit rules provide for hit counts
        to track and monitor out-of-bounds and suspicious applications.

