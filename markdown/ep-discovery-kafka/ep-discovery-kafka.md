author: Dishant Langayan
summary: A guided walk through of PubSub+ Event Portal Discovery with Kafka
id: ep-discovery-kafka
tags: guide,event-portal,kafka
categories: Portal,Kafka
environments: Web
status: Draft
feedback link: https://solace.community/
analytics account: UA-3921398-10

# Guided Walk Through of PubSub+ Event Portal Discovery with Kafka

## Introduction

Duration: 0:02:00

Are you looking to discover, visual, catalog, share, and reuse your Kafka event streams, but don't know how and or where to begin. Or does your organization look something like the picture below and you are struggling to understand what is the data that is really going through your Kafka clusters?

![Kafka Organization](img/kafka_org.png)

Well you have come to the right place, and in this guided walk through, we will show you how to:

* Run a discovery scan on a Kafka cluster
* Upload the scan to PubSub+ Event Portal to visualize the results
* And finally take action on your Kafka consumer groups and topics by linking them to applications, organizing them in a domain, sharing and collaborating on the data with your teams

We expect with this knowledge you will be able to scan your own Kafka clusters to discover new event streams or consumer groups you may not be aware off. 

To make this walk through engaging and meaningful, we will make use of a real-world use, which we will jump into a bit, and ask you to transport yourself to be an employee of a new company. We also cover some foundational concepts so we all aligned on the same page.

So let's get started!

## Use Case: NYC Taxi Co.

Duration: 0:03:00

You are a member of the engineering team at the _NYC Modern Taxi Co_, a fictional taxi cab company based in New York City. Your team is playing from behind and racing to catch up with technology innovation introduced to the industry by Rideshare competitors such as Uber and Lyft. In order for the company to survive and eventually thrive your team has convinced the board that transforming the companies' IT systems is of utmost importance. Your team has done it's research and determined that moving to an Event-Driven Architecture is essential to future rapid innovation and has already kicked this initiative off by deploying a Solace Event Mesh and updating the taxi fleet to stream real-time events that include ride and location information. We know what the fleet is up to! Now it's time to start to continually improve and provide a world class customer experience.

In order to react in a real-time manner the team has decided that we want to process the updates as they stream in from the fleet of taxis instead of putting them directly into a datastore and then having to retrieve them to do processing later. To prototype this work, you'll see a high level design in the diagram below. Since we already have the taxi fleet streaming their updates into our PubSub+ Event Mesh we need to do three things: 

1. 🚖 Capture this high level design in the PubSub+ Event Portal where we can define our Event-Driven Architecture, including its' components: Applications, Events and Schemas. This will allow us to define the details needed to implement, visualize and extend the architecture as it evolves, and share/collaborate with our entire engineering team as we continue to innovate.  
1. 🚕 Next up we're going to create the _RideDropoffProcessor_ microservice which will subscribe to the stream of _dropoff_ taxi updates from the fleet, capture events for a specified time window (we'll use 20 seconds to make it easy), calculate the averages, and publish a new _RideAverageUpdate_ event for each window.  
1. 🚖 Lastly we'll create a _RideDropoffConsumer_ that receives the stream of _RideAverageUpdate_ events and captures them for display and further processing. 


![Architecture](img/arch.webp)

Positive
: The dataset you will be using in this lab originally comes from the NYC Taxi & Limousine Commission's open data release of more than a billion taxi ride records. Google then extended one week worth of data (3M taxi rides) from their original pickup and drop-off points into full routes in order to simulate a fleet of taxis roaming the streets of NYC as they define [here](https://codelabs.developers.google.com/codelabs/cloud-dataflow-nyc-taxi-tycoon/?_ga=2.11039092.-1355519641.1572284467/#0). Solace is streaming this data over Solace PubSub+ for you to analyze and process. 
<p>Terms of Use: This dataset is publicly available for anyone to use under the following terms provided by the Dataset Source — [https://data.cityofnewyork.us/](https://data.cityofnewyork.us/) — and is provided "AS IS" without any warranty, express or implied, from Solace. Solace disclaims all liability for any damages, direct or indirect, resulting from the use of the dataset.</p>

## Foundation Concepts

Duration: 0:03:00

Before we dive deeper, let ensure we are all aligned with Kafka & PubSub+ Event Portal objects and concepts we will use.

### Consumer Groups

TODO: What are consumer groups?

### Topics

TODO: Kafka topics vs Solace topics?

### Schemas

TODO: What are schemas?

### Application Domain

TODO: What are app domains?

### Applications

TODO: What are applications?

## What you need: Prerequisites

Duration: 0:02:00

TODO: explain the support Kafka versions, and other things required to run the agent

Provide the Pre-canned scan file here if users are to skip scanning a kafka cluster.

## Scan a Kafka Cluster
Duration: 0:05:00

## Uploading a Scan to Event Portal
Duration: 0:01:00

## Visualizing Your Scan
Duration: 0:15:00

### Creating an App Domain

### Linking Consumer Groups to Application

### Linking Topic to Publishers

### Making Links Across App Domains

### Commit to Event Portal

## Designer and Catalog 
Duration: 0:05:00

## Next Steps
Duration: 0:01:00

Summarize and key takeaways

✅ < Fill IN TAKEAWAY 1>   
✅ < Fill IN TAKEAWAY 2>   
✅ < Fill IN TAKEAWAY 3>   

Next steps -> scan your own clusters