MSSP Templates Overview
=======================

The Palo Alto Networks MSSP templates are provided to simplify the deployment of security services. Instead of extensive and detailed 'how to'
documentation, the MSSP templates provide an easy to implement configuration model.

The benefits of this template model include:

    + Faster time to implement
    + Reduce configuration errors
    + Improve security posture

For the MSSP, the focus of templating is on the repeatable aspects of deployment. This can include day one starter configs
for bespoke deployments, branch deployments, or SMB Internet Gateway offerings bundle with network services.

With the emphasis on repeatability, the templates provided cover:

    + Panorama-based internet gateway services

    + Direct firewall internet gateway configs (xml and set snippets)

    + GPCS core and remote_branch using Panorama

    + Sample CPE IPSEC tunnel snippets for GCPS remote networks


Relationship to the IronSkillet Project
----------------------------------------
Instead of a complete set of configuration snippets, the MSSP templates are incremental to the IronSkillet day one
best practice configurations.

More information about IronSkillet can be found at:

|skilletdocs|


The day one configuration provides reference configurations primarily including security profiles, logging, reporting,
device hardening, and dynamic update scheduling. It is use-case agnostic and relies on additional configuration elements
such as the MSSP internet gateway templates to be deployment ready.


Gold-Silver-Bronze Variants
---------------------------

IronSkillet assume that users have all subscriptions (Threat Protection, URL Filtering, Wildfire) enabled to meet the
criteria of best practice. However, the MSSP can elect to tier services with incremental price points based on subscriptions.

The template tiers using the generic Gold/Silver/Bronze naming convention provide alignment to subscription tiers:

    + Gold: includes all subscriptions (Threat, URL, Wildfire)

    + Silver: includes Threat (no URL or Wildfire)

    + Bronze: No subscriptions providing for limited or port-based protections



Using the templates
-------------------

The templates are available on GitHub at |repourl|.

Select the branch specific to the software release for your deployment.

The library consists of a set of xml and set configuration templates grouped by:

    + ``panos`` for stand-alone next-gen firewall deployments
    + ``panorama`` for Panorama system and managed device configurations

The templates in each device-type folder include:

    + ``snippets`` for more granular configuration elements
    + ``set commands`` for traditional CLI configuration



PAN-OS Excel set command spreadsheet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Also included for easy loading is an Excel formula-based spreadsheet with set commands. A variable value worksheet can be
edited to update the spreadsheet using localized values for various configuratino attributes.

More information for using the spreadsheet can be found at: :ref:`using_the_spreadsheet`.

.. NOTE::
        The spreadsheet set commands are specific to the firewall for sandboxing and non-Panorama deployments. The current
        Panorama model is focused on API-based xml configuration elements.


Jinja-based xml snippet and set command templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scripting or automation-centric users may prefer to use the base template files.
These are variable-based templates using a jinja ``{{ variable }}`` notation.

The xml snippets with metadata are designed to use API-based configuration loading into Panorama or the firewall and
can be coupled with workflow tools for repeatable deployments.



