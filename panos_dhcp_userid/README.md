# DHCP only UserID

A simple userID configuration that sends local DHCP server log information
to the firewall and parses out user information.

This only works with DHCP devices. No coverage for static IP addresses.

## Variables

* TARGET_IP: IP address of the management interfaces

* TRUST_ZONE: Internet interface where userID will be enabled