HomeSkillet Overview
====================

HomeSkillet is a home-based deployment configuration as a simple Internet Gateway using 2 zones.

It is compatible with PAN-OS versions 10.0 and 10.1.

Key Features
------------

        * IronSkillet foundation providing security profiles and device hardening
        * 2 zones and interfaces, one internet and one internal
        * L3, Hybrid L2/L3, and vwire options available for network configuration
        * Outbound port-based NAT policy
        * Outbound security policies referencing the Outbound security profile group
        * DHCP client interface for the untrust interface
        * Simple DHCP server configuration inheriting DNS from the untrust interface


Relationship to the IronSkillet Project
---------------------------------------
The configuration is based extensively on the IronSkillet configuration with a few variations designed for basic home use.

The config element omitted from HomeSkillet include:

        * No certificate checks for the no-decrypt traffic that may cause issues with in-home devices
        * No email alert configuration elements
        * No http range that when disabled can impact video streaming services

More information about IronSkillet can be found at: https://iron-skillet.readthedocs.io


Required Subscriptions
----------------------

The configuration assumes all subscriptions are enabled including:

        * Threat Protection
        * URL Filtering
        * Wildfire Analysis
        * DNS Cloud Service


Skillet District Content
------------------------

Visit the `HomeSkillet page`_ in the Live community Skillet District for additional updates and related skillets.

.. _HomeSkillet page: https://live.paloaltonetworks.com/t5/quickplay-solutions-articles/homeskillet-internet-gateway/ta-p/307751







