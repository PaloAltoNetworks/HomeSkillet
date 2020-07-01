# IronSkillet variations for HomeSKillet configuration

The primary assumption is that home users with a PA-220 or similar device
already have their management port configured and operational. The same
is true for the admin superuser. Therefore this portion of the configuration
is omitted during snippet loading.

Residential usage can be impacted with a full IronSkillet configuration.
Therefore items such as decryption cert checks and email alerts not part
of the HomeSkillet base configuration.

The following snippets and associated variables have been omitted from the
snippet loading:

* device_system_dns
* email_scheduler_simple
* log_settings_profiles_email
* mgt_config_users
* shared_log_settings_email
* hs_device_setting_allow_httprange
* address
* hs_rulebase_decryption_disable

  
    
   


