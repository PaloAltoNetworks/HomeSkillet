# Internet Gateway template base configuration

This set of snippets are loaded prior to the security tier selection.

The snippets included are:

* interface: simple vwire interface model

* * zone: 2-zone model with internet and trust zones

* network profiles: management interface profile

The MSSP can edit/append as required for their specific deployments.

**NOTE**: The `zone_import_interface` snippet is used to create a mapping
of interfaces and zones. This element is managed by the system when doing
standard GUI/CLI edits yet required for a working xml configuration.


