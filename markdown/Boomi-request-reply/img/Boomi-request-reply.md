author: Michael Hilmen
summary:
id: Boomi-request-reply
tags: 
categories: Boomi, request, reply
environments: Web
status: Draft
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/Boomi-request-reply

# How to use the Solace Connector for Boomi Request Action

## What you'll learn: Overview

Duration: 0:05:00

Sometimes Boomi Atom Processes need to communicate with external services in the middle of process execution.  Anything from pulling data from a database, calling a service for a credit check, or validating the status of a warranty claim for processing a product return.  These are synchronous types of calls, meaning the Boomi Atom Process needs to wait for the response before proceeding.  On May 15th 2021, Boomi released the latest version of the Solace connector to support this type of interaction, support for a Request Action in the Solace Connector Shape.

You will learn how to implement the Solace Connector for Boomi Request Action.

## What you need: Prerequisites

Duration: 0:07:00

1. A general understanding of [event-driven architecture (EDA) terms and concepts](https://docs.solace.com/#Messagin).
1. Basic knowledge of the Boomi GUI and deployments. A good place to start would be the [Getting Started with Boomi and Solace](https://codelabs.solace.dev/codelabs/boomi-v2-getting-started/index.html) Codelab.

After you finish the Getting Started with Boomi and Solace codelab, you’ll have the following

- A Solace trial account
- A Boomi trial account
- A local atom up and running
- An understanding of how to deploy a Boomi process to a Boomi Atom

Positive
: If you’re new to the world of events, welcome! Solace has [extensive blogs focusing on event-driven architecture and development.](https://solace.com/blog/)


## Use Case Overview

Duration: 0:15:00

In this example, we will be using the new Request Action within the Solace Connector Shape to perform a blocking synchronous request/reply in the middle of a Boomi Process.  We will be using Solace to handle the request which means the document that we feed to the Solace Connector Request will be published onto a topic that we know ahead of time.  The replying service will consume that document do something with it, and reply to a dynamically created ReplyTo topic with the response and the correlationID (also dynamically created by the Solace Connector).  

We are not going to create a service replier the first time through.  We are going to use a Solace web GUI to perform the reply so we can better see the inner workings.  

Let’s get started!

## Create a Boomi Request Process

The first thing we will do is create a simple Process in Boomi that makes a request via a publication to a Solace topic

1. In your Boomi environment, create a new Process.  You may call it anything you like, we will be calling ours Boomi Requestor

![Boomi Request Process Create](img/CreateBoomiReqReplyProcess.png)

1. Configure the Solace Connector Shape
* Set the start shape type to "No Data"

![No Data Start Shape](img/NoDataStartShape.png)

1. Drag a Message Shape onto the canvas and give it some sample data
* I am putting a silly question in, but it does not matter.  We are not really processing this data.

![Message Shape - sample data](img/MessageShape-sampleData.png)

1. Drag a Solace Connector Shape onto the canvas and configure to send a Request
* Set the Connection to your Solace instance
* Configure the operation as below: 

![Message Shape - sample data](img/Solace Request Shape.png)











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

### Add an Image or a GIF

![Soly Image Caption](img/soly.gif)

## What you need: Prerequisites

Duration: 0:07:00

Enter environment setup & prerequisites here

### Add a Link
Add a link!
[Example of a Link](https://www.google.com)

### Embed an iframe

![https://codepen.io/tzoght/embed/yRNZaP](https://en.wikipedia.org/wiki/File:Example.jpg "Try Me Publisher")

## Custom Step 1
## Custom Step 2
## Custom Step 3

## Takeaways

Duration: 0:07:00

✅ < Fill IN TAKEAWAY 1>   
✅ < Fill IN TAKEAWAY 2>   
✅ < Fill IN TAKEAWAY 3>   

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
