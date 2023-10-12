author: HariRangarajan-Solace
summary: Day 3/5 : This code lab walks the participant through the experience of using SAP AEM to event enable their SAP ecosystem and workflows
id: sap-aem-int-day-3
tags: SAP, AEM, Event Portal, SAP BTP, CAPM
categories:
environments: Web
status: Hidden
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/sap-aem-int-day-3

# Event Enable SAP Using SAP Advanced Event Mesh - Day 3

## What you'll learn: Overview

Duration: 0:05:00

Day 3 of 5.
Topics covered :
- Event enabling integration flows

## What you need: Prerequisites

Duration: 0:07:00

Enter environment setup & prerequisites here


## Step 1 - Event Enabled Integration flows

### 1 - Download and import the template integration flows


Download [AEMBusinessPartnerAddressCheck.zip](artifacts/cloud-integration-flows/AEMBusinessPartnerAddressCheck.zip), [AEMLegacyOutputAdapter.zip](artifacts/cloud-integration-flows/AEMLegacyOutputAdapter.zip) & [AEMSalesOrderNotification.zip](artifacts/cloud-integration-flows/AEMSalesOrderNotification.zip)

- Import AEMBusinessPartnerAddressCheck.zip, AEMLegacyOutputAdapter.zip & AEMSalesOrderNotification.zip into your
  Integration Suite tenant

### 2a - Setup/configure SAP AEM

Create input queues for your integration flows:
[Go to Cluster Manager -> <your service> -> Manage -> Queues - to open the Broker UI]

1. For AEMBusinessPartnerAddressCheck:
    * CIBusinessPartnerChecker
      ![queue settings](img/CIBusinessPartnerChecker-queue-settings.png)
      ![queue settings pt2](img/CIBusinessPartnerChecker-queue-settings-pt2.png)
      *Add the following subscriptions to the queue
      ![queue subscriptions](img/CIBusinessPartnerChecker-queue-subs.png)

    * CIBusinessPartnerCheckerDMQ
      ![queue settings](img/CIBusinessPartnerCheckerDMQ-queue-settings.png)
    * CIBusinessPartnerChecked (optional)
      ![queue settings](img/CIBusinessPartnerChecked-queue-settings.png)
      *Add the following subscriptions to the queue
      ![queue subscriptions](img/CIBusinessPartnerChecked-queue-subs.png)
    * CIBusinessPartnerInvalid (optional)
      ![queue settings](img/CIBusinessPartnerCheckedInvalid-queue-settings.png)
      *Add the following subscriptions to the queue
      ![queue subscriptions](img/CIBusinessPartnerCheckedInvalid-queue-subs.png)

2. For AEMSalesOrderNotification
    * CISalesOrderNotification
      ![queue settings](img/CISalesOrderNotification-queue-settings.png)
      ![queue settings pt2](img/CISalesOrderNotification-queue-settings-pt2.png)
      *Add the following subscriptions to the queue
      ![queue subscriptions](img/CISalesOrderNotification-queue-subs.png)

    * CISalesOrderNotificationProcessed (optional)
      ![queue settings](img/CISalesOrderNotificationProcessed-queue-settings.png)
      *Add the following subscriptions to the queue
      ![queue subscriptions](img/CISalesOrderNotificationProcessed-queue-subs.png)

3. For AEMLegacyOutputAdapter
    * CILegacyAdapterIn
      ![queue settings](img/CILegacyAdapterIn-queue-settings.png)
      ![queue settings pt2](img/CILegacyAdapterIn-queue-settings-pt2.png)
      *Add the following subscriptions to the queue
      ![queue subscriptions](img/CILegacyAdapterIn-queue-subs.png)

    * CILegacyAdapterInDMQ
      ![queue settings](img/CILegacyAdapterInDMQ-queue-settings.png)

### 2b - Setup/configure dependency services

1. For AEMBusinessPartnerAddressCheck
    * Activate SAP's Data Quality Management Service (DQM) by following
      this [blog](https://blogs.sap.com/2022/02/15/getting-started-with-sap-data-quality-management-microservices-for-location-data-btp-free-tier/)
2. For AEMSalesOrderNotification
    * You'll need an external email service to be able to automatically send emails, details like smtp server address,
      username (email) and password.
3. For AEMLegacyOutputAdapter
   > The legacy output adapter is simulating appending events to a file via an SFTP adapter, which could be imported to
   a legacy system. The actual flow doesn't require a working sftp destination as it's just being used to simulate a
   failure to demonstrate the retry and error handling capabilities of AEM. The flow will try a few times to deliver
   each event to the SFTP destination. After 3 failed attempts messages will be moved to a Dead Message Queue for manual
   processing by a UI5 and Business Process Automation workflow.

   > If, after successful demonstration of the error handling, you would still like to see a successful delivery of
   events to a file via sftp, you will need an sftp server and sftp credentials to configure the flow with a valid
   endpoint (sftp server address and username password) and import the ssh identidy into .

### 3 - Configure your integration flows

### 4 - Deploy your integration flows

## Takeaways

Duration: 0:07:00

✅ < Fill IN TAKEAWAY 1>   
✅ < Fill IN TAKEAWAY 2>   
✅ < Fill IN TAKEAWAY 3>   

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
