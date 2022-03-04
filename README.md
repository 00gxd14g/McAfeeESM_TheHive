# McAfee SIEM Open Case to TheHive API

### Usage

- $Alarm_Name = The "alarm name" field is a variable on the Remote Commands McAfee SIEM side.
- $Description = The "Description" field is a variable on the Remote Commands McAfee SIEM side.
- $Severity = The "Severity" field is a variable on the Remote Commands McAfee SIEM side.
- $Source_IP = The "Source IP" field is a variable on the Remote Commands McAfee SIEM side.
- TheHive_IpAddress = "TheHive_IpAddress" is the ip address of the server where thehive is installed. ex: 1.1.1.1 default port 9000

### Todo : 

- Command String are: send_thehive.py -thehiveip="$TheHive_IpAddress" --username="" --password="" --title="[$Alarm_Name]" --description="[$Description]" --severity="- [$Severity]"  --ip="[$Source_IP]"
- 
### Info

With this script, you can automatically send the alarms that occur on "McAfee SIEM" to the "TheHive" platform, the alarms you send will be automatically opened as a case.

If you want all alarm logs to be opened, you need to configure the remote command execution page of all your alarms.


![](https://fortinetweb.s3.amazonaws.com/docs.fortinet.com/v2/connectors-resources/McAfee%20ESM/McAfee%20ESM%20v2.1.0/McAfeeConnector_AlarmSettingsActionTab.png)

"Execute remote command" must be selected in your alarm settings.

![](https://community.mcafee.com/legacyfs/online/73424_pastedImage_0.png)

To automatically send alarms, you need a server that you can connect to with a "ssh". then you can save it by entering the appropriate parameters in the "Command String" field.

![](https://img001.prntscr.com/file/img001/o3FdObfmRsK9CPxzoFApIw.png)

