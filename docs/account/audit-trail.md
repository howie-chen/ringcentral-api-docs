# Audit Trail

Audit Trail allows you to track configuration changes made to a RingCentral online account. If other Administrators are working on the same account, you need a change log to provide coordinated support. Additionally, failed logins and locked accounts are viewable through the Audit Trail API.

!!! hint "Audit Trail API is in beta - please request access"
    To call the Audit Trail API your application needs to have 'Read Audit Trail' permission. If you are using an application that doesn't have that permission, you can reach out to our support team with your application's Client ID and [fill out the following form](https://forms.gle/uAiekJWr2rK8vX2u9).


## Configuration Changes to Track

Administrators can make several account changes including managing phones & devices, users, meetings, and even billing. Since Audit Trail API tracks the same configuration changes as the admin UI, you can use the link below for a list of configuration changes that are tracked.

* [Configuration Changes](https://support.ringcentral.com/article/Audit-Trail-Configuration-Changes-Tracked).

## Tracking Changes in AWS or Splunk

Tracking these changes is important for compliance reasons and there are times when you need to retain and easily search these configuration changes in an external system like AWS DynamoDB or Splunk. You may even want to retain configuration changes for longer than 180 days or more than 10,000 records. The Audit Trail API allows you to collect these configuration changes in an external system periodically. Here is a demonstration and some sample code for how you would use the Audit Trail API to put configuration change details into an external system.

* [Sample Code for AWS DynamoDB and Splunk](https://github.com/ringcentral/audit-trail-demo)

## Limitations

The Audit Trail API was not designed to hold a lot of data nor be called frequently. For this reason, limitations have been put on the Audit Trail API. 

For each account:

* Up to 180 days of records
* 10,000 total records

This means if you have more than 10,000 records within 30 days, then you have hit the limit.

Also, this API belongs to the Heavy usage plan and is rate limited by it.

## Sample code

To get you started, here is some sample python code to retrieve audit logs from your account.  This sample code assumes you have built an `envjwt.py` file with your own environment variables

=== "Python"

``` python
{!> code-samples/account/audit-trail.py !} 
```
