# Internet Gateway template base configuration

This set of snippets are loaded prior to the security tier selection.

The snippets included are:

* interface: simple dual interface Internet Gateway model

* virtual router: sets of basic routing with a default-gateway to the internet

* zone: 2-zone model with internet and trust zones

* NAT: source-based port NAT mapping all users to a single public IP

* network profiles: management interface profile

The MSSP can edit/append as required for their specific deployments.

**NOTE**: The `zone_import_interface` snippet is used to create a mapping
of interfaces and zones. This element is managed by the system when doing
standard GUI/CLI edits yet required for a working xml configuration.


### This template assumes the device has the following licenses:

* Threat Protection

* URL Filtering

* Wildfire

This provides the highest level of security aligned with best practices.

Outbound rules are created using the recommended profile settings from
the IronSkillet day one configuration.

In addition, a security rule to provide more aggressive file-blocking
for unknown category URLs has been added.

