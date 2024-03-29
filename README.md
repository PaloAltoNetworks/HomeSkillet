# HomeSkillet

## Overview

HomeSkillet is a home-based deployment configuration as an Internet Gateway
using 2 zones, the untrust zone as a dhcp-client.

The security policy provides for outbound policies using IronSkillet
best practice security profiles and groups.

More details can be found at the
[HomeSkillet docs page](https://HomeSkillet.readthedocs.io)

## HomeSkillet and panhandler

HomeSkillet is designed to be used with the panhandler application to API
load structured configurations. It also captures web form data to semi-customize
the configuration for local use.

[k start guide](https://live.paloaltonetworks.com/t5/Skillet-Tools/Install-and-Get-Started-With-Panhandler/ta-p/307916)

[panhandler docs](https://panhandler.readthedocs.io)


## Support Policy
These scripts should be seen as community supported as Palo Alto Networks no longer officially
contributes to future releases. We do not provide technical support or help in using
or troubleshooting the components of the project through our normal support options
such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) partners
and backline support options. The underlying product used (the VM-Series firewall)
by the scripts or templates are still supported, but the support is only for the
product functionality and not for help in deploying or using the template or script itself.
