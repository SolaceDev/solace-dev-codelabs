author: HariRangarajan-Solace
summary: Day 4/5 : This code lab walks the participant through the experience of using SAP AEM to event enable their SAP ecosystem and workflows
id: sap-aem-int-day-4
tags: SAP, AEM, Event Portal, SAP BTP, CAPM
categories:
environments: Web
status: Hidden
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/sap-aem-int-day-4

# Event Enable SAP Using SAP Advanced Event Mesh - Day 4

## What you'll learn: Overview

Duration: 0:05:00

Day 4 of 5.
Topics covered :
- Using SAP BPA to handle event exceptions

## What you need: Prerequisites

Duration: 0:07:00

Enter environment setup & prerequisites here

## Step 1 - Using SAP BPA to handle event exceptions

# In the world of Event Driven Asynchronous messaging...

[Link to Blog](https://solace.com/blog/pubsub-message-handling-features-dead-message-queues/)

In our scenario, we will artificially create a situation where messages cannot be delivered to the endpoint...

![BPA Image](/img/BPA-1.jpg)

## Step 1 – Configure the required components for a Rest Delivery Point on the broker

Navigate to the main console and go to the cluster manager. From there, select the broker where you will be configuring your Rest Delivery Point...

![BPA Image 3](/img/BPA-3.jpg)

From this screen, you will select the manage option at the top...

![BPA Image 4](/img/BPA-4.jpg)

You will then select “Queues” towards the middle of the screen...

![BPA Image 5](/img/BPA-5.jpg)

On this screen, we will start by creating a Queue and Subscription...

![BPA Image 6](/img/BPA-6.jpg)

Create a new Queue with the name “SOREJECTED”...

![BPA Image 22](/img/BPA-22.jpg)

Now we will create a subscription that will capture all the messages that are being pushed out from the Integration Card from the Dead Message Queue...

![BPA Image 24](/img/BPA-24.jpg)

Repeat the process to add another Queue called “SO_WF”...

![BPA Image 23](/img/BPA-23.jpg)

Next step to create the Rest Delivery Point and associated components...

![BPA Image 10](/img/BPA-10.jpg)

The name of the RDP is “RDP1”...

![BPA Image 11](/img/BPA-11.jpg)

You will now create a Rest Consumer that will be the target for your Events...

![BPA Image 12](/img/BPA-12.jpg)

Enter “SO_WF_REST_CONSUMER” and press “Create”...

![BPA Image 13](/img/BPA-13.jpg)

This is the screen that requires some attention to detail...

![BPA Image 14](/img/BPA-14.jpg)

Next you will create the connection between the Rest Consumer and the Queue that it will use...

![BPA Image 15](/img/BPA-15.jpg)

From the dropdown, select the previously created Queue “SO_WF”...

![BPA Image 16](/img/BPA-16.jpg)

This is where you will enter the remainder of the endpoint…aka the endpoint for creating the Workflow Instances...

![BPA Image 17](/img/BPA-17.jpg)

At this point, you should have a functioning RDP...

Congratulations, you have completed setup of the Rest Delivery Point. Each time a message is placed into the Queue, it will automatically call the API associated with the RDP.

## Integration Suite Setup

In the Business Process Automation scenario...

![IS Image 1](/img/IS-1.jpg)

Once you have the package in edit mode, select the DropDown under “Add” and select “Message Mapping”...

![IS Image 2](/img/IS-2.jpg)

At the top of this form, you will select “Upload” and then you will select the zip file with the “MM” at the end for Message Mapping...

![IS Image 3](/img/IS-3.jpg)

The 2nd way to deploy an artifact is from the main screen as shown below...

![IS Image 4](/img/IS-4.jpg)

Now we will import the iFlow using the same approach we just followed for the Message Mapping...

![IS Image 5](/img/IS-5.jpg)

Before proceeding, please check the monitor to ensure that both artifacts have been deployed successfully...

![IS Image 9](/img/IS-9.jpg)

## Business Process Automation Setup

The business process that we will deploy is activated by an API Trigger...

![SAP BPA Image 1](/img/SAP-BPA-1.jpg)

From the BTP Cockpit, Select the “New Destination” option. You will be creating a destination called “AEMBROKERREST”...

![BPA Image 20](/img/BPA-20.jpg)

For the destination information needed below, you will need connectivity information from your broker...

![AEM Image 1](/img/AEM-1.jpg)

You will populate the Destination information as shown below...

![BPA Image 21](/img/BPA-21.jpg)

## Creating the SAP BPA Project

For the SAP BPA setup, we will be importing 2 different projects: a project of type “Actions”...

![SPA BPA Image 11](/img/SPA-BPA-11.jpg)

In order to deploy the Action project, you need to first configure the project with a Destination...

![SAP BPA Image 12](/img/SAP-BPA-12.jpg)

Return to the “Lobby” and Click into the AEMSALESORDERAPI project...

![SAP BPA Image 9](/img/SAP-BPA-9)

Once the project is released, select the “Publish to Library” button...

![SAP BPA Image 10](/img/SAP-BPA-10)


## Takeaways

Duration: 1:30:00

✅  Understand concept of Dead Message Queus
✅  Understand how to use SAP BPA to process Dead Messages



![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
