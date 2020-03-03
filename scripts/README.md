# Operational Scripts

A suite of python scripts to perform various operation tasks outside of configuration.

## Scripts Overview

### Content Update

Referenced by the content update skillet to check and update threat/content signatures as
required in a new platform.

### Install License

Referenced by the install license skillet to install and activate licenses.

### Load Baseline

Referenced by the load baseline skillet. Import, Load, and Commit an empty configuration
including only the management interface and admin elements.

## Why the Scripts Folder?

For python scripts used in a single application set like HomeSkillet, the optimal
model is a single set of requirements and associated virtual environment. This avoids the
overhead of each script loading its own virtual environment.