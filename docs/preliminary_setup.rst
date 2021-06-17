
Preliminary Setup
=================

These skillets are used in the workflow ahead of configuration to create an empty configuration
and install the latest content updates.

Load Empty Baseline Config
----------------------------

A python skillet that resets the configuration to an empty baseline with only the management
interface, admin user, and DNS configured.

The steps of the skillet include:

    + Render the full configuration using supplied values
    + Import the configuration file
    + Load the configuration as candidate
    + Commit the configuration

Content Updates
---------------

An ansible playbook that checks if the latest content and threat updates are installed.
If not, the playbook will download and install the latest updates.

The content update is often required before configuration of skillets to have the latest predefined elements
such as Palo ALto EDLs, URL filtering categories, WF filetypes, etc. Updates may also be required before software
upgrades.

