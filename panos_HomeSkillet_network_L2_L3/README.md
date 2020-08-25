# Internet Gateway template base configuration

This set of snippets are loaded prior to the security tier selection.

The snippets included are:

* interface: Multiple internal L2 interfaces and vlan along with L3 internet interface

* virtual router: sets of basic routing with a default-gateway to the internet

* zone: 3-zone model with L2 and L3 trust and untrust zones

* NAT: source-based port NAT mapping all users to a single public IP

* network profiles: management Interface profile

