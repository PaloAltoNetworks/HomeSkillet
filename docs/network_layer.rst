
Network Layer Skillets
======================

Layer 3 Routing Configuration
-----------------------------

This section provides templated configurations for network elements used.

The Internet gateway deployment is a 2-zone, 2-interface model with IP routing.


Interface settings
~~~~~~~~~~~~~~~~~~

Sample interface configurations with one for external/untrust and one internal/trust.

    + untrust interface uses DHCP and provides default route inheritance to the internet

    + trust interface is uses a static IP configuration

    + the interface names and the trust IP address are variables to adjust as needed

Zones
~~~~~

Two zones are provided in the template. The names are variables with default values set to trust and internet.


Virtual Router
~~~~~~~~~~~~~~

The internet gateway deployment uses L3 zones and interfaces so routing configuration is required.

    + adds each of the firewall interfaces

    + uses inheritance from the DHCP internet interface to create a default gateway route to the internet


Source NAT
~~~~~~~~~~

Provides dynamic ip and port mapping using the public internet interface address.


DHCP Server
~~~~~~~~~~~

Simple DHCP server mapped to the trust interface

    + use of IP address range located in the trust subnet

    + inherits DNS information from the untrust interface

.. Note::
        This skillet does not include Dynamic DNS (DDNS) although it is a supported feature in PAN-OS v9.0.
        DDNS is recommended if GlobalProtect other configurations using the public IP are used.


Network Profiles
~~~~~~~~~~~~~~~~

Interface management profiles

    + sets the interface interface for ping only

    + allows for configuration access from the trust interface

.. NOTE::
    Device management will vary by users. It is expected that these profiles will be updated specific to the user management
    model.

