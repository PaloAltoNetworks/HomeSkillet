
Main Workflow
=============

HomeSkillet functions as a workflow to allow for menu inputs and play the necessary skillets/submodules. This workflow
allows the user to go from a baseline NGFW to a fully configured NGFW with proper network components, zones, policies, etc.
including IronSkillet best practices.


Full End-to-End Workflow
------------------------

Provides an end-to-end experience using the following options:

Workflow Options
~~~~~~~~~~~~~~~~

    (1) Load empty baseline configuration
    (2) Perform content updates
    (3) Validation check (pre-ironskillet) [fail expected]
    (4) IronSkillet-based configuration (commit required for online validation test)
    (5) Validation check (post-ironskillet) [pass expected]
    (6) Configure HomeSkillet network components
    (7) Configure security policies

Network Deployment Options
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Selected choice will apply to the configuration mode in step (6)

    * L3 routing mode with 2 zones and 2 interfaces
    * Hybrid L3 with L2 interfaces
    * Virtual Wire (vwire)

Add-on configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + Basic gateway security policies

Version Selection Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Selected choice will apply to the configuration mode in step (4)

    + v10.0 - loads IronSkillet 10.0 snippets
    + v10.1 - loads IronSkillet 10.1 snippets
    + v10.2 - loads IronSkillet 10.2 snippets


REST device queries
~~~~~~~~~~~~~~~~~~~

  Not shown in the menus yet part of the skillet framework are REST skillet types.
  These are used to query the firewall and get the interface and zone name information to be
  used as dropdown options in the deployment and security policy web forms.




