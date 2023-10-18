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

In the world of Event Driven Asynchronous messaging, sometimes events cannot be successfully processed by a consumer and as a result, they need to be dealt with on an exception basis. As a result, there is built in capability within the broker referred to a Dead Messages Queue. Essentially, messages can be placed into a special queue where they can later be reviewed and properly dealt with. Should you wish to read more on the concept of Dead Message Queues, please refer to the following link. 

[Link to Blog](https://solace.com/blog/pubsub-message-handling-features-dead-message-queues/)

In our scenario, we will artificially create a situation where messages cannot be delivered to the endpoint. As a result, they end up in the Dead Message Queue and the application shown below has an integration card on it called "Dead Message Queue". This card is a very simple Queue browser. It displays the messages without removing them from the Queue unless you hit the submit button. Hitting the submit button will release the message from the Queue and it will be sent to the broker with a special topic. A special topic that will result in the message being placed into a Queue that is being actively monitored by Cloud Integration. The message will be transformed by Cloud Integration and the message will be placed back into the mesh. The broker will act upon this new message and instantiate a new business process for each message.

![BPA Image](img/BPA-1.jpg)

## Configure the required components for a Rest Delivery Point on the broker

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

Next step to create the Rest Delivery Point and associated components. Navigate to the clients tab as shown on the left and then click the + Rest Delivery Point Button.. The name of the RDP is “RDP1”.


![BPA Image 10](img/BPA-10.jpg)
You will now create a Rest Consumer that will be the target for your Events.

![BPA Image 11](img/BPA-11.jpg)

 Enter “SO_WF_REST_CONSUMER” and press “Create”.

![BPA Image 12](img/BPA-12.jpg)

This is the screen that requires some attention to detail. For starters, if you notice in the first red highlighted box, it’s not the entire endpoint, this will come later. This is the address of your BPA service on BTP. Also take note of the Port and Http Method. The next section is the Authentication Scheme. You will need to select oAuth 2.0 Client Credentials. Once you have selected those, you will need to retrieve the oAuth specifics from the BTP Cockpit…specifically the Client ID and the Token URL.

![BPA Image 13](img/BPA-13.jpg)

Next you will create the connection between the Rest Consumer and the Queue that it will use. Select Queue Bindings and then click the “+Queue Binding”.

![BPA Image 14](img/BPA-14.jpg)



![BPA Image 15](img/BPA-15.jpg)

From the dropdown, select the previously created Queue “SO_WF”.

![BPA Image 16](img/BPA-16.jpg)

This is where you will enter the remainder of the endpoint…aka the endpoint for creating the Workflow Instances. This should be the same so you can use the same value “/workflow/rest/v1/workflow-instances”

![BPA Image 17](img/BPA-17.jpg)

At this point, you should have a functioning RDP. The operational status on the screen should say Up for all components with the exception of the RDP Client. If any of them indicate “Down”, you will need to Troubleshoot, go back and double check your settings. There is also a Stats link that you can use to see the Error Messages.

Congratulations, you have completed setup of the Rest Delivery Point. Each time a message is placed into the Queue, it will automatically call the API associated with the RDP.

## Integration Suite Setup

In the Business Process Automation scenario, we will activate an instance each time a record from the Dead Message Queue is submitted for review. The Sales Order Event from the Queue will need to be augmented with some additional metadata that is required for the BPA API. In order to augment the message with the additional elements, we will use 2 Cloud Integration Artifacts to do this:
- SalesOrderToBPASalesOrderMM – This message mapping artifact will map the incoming Sales Order Event to the Structure required for the BPA API
- SalesOrderToBPAiFlow – This iFlow will connect to the Advanced Event Mesh and pull in all orders that have been submitted for processing from the UI5 application. Technically, the iFlow connects to a Queue that you will create on the broker. Once the Sales Order event is received, it will be routed  through the mapping and then published onto a new topic with the augmented schema. 

Two artifacts will be provided to you for import, so the first step is to navigate to the package where you will create your content and place your package into “Edit” mode.


![IS Image 1](img/IS-1.jpg)

Once you have the package in edit mode, select the DropDown under “Add” and select “Message Mapping”.

![IS Image 2](img/IS-2.jpg)

At the top of this form, you will select “Upload” and then you will select the zip file with the “MM” at the end for Message Mapping.
***Ignore the Red X…I had already deployed the mapping in my environment and hence the message 😊 ***

![IS Image 3](img/IS-3.jpg)
Once the artifact is uploaded, you will open it up and edit one of the properties. You will see one of the attributes in the target mapping is “DefinitionID”. This is the unique ID of the Business Process Automation process that we will be activating. This ID will be taken from the BPA environment. Within the BPA environment, navigate to the Monitor section, find your business process and you will find the ID that needs to be entered. Once you have modified the ID, be sure to hit Save at the top and then you can hit “Deploy” from there or back from the main screen as shown below.
![IS Image 8](img/IS-8.jpg)

The 2nd way to deploy an artifact is from the main screen as shown below.

![IS Image 4](img/IS-4.jpg)

Now we will import the iFlow using the same approach we just followed for the Message Mapping.

![IS Image 5](img/IS-5.jpg)
Select the “Upload” checkbox and use the 2nd zip file that contains the iFlow (***Not the one with the MM Extension ***).

![IS Image 6](img/IS-6.jpg)

Once after the iFlow is successfully imported, we need to configure the appropriate connection information to connect to the AEM Service. You should know where to find this information now :-)

![IS Image 12](img/IS-12.jpg)

On this screen, we will configure the iFlow to be watching the Queue "SOREJECTED"....short for Sales Orders Rejected.
![IS Image 13](img/IS-13.jpg)

Now we need to configure the publishing component of the iFlow. It will be the same connection information as the consumer above.
![IS Image 14](img/IS-14.jpg)
Now we configure the iFlow. We will publish to a topic called "sap.com/bpasalesorder/rejected/V1". The thought here is that we still have a Sales Order but it's been formated for the Business Process Automation API. Earlier in the exercise you setup a Queue listening for this event so it's really important that these 2 topics match so that all BPA rejected sales orders get attracted into the right Queue. You could add another level to the Topic to reflect the use case or embed something in the name like I have done.
Save and Deploy the iFlow.
![IS Image 15](img/IS-15.jpg)

Now that both artifacts have been deployed, you need to create the secure parameter. Under "Monitor" Select Integrations.

![IS Image 17](img/IS-17.jpg)

From here, you will create a Secure Paramater and you will use the name "CABrokerUserPass" ***or you can use another name, just be sure to use the same one in the iFlow*** You will enter the corresponding password for the solace-cloud-client Username.

![IS Image 7](img/IS-16.jpg)

Before proceeding, please check the monitor to ensure that both artifacts have been deployed successfully.

![IS Image 9](img/IS-9.jpg)

## Business Process Automation Setup

The business process that we will deploy is activated by an API Trigger which can be seen in the diagram and the last step of the process is the publishing of an event. This process uses a Rest Call to the broker that is encapsulated in the SAP BPA “Action” highlighted in Red Below. 

![SAP BPA Image 1](img/SPA-BPA-1.jpg)

The "Action" component needs to be associatd with a destination. For the destination information needed below, you will need "REST" connectivity information from your broker. Navigate to your AEM Cloud Console, you will select the Cluster Manager and then you will select your broker. From there, you will select the “Connect” option at the top. On this screen, make sure that the “View By” is set to Protocol as the first step. From there, expand the REST protocol and everything you need to create the destination will be visible.

![SAP BPA Image 2](img/AEM-2.jpg)

Once you have the connectivity information, open the BTP Cockpit, Select the “New Destination” option. You will be creating a destination called “AEMBROKERREST”.

![BPA Image 20](img/BPA-20.jpg)

You will populate the Destination information as shown below and you will add two properties that are both set to true.
- sap.applicationdevelopment.actions.enabled – true
- sap.applicationdevelopment.actions.enabled – true

When your destination is finished and saved, double check to make sure both properties are there.


![BPA Image 21](img/BPA-21.jpg)

## Creating the SAP BPA Project

For the SAP BPA setup, we will be importing 2 different projects: 
- a project of type “Actions”
- a project of type “Process Automation”
- 
We will start by importing the Action project. Select the import option which is highlighted by the red square. When prompted, select the AEMSALESORDERAPI.mtar file for import. Once it’s successfully imported, you will see it listed as per the screenshot below and you should see type “Actions” listed. Repeat the exact same process to import the second file SAPAEMSO.mtar. It will result in the  project being imported of type “Process Automation”.

>aside negative
> Depending on the versions of the deployed project, there might be some differences between your project and the screenshot in this codelab. This is acceptable.

![SPA BPA Image 11](img/SPA-BPA-11.jpg)

In order to deploy the Action project, you need to first configure the project with a Destination that you have already created in BTP. The Destination will be selected in the deployment so we need to create that first. Navigate to the “Settings” tab from the BPA environment.
In this example, we are not really creating a destination but more referencing an already existing Destination. When you click “New Destination”, you should see the Destination you created in BTP called “AEMBROKERREST”, if you don’t, you have not specified the properties correctly and you will need to investigate. Select the Destination and you should see it populate in the UI. Now, we can deploy the Action project.


![SPA BPA Image 12](img/SPA-BPA-12.jpg)

Return to the “Lobby” and Click into the AEMSALESORDERAPI project. From this screen you will now hit the Release Button.

![SPA BPA Image 9](img/SPA-BPA-9.jpg)

Once the project is released, select the “Publish to Library” button.

![SPA BPA Image 10](img/SPA-BPA-10.jpg)

Now we will deploy the SAPAEMSO project. Click on the project to open it in the designer.
![SPA BPA Image 13](img/SPA-BPA-13.jpg)

From this screen you can Release the project in the top right corner. Alternatively, you can click on the "Sales Order Review" process to review the structure of the process to see how it is built.

![SPA BPA Image 14](img/SPA-BPA-14.jpg)
You can select the appropriate version with either of the radio boxes and then press the release button.
![SPA BPA Image 15](img/SPA-BPA-15.jpg)

Once the project is released, you should see the Deploy Button. Press it to trigger a serious of project checks.
![SPA BPA Image 16](img/SPA-BPA-16.jpg)
Press Next
![SPA BPA Image 17](img/SPA-BPA-17.jpg)
Here you must select your destination for the action. If your destination is not in the dropdown, something has not been configured properly in the Settings of the project.
![SPA BPA Image 18](img/SPA-BPA-18.jpg)
This is the last step to deploy your business process, click Deploy.
![SPA BPA Image 19](img/SPA-BPA-19.jpg)
You should now see "Deployed" and "Active" on the top left of the screen and your process should now be running.
![SPA BPA Image 20](img/SPA-BPA-20.jpg)

Theoretically, the process should be running and the next time you press "Submit" on the Dead Message Queue Integration Card, you should activate the flow. The question is how will you know? For starters, do you know how to check your inbox for messages?

From the main screen of the BPA Lobby, you can see in the upper right, a little inbox symbol...Click It.
![SPA BPA Image 21](img/SPA-BPA-21.jpg)
Now you will see the form that we created to display the contents of a Sales Order Event.
![SPA BPA Image 22](img/SPA-BPA-22.jpg)

## Testing the components
At the moment, you should have a fully integrated scenario. Whenever you press the Submit button on the Dead Message Queue Card, you should see a new Inbox Item magically appear in your Inbox. However, what if you don't?

My first suggestion would be to use the "Try Me" tab on the broker with the configured Rest Delivery Point and let's do some simple tests.

![SPA BPA Image 23](img/SPA-BPA-23.jpg)
On this screen, we can test several things. For starters, we can confirm that the iFlow that we deployed is working and successfully transforming our message.
On the publisher side, connect to the broker and use "sap.com/salesorder/rejected/V1" as the topic and for the message use the following structure. This will simulate an event being submitted for Review from the Integration Card.
```JSON
{
	"orderHeader": [
		{
			"salesOrderNumber": "SO1002",
			"creator": "Jane Smith",
			"date": 1691193600000,
			"salesType": "In-store",
			"ordertype": "Express",
			"salesOrg": "SA02",
			"distributionChannel": "DC02",
			"division": "DV02",
			"customer": [
				{
					"customerId": "CUST002",
					"customerName": "XYZ Ltd",
					"zipCode": "54321",
					"street": "First Avenue",
					"phone": "555-987-6543",
					"country": "USA",
					"city": "Los Angeles"
				}
			],
			"orderItem": [
				{
					"item": "ITEM002",
					"material": "MAT002",
					"materialType": "Service",
					"itemType": "Premium",
					"orderSchedule": [
						{
							"scheduleNumber": "SCH002",
							"quantity": 50,
							"uom": "Hrs"
						}
					]
				}
			]
		}
	]
}
```
On the subscriber side, connect to the broker and use ">" as your topic. This will show everything. When you publish your message, you should immediately see a message appear in the subscriber window and you should be looking for a couple of things:
- A new message with a different Topic - sap.com/bpasalesorder/rejected/V1
- The body of the message should essentially be the same BUT it has a new wrapper called "context" and a new attribute called "definitionId". If you don't see both of these things, something is wrong with the iFlow.
- After you publish the method, you should see a new item in your inbox. If the message appears to have the right structure in the subscriber window  (aka your iFlow is working) then the next place to look is the configuration of the Rest Delivery Point. The RDP will be listening for these rejected messages and then calling the API to start the BPA process. If it's not, potentially check the queue to see if messages are accumulating in SO_WF.

  ### IF YOU SEE MESSAGES IN THE INBOX....WOOHOO


## Takeaways

✅  Understand concept of Dead Message Queues
✅  Understand how to use SAP BPA to process Dead Messages
✅  Understand how to use an iFlow with an Event for transformations
✅  Understand how to setup a Rest Delivery Point




![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
