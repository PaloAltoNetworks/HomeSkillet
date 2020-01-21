
Workflows
=========

Full End-to-End Workflow
------------------------

Provides an end-to-end experience using the following skillets:

    + revert to an empty starter configuration
    + download and apply the latest threat and AV content updates
    + post step 1 validation showing all 'Fail' test results
    + step 1 day one configuration based on a subset of IronSkillet (commit currently required to pass 2nd validation)
    + post step 1 validation showing all 'Pass' test results and able to load steps 2 and 3
    + step 2 network configuration currently based on a 2-zone, 2-interface L3 gateway
    + step 3 security policy configuration for outbound Internet traffic

Add-on configuration options

    + simple DHCP-based userID using local firewall DHCP and logs to create userID dynamic entries




