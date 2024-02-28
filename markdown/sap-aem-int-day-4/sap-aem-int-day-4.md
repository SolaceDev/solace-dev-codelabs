author: Scott Dillon
summary: Day 4/5 : This code lab walks the participant through the setup and configuration of using SAP Business Process Automation to deal with message exceptions generated when using SAP AEM. This scenario will use SAP BPA, SAP Cloud Integration and SAP UI5 for the end to end scenario.
id: sap-aem-int-day-4
tags: SAP, AEM, Event Portal, SAP BTP, CAPM
categories:
environments: Web
status: Hidden
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/sap-aem-int-day-4

# Event Enable SAP Using SAP Advanced Event Mesh - Day 4

## What you'll learn: Overview

Duration: 1:30:00

Day 4 of 5.
Topics covered :
- Using SAP Business Process Automation to review event exceptions

## What you need: Prerequisites
- SAP Business Process Automation Activated  
- Access to SAP BTP Cockpit and ability to create Destinations
- Access to Cloud Integration and Ability to create development artifacts
- Access to the AEM Console


## Using SAP BPA to handle event exceptions

In the world of Event Driven Asynchronous messaging, sometimes events cannot be successfully processed by a consumer and as a result, they need to be dealt with on an exception basis. As a result, there is built in capability within the broker referred to as a Dead Messages Queue. Essentially, messages can be placed into a special queue where they can later be reviewed and properly dealt with. Should you wish to read more on the concept of Dead Message Queues, please refer to the following link. 

[Link to Blog](https://solace.com/blog/pubsub-message-handling-features-dead-message-queues/)

In our scenario, we will artificially create a situation where messages cannot be delivered to the endpoint. As a result, they end up in the Dead Message Queue and the application shown below has an integration card on it called "Dead Message Queue". This card is a very simple Queue browser. It displays the messages without removing them from the Queue unless you hit the submit button. The steps and diagram below walk through the exact flow you will be implementing.

In the following diagram, you can see the flow you are about to implement.
- Step 1 -> The user decides to investigate the item displayed in the dead message queue so they hit the submit button which causes the message to be published on the topic shown.
- Step 2 -> There a queue that you will create called SOREJECTED that has a subscription to attract these events.
- Step 3 -> The cloud integration iFlow is listening on the SOREJECTED queue for these events.
- Step 4 -> The iFlow is responsible for transforming the message into a different format that can be used later by the BPA API.
- Step 5 -> The SO_WF queue is attracting events with this new format.
- Step 6 -> A rest delivery point will use the information in the event to call the API for starting the BPA process
- Step 7 -> The BPA Process will place an entry in the Inbox for Approval
- Step 8 -> Once the SalesOrder is approved via the Form, it will be re-published for processing which triggers an updated on the orginal screen that started the entire process.

![BPA Image](img/BPAPRocess2.png)

## Creating the Queues for BPA Scenario
Note: If you prefer not to use the CI/CD tool, check out the Appendix further down to find instructions to do it manually.

You will now create the queues for this scenario via the CI/CD tool that can be found at this link:

https://rapid-pilot-createconfig-quiet-elephant-yt.cfapps.ca10.hana.ondemand.com/

![BPACLI1](img/BPACLI1.jpg)

Below you will find the JSON structure to paste into the window. The only other thing you will need is the SEMP (Solace Element Management Protocol) Connection details. Details to find the SEMP API will be provided after the JSON Structure.

```JSON
{
    "Queues": [
        {
            "name": "SO_WF",
            "owner": "#rdp/RDP1",
			"access-type": "non-exclusive",
            "redelivery": true,
            "try-forever": false,
            "max-redelivery-count": 3,
			"non-owner-permission" : "consume",
            "subscriptions": [
                "sap.com/bpasalesorder/rejected/V1"
                
            ]
        },
        {
            "name": "SORJECTED",
			"access-type": "exclusive",
            "owner": "",
            "redelivery": true,
			"non-owner-permission" : "consume",
            "subscriptions": [
                "sap.com/salesorder/rejected/V1"
            ]
        }
    ]
}
```

From the manage tab within the web console, towards the bottom, you will see "Other Management Tools", expand the "SEMP - REST API" section. From there, you can find the 4 pieces of information you need to execute the tool above. 
![SEMPDETAILS](img/SEMPDETAILS.jpg)
Copy/paste those details into the tool above along with the JSON structure and press the "Create Configuration" Button and voila, you should have your 2 queues and subscriptions created.
**** When copying the details over, make sure not to copy over extra spaces like I did on my first 3 attempts :-) ****

**** Of course, it would be a great idea to check the queues on the console and verify that you have 2 new queues SOREJECTED and SO_WF :-) ****

## Creating the Rest Delivery Point

Next step to create the Rest Delivery Point and associated components. Navigate to the clients tab as shown on the left and then click the + Rest Delivery Point Button.. The name of the RDP is “RDP1”.


![BPA Image 10](img/BPA-10.jpg)

You will now create a Rest Consumer that will be the target for your Events.

![BPA Image 11](img/BPA-11.jpg)

 Enter “SO_WF_REST_CONSUMER” and press “Create”.

![BPA Image 12](img/BPA-12.jpg)

In order to fill out the information for the Rest_Consumer, we need to get the authentication information for the Rest Consumer.

From the BTP Cockpit, we need to find the service key for the BPA Service. Navigate to the sub-account where you can find the BPA service. From there, click on the "Instances and Subscriptions" and navigate to the 3 "..." at the end.
![BPA Image 25](img/SPA-BPA-25.jpg)
To the right of the service key, you should again see 3 "..." where you can click "View". This will display the service key.
![BPA Image 26](img/SPA-BPA-26.jpg)
The service key has all the information you need. In this screenshot, copy from the Service Key as shown in this screenshot to configure the oAuth authentication. Pay attention to the detail that outlines the necessary information to be added to the Token URL
![SK Image 2](img/SK-2.jpg)
Next you will create the connection between the Rest Consumer and the Queue that it will use. Select Queue Bindings and then click the “+Queue Binding”.

![BPA Image 14](img/BPA-14.jpg)

From the dropdown, select the previously created Queue “SO_WF”.

![BPA Image 15](img/BPA-15.jpg)

This is where you will enter the remainder of the endpoint…aka the endpoint for creating the Workflow Instances. This should be the same so you can use the same value “/workflow/rest/v1/workflow-instances”

![BPA Image 16](img/BPA-16.jpg)

The type of content that we will send to the API is of JSON format. In order to indicate this, we need to create a request header called "Content-Type" and set the value to "application/json".

![rdp Image 1](img/rdp-1.jpg)

Last but not least, one last small change. The RDP process will be the owner of this queue so now that we have the RDP Created, lets ensure that we set the owner properly. Modify the owner of the SO_WF as per the following screenshot.
![rdp Image 1](img/SOWFSettings.png)
At this point, you should have a functioning RDP. The operational status on the screen should say Up for all components with the exception of the RDP Client. If any of them indicate “Down”, you will need to Troubleshoot, go back and double check your settings. There is also a Stats link that you can use to see the Error Messages.

![BPA Image 17](img/BPA-17.jpg)



Congratulations, you have completed setup of the Rest Delivery Point. Each time a message is placed into the Queue, it will automatically call the API associated with the RDP.


## Creating BTP Destination for BPA

The business process that we will deploy is activated by an API Trigger which can be seen in the diagram and the last step of the process is the publishing of an event. This process uses a Rest Call to the broker that is encapsulated in the SAP BPA “Action” which can be seen in the screenshot immediately following the "Approve" action. 

![SAP BPA Image 1](img/SPA-BPA-1.jpg)

The "Action" component needs to be associated with a destination. In order to create the destination, you will need "REST" connectivity information from your broker. Navigate to your AEM Cloud Console, you will select the Cluster Manager and then you will select your broker. From there, you will select the “Connect” option at the top. On this screen, make sure that the “View By” is set to Protocol as the first step. From there, expand the REST protocol and everything you need to create the destination will be visible.

![SAP BPA Image 2](img/AEM-2.jpg)

### Navigate to the BTP Cloud Cockpit
Once you have the connectivity information, Navigate to the Destinations Section within the BTP Cockpit, Select the “New Destination” option. You will be creating a destination called “AEMBROKERREST”.

![BPA Image 20](img/BPA-20.jpg)

You will populate the Destination information as shown below and you will add two properties that are both set to true.
- sap.applicationdevelopment.actions.enabled – true
- sap.processautomation.enabled – true

When your destination is created, double check to make sure both properties are there.


![BPA Image 21](img/BPA-21.jpg)

## Creating the SAP BPA Project

For the SAP BPA setup, we will be importing 1 File that contains several components: 
- 11 Artifacts
- 1 Trigger
- 1 Dependency for the Action Group that represents the action group
- a project of type “Process Automation”

We will import the SAPAEMSO_3.1.0.mtar file. Select the import option which is highlighted by the red square. When prompted, select the SAPAEMSO_3.1.0.mtar file for import. Once it’s successfully imported, you will see 1 project listed as per the screenshot below 
*** You can download the file here https://github.com/SolaceLabs/aem-sap-integration/blob/main/deployable/SAPAEMSO_3.1.0.mtar ***

![SPA BPA Image 11](img/SPA-BPA-11.jpg)

In order to deploy the BPA project, you need to associate the project with the Destination that you have already created in BTP. The deployment process will ask you to select a Destination so you need to register the destination with the BPA tooling. Expand the menu options on the top left.

![SPA BPA LOBBY](img/BPA_LOBBY.png)

Click on the Control Tower and Select Destinations

![SPA BPA ControlTower](img/BPA_ControlTower.png)

When you click “New Destination”, you should see the Destination you created in BTP called “AEMBROKERREST”, if you don’t, you have not specified the properties correctly and you will need to investigate. Select the Destination and you should see it populate in the UI. Now, we can deploy the project.

![SPA BPA Destination](img/BPA_Destination.png)

Head back to the Lobby and Click on the SAPAEMSO project.
![SPA BPA LOBBY](img/BPA_LOBBY.png)

Prior to releasing the project, we have to make a small change to the project. Lets start by clicking on the "Sales Order Review" Process.

![SPA BPA Image 14](img/SPA-BPA-14.jpg)

In the business process, we must indicate which users will have the notification delivered to their inbox. Click on the Approval Form for Sales Order. You will see properties appear on the right side of the screen. Specify the userid of users who should have the notification sent to their inbox. In this case, I have specified 2 IDs separated by a comma.
Once you have made the change, we now need to release and deploy the project. Click the "Release" option in the upper right.
![SPA BPA Image 25](img/BPA-25.jpg)

You can select the appropriate version with either of the radio boxes and then press the release button.
![SPA BPA Image 15](img/SPA-BPA-15.jpg)

Once the project is released, you should see the Deploy Button. Press it to reveal a new feature that will ask you to select an environment. Select the "Public" environment and press "Upgrade".
***Note, in my case, I have several versions already deployed, so if it's the first deployment, it might not say "upgrade" as in the screenshot.***
![SPA BPA Image 15](img/SPA-BPA-15A.jpg)
You will likely getting a warning message that indicates this deployment could have an affect on already deployed triggers..." press deploy.

![SPA BPA Image 15](img/SPA-BPA-15B.jpg)

Here you must select your destination for the action. If your destination is not in the dropdown, something has not been configured properly in the Settings of the project.
![SPA BPA Image 17](img/SPA-BPA-17.jpg)

This is the last step to deploy your business process, click Deploy.
![SPA BPA Image 19](img/SPA-BPA-19.jpg)

You should now see "Deployed" and "Active" on the top left of the screen and your process should now be running.
![SPA BPA Image 20](img/SPA-BPA-20.jpg)


The process should now be running. Now we need to add an iFlow to transform messages so that they can be used to Trigger the process.

## Integration Suite Setup

In the Business Process Automation scenario, we will activate an instance each time a record from the Dead Message Queue is submitted for review. The Sales Order Event from the Queue will need to be augmented with some additional metadata that is required for the BPA API. In order to augment the message with the additional elements, we will use 2 Cloud Integration Artifacts to do this:
- SOTOBPASOV2 – This message mapping artifact will map the incoming Sales Order Event to the Structure required for the BPA API
- SalesOrderToBPAiFlow – This iFlow will connect to the Advanced Event Mesh and pull in all orders that have been submitted for processing from the UI5 application. Technically, the iFlow connects to a Queue that you will create on the broker. Once the Sales Order event is received, it will be routed  through the mapping and then published onto a new topic with the augmented schema. 

Two artifacts will be provided to you for import, so the first step is to navigate to the package where you will create your content and place your package into “Edit” mode.


![IS Image 1](img/IS-1.jpg)

Once you have the package in edit mode, select the DropDown under “Add” and select “Message Mapping”.

![IS Image 2](img/IS-2.jpg)

At the top of this form, you will select “Upload” and then you will select the zip file with the name "SOTOBAPSOV2" for Message Mapping.

![IS Image 3](img/IMPORTMM.jpg)
Once the artifact is uploaded, you will open it up and edit one of the properties. You will see one of the attributes in the target mapping is “DefinitionID”. This is the unique ID of the Business Process Automation process that we will be activating. This ID will be taken from the BPA environment. Within the BPA environment, navigate to the Monitor section, find your business process and you will find the ID that needs to be entered. (** Go see the next screenshot to see specific details on how to find ID**) Once you have modified the ID, be sure to hit Save at the top and then you can hit “Deploy” from there or back from the main screen as shown below.
![IS Image 8](img/MMDEFID.jpg)
Navigate Back to the SAP Business Process Automation Environment temporarily.
From the Business Process environment, navigate to the "Monitoring" section. To find this, simply click on the SAP Icon at the top to reveal the main menu. From there, on the left side, Click "Monitoring" and then "Processes and Workflows".
![IS Image 27](img/MonitoringBPA.jpg)
You should now see the "Sales Order Review" process listed and right below it you should see the ID. This is the ID you want to copy and paste into the iFlow mapping section. You will take the ID and you will use it in the iFlow to uniquely identify the Workflow to be started. Essentially, the API from SAP is very generic. You call the API with the ID of the workflow to be started with the payload and voila, you can start the process. *** If for some reason, the Sales Order Review process is not visible, select "Navigation" at the top to select Sales Order Review.
![IS Image 27](img/BPAID.jpg)

Now we will import the iFlow using the same approach we just followed for the Message Mapping.

![IS Image 5](img/IS-5.jpg)
Select the “Upload” checkbox and use the 2nd zip file called "SalesOrderToBPAiFlow.zip.

![IS Image 6](img/IS-6.jpg)

Once after the iFlow is successfully imported, we need to configure the appropriate connection information to connect to the AEM Service. You should know where to find this information now :-)

![IS Image 12](img/IS-12.jpg)

On this screen, we will configure the iFlow to be watching the Queue "SOREJECTED"....short for Sales Orders Rejected.
![IS Image 13](img/IS-13.jpg)

Now we need to configure the publishing component of the iFlow. It will be the same connection information as the consumer above.
### Please note the creation of the Secure Parameter is further down 
![IS Image 14](img/IS-14.jpg)
Now we configure the iFlow. We will publish to a topic called "sap.com/bpasalesorder/rejected/V1". The thought here is that we still have a Sales Order but it's been formated for the Business Process Automation API. Earlier in the exercise you setup a Queue listening for this event so it's really important that these 2 topics match so that all BPA rejected sales orders get attracted into the right Queue. You could add another level to the Topic to reflect the use case or embed something in the name like I have done.

![IS Image 15](img/IS-15.jpg)

Now that both the message mapping and the iFlow have been imported and configured, you need to deploy them both. You have a few ways to deploy an artifact. As you are editing within the editor and have saved your changes, you can deploy from within the editor. The 2nd option is from the list of artifacts within the folder.
![IS Image 17](img/iFlowDeploy.jpg)

Once both of the artifacts have been deployed, your last step is to create the secure parameter. Under "Monitor" Select Integrations.

![IS Image 17](img/IS-17.jpg)

From here, you will create a Secure Paramater and you will use the name "CABrokerUserPass" ***or you can use another name, just be sure to use the same one in the iFlow*** You will enter the corresponding password for the solace-cloud-client Username.

![IS Image 7](img/IS-16.jpg)

Before proceeding, please check the monitor to ensure that both artifacts have been deployed successfully.

![IS Image 9](img/IS-9.jpg)





## Testing the components
At the moment, you should have a fully integrated scenario. 

From the Sales Order Dashboard, hit "Submit" on the "Dead Message Queue" card to send a message for review. Now we to check if the event triggered a creation of an Inbox Item.

From the main screen of the BPA Lobby, you can see in the upper right, a little inbox symbol...Click It.
![SPA BPA Image 21](img/SPA-BPA-21.jpg)
Now you will see the form that we created to display the contents of a Sales Order Event.
![SPA BPA Image 22](img/SPA-BPA-22.jpg)

Of course, this is the Happy Path :-) Everything Worked. 
However, what if you don't see the item in the inbox ?

My first suggestion would be to use the "Try Me" tab on the broker with the configured Rest Delivery Point and let's do some simple tests.

![SPA BPA Image 23](img/SPA-BPA-23.jpg)
On this screen, we can test several things. For starters, we can confirm that the iFlow that we deployed is working and successfully transforming our message.
On the publisher side, connect to the broker and use "sap.com/salesorder/rejected/V1" as the topic and for the message use the following structure. This will simulate an event being submitted for Review from the Integration Card.
```JSON
{
	"orderHeader": [
		{
			"salesOrderNumber": "SO1001",
			"creator": "John Doe",
			"date": "2023-08-04",
			"salesType": "Online",
			"ordertype": "Standard",
			"salesOrg": "SA01",
			"distributionChannel": "DC01",
			"division": "DV01",
			"netvalue": 375,
			"currency": "USD",
			"customer": [
				{
					"customerId": "CUST001",
					"customerName": "ABC Corp",
					"zipCode": "12345",
					"street": "Main Street",
					"phone": "555-123-4567",
					"country": "USA",
					"city": "New York",
					"emailAddress": [
						{
							"email": "john.doe@abccorp.com"
						}
					]
				}
			],
			"orderItem": [
				{
					"item": "ITEM001",
					"material": "MAT001",
					"materialType": "Product",
					"itemType": "Standard",
					"itemDescription": "Rocky Ridge Mountain bike",
					"orderSchedule": [
						{
							"scheduleNumber": "SCH001",
							"quantity": 100,
							"uom": "EA"
						}
					]
				}
			]
		}
	]
}
```
On the subscriber side, connect to the broker and use ">" as your topic. This will show everything. When you publish your message, you should immediately see a message appear in the subscriber window and you should be looking for a couple of things:
- The message that you published above
- A new message with a different Topic - sap.com/bpasalesorder/rejected/V1
- The body of the message should essentially be the same BUT it has a new wrapper called "context" and a new attribute called "definitionId". If you don't see both of these things, something is wrong with the iFlow. It's important that the "definitionID" is populated with the definition ID that represents your process or it won't work.
- After you publish the event, you should see a new item in your inbox. If the message appears to have the right structure in the subscriber window, then your iFlow is working as designed. If the iFlow is working then the next place to look is the configuration of the Rest Delivery Point. The RDP will be listening for these rejected messages and then calling the API to start the BPA process. Below we have a section that outlines how to see the logs associated with the rest delivery point. Last but not least, check to see if messages are accumulating in SO_WF.

  ### IF YOU SEE MESSAGES IN THE INBOX....WOOHOO

## Debugging RDP Error

This is an optional step in case you encounter any issue with AEM RDP Connection.

Below steps will allow you to connect to AEM CLI console and look at the logs.

### Enable the Access to Port 22

Before accessing the CLI, we need to make sure that access to port 22 (default ssh port) is open.

1.	From the SAP AEM Console, select your service that you want to debug
      ![BPA Image 3](img/BPA-3.jpg)

2.	Select Manage and then Advanced Options

	![AEM Image 3](img/AEM-3.jpg)

3.	This will open up New Advanced Management Options Page

	![AEM Image 4](img/AEM-4.jpg)

4.	Scroll down to “Port Configuration” Section. On the Public Endpoint section, select “…” to edit the port configuration

	![AEM Image 5](img/AEM-5.jpg)

5.	Scroll down to “Management” and check the “Enable Secured CLI Host (SSH), use port” option. This will allow access to the broker command line utility

	![AEM Image 6](img/AEM-6.jpg)

6. Go back to Manage Tab from Advanced Management Options page.

   ![AEM Image 7](img/AEM-7.jpg)

7. Get the hostname, management userid and password of the service. Make sure to get the viewer credentials

   ![AEM Image 8](img/AEM-8.jpg)

### Accessing AEM Service Commandline Utility

8. Use any commandline utility and ssh to the service using valid hostname, userid and password as below: \
   *`ssh userid@hostname`*  
\
   ![AEM Image 9](img/AEM-9.jpg)

9.	Now you can view the rdp error logs using the command

*`show log rest rest-delivery-point errors`*

This command will give you HTTP error (if any)that you might have received from BPA web endpoint.

## Appendix 1 - Creating Queues Manually for Section 4
If you want extra practice creating queues via the web console, you can follow these instructions and then return to section 4 to finish your configuration
Navigate to the main console and go to the cluster manager. From there, select the broker where you will be configuring your Rest Delivery Point.

![BPA Image 3](img/BPA-3.jpg)

From this screen, you will select the manage option at the top.

![BPA Image 4](img/BPA-4.jpg)

You will then select “Queues” towards the middle of the screen. 
Selecting the Queue option will now re-direct you to a different screen and will open the Broker Manager for the selected broker. 

![BPA Image 5](img/BPA-5.jpg)

On this screen, we will start by creating a Queue and Subscription that will be used to capture the items from the DMQ that users would like to start review processes for. Click on the “+Queue” option.

![BPA Image 6](img/BPA-6.jpg)

Create a new Queue with the name “SOREJECTED”.

![BPA Image 22](img/BPA-22.jpg)

Now we will create a subscription that will capture all the messages that are being pushed out from the Integration Card. Messages are published from the Integration Card and then removed from the Queue.
Add a Subscription by Clicking the “+Subscription” button and then add the subscription “sap.com/salesorder/rejected/V1”. Once messages are received into this Queue, they will be picked up by the Integration Flow that will augment the schema of the message. This iFlow will publish a message that will be used to activate the Business Process Automation process.


![BPA Image 24](img/BPA-24.jpg)

Repeat the process to add another Queue called “SO_WF”. Add a subscription for “sap.com/bpasalesorder/rejected/V1”. The iFlow that enriches the SalesOrder publishes the new message using that topic.

![BPA Image 23](img/BPA-23.jpg)

## Takeaways

✅  Understand concept of Dead Message Queues
✅  Understand how to use SAP BPA to process Dead Messages
✅  Understand how to use an iFlow with an Event for transformations
✅  Understand how to setup a Rest Delivery Point


![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
