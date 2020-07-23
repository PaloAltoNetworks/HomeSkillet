# IronSkillet variations for HomeSKillet configuration

The primary assumption is that home users with a PA-220 or similar device
already have their management port configured and operational. The same
is true for the admin superuser. Therefore this portion of the configuration
is omitted during snippet loading.

Residential usage can be impacted with a full IronSkillet configuration.
Therefore items such as decryption cert checks and email alerts not part
of the HomeSkillet base configuration.
Users have an option in the workflow to load v9.0 or v10.0 IronSkillet base 

The following snippets and associated variables have been omitted from the
snippet loading:

v9.0

    * device_system_dns
    * email_scheduler_simple
    * log_settings_profiles_email
    * mgt_config_users
    * shared_log_settings_email

Instead of remove the decryption configuration it is left for reference but
disabled using the snippet:

hs_rulebase_decryption_disable

This can easily be enabled as required
The following are edits based on observed issues in home configurations.

hs_device_setting_allow_httprange: this is enabled to ensure home streaming
and other applications are not impacted. This has been observed with
Amazon Prime video streaming.



v10.0

    * device_system_dns
    * email_scheduler_simple
    * log_settings_profiles_email
    * mgt_config_users
    * shared_log_settings_email
    * hs_device_setting_allow_httprange
    * address
    * hs_rulebase_decryption_disable

  
    
   


