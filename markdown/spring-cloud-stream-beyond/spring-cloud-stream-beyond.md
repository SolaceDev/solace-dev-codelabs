author: Marc DiPasquale
summary: This Codelab Covers more advanced features of using Spring Cloud Stream and the Solace PubSub+ Binder
id: spring-cloud-stream-beyond
tags: workshop
categories: spring, java
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/spring-cloud-stream-beyond

# Spring Cloud Stream - Beyond the Basics

## What you'll learn: Overview
Duration: 0:03:00

Enter a codelab overview here: what & why and github repo link where you can find related code if applicable

## What you need: Prerequisites
Duration: 0:05:00
Enter environment setup & prerequisites here

## Communication Models and the Solace Binder
Duration: 0:7:00

### Choosing Persistent Publish-Subscribe or Consumer Groups
include hte group or not
how this affects the queue that is created

### Concurrency
how to do it! non-exclusive :) 

## Message Headers
Duration: 0:07:00
Consumer Side
Publisher Side

They are copied from input message to output message if not set...

## Wildcard Subscriptions
Duration: 0:15:00
2 ways: in the destination in queueAdditionalSubscriptions
<NEW> Extract topic levels as variables? 

## Dynamic Publishing
Duration: 0:15:00
2 ways: StreamBridge and TARGET_DESTINATION Header

## Batch Publishing
Duration: 0:07:00
return Collection<Message<?>>

## Consumer Error Handling
Duration: 0:15:00
Retry Templates in framework
Solace redeliveries and DLQ/DMQ
Publish to Error Queue
Custom! 

## Publisher Error Handling
Duration: 0:07:00
How to handle it!

## Takeaways & Next Steps
Duration: 0:03:00
✅ < Fill IN TAKEAWAY 1>   
✅ < Fill IN TAKEAWAY 2>   
✅ < Fill IN TAKEAWAY 3> 

Next Steps: 
AsyncAPI Code Gen
Tracing?

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.

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

