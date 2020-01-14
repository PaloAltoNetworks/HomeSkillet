
Supporting Skillets
===================

Revert to Empty Configuration
-----------------------------

A python skillet that resets the configuration to an empty baseline with only the management
interface, admin user, and DNS configured.

The steps of the skillet include:

    + render the full configuration using supplied values
    + import the configuration file
    + load the configuration as candidate
    + commit the configuration

Content Updates
---------------

A python skillet that downloads the latest content and threat updates and applies them to the firewall

The content update is often required before configuration of skillets to have the latest predefined elements
such as palo alto EDLs, URL filtering categories, WF filetypes, etc. Updates can also be required before software
upgrades.




