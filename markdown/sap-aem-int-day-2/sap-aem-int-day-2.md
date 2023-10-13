author: HariRangarajan-Solace
summary: Day 1/5 : This code lab walks the participant through the experience of using SAP AEM to event enable their SAP ecosystem and workflows
id: sap-aem-int-day-2
tags: SAP, AEM, Event Portal, SAP BTP, CAPM
categories:
environments: Web
status: Hidden
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/sap-aem-int-day-2

# Event Enable SAP Using SAP Advanced Event Mesh - Day 2

## What you'll learn: Overview

Duration: 0:05:00

Day 2 of 5.
Topics covered :

SAP EDA artifacts visualized using the Event Portal
- Explore the Event Portal and learn how to import objects.
- Learn how to create a design so that your events can be maped and understood.

SAP UI5 Integration cards displaying events in real time
- Using the services provided in the SAP BTP, you will learn how to create visualizations for your data using eventing.
- Learn how easy it is to bring your events to life.

## What you need: Prerequisites

Duration: 0:07:00

Complete all activities in day 2. You access and use the same broker you setup previously as well as the simulator push events.

## Step 1 - SAP EDA artefacts visualized

In this task, you will be importing the design representing the events for this rapid evaluation. \
This design is an example, and not a full implementation. The intent is to have enough design for an evaluation while
allowing easy understanding of the concepts being demonstrated.
The level of detail in the model is "medium size," meaning that there are enough attributes to enable the demonstration,
but it is not the full schema for the SAP objects involved.

1. From the SAP AEM Console, open the Designer. \
   ![SAP AEM EP Designer](img/ep-designer.png)

2. Import the demo domain from the provided export file. \
   \
   Pull down the menu extension in the Application Domains view and select the import function.
   ![SAP AEM EP Designer Import AppDomain-1](img/ep-designer-import-app-domain-1.png)\
   ![SAP AEM EP Designer Import AppDomain-2](img/ep-designer-import-app-domain-2.png)\
   \
   Select the demo file from the file system. \
   ![SAP AEM EP Designer Import AppDomain-3](img/ep-designer-import-app-domain-3.png)\
   After the import is complete, you will see the evaluation domain in the domains list. \
   ![SAP AEM EP Designer Import AppDomain-4](img/ep-designer-import-app-domain-4.png)


3. Take a quick tour of the domain model. \
   \
   The initial view of the domain will be of the Applications tab. \
   You will see a number of modeled applications in the list related to the demo. \
   Note that these are simple references that allow visualization of the event flows – The designer tool does not
   simulate the actual applications. \
   ![SAP AEM EP Designer AppDomain-view](img/ep-designer-appDomain-view.png)

   Event APIs and Event API Products can be used to expose and manage AsyncAPI interfaces within organizations, or with
   external partners through your APIM vendor.
   > aside negative
   > Note that Event APIs and Event API Products are advanced topics that will not be covered by this demonstration
   design.

   Clicking on the Events tab, you will see a listing of 17 events defined for the domain.
   ![SAP AEM EP Designer events list](img/ep-designer-events-list.png)
   \
   Clicking on the Schemas tab, you will see 5 schemas.
   ![SAP AEM EP Designer schema list](img/ep-designer-schema-list.png)
   \
   For simplicity, we have defined one schema for use by all events dealing with each object. \
   Clicking on the Enumerations tab, you will see one enum.
   ![SAP AEM EP Designer enum list](img/ep-designer-enum-list.png)
   \
   Enums are used in the model to show a finite set of possible values. \
   This one is defined to hold a concise set of rejected reason code values for sales orders.

   Moving back to the Events tab, we can use the search box near the top to filter down to the event(s) we want to find.
   For example, typing "Sales" here results in a live search that filters the list down to just Sales Order related
   events.
   ![SAP AEM EP Designer events filter](img/ep-designer-events-filter.png)\
   \
   Clicking on the Sales Order Create event in this view will drill into the definition of that event.
   ![SAP AEM EP Designer event definition](img/ep-designer-event-defn.png)
   \
   This provides an overview of the event details including the version, state, description, topic address, schema
   reference, and reference-by links.
   ![SAP AEM EP Designer event details](img/ep-designer-event-details.png)

   **Version & State:** \
   Designer can be used to manage the version and state of model objects and tracks their relationships for you,
   enabling full SDLC (software development lifecycle) visibility.
   It also serves as a collaboration space that allows you to leverage events you create more effectively to derive new
   value for the business.
   \
   **Topic Address:** \
   For AEM services (type = Solace), the topic address is a string with **"/"** separators that enables dynamic routing
   and filtering. Following best practice guidelines for creating topic strings is critical to your EDA success. \
   The general format is **ORG/DOMAIN/VERB/VERSION/{ATTRIBUTE1}/{ATTRIBUTE2}/ …** \
   Topics are a powerful mechanism employed by AEM to perform dynamic routing in an event mesh, moving copies of events
   only where they are needed. It also enables consuming clients to filter events within topics using subscriptions and
   wildcard characters **(*, >)**. \
   This capability avoids client applications having to implement brittle, complex filtering logic to reject unwanted
   events.\
   \
   Next, click on the referenced schema to expand your view.
   ![SAP AEM EP Designer event schema reference](img/ep-designer-event-schema-ref.png)\
   The referenced schema can be displayed as content in this view. \
   Now click on the expanded menu in this section and select Open Schema. \
   ![SAP AEM EP Designer event schema open](img/ep-designer-event-schema-open.png)\
   This takes you directly to the Schema tab content. Here, you can see a more detailed description and have control to
   edit, create a version, and adjust the state of the schema. \
   The description includes links to references used to define the objects in the demonstration. \
   If you click on the expander, you can view just the schema text in a larger view without opening it for editing.
   ![SAP AEM EP Designer schema designer](img/ep-designer-schema-designer.png)\
   The Designer tool will be a useful way to explore the demonstration data throughout your evaluation.

## Step 2 - UI5 Cards in realtime

SAP Ui5 Integration cards present a new means to expose application content to the end user in a unified way. Depending
on the use cases, cards can be easily embedded in a host environment, such as an application, SAP Build, dashboards, or
any HTML page. A variety of card types can be configured by a simple JSON configuration (schema) without the need to
write code for UI rendering. In this way, even users without programming skills are enabled to create new cards
according to their specific needs. Cards are composite controls that follow a predefined structure and offer content in
a specific context. Cards contain the most important information for a given object (usually a task or a list of
business entities). You can use cards for presenting information, which can be displayed in flexible layouts that work
well across a variety of screens and window sizes.

With the use of cards, you can group information, link to details, or present a summary. As a result, your users get
direct insights without the need to leave the current screen and choose further navigation options.

For more information on SAP Ui5 Integration cards, you can refer to the
link: [UI Integration cards](https://ui5.sap.com/test-resources/sap/ui/integration/demokit/cardExplorer/index.html)

To showcase the simplicity of using SAP integration cards to visualize the power of the SAP Advanced Event Mesh, we have
created a dashboard using HTML5 for each business scenario. We also made them easy to use. All you need to do is enter
your broker details, click "Connect," and watch the business case come to life as events flow in. Each integration card
that is displayed in the dashboard represents another tool at your fingertips to visualize your data. The cards are each
subscribed to the various Topics in which you will send your events from your SAP System. Follow the steps below to set
up your dashboard and get started.

### 1: Choose the Business Case Dashboard

Here is a portal where you can find all of the available dashboards that support the 5 business scenarios. Visit the
link below and choose the dashboard that you want to see. Here you will also find additional documentation and helpful
videos to get started with.

- [DashBoard Portal](https://solacedemo-uf1dchbp.launchpad.cfapps.ca10.hana.ondemand.com/125692ff-95ad-4b2d-a216-fde644eef1c0.DashboardPortal.DashboardPortal-1.0.0/index.html)

![Portal](img/Portal_Dashboard.png)

### 2: Connect with Your Broker Details

To connect with your broker details:

- Open your broker and select the “connect” tab at the top.
  ![BrokerDetails](img/Broker_Credentials_Find1.png)
- Then, under the “Solace Web Messaging” section, you will find the 4 inputs you need to connect your broker to the
  dashboard.
  ![BrokerDetails](img/Broker_Credentials_Find2.png)
- Now, you can copy and paste each input into the fields at the top of the dashboard and then finally click “Connect”.
  ![Dashboard](img/Broker_Credentials_Dashboard.png)
- If your credentials are entered correctly, you will get a “Success” message that will verify that you are connected
  properly to the dashboard. If you do not see a “Success” message, then try again and make sure your details are
  correct for each input.
  ![Dashboard](img/Broker_Connected_Dashboard.png)

Repeat these steps for each dashboard.

### 3: Getting to Know Your Dashboard

Each dashboard has different components and scenarios to showcase the capabilities of SAP Advanced Event Mesh. For
example, in the Sales Order Dashboard, there is a card that is reading messages from a Dead Message queue. This
showcases how error handling can be achieved. Furthermore, you can submit a message from that queue to trigger an SAP
Process Automation flow with the click of a button. You'll also find different data visualization types, as well as
functional visualizations that highlight integration with other parts of SAP BTP.

### Troubleshooting

Here are some troubleshooting tips:

- Use the latest version of Chrome, and you can try opening the dashboard in “incognito” mode if you have issues with
  caching.
- If you do not see the “Success” message at the top, then you are not connected. In case you entered your credentials
  correctly and still don’t see the message, try to refresh your browser to prompt the application to try your
  credentials again. You may need to refresh a couple of times to get the “Success” message.
- If messages are being sent and the cards are not updating, right-click anywhere on the dashboard and click “inspect”.
  Then select the “console” tab and look at the logs. It may be the case that the payload format is off, or possibly
  that the events are flowing to the wrong topic. Error messages here should help.

## Takeaways

Duration: 0:07:00


![Soly Image Caption](img/soly.gif)

Thank you for participating on Day 2. Today you learned how to import objects into the Event portal and also had a chance to visualize events coming from the simulator into your broker. We look forward to seeing you on Day 3 where you will begin to setup some SAP Integration Flows.
