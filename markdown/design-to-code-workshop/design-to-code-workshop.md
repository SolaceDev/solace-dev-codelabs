author: Marc DiPasquale
id: design-to-code-workshop
summary: This codelab walks you through how to design an EDA using the Solace PubSub+ Event Portal, export the AsyncAPI documents, generate code using the AsyncAPI generator and see your events flow across your apps!
tags: AsyncAPI, Spring, Java, Portal
categories: workshop
environments: Web
status: Published
feedback link: https://github.com/Mrc0113/design-to-code-workshop
analytics account: UA-3921398-10

# Developer Workshop: Design to Code using Portal + AsyncAPI Code Generation

## What You'll Learn
Duration: 0:05:00

## What You'll Need
Duration: 0:05:00

### Solace Event Portal 

#### Login or Sign-up

#### Import Application Domain

### Terminal Access?

## Use Case Overview
Duration: 0:05:00

![Architecture](img/arch.webp)

## Design Your EDA
Duration: 0:05:00

Now that you're familiar with the use case and you've imported the application domain into the Event Portal let's get update our Event-Driven Architecture (EDA). 

Open the _NYC Modern Taxi Co_ Application Domain that you previously imported in the Event Portal Designer. You should see a _Taxis_ Application which publishes _TaxiStatusUpdate_ Events. We want to extend this architecture to match the design discussed for in our use case.

### Add the RideDropoffProcessor Application
The first step towards doing this is to add the _RideDropoffProcessor._ To do this right click on the graph and choose _Create Application_. 

Fill in the fields as follows: 
1. **Name**: RideDropoffProcessor
1. **Description**: This is a Spring Cloud Stream microservice that will consume the TaxiStatusUpdates with a ride status of "dropoff", process the events, and output summary events. 
1. Click _Add/Remove Owners_ and choose yourself
1. Click _Add/Remove Tags_ and add "SCSt" as a tag. This tag is short for "Spring Cloud Stream" which is the framework we will use to develop our microservice later. 
1. Click the _Manage Events_ button, search for "TaxiStatusUpdate" and click _Sub_ next to it. This means that your application will subscribe to these events.
1. Click the _Save_ Button

You should now see your _RideDropoffProcessor_ added to the graph. 


### Add the RideAverageUpdate Event
It's great that the _RideDropoffProcessor_ is now consuming the _TaxiStatsUpdate_ events, but we want it to process those events and publish _RideAverageUpdate_ events. To show this we need to create the _RideAverageUpdate_ event and the schema which defines it's payload. 

Right click on the graph and choose _Create Event_ 

Fill in the fields as follows: 
1. **Name**: RideAverageUpdate
1. **Description**: This event contains the average cost of rides over a specified duration
1. **Topic**: taxi/nyc/v1/stats/dropoff/avg
1. Click _Add/Remove Owners_ and choose yourself 
1. For **Payload Schema** click _Add New_ 

Positive
: When designing your own Event-Driven Architecture the defining of your topic space is an important step towards achieving the benefits promised by an EDA. Be sure to take the time to read our [Topic Architecture Best Practices](https://docs.solace.com/Best-Practices/Topic-Architecture-Best-Practices.htm).  

Since our data is JSON we'll define a JSON Schema to define our event payload. 

Fill in the fields as follows: 
1. **Name**: RideAveragePayload
1. **Description**: Event Payload which contains average meter readings, average passenger counts, and the number of rides in a given window duration.
1. **Content Type**: JSON
1. Click _Add/Remove Owners_ and choose yourself 
1. Under _Content_ paste the JSON schema info from below. This schema was generated from a sample message from [jsonschema.net](https://jsonschema.net) 
1. Click _Save_ 
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
            "timestamp": "2020-06-04T20:09:59.99832-04:00",
            "avg_meter_reading": 21.615217,
            "avg_passenger_count": 1.5,
            "window_duration_sec": 300,
            "window_ride_count": 5
        }
    ],
    "required": [
        "timestamp",
        "avg_meter_reading",
        "avg_passenger_count",
        "window_duration_sec",
        "window_ride_count"
    ],
    "additionalProperties": true,
    "properties": {
        "timestamp": {
            "$id": "#/properties/timestamp",
            "type": "string",
            "title": "The timestamp schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2020-06-04T20:09:59.99832-04:00"
            ]
        },
        "avg_meter_reading": {
            "$id": "#/properties/avg_meter_reading",
            "type": "number",
            "title": "The avg_meter_reading schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0.0,
            "examples": [
                21.615217
            ]
        },
        "avg_passenger_count": {
            "$id": "#/properties/avg_passenger_count",
            "type": "number",
            "title": "The avg_passenger_count schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0.0,
            "examples": [
                1.5
            ]
        },
        "window_duration_sec": {
            "$id": "#/properties/window_duration_sec",
            "type": "integer",
            "title": "The window_duration_sec schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                300
            ]
        },
        "window_ride_count": {
            "$id": "#/properties/window_ride_count",
            "type": "integer",
            "title": "The window_ride_count schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                5
            ]
        }
    }
}
```  

We have now created a new payload schema and the schema has automatically been added to our event. 

Go ahead and click _Save_ to complete the creation of our _RideAverageUpdate_ event.

### Add the RideDropoffConsumer Application
To complete the architecture for our use case we just need to add the _RideDropoffConsumer_ application. Don't worry, this one will be quick since we've already created all of the needed Events and Payloads :) 

Right click on the graph and choose _Create Application_. 
Fill in the form as follows: 
1. **Name**: RideDropoffConsumer
1. **Description**: This is a nodejs application that will consume summary events via MQTT for further analysis
1. Click _Add/Remove Owners_ and choose yourself
1. Click _Manage Events_, search for "RideAverageUpdate" and click "Sub" next to it since the _RideDropoffConsumer_ wants to subscribe to these events. 
1. Click _Save_ 

That's it! Our Use Case design is now reflected by our architecture captured in the Event Portal and we're ready for implementation!

## Code Generation
Duration: 0:05:00

## Takeaways
Duration: 0:05:00

### Info Boxes
Plain Text followed by green & yellow info boxes 

Negative
: This will appear in a yellow info box.

Positive
: This will appear in a green info box.

### Bullets
Plain Text followed by bullets
* Hello
* CodeLab
* World

### Numbered List
1. List
1. Using
1. Numbers

### Add a Link
Add a link!
[Example of a Link](https://www.google.com)

### Embed an iframe
![https://codepen.io/tzoght/embed/yRNZaP](https://en.wikipedia.org/wiki/File:Example.jpg "Try Me Publisher")
