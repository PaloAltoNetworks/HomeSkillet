What are the changes from standard IronSkillet?
===============================================

In order to create a simplified in-home template, the following elements have been removed from the standard
IronSkillet configuration:

    + email alerts and scheduling: assumes no email server available in a simple deployment

    + disable the 'no decrypt' decryption rule to avoid untrusted and expired cert issues

    + remove the superuser admin/password config - assumes user has setup their own login access

    + remove the management interface IP and DNS configuration - assumes already online for initial updates

    + allows for http range to avoid issues with home use