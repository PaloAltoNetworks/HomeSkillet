
Validations
===========

Network and Policy Dependencies
-------------------------------

A set of validation checks are performed to ensure dependency required for config elements added in steps 2 and 3
exist in the firewall.

This validation is used twice in the workflow: once before the IronSkillet configuration with an assumed fail
for a new install and then after the IronSkillet configuration and commit to show a pass condition.


Dependency Checks
~~~~~~~~~~~~~~~~~

The following categories of tests are performed

    + named zone protect profile exists

    + referenced security profiles and profile groups

    + referenced logging profile
