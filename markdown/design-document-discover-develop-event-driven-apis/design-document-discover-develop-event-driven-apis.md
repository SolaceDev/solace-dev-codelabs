author: Jonathan Schabowsky
summary: In this tutorial we'll cover how to design, extend and implement your event-driven APIs using Solace PubSub+ Event Portal
id: design-document-discover-develop-event-driven-apis
tags: workshop
categories: Solace, taxi, Portal
environments: Web
status: Published
feedback link: https://solace.community/categories/pubsub%2B-event-portal
analytics account: UA-3921398-10

# Be Real-Time: Design, Document, Discover and Develop Event-Driven APIs

## What you'll learn

Duration: 0:01:00

Most organizations are adopting an event-driven architecture (EDA) to compete in a world where customer satisfaction requires real-time outcomes. 

In this code lab we’ll build and expand your toolbox by learning how an Event Portal, paired with industry standard specifications and frameworks, enable a smooth journey to bring your EDA from initial architecture and design to code running in production while also setting your team up for success as the business needs, architecture and applications themselves are enhanced over time.

Throughout this workshop we will get hands on and talk about:

PubSub+ Event Portal
* Architect, Design and extend an EDA which includes multiple Applications, Events and Schemas.
* Document Applications, Events and Schemas along with best practices for documentation
* Use Discovery capability to see what you already have in runtime and audit for changes
* Use the Event Catalog and Designer to Learn, Understand and Ideate 

AsyncAPI
* AsyncAPI is an open initiative for defining asynchronous APIs, providing a specification, and tooling such as code generation.
* Use the AsyncAPI Generator to generate skeleton code and object models for event-driven microservices

Positive
: Artifacts created or used throughout this codelab can be found in [this Github repo](https://github.com/Mrc0113/ep-design-workshop)

## What you need: Prerequisites

Duration: 0:08:00

🛠 This page covers the setup needed to perform this codelab. 🛠 

### AsyncAPI Generator Requirements
✅ Install instructions available [here](https://github.com/asyncapi/generator#requirements)
* Node.js v12.16+ (Check version using `node -v`)
* npm v6.13.7+  (Check version using `npm -version`)

We'll install the generator itself later 👍

### Java / Spring Cloud Stream Requirements
✅ Spring Cloud Stream just requires Java and Maven to use 🚀  
* Java 1.8+ (Check version using `java -version`)
* Maven 3.3+ (Check version using `mvn -version`)
	* On mac you can `brew install maven`
	* Other install instructions [here](https://maven.apache.org/install.html)
* Your favorite Java IDE 💥

### Python / Paho Requirements
✅ There are only a few requirements for the Python steps! 
* Python version 3.8+ (Check version using `python3 -V`)
* paho mqtt (Can be installed using `pip3 install paho-mqtt`)
* Your favorite Python IDE

### PubSub+ Event Broker Connection Info
✅ The credentials below are for a public event feed found on the [Solace feed Marketplace](http://solace.dev/marketplace) that we'll use during this codelab.
* SMF Host: `tcp://taxi.messaging.solace.cloud:55555`
* MQTT Host: `ssl://taxi.messaging.solace.cloud:8883`
* Message VPN: `nyc-modern-taxi`
* Username: `public-taxi-user`
* Password: `iliketaxis`

✅ Note that this client-username has permissions to subscribe to `taxinyc/>` and `test/taxinyc/>` and permissions to publish to `test/taxinyc/>`

### Prepare PubSub+ Event Portal

#### Sign-up for Solace Cloud
✅ If you already have a Solace Cloud account just login, otherwise please sign-up for a free Solace Cloud Account using [this link](https://bit.ly/try-solace-free). Note that no credit card is required. You will receive an email to activate the account and will then be prompted to start the free trail. 

![sc_trial](img/sc_trial.webp)


#### Import Existing Designed EDA
✅ Download the Application Domain export file: [EventPortalExport_Initial.json]( https://github.com/Mrc0113/ep-design-workshop/blob/main/EventPortalExport_Initial.json)

You can download the file via curl or by cloning the git repo
```bash
curl -k -XGET https://raw.githubusercontent.com/Mrc0113/ep-design-workshop/main/EventPortalExport_Initial.json -o EventPortalExport_Initial.json
```
OR
```bash
git clone https://github.com/Mrc0113/ep-design-workshop.git
```

✅ Inside of your logged into Solace Cloud Account navigate to the Event Portal Designer by clicking "Designer" in the menu on the left. 

![ep_select_designer](img/ep_select_designer.webp)

✅ Then import the previously downloaded Application Domain file by clicking the `Import` button at the top right of the _Designer_ and importing the  file. 

![ep_click_import](img/ep_click_import.png)


🚀 Setup complete! Let's get going! 🚀


## Foundational Concepts 

Duration: 0:08:00

Before we dive deeper, lets ensure we are all aligned with terminology of the objects and concepts we will use in PubSub+ Event Portal. 

### Application Domain & Workspace

An application domain represents a namespace where applications, events, and schemas can live. Within this namespace, you can create a suite of applications, events and schemas that are independent of other application domains. In our NYC Taxi use case we introduced earlier, we may group applications into different domains, for ex. we may have a domain for our rideshare apps and services, one for our back-office apps where invoicing and background checks are being processed, and maybe another domains for analytics where we group apps that are responsible for analyzing the successful operation of our rideshare services.

In the Event Portal you will associate all objects like Consumer Groups, Topics, Schema, etc, to one or more Application Domains. 

You can further group multiple domains into a *Workspace*, which will make it easier to review our Discovery scan. So our Analytics, Operations, and Back-Office Application Domain in the NYC taxi example could be part of a single Workspace.

![Workspace Example](img/workspace_example.png)

### Events/Topics

Events are an important part of the Event Portal. Think of a event as a concept of the publish-subscribe (pub/sub) architectural pattern. Topics are used to route data or events (in the form of messages) between distributed applications, often using a message broker or an event broker.

A Solace topic and an Apache Kafka topic might seem fundamentally the same but there are quite a few [differences between them](https://solace.com/blog/solace-topics-vs-kafka-topics/). Later in this CodeLab, when you run a discovery scan against a Kafka cluster the Topic Scheme for events discovered will be Kafka format.

Here are some examples from our use case:

Kafka Topics: 
* taxinyc.analytics.fraud.alerted.v1 
* taxinyc.ops.payment.charged.v1 
* taxinyc.ops.ride.called.v1 

Solace Topics: 
* taxinyc/ops/ride/updated/v1/${ride_status}/${driver_id}/${passenger_id}/${current_latitude}/${current_longitude}
* taxinyc/backoffice/payment/charged/v1/${payment_status}/${driver_id}/${passenger_id}

### Schemas

In simple terms, a schema represents the contract to describe the payload of an event. Producers and consumers of an event can trust that the event's payload matches the schema definition assigned to that event. Schemas define a type of payload through JSON, AVRO, XML, Binary, or Text. JSON, AVRO, and XML schemas have content that describes each property of the schema. 

In our use case all events are in AVRO Schema format.

![Schema Example](img/schema_example.png)

### Applications

An application represents a piece of software that produces and consumes events. Applications connect to the event broker in an event-driven architecture and communicate with other applications via events. A single application represents a class of applications that are running the same code base; therefore, a Kafka consumer group can be associated with an Application object in the Event Portal.

### Kafka Specific Objects and Terminology 

#### Consumer Groups

Event Portal supports the concept of Kafka's consumer groups. A consumer group is used by Kafka to group consumers into a logical subscriber for a topic. In the Event Portal, you can model consumer groups in the Designer. This enables the Event Portal's runtime discovery to associate a discovered consumer group to an existing application. 

Kafka consumers that belong to the same consumer group share a group ID. The consumers in a group divide the topic partitions, as fairly as possible, so that each consumer consumes only a single partition from the group.

A few examples of Consumers Groups from our NYC Taxi Analytics use case would be:

* Passenger Surge Detection
* Fraud Detection
* Driver Incentive Calculation

#### Connector

A connector is used in Kafka for connecting Kafka brokers with external systems to stream data into or out of Apache Kafka. In the Event Portal, a Kafka Connector is an application class you select to configure associated published and/or subscribed events and a set of Kafka-native attributes like Connector Type, Class, Cluster ID, and Maximum Task.

## Best Practices
Duration: 0:08:00

### Decomposing the Enterprise 

Whether you perform discovery manually or using our agent, it is important to consider how your enterprise is organized so that it can be decomposed using the Application Domain construct. An Application Domain provides the ability to organize and decompose an enterprise into logical groupings. These groupings could be based on-line of business, related functional capabilities or based on team dynamics. The benefits of doing this include: 
1. **Event sharing rules** – decide which events should be shared with other application domains and those which are for internal application domain usage only. This has implications both from a security perspective, but also which events need to be managed more tightly as they affect others outside of the application domain
1. **Provide uniform event topic prefixes** – ensures that the prefix is unique and that topic best practices are followed

### Topic Naming Best Practices 
The topic of which an event is addressed seems like a pretty simple decision, but in reality, it can result in some negative consequences if not planned in advance. A topic is more than an address, it is metadata that describes the event and can be used for several purposes such as routing, access control and versioning. Thus, it is important to properly govern and manage the topic structure. **Regardless of your broker type**, it is a good practice to make topics structured and hierarchical the same way a RESTful Resource uses hierarchical addressing. In other words we want to produce hierarchical topics that rank from least specific to most specific. 

#### Parts of the Event Topic
The event topic structure has two parts:

1. The **Event Topic Root** contains enough information to describe the type of event that has occurred. Each Event Topic Root is a static field that describes the type of event. The list of Event Topic Roots forms a catalog of events that can be produced and consumed. This catalog could be brought into the PubSub+ Event Portal's event catalog, listing each event type along with details about the event. Each Event Topic Root describes the event in as much detail as necessary to map it to a single data schema.  
1. The **Event Topic Properties** are optional fields that further describe a particular event. This part of the topic has fields that are dynamically filled when the producer publishes the event. These fields are used to describe the specific or unique attributes of this event instance that would be used for routing and filtering.

* Event Topic Root: The Event Topic Root of an event should have the following form:
        
        Domain/ObjectType/Verb/Version/

* Event Topic Properties: The Event Topic Properties should have the following form:
        
        Locality/SourceID/ObjectID  

Positive
: Complete Event Topic Format: Putting together an Event Topic Root and Event Topic Properties creates an event topic that describes the event with a series of fields from least specific to most specific.
      
        Domain/ObjectType/Verb/Version/Locality/SourceID/ObjectID
        
For more information about topic best practices, review the [Topic Architecture Best Practices Guide] (https://docs.solace.com/Best-Practices/Topic-Architecture-Best-Practices.htm)

### Event Information Exchange Patterns 
There are multiple Event Exchange Patterns (EEP) that should be considered when using EDA:

#### Thin Event Notification

* If using a _Thin Event Notification_ pattern, where only the necessary details are provided from a data point of view, this does tend to increase coupling between the event source and sink’s (consumers) as what attributes are provided are typically directly correlated with the needs of the use case vs being more flexible. 

Positive
: The pro of this pattern however is that the data is smaller in size and can thus reduce latency and bandwidth when important. In general, the source of that event should be the single authoritative source for all published attributes. 

#### Hypermedia-Driven Events

* If using _Hypermedia-Driven Events_ pattern, links are provided in the event payload and works to bridge event notifications with dynamic API backends. This can be a good pattern to use where multiple levels of security are concerned related to attributes of the event. Consumers are still notified in realtime of state changes but must invoke the hyperlink in order to get access to more data. The service can then filter the response based on the client’s access level. 

Negative
: The con to this pattern is it increases the latency of the interaction as all the data is not available within the event and puts more complexity on the client and its behavior. 

#### Event-Carried State Transfer

* If using _Event-Carried State Transfer_ pattern, all known data is broadcast with the event (possibly entire record) thus enabling the consuming system to know the entire entity state vs just what changed as is the case with Thin Events. This is very common approach as many times the subscribing application want the entire snapshot to avoid having to persist previous state changes. 

Negative
: The challenge in this case is that the publishing application may not be the authoritative source of all attributes published. Additionally, the event may become large and increase latency/decrease performance. 

Positive
: The benefit however is that decoupling has been achieved in that it will support a variety of use cases and the publisher does not need to be aware of the client’s usage of the data. 

## Use Case Overview
Duration: 0:05:00

You are a member of the engineering team at the _NYC Modern Taxi Co_, a fictional taxi cab company based in New York City. Your team is playing from behind and racing to catch up with technology innovation introduced to the industry by Rideshare competitors such as Uber and Lyft. In order for the company to survive and eventually thrive your team has convinced the board that transforming the companies' IT systems is of utmost importance. Your team has done it's research and determined that moving to an Event-Driven Architecture is essential to future rapid innovation and has already kicked this initiative off by deploying a Solace Event Mesh and updating the taxi fleet to stream real-time events that include ride and location information. We know what the fleet is up to! Now it's time to start to continually improve and provide a world class customer experience.  

In order to react in a real-time manner the team has decided that we want to process the updates as they stream in from the fleet of taxis instead of putting them directly into a datastore and then having to retrieve them to do processing later. To prototype this work, you'll see a high level design in the diagram below. Since we already have the taxi fleet streaming their updates into our PubSub+ Event Mesh we need to do three things: 

1. 🚖 Create and capture this design in the PubSub+ Event Portal where we can define our Event-Driven Architecture, including its' components: Applications, Events and Schemas. This will allow us to define the details needed to implement, visualize and extend the architecture as it evolves, and share/collaborate with our entire engineering team as we continue to innovate.  
1. 🚕 Next up we're going to document some of the designed applications and events so that they can be understood and reused by others.
1. 🚕 We will run a "discovery" scan of a Kafka Cluster to reverse engineer what another team at NYC Taxi already has implemented
1. 🚕 Learn, Understand and Reuse some of our events in a new use case
1. 🚖 Lastly we'll implement the _ProcessPayment_ microservice that that receives the stream of _RideUpdated_ events, charges the customer's credit card and generate a _PaymentCharged_ Event. 


![Architecture](img/arch2.jpg)


Positive
: The dataset you will be using in this lab originally comes from the NYC Taxi & Limousine Commission's open data release of more than a billion taxi ride records. Google then extended one week worth of data (3M taxi rides) from their original pickup and drop-off points into full routes in order to simulate a fleet of taxis roaming the streets of NYC. Solace is streaming this data over Solace PubSub+ for you to analyze and process. 
<p>Terms of Use: This dataset is publicly available for anyone to use under the following terms provided by the Dataset Source — [https://data.cityofnewyork.us/](https://data.cityofnewyork.us/) — and is provided "AS IS" without any warranty, express or implied, from Solace. Solace disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.</p>


## Design an Event Driven Architecture
Duration: 0:10:00

By designing a new event-driven application or extending your event-driven architecture, you're able to deliver new real-time business capabilities in a decoupled and reusable fashion. There are however several key elements which should be considered when designing events, schemas and applications including topic best practices, options for exchanging event data and sharing/visibility rules. Considering these things early will put you on the road to success and enable better reusability down the road.

Now that you're familiar with the use case 🚕 🚖 🚕 and you've imported the application domain into the Event Portal, let's update our Event-Driven Architecture (EDA).

Lets say that your tasked with working within the Back Office team (where the cool kids all work) and are asked to architect the way in which we will charge our passengers for their rides and if the passenger is part of a commercial account, send to our Invoicing System. This is composed of 4 steps
1. Ideate 
1. Design the schema
1. Design the event
1. Design the applications

### Step 1: Determine What Can Trigger Payment - Ideate
So essentially we need to consider, is there a business event that would help us trigger on the moment when the ride has been completed?

Positive
: Event-Driven Ideation: To create new business value you must be able to imagine or conceive of a new solution to an existing problem. These ideas can be derived from two different directions. First, I have a known problem and I am searching for a solution or secondly, let us look at what is available and uncover unique solutions for problems we were not actively looking for. The Event Portal enables learnings from both directions as without it, you do not have a central location to capture all of the events that are available, nor do you have a way to understand whether a given event stream solves your problem. The search and filter functionality enable the user to perform keyword searches which range from data level attributes to metadata within the description. 
1. Navigate to the _Catalog_ component of the Event Portal    
![](img/catalog.gif)
1. Click on the _Schemas_ tab and search for "dropoff"
![](img/catalog-search.png)
1. In the Search Results click on the RideUpdated event in order to understand the matching text context. 
1. We now know that the RideUpdated Schema has a field called **ride_status** that can have a value of _dropoff_. So how do we get access to that data? Click on the _RideUpdated_ schema and we will find out! 
![](img/ride_status.png)
1. We now see the metadata about the RideUpdated schema and at the bottom we can see there is an Event that references this schema called _RideUpdated_. The topic being used leverages the **ride_status** attribute which is pretty sweet! So we can filter on dropoff as a client.
![](img/rideStatusEvent.png)
1. Lets navigate to the _RideUpdated_ Event and look at its documentation to ensure its what we would want to trigger our _ProcessPayment_ Application.  

### Step 2: Design the _PaymentCharged_ Schema 
Next we should decide what we want the data to look like once we have processed a payment. 

1. First we must decide what Event Exchange Pattern (EEP) we will use. For Maximum flexibility, and because time is not of the essence, we will leverage "Event-Carried State Transfer".
1. Click into the _Designer_ component of the Event Portal  
![](img/designer-tab.png)
1. Double Click on the _NYC Modern Taxi Co - Back Office_ Application Domain and its time to get creating! 
![](img/domain-dive.gif)

1. On the Upper Right Corner, Click the _Create_ button and select _Create Schema_  
![](img/create-schema.png)
    1. Name: PaymentCharged
    1. Content Type: JSON
    1. Shared: YES
    1. Owner: Assign Yourself 
    1. Tags: NONE
    1. Description: NONE
    1. Versions: Leave unchecked
    1. Content: 

```
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "$id": "http://example.com/example.json",
  "type": "object",
  "title": "The root schema",
  "description": "The root schema comprises the entire JSON document.",
  "default": {},
  "examples": [
    {
      "payment_charged_id": "23232323",
      "timestamp": "2020-06-03T16:51:47.29612-04:00",
      "information_source": "ProcessPayment",
      "payment_status": "accepted",
      "invoice_system_id": "PSG-32923",
      "amount_charged": 12.32,
      "ride_id": 2345234,
      "entity_type": "Driver",
      "driver": {
        "driver_id": 1234132,
        "first_name": "Frank",
        "last_name": "Smith",
        "rating": 4,
        "car_class": "SUV"
      },
      "passenger": {
        "passenger_id": 2345243,
        "first_name": "Jesse",
        "last_name": "Menning",
        "rating": 2
      }
    }
  ],
  "required": [
    "payment_charged_id",
    "timestamp",
    "information_source",
    "payment_status",
    "invoice_system_id",
    "amount_charged",
    "ride_id",
    "entity_type",
    "driver",
    "passenger"
  ],
  "properties": {
    "payment_charged_id": {
      "$id": "#/properties/payment_charged_id",
      "type": "string",
      "title": "The payment_charged_id schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": [
        "23232323"
      ]
    },
    "timestamp": {
      "$id": "#/properties/timestamp",
      "type": "string",
      "title": "The timestamp schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": [
        "2020-06-03T16:51:47.29612-04:00"
      ]
    },
    "information_source": {
      "$id": "#/properties/information_source",
      "type": "string",
      "title": "The information_source schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": [
        "ProcessPayment"
      ]
    },
    "payment_status": {
      "$id": "#/properties/payment_status",
      "type": "string",
      "title": "The payment_status schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": [
        "accepted"
      ]
    },
    "invoice_system_id": {
      "$id": "#/properties/invoice_system_id",
      "type": "string",
      "title": "The invoice_system_id schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": [
        "PSG-32923"
      ]
    },
    "amount_charged": {
      "$id": "#/properties/amount_charged",
      "type": "number",
      "title": "The amount_charged schema",
      "description": "An explanation about the purpose of this instance.",
      "default": 0,
      "examples": [
        12.32
      ]
    },
    "ride_id": {
      "$id": "#/properties/ride_id",
      "type": "integer",
      "title": "The ride_id schema",
      "description": "An explanation about the purpose of this instance.",
      "default": 0,
      "examples": [
        2345234
      ]
    },
    "entity_type": {
      "$id": "#/properties/entity_type",
      "type": "string",
      "title": "The entity_type schema",
      "description": "An explanation about the purpose of this instance.",
      "default": "",
      "examples": [
        "Driver"
      ]
    },
    "driver": {
      "$id": "#/properties/driver",
      "type": "object",
      "title": "The driver schema",
      "description": "An explanation about the purpose of this instance.",
      "default": {},
      "examples": [
        {
          "driver_id": 1234132,
          "first_name": "Frank",
          "last_name": "Smith",
          "rating": 4,
          "car_class": "SUV"
        }
      ],
      "required": [
        "driver_id",
        "first_name",
        "last_name",
        "rating",
        "car_class"
      ],
      "properties": {
        "driver_id": {
          "$id": "#/properties/driver/properties/driver_id",
          "type": "integer",
          "title": "The driver_id schema",
          "description": "An explanation about the purpose of this instance.",
          "default": 0,
          "examples": [
            1234132
          ]
        },
        "first_name": {
          "$id": "#/properties/driver/properties/first_name",
          "type": "string",
          "title": "The first_name schema",
          "description": "An explanation about the purpose of this instance.",
          "default": "",
          "examples": [
            "Frank"
          ]
        },
        "last_name": {
          "$id": "#/properties/driver/properties/last_name",
          "type": "string",
          "title": "The last_name schema",
          "description": "An explanation about the purpose of this instance.",
          "default": "",
          "examples": [
            "Smith"
          ]
        },
        "rating": {
          "$id": "#/properties/driver/properties/rating",
          "type": "integer",
          "title": "The rating schema",
          "description": "An explanation about the purpose of this instance.",
          "default": 0,
          "examples": [
            4
          ]
        },
        "car_class": {
          "$id": "#/properties/driver/properties/car_class",
          "type": "string",
          "title": "The car_class schema",
          "description": "An explanation about the purpose of this instance.",
          "default": "",
          "examples": [
            "SUV"
          ]
        }
      },
      "additionalProperties": true
    },
    "passenger": {
      "$id": "#/properties/passenger",
      "type": "object",
      "title": "The passenger schema",
      "description": "An explanation about the purpose of this instance.",
      "default": {},
      "examples": [
        {
          "passenger_id": 2345243,
          "first_name": "Jesse",
          "last_name": "Menning",
          "rating": 2
        }
      ],
      "required": [
        "passenger_id",
        "first_name",
        "last_name",
        "rating"
      ],
      "properties": {
        "passenger_id": {
          "$id": "#/properties/passenger/properties/passenger_id",
          "type": "integer",
          "title": "The passenger_id schema",
          "description": "An explanation about the purpose of this instance.",
          "default": 0,
          "examples": [
            2345243
          ]
        },
        "first_name": {
          "$id": "#/properties/passenger/properties/first_name",
          "type": "string",
          "title": "The first_name schema",
          "description": "An explanation about the purpose of this instance.",
          "default": "",
          "examples": [
            "Jesse"
          ]
        },
        "last_name": {
          "$id": "#/properties/passenger/properties/last_name",
          "type": "string",
          "title": "The last_name schema",
          "description": "An explanation about the purpose of this instance.",
          "default": "",
          "examples": [
            "Menning"
          ]
        },
        "rating": {
          "$id": "#/properties/passenger/properties/rating",
          "type": "integer",
          "title": "The rating schema",
          "description": "An explanation about the purpose of this instance.",
          "default": 0,
          "examples": [
            2
          ]
        }
      },
      "additionalProperties": true
    }
  },
  "additionalProperties": true
}
```
    1. Revision Comment: <Optional> "Initial Creation of Schema"
    1. Click _Save_
    
                   

### Step 3: Design _PaymentCharged_ Event
So now that we have constructed the payload format for the PaymentCharged event, it is time to design the event itself. What's involved? Well we need to apply our best practices as it comes to the Topic name! 
1. Click into the _Designer_ component of the Event Portal
1. Double Click on the _NYC Modern Taxi Co - Back Office_ Application Domain
1. On the Upper Right Corner, Click the _Create_ button and select _Create Event_
![](img/create-event.png)
    1. Name: PaymentCharged
    1. Shared: YES
    1. Description: NONE
    1. Topic Scheme: Solace
    1. Topic
        1. As you can see the domain aleady has some of the "Event Topic Root" `taxinyc/backoffice/`
        1. We need to apply the best practice of _Domain/ObjectType/Verb/Version/Locality/SourceID/ObjectID_ to this event
        1. We will use the topic name of: `taxinyc/backoffice/payment/charged/v1/${payment_status}/${driver_id}/${passenger_id}`
    1. Value: 
        1. Keep the Schema radio button selected
        1. Choose the Schema "PaymentCharged" that we created in the previous step
    1. Owner: Assign Yourself 
    1. Tags: NONE
    1. Revision Comment: <Optional> "Initial Creation of Event"
    1. Click _Save_

### Step 4a: Design _ProcessPayment_ Application
Now for the fun part! We need to design the event-driven interface of the _ProcessPayment_ Application. This is pretty easy as it has one input which triggers a single output. 
1. Click into the _Designer_ component of the Event Portal
1. Double Click on the _NYC Modern Taxi Co - Back Office_ Application Domain 
1. On the Upper Right Corner, Click the _Create_ button and select _Create Application_
    1. Name: ProcessPayment
    1. Description: NONE
    1. Application Class: Unspecified
    1. Owners: Assign Yourself
    1. Tags: NONE
    1. Associated Events: 
        1. Click the _Manage_ link
            1. Select the _Sub_ button next to the _RideUpdated_ event 
            1. Select the _Pub_ button next to the _PaymentCharged_ event
            1. Click _Save_
    1. Revision Comment: <Optional> "Initial Creation of Application"
    1. Click _Save_
1. You should now see the newly added application on the graph! 

Positive
: Pro Tip!: If you wanted to develop/implement this application you could right click on the _ProcessPayment_ Application in graph and export an AsyncAPI Document that could be used to generate code!

### Step 4b: Design _InvoiceSystem_ Application
Remember back to our use case... We have designed how we process payment but still have to deal with invoicing customers when the payment_status says to invoice. Therefore, our plan is to create an application that integrates with our invoicing system. 
1. Click into the _Designer_ component of the Event Portal
1. Double Click on the _NYC Modern Taxi Co - Back Office_ Application Domain 
1. On the Upper Right Corner, Click the _Create_ button and select _Create Application_
    1. Name: InvoiceSystem
    1. Description: NONE
    1. Application Class: Unspecified
    1. Owners: Assign Yourself
    1. Tags: NONE
    1. Associated Events: 
        1. Click the _Manage_ link
            1. Select the _Sub_ button next to the _PaymentCharged_ event 
            1. Click _Save_
    1. Revision Comment: <Optional> "Initial Creation of Application"
    1. Click _Save_
1. You should now see the newly added application on the graph! 

![](img/final-arch.png)
### Reuse _PaymentCharged_ Event
Getting reuse of your events is an important part of proving return on investment (ROI) and also enables other applications and teams to integrate with realtime data. 

In this scenerio we will act as though we are members of the "Ops" team (they are not as cool as us back office kids, but oh well). They have a use case that Payment charged events should go to the _Rider Mobile Application_. Lets make it happen! 

1. Click into the _Designer_ component of the Event Portal
1. Double Click on the _NYC Modern Taxi Co - Ops_ Application Domain 
1. Double Click on the _RIder Mobile Application_ 
1. On the Upper Right Corner, Click the _Edit_ button
    1. Associated Events: 
        1. Click the _Manage_ link
            1. Select the _Sub_ button next to the _PaymentCharged_ event 
            1. Click _Save_
    1. Revision Comment: <Optional> "Updated to Satisify JIRA-01245"
    1. Click _Save_
1. You should now see the relationship on the on the graph where we are subscribed to the _PaymentCharged_ event and the dependency on the Back Office App domain! 

![](img/share-event.png)

Positive
: Change Impact Analysis: Changes happen. The question is what is the effect and who is affected? In the synchronous world changes to an API of course may/will affect the clients, so changes are rolled out, clients notified, and changes implemented. The challenge in the EDA world is that consumers are decoupled from producers and vice/versa. In addition, the ripple effect can be large in that integrations though connectors and integration capabilities can move events between different groups which further casts a fog upon dependency management. The Event Portal enables you to navigate the relationships you just designed and understand impact.

## Documentation Best Practices
Duration: 0:05:00

💡  **Know your Audience**   
The events which you have are used to enable real-time collaboration between systems and solve a problem for a specific industry and organization. These events are integrated into applications by software developers/engineers but they are not all the same and can be decomposed into:

* **Decision Makers** - Some people in the organization are looking and evaluating the events and schemas available in order to decide if it makes sense to have the development team further explore the service. They are evaluating with a problem in mind and are looking to see if the events registered within the Event Portal can be used to solve that problem. In many cases they will not be the ones writing the code that solves the problem but are extremely important as they drive the decision as to if the effort to use it will be undertaken. Examples of these types of decision makers include but are not limited to: CTO, Product Managers, Data Analysts and Data Scientists/Engineers. 
* **Users** - These are the people who will be directly consuming and developing using the events and schemas defined in the event portal. Typically, the decision to use an event/schemas has been made and they need to understand the event, how it applies to their use case and how to integrate with it. They are critical to enable as they are always short on time and are the last link to getting an event to be reused. In addition, these users are the ones creating the documentation to enable others if they are the author of an event or schema so they are critical to the maintainability of the event-driven ecosystem of documentation. Examples of users include but are not limited to integration engineers, front end developer, backend developer. 

💡  **Capture Business Point of View and Moment**
* The hardest thing to capture is the “what does this event represent” and without it, it will be hard for a decision maker to understand if it provides value. Be sure to document the moment in which the event was generated, the attributes of which it is the authoritative source and the intended use of the event. Do not assume the user will read the corresponding payload schema or understand much about the publishing application so focus on documenting the event concisely and thoroughly 

💡  **Technical Requirements**
* This is the section where you need to provide the developer the information needed to consume the event itself. What are some suggest client APIs that should be used to consume the event? Are there important headers being used? What authentication/authorization schemes are required? All of this type of information should be captured to ensure an easy development process.

💡  **Link to other References**
* The Event Portal is just one source of information within the organization. Addition info on the application may be stored in a github repo, so provide a link. A schema may also have a corresponding github or wiki page, so provide a link. An event may have been a part of a larger development task tracked in JIRA, so provide a link. The point is link to all of the places the organization captures information and ideally link from those places into the event portal so that no matter where you start, you can understand what’s available and the state. 

💡  **Provide Examples**
* An example can be an often-underutilized format of communication. By seeing an example of an event, the user may better understand a concrete business moment rather than the description. In addition, those examples are also all part of our search mechanism so anything within it provides better search context. 

💡  **Terms of Use**
* This is the legal agreement between the event producer and any/all consumers. Talk to the API teams about their Terms of Use contracts and decide if it should be updated for event-driven API relationships. Also think of others within the same organization and their expectations of use and document them here. 

💡  **Tags**
* When in doubt, add a tag (within reason). As more and more events, apps and schemas are input into the system, search and tagging becomes more and more important for users to find the capabilities available. Browse the existing tags and see which may apply to your event, application or schema. Add tags if needed so that others can more easily filter and find your event, application or schema. 



## Document Events, Applications and Schemas
Duration: 0:08:00
Events are only as good as their documentation. After all, it is up to a human to understand what something is and make a determination as to wither it provides value. This is why documentation is critical for success in Event Driven Architecture. Creating and maintaining good documentation that’s easy to read, enjoyable to interact with and sets up the user for success can be challenging. Great documentation requires effort but has significant implications on the reuse of the events within the eco-system. The PubSub+ Event portal enables you to document Events easily while also managing the decoupled relationships so that users can easily understand the context of an event. Before you sit down and write documentation on events, applications and schemas, its good to consider its purpose along with who will be using it. 

Positive
: Organizational Enablement: Organizational changes happen all the time. How ready are you to take over another groups EDA implementation? How about enable new members on yours?  What if your current architect were to resign, are you capturing everything you should be? Tribal knowledge happens and is dangerous. The above organizational changes showcase the multitude of scenarios that can occur that leave the business in limbo and result in reverse engineering something that was already engineered. If you get into the habit and develop the muscle memory around designing/documenting and continuously validating your EDA, tribal knowledge is eliminated as its now available centrally and kept up to date. While most organizations believe they have a software development and governance process that will prevent this from happening, it is typically comprised of multiple conflicting sources of truth, none of which actually representing the current truth. This leads the team to constantly as the question “so how does this actually work” and wasting time trying to investigate vs simply using a tool that captures the information and ensures it matches reality. 

### Update Documentation of _PaymentCharged_ Event
Remember how we did not provide any description or tags for the Events and Applications we created before? Well, lets go in and follow our best practices to fix this. 
Lets enhance the documentation of the _PaymentCharged_ Event 
1. Click into the _Designer_ component of the Event Portal
1. Double Click on the _NYC Modern Taxi Co - Back Office_ Application Domain 
1. Double Click on the _PaymentCharged_ Event in the graph
    1. Click on the _Edit_ button <Top Right>
        1. Copy and Paste the following into the _Description_ field:
```
Description of Business Moment

	Overview: 

		The PaymentCharged Event exists in order to notify other systems that we have attempted to charge the passenger. There are also other states such as:
            accepted - customer credit card on file has been charged
            declined - customer credit card on file has been declined
            org - the customer is part of a B2B org and does not provide automated payment


Technical Requirements

Format: JSON
Security Level: PCI 

Terms of Use

N/A
```
        1. Lets make it nicer to read by using bullets, bold, italics etc
        1. Lets now also add Tags
            1. Click _Add/Remove Tags_
                1. Type _PCI_ in the box and Select (Create a new tag) below. 
                1. Optionally add other tags. 
                1. Click Done
        1. The documentation should look something like: 
            ![asyncapi_doc2](img/EventDoc.png)
        1. Click _Save_

### Update Documentation of _ProcessPayment_ Application 
Lets enhance the documentation of the _ProcessPayment_ Application and put our Documentation Best Practices to work! 
1. Click into the _Designer_ component of the Event Portal
1. Double Click on the _NYC Modern Taxi Co - Back Office_ Application Domain 
1. Double Click on the _ProcessPayment_ Application in the graph
    1. Click on the _Edit_ button <Top Right>
        1. Copy and Paste the following into the _Description_ field:
```
Description of Business Capability

	Overview: 

		The ProcessPayment application solely exists in order to monitor for when Passenger Rides are completed such that final billing can be performed against the passengers credit card. Because this application will need to look up the passenger's billing information it is important that security be taken into account as it will need to be PCI compliant. Upon successful payment, the application shall emit an event to signify that payment has happened.



Technical Requirements

Java Version:  OpenJDK 11.0.4
Spring Cloud Version:  Hoxton.SR8
Number of Instances: 1
Cloud: AWS us-east
Security Level: PCI 
Event Broker Profile: Solace


Source Code Repository

github repo



Terms of Use

N/A
```
        1. Lets make it nicer to read by using bullets, bold, italics etc
        1. Lets add a hyperlink to the _github repo_ that points to https://github.com
        1. Lets now also add Tags
            1. Click _Add/Remove Tags_
                1. Type _PCI_ in the box and Select below. 
                1. Optionally add other tags. 
                1. Click Done
        1. The documentation should look something like: 
            ![asyncapi_doc2](img/AppDoc.png)
        1. Click _Save_
                
                

## Discover Existing EDA Assets
Duration: 0:36:00

Most organizations already leverage event driven architecture (EDA) and have one or more event brokers. Today the Solace PubSub+ Event Portal supports the ability to scan, catalog and reverse engineer the following Event Brokers: 
1. Kafka – Confluent Kafka, Amazon MSK, Apache Kafka
1. Solace PubSub+ Event Broker – Coming Soon!

If you have a non-supported Event Broker type/configuration, then you will need add the schemas, events and applications to the Event Portal manually by using your existing documentation. While this may seem like a lot of work, it may be possible to capture this metadata and use the PubSub+ Event Portal’s APIs in order to automate the ingestion of this data. The benefits of doing this from a dependency management perspective is enormous as your EDA evolves and enables you to begin to manage and expose the existing event-driven capabilities implemented. 


### Automated Discovery and Data Importation from Kafka 
Once you have decided on the application domains that are required for your enterprise, it is time to start the data importation process. 

If you have an event broker type/configuration that is supported by the discovery agent then an automated discovery process not only provides a faster path to managing and governing your existing EDA assets, it also ensures that the data is valid and up to date. 

[Event Portal Discovery with Kafka Code Lab] (https://codelabs.solace.dev/codelabs/ep-discovery-kafka)


## The AsyncAPI Initiative 
Duration: 0:03:00

The [AsyncAPI Initiative](https://www.asyncapi.com/) is an open source initiative that provides both the AsyncAPI specification to define your asynchronous APIs, and open source tools to enable developers to build and maintain an event-driven architecture.

Positive
: Learn More in the [AsyncAPI Docs](https://www.asyncapi.com/docs/getting-started)

The AsyncAPI Generator allows you to generate a wide variety of things from an AsyncAPI document depending on what template you choose. The latest list of templates can be found [here](https://github.com/asyncapi/generator#list-of-official-generator-templates)

![asyncapiSpecExample](img/asyncapiSpecExample.webp)


![asyncapiGeneratorTemplates](img/asyncapiGeneratorTemplates.webp)


### Install the AsyncAPI Generator

Now that we've defined the architecture for our use case in the Event Portal we're ready to write some code! But we don't want to have to write everything from scatch so we're going to use the [AsyncAPI Generator](https://github.com/asyncapi/generator)

In order to use the AsyncAPI Generator we first need to install the CLI. 

If you have the prequisites installed as defined earlier in the "What You'll Need" section you should be able to pop open your terminal and use the command below to install the CLI. 

```bash
npm install -g @asyncapi/generator@0.53.1
```

Negative
: Note that the AsyncAPI project is continuously updated so if you previously installed the generator you can also use the command above to update to the latest.


## Implement ProcessPayment (Java/Spring)
Duration: 0:12:00

### Develop the ProcessPayment Microservice

🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕
On to developing the _ProcessPayment_ App. As defined during the design sections of this codelab, we determined that this will be a microservice written using Java & Spring. We are going to use the [Spring Cloud Stream](https://spring.io/projects/spring-cloud-stream) framework to develop this microservice since it was created for the exact purpose of developing event-driven microservices. We'll also keep the business logic to a minimum to focus on the process of creating an event-driven microservice with AsyncAPI + Spring Cloud Stream and getting it running! 

#### Generate the Code Skeleton
In the Solace Event Portal right click on the _ProcessPayment_ application, Choose _AsyncAPI_, Choose _**YAML**_ and click _Download_

![processPaymentAsyncapi](img/processPaymentAsyncapi.webp)

Positive
: The AsyncAPI Java Spring Cloud Stream Generator Template includes many [Configuration Options](https://github.com/asyncapi/java-spring-cloud-stream-template#configuration-options) that allow you to change what the generated code will look like. 

Let's add a few of the template's configuration options to the downloaded AsyncAPI document. 
* Add `x-scs-function-name: processPayment` under the _subscribe_ operation **and** the _publish_ operation under our two channels. By adding this you are telling the generator the name of the function you would like to handle events being exchanged and by adding the same function-name for both the _subscribe_ and the _publish_ operation you are saying you want them handled by the same function! 
* Add `x-scs-destination: test/taxinyc/PaymentProcessorQueue` under the _subscribe_ operation. By adding this and using the _Solace_ binder you are specifying the durable queue name if you're using a Consumer Group, or part of the temporary queue name if you're not. This will also add a topic subscription matching the channel specified in the Asyncapi document to the queue.  

✅ After adding those configuration options your channels section of the AsyncAPI document should look like the image below. 
```
channels:
  'taxinyc/backoffice/payment/charged/v1/${payment_status}/${driver_id}/${passenger_id}':
    publish:
      x-scs-function-name: processPayment
      message:
        $ref: '#/components/messages/PaymentCharged'
  'taxinyc/ops/ride/updated/v1/${ride_status}/${driver_id}/${passenger_id}/${current_latitude}/${current_longitude}':
    subscribe:
      x-scs-function-name: processPayment
      x-scs-destination: test/taxinyc/PaymentProcessorQueue
      message:
        $ref: '#/components/messages/RideUpdated'
```

Negative
: Note that by default, AsyncAPI code generator templates generate publisher code for subscribe operations and vice versa. You can switch this by setting the `info.x-view` parameter to `provider`. This parameter is automatically set in AsyncAPI documents exported from the Solace PubSub+ Event Portal. 

🚀 Our AsyncAPI document is now ready to generate the actual code so go over to your terminal and enter the command in the code snippet below. 

Note the different pieces of the command: 
* `ag` is the AsyncAPI Generator command
* `-o` is the output directory
* `-p` allows you to specify [parameters](https://github.com/asyncapi/java-spring-cloud-stream-template#parameters) defined for the template you're using
* `binder` is the Spring Cloud Stream binder you wish to use, in this case Solace
* `artifactId` & `groupId` configure Maven params of the same names
* `javaPackage` specifies the Java Package to place the generated classes into
* `host`, `username`, `password` and `msgVpn` allow you to set binder connection information.
* The yaml file is our AsyncAPI document
* And lastly, the `@asyncapi/java-spring-cloud-stream-template` is the AsyncAPI generator template that we are using. 

```bash
ag -o ProcessPayment -p binder=solace -p artifactId=ProcessPayment -p groupId=org.taxi.nyc -p javaPackage=org.taxi.nyc -p host=taxi.messaging.solace.cloud:55555 -p username=public-taxi-user -p password=iliketaxis -p msgVpn=nyc-modern-taxi ~/Downloads/ProcessPayment.yaml @asyncapi/java-spring-cloud-stream-template
```

✅ After running the command you should see output that ends with where you can find your generated files. 
```
Done! ✨
Check out your shiny new generated files at /private/tmp/codelab/ProcessPayment.
```

#### Import and Explore the Generated Project
The generated project is a Maven project so head over to your IDE and import the project so we can add our business logic. Once imported you should see something like the image below.     
![projectsetup2](img/projectsetup2.webp)

A few notes on the project: 
* The generated java classes are in the `org.taxi.nyc` package that we specified. 
* The `PaymentCharged` and `RideUpdated` POJOs were generated from the schemas defined in our AsyncAPI document and includes getters/setters/toString/etc.
* `Application.java` contains a `processPayment` method which is a `Function` that takes in a `RideUpdated` POJO and returns a `PaymentCharged` POJO.  
* The `application.yml` file contains the Spring configuration which tells our app how to connect to Solace using the SCSt binder as well as which message channels to bind our methods to. 
* The `pom.xml` file contains the dependencies needed for the microservice. These include the `solace-cloud-starter-stream-solace` dependency which allows you to use the Solace SCSt. Binder. 

#### Subscribe to _dropoff_ events
As of the writing of this codelab, dynamic topics are not yet supported by the Event Portal or the AsyncAPI Code Generator template. Because our Taxis are publishing their _RideUpdate_ events to a dynamic topic structure of `taxinyc/ops/ride/updated/v1/${ride_status}/${driver_id}/${passenger_id}/${current_latitude}/${current_longitude}` we need to update the `application.yml` file to subscribe to only `dropoff` events. To do this change the `queueAdditionalSubscriptions` parameter value to `taxinyc/ops/ride/updated/v1/dropoff/>`

Positive
: Note that the `>` symbol, when placed by itself as the last level in a topic, is a multi-level wildcard in Solace which subscribes to all events published to topics that begin with the same prefix. Example: `animals/domestic/>` matches `animals/domestic/cats` and `animals/domestic/dogs`. [More wildcard info, including a single level wildcard, can be found in docs](https://docs.solace.com/PubSub-Basics/Wildcard-Charaters-Topic-Subs.htm)


#### Publish to a personalized topic for uniqueness
Because there are potentially multiple people using a shared broker participating in this codelab at the same time we need to make sure we publish to a unique topic. Change your `spring.cloud.stream.bindings.processPayment-out-0.destination` to be `test/taxinyc/<YOUR_UNIQUE_NAME>/ops/payment/charged/v1/accepted`. **Be sure to replace <YOUR_UNIQUE_NAME> with your name or some unique field; and remember it for later!**

✅ After updating the `spring.cloud.stream` portion of your _application.yml_ file should look something like this:

```yaml
spring:
  cloud:
    stream:
      function:
        definition: processPayment
      bindings:
        processPayment-out-0:
          destination: test/taxinyc/yourname/backoffice/payment/charged/v1/accepted
        processPayment-in-0:
          destination: test/taxinyc/ProcessPaymentQueue
      solace:
        bindings:
          processPayment-in-0:
            consumer:
              queueAdditionalSubscriptions: 'taxinyc/ops/ride/updated/v1/dropoff/>'
```


#### Fill in the Business Logic
Obviously in the real world you'd have more complex business logic but for the sake of showing simplicity we're just going to log the _RideUpdated_ events as they're received and create a new PaymentCharged event for each. 

Open the _Application.java_ file and modify the `processPayment` method to log the events. When you're done it should look something like the code below. 

```java
@Bean
public Function<RideUpdated, PaymentCharged> processPayment() {
	return rideUpdated -> {
		logger.info("Received Ride Updated Event:" + rideUpdated);
		//TODO Process Payment
		PaymentCharged pc = new PaymentCharged();
		pc.setRideId(rideUpdated.getRideId());
		pc.setAmountCharged(rideUpdated.getMeterReading());
		pc.setPaymentStatus("accepted");
		pc.setPaymentChargedId(UUID.randomUUID().toString());
		pc.setInvoiceSystemId("PSG-" + RandomUtils.nextInt());
	    pc.setInformationSource("ProcessPayment Microservice");
		pc.setTimestamp(Instant.now().toString());
		pc.setEntityType("Driver");
		logger.info("Created PaymentCharged Event:" + pc);
		return pc;
	};
}
```


That's it! The app development is complete. 

🚀🚀🚀 Was that simple enough for you!? 🚀🚀🚀

### Run the app! 
Now that our app has been developed let's run it! 

If your IDE has support for Spring Boot you can run it as a Spring Boot App. 

Or run it from the terminal by navigating to the directory with the pom and running the `mvn clean spring-boot:run` command. 

Negative
: If you get an error that says something like `Web server failed to start. Port XXXX was already in use.` then change the `server.port` value in `application.yml` to an open port.

Once running you should see that for each RideUpdated event that is received a PaymentCharged Event is created which is being published back out onto the broker for downstream apps to consume. The output should look something like the below. 

```
2020-11-12 14:25:54.451  INFO 97106 --- [pool-2-thread-1] org.taxi.nyc.Application                 : Received Ride Updated Event:RideUpdated [ rideId: f3ce97cb-e2df-4ed2-bb07-ab6afe9db629 heading: 168 latitude: 40.666628 passengerCount: 2 pointIdx: 1025 informationSource: RideDispatcher speed: 22 driver: Driver [ driverId: 16 rating: 2.37 lastName: Sawyer carClass: Coupe firstName: Miwa ] passenger: Passenger [ passengerId: 13817844 rating: 4.43 lastName: Bateman firstName: Chantal ] meterIncrement: 0.0198049 longitude: -73.85236 timestamp: 2020-11-12T14:25:54.206-05:00 meterReading: 20.3 rideStatus: dropoff ]
2020-11-12 14:25:54.453  INFO 97106 --- [pool-2-thread-1] org.taxi.nyc.Application                 : Created PaymentCharged Event:PaymentCharged [ rideId: f3ce97cb-e2df-4ed2-bb07-ab6afe9db629 entityType: Driver amountCharged: 20.3 driver: null paymentChargedId: 59d3caed-cad1-438b-9e9a-b37b8660efe7 passenger: null paymentStatus: accepted invoiceSystemId: PSG-616368280 informationSource: ProcessPayment Microservice timestamp: 2020-11-12T19:25:54.452Z ]
```

🤯🤯 **The Microservice is now Running, connected to the Solace Event Broker and processing events!** 🤯🤯

## Implement InvoiceSystem (Python w/ MQTT)
Duration: 0:08:00

### Develop the InvoiceSystem Python App

🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕 🚖 🚕
On to developing the _InvoiceSystem_ python app that we previously designed. We are going to be using the Python Paho library to communicate with our event broker over MQTT. To do this we will leverage the [Python Paho AsyncAPI Generator Template](https://github.com/asyncapi/python-paho-template) to bootstrap our app creation. Note that [MQTT](https://mqtt.org/) is an open standard messaging protocol very popular in Internet of Things (IoT) world and is designed to be extremely lightweight and 

#### Generate the Code Skeleton
In the Solace Event Portal right click on the _InvoiceSystem_, Choose _AsyncAPI_, Choose _**YAML**_ and click _Download_

![invoiceSystemAsyncapi](img/invoiceSystemAsyncapi.webp)
  
Negative
: Note that by default, AsyncAPI code generator templates generate publisher code for subscribe operations and vice versa. You can switch this by setting the `info.x-view` parameter to `provider`. This parameter is automatically set in AsyncAPI documents exported from the Solace PubSub+ Event Portal. 

🚀 Our AsyncAPI document is now ready to generate the actual code so go over to your terminal and enter the command in the code snippet below. 

Note the different pieces of the command: 
* `ag` is the AsyncAPI Generator command
* `-o` is the output directory
* The yaml file is our AsyncAPI document
* And lastly, the `@asyncapi/python-paho-template` is the AsyncAPI generator template that we are using. 

```bash
ag -o InvoiceSystem ~/Downloads/InvoiceSystem.yaml @asyncapi/python-paho-template
```

✅ After running the command you should see output that ends with where you can find your generated files. 
```
Done! ✨
Check out your shiny new generated files at /private/tmp/codelab/InvoiceSystem.
```

#### Explore the Generated Project
The AsyncAPI Generator generated a python project in the directory specified by the `-o` parameter so head over to your favorite Python IDE and open it up. Once opened you should see something like the image below.     

![pythonProjectSetup](img/pythonProjectSetup.webp)

**A few notes on the project:** 
* The `paymentCharged.py` file contains the `PaymentCharged` class which is based on the schemas defined in our AsyncAPI document and leverages the `Entity` class in the `entity.py` file to provide json serialization methods. 
* The `messaging.py` class contains messaging logic to publish & subscribe using the paho mqtt library.
* The `config-template.ini` file is a template for the connection info needed to connect the paho mqtt library to a mqtt compliant broker. Note that if our AsyncAPI document contained a servers section then it would have automatically been filled out for us. The filling in of your servers based on a specific environment is on the PubSub+ Event Portal's roadmap and will be available at some point in the future. 
* The `main.py` file contains the heart of our app where the configuration is parsed, our consumer is defined, and the app starts up and connects to receive and process events. 


#### Add the broker connection info
Before coding our python app let's go ahead and put our credentials in place. 
1. Copy the `config-template.ini` file to `config.ini`
1. Modify the contents to look like below: 

```
[DEFAULT]
host=taxi.messaging.solace.cloud
password=iliketaxis
port=8883
username=public-taxi-user
```

#### Subscribe to _PaymentCharged_ events
As of the writing of this codelab, dynamic topics are not yet supported by the Event Portal or the AsyncAPI Code Generator template. Because our ProcessPayment microservice is publishing the PaymentCharged events to a dynamic topic structure of `test/taxinyc/<YOUR_UNIQUE_NAME>/backoffice/payment/charged/v1/${payment_status}/${driver_id}/${passenger_id}
` we need to update our subscription to subscribe to all _PaymentCharged_ events no matter their payment_status, driver_id or passenger_id. To do this change the subscription on line `33` of `main.py` to `test/taxinyc/<YOUR_UNIQUE_NAME>/backoffice/payment/charged/v1/#` where you substitute `<YOUR_UNIQUE_NAME>` for the name you used when creating the java app. 

Positive
: Note that the `#` symbol, when placed by itself as the last level in a MQTT topic, is a multi-level wildcard which subscribes to all events published to topics that begin with the same prefix. Example: `animals/domestic/#` matches `animals/domestic/cats` and `animals/domestic/dogs`. [More wildcard info, including a single level wildcard, can be found in docs](https://docs.solace.com/Open-APIs-Protocols/MQTT/MQTT-Topics.htm#Wildcard)


#### Make some quick updates for SSL
By default the app that is created using the Paho MQTT template expects to connect to an unencrypted port to exchange messages, however the broker we are using requires encrypted communications so add the following two lines below the `self.client.on_connect = on_connect` line (should be line 21) in `messaging.py`.
```
self.client.tls_set_context()
self.client.tls_insecure_set(True)
```

#### Temporary Step: Fix some Issues
Currently there is a bug in the AsyncAPI generator template for python-paho that prevents JSON parsing from working. To get around this go ahead and comment out lines `23` and `24` in `main.py`. Note that a github issue has been opened on the AsyncAPI generator template to remedy this :) 

That's it! The app development is complete. 

🚀🚀🚀 Was that simple enough for you!? 🚀🚀🚀

### Run the app! 
Now that our app has been developed let's run it! 

Run it from your IDE or from the command line by executing `python3 main.py`

🤯🤯 **The Python app is now Running, connected to the Solace Event Broker and receiving and logging events!** 🤯🤯

## Implement: Other Options! 
Duration: 0:04:00

You can create event driven applications in a wide variety of different options as shown here: 
![APIs and Protocols] (img/Solace-PubSub-Platform-Diagram-1.png)

### Generate Custom Code
Since the AsyncAPI Specification provides a machine readable way to define your Asynchronous applications it allows for the creation of custom code generators. The easiest way to likely do this is to leverage the tooling that the AsyncAPI Initiative has already put in place and create a new template for the [AsyncAPI Generator](https://github.com/asyncapi/generator) 

### Use an Integration Platform

[Dell Boomi Connector] (https://solace.com/boomi/)

## Takeaways
Duration: 0:04:00

✅ Event Driven Architecture does not have to be hard if you understand some key fundementals and follow best practices.

✅ The Solace PubSub+ Event Portal is an excellent tool to design, visualize and document your Event-Driven Architecture, discover what events exist, collaborate with your team and kickstart development via exporting of AsyncAPI documents.

✅ AsyncAPI Generator templates allow developers to consistently create event-driven applications by generating code skeletons that are pre-wired with the events and channels defined in the AsyncAPI documents.


![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
