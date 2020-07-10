
Main Workflow
=============

HomeSkillet uses a workflow skillet to allow for menu inputs and drive the skillets to the be played.


Full End-to-End Workflow
------------------------

Provides an end-to-end experience using the following options.

Workflow Options
~~~~~~~~~~~~~~~~

    (1) revert config to new install
    (2) load threat and content updates
    (3) validation check prior to step 1 config - see FAIL output
    (4) IronSkillet-based configuration (commit required for online validation test)
    (5) validation check after day 1 load - see PASS output
    (6) network and zone config elements
    (7) security policy config elements

Network Deployment Options
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Selected choice will apply to the configuration mode in step (6)

    * L3 routing mode with 2 zones and 2 interfaces
    * Virtual router mode with 2 zones and 2 interfaces

Add-on configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + simple DHCP-based userID using DHCP log parsing

Version Selection Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Selected choice will apply to the configuration mode in step (4)

    + v9.x - loads IronSkillet 9.0 snippets
    + v10.x - loads IronSkillet 10.0 snippets





REST device queries
~~~~~~~~~~~~~~~~~~~

  Not shown in the menus yet part of the skillet framework are REST skillet types.
  These are used to query the firewall and get the interface and zone name information to be
  used as dropdown options in the deployment and security policy web forms.




