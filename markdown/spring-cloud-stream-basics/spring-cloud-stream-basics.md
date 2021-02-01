author: Marc DiPasquale
summary: This codelab walks a developer through the basics of Spring Cloud Stream
id: spring-cloud-stream-basics
categories: Spring,Java
tags: workshop
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/spring-cloud-stream-basics/spring-cloud-stream-basics.md
analytics account: UA-3921398-10

# Spring Cloud Stream Basics

## What You'll Learn
Duration: 0:02:00

![](img/spring-cloud-logo.png)

This codelab will help you get started with Spring Cloud Stream. We'll quickly cover some basic fundamentals before jumping in to actually creating some Spring Cloud Stream microservices to see the framework in action. 

You'll learn: 
* Spring Cloud Stream Basics
* How to create a Cloud Stream Processor
* How to use Function Composition to create a processing pipeline
* Tips, Tricks & Insights along the way


Valuable Resources: 
* The Spring Cloud Stream [Reference Guide](https://cloud.spring.io/spring-cloud-static/spring-cloud-stream/current/reference/html/spring-cloud-stream.html#spring-cloud-stream-reference)
* Spring Sample [Github Repository](https://github.com/spring-cloud/spring-cloud-stream-samples)
* Solace Sample [Github Repository](https://github.com/SolaceSamples/solace-samples-spring)


## What You'll Need
Duration: 0:08:00

🛠 This page covers the setup needed to perform this codelab. 🛠 

### Spring Cloud Stream Requirements
✅ Spring Cloud Stream just requires Java and Maven to use 🚀  
* Java 1.8+ (Check version using `java -version`)
* Maven 3.3+ (Check version using `mvn -version`)
	* On mac you can `brew install maven`
	* Other install instructions [here](https://maven.apache.org/install.html)
* Your favorite Java IDE 💥

### Create your Messaging Service
✅ (1) Sign up for a free Solace Cloud account

Navigate to [this link](https://console.solace.cloud/login/new-account) and fill out the required information. No credit card required! If you already have an account, skip right to #2.

✅ (2) Create a messaging service

After you create your Solace Cloud account and sign in to the Solace Cloud Console, you'll be routed to the Solace Cloud Landing page.

![Solace Cloud Event Mesh Page](img/landing-page-event-mesh.webp "Solace Cloud Event Mesh")

Click on 'Messaging Services' and all the messaging services associated with your account will show up if you have any already created. To create a new service, click either button as depicted in the image below:

![Solace Cloud Landing Page](img/landing-page-signup.webp "Solace Cloud Landing Page")

Fill out all the details for your messaging service, and then click "Create" at the bottom of the page. Note: make sure you choose the "Developer" option for the Service Type

![Create Solace Cloud Messaging Service](img/create-service.png "Solace Cloud Messaging Service")

Your service should be ready to use in a few minutes

✅ (3) Take note of the connection details

If your messaging service was created successfully, you'll be routed to the summary page of your new messaging service. From the service summary page, click on the "Connect" tab so we can take note of the connection details we'll need later.

![Connect Tab Preview](img/service-summary-page.webp "Connect Tab Preview")

After you click the "Connect" tab, click the "Solace Messaging" box, and then take note of the "Connection Details" section. We'll be using the "Secured SMF Host" URL.

![Solace Web Messaging Tab](img/smf-messaging-connect-tab.webp "Solace Messaging Tab")


🚀 Setup complete! Let's get going! 🚀


## Cloud Stream Fundamentals
Duration: 0:05:00

### Cloud Stream Basics

Spring Cloud Stream is a framework for creating highly scalable, event-driven microservices connected by pluggable messaging services. Messaging services are pluggable via Binders that we'll cover in a bit. The framework is based on Spring Boot and Spring Integration.

Spring Cloud Stream has three different types of message exchange contracts as pictures below. 
1. Suppliers are sources of events
1. Sinks are consumers of events
1. Processors are both consumers and subscribers of events

![Cloud Stream Intro](img/cloudstreamintro.webp)


### Message Exchange Contracts Map to Java Functions
As of Spring Cloud Stream v3 the preferred programming model is to use Java Functions to implement your cloud stream apps. 

We just mentioned the 3 types of Cloud Stream message exchange contract are "Sources", "Sinks" and "Processors". 
Those map to functions as follows: 
* `java.util.function.Supplier` -> Source [Producer/Publisher of Events]
* `java.util.function.Consumer` -> Sink [Subscriber/Consumer of Events]
* `java.util.function.Function` -> Processor [ Consumes, Processes, and Produces Events ]

### Binders
Spring Cloud Stream Binders are really what make the framework useful. Binders provide an abstraction layer between your code and the messaging systems over which events are flowing. This allows you to write your code without having to worry about learning messaging APIs! When messages are sent or received from the messaging system they pass through the messaging system specific binder which knows how to communicate with that specific message broker. 

As of the creation of this codelab the available Cloud Stream Binders are: 
* RabbitMQ
* Apache Kafka
* Amazon Kinesis
* Google PubSub
* Solace PubSub+
* Azure Event Hubs
* Apache RocketMQ

Today we're going to use the [Solace PubSub+ Binder](https://github.com/SolaceProducts/solace-spring-cloud/tree/master/solace-spring-cloud-starters/solace-spring-cloud-stream-starter) which supports publish subscribe and consumer groups. 

### Communication Models
Instead of having to learn Messaging APIs, developers just have to understand the communication models that Spring Cloud Stream supports. There are 3 supported models, but support varies per binder. 

1. Publish-subscribe:  subscribers are independent from each other & receive events in order
1. Consumer groups:  fan-out and load-balancing across multiple consumers
1. Stateful partitioning support:  in-order processing for consistency and performance

🚀 So what are we waiting for!? Let's get started 🚀

## Your First Processor
Duration: 0:10:00

### Use Spring Initializr to Generate your Project

🚀 First we're going to use Spring Initializr to generate our Spring Boot project for us. 
1. Open the Spring Tool Suite IDE. 
1. Choose `File -> New -> Spring Starter Project`
  ![Spring Starter Project](img/springStarterProject.webp)
1. On the first screen give your project a name of "springone" and click `Next`
1. On the second screen search for "solace" under Available and choose both "Solace PubSub+" and "Cloud Stream"
  ![Add Dependencies](img/solaceDependencies.webp)
1. Click `Finish`

✅ You should see a new project named "springone" in your IDE!

If you look at the `pom.xml` file you'll see a few important things: 
* This is a Spring Boot project which has a parent of `spring-boot-starter-parent`
* The java version you chose is included
* The "Spring Cloud Stream" and "Spring Cloud Starter Stream Solace" dependencies are included

![Pom File](img/pom.webp)

### Add Messaging Service Connection Info
Open the `application.properties` file under `src/main/resources` and enter the properties below substituting the connection information with your messaging services' connect info we got from the Solace Cloud Connect tab in the previous section. 

```
spring.cloud.stream.binders.solace.type=solace
spring.cloud.stream.binders.solace.environment.solace.java.host=tcp://localhost:55555
spring.cloud.stream.binders.solace.environment.solace.java.msgVpn=default
spring.cloud.stream.binders.solace.environment.solace.java.clientUsername=default
spring.cloud.stream.binders.solace.environment.solace.java.clientPassword=default
spring.cloud.stream.binders.solace.environment.solace.java.connectRetries=0
spring.cloud.stream.binders.solace.environment.solace.java.connectRetriesPerHost=0
```

### Write the Java Function
Now to write some code! 

Open the `SpringoneApplication.java` file. Unless you chose different settings when creating your project it should be under `src/main/java/com/example/demo`

When you open the project you'll see the basic skeleton of a Spring Boot app, including the `@SpringBootApplication` java annotation. 

Positive
: **@SpringBootApplication** Indicates a configuration class that declares one or more @Bean methods and also triggers auto-configuration and component scanning. This is a convenience annotation that is equivalent to declaring @Configuration, @EnableAutoConfiguration and @ComponentScan.

Let's go ahead and create a `java.util.function.Function` bean that takes in a String, changes is it to all uppercase and returns a String. 
The code might look something like below: 
```
@Bean
public Function<String, String> uppercase(){
   return v -> {
      System.out.println("Uppercasing: " + v);
      return v.toUpperCase();
   };
}
```

Negative
: Note: You might need to add imports, this is done by clicking `ctrl + shift + 0` and then choose java.util.function.Function

🚀 That's it! No Messaging code and we have an app that can retrieve a message, process it and publish a message! 
🚀 Let's test it out. 

Run your app by right clicking on your project, choosing "Run As" and "Spring Boot App" if using Spring Tool Suite. From the command line you can also run by entering `mvn clean spring-boot:run`
![Run App](img/runApp.webp)

## Test your Microservice
Duration: 0:03:00

✅ In order to test your function open Solace Cloud, select the messaging service and navigate to the Try Me! tab

![tryme](img/tryme.png "tryme")


This page will allow you to send and receive messages to see if your function is working as expected.

To test your function perform the following steps:
1. Click the `Connect` button for the "Subscriber"
1. Type "uppercase-out-0" into the "Subscribe to a topic to receive direct messages" box and click `Subscribe`
1. Click the `Connect` button for the "Publisher"
1. Type "uppercase-in-0" as the topic to publish to. 
1. Type "Spring One is Awesome!" in the "Message Content" box and click `Publish`

🚀 You should see your application printed "Uppercasing: Spring One is Awesome!" in your IDE and the "Subscriber" in the "Try Me!" menu in Solace Cloud should show that a message was received that contained "SPRING ONE IS AWESOME!"

Positive
: Note that the "uppercase-in-0" and "uppercase-out-0" are default binding names which follow a convention of `<functionName>` + `-in-` + `<index>` for input bindings and `<functionName>` + `-out-` + `<index>` for output bindings. Those can be changed by setting them in the Spring configuration file. [More information here](https://cloud.spring.io/spring-cloud-static/spring-cloud-stream/current/reference/html/spring-cloud-stream.html#_common_binding_properties)

🎉 **Congratulations! You just created your first Spring Cloud Stream microservice!**

## Function Composition
Duration: 0:10:00

Another powerful feature of Spring Cloud Stream is inherited from Spring Cloud Function, and that feature is the capability of doing Function Composition. This allows you to create simple functions as Spring Beans that can be individually tested, re-used and chained together to create a processing chain. 

Instead of just talking about Function Composition let's try it out 😁. 

In the same class where you already have your "uppercase" function let's create a "reverse" function that takes in a string and reverses the ordering. This function would like something like this: 
```
@Bean
public Function<String, String> reverse(){
	return v -> {
		System.out.println("Reversing: " + v);
        return new StringBuilder(v).reverse().toString();
   };
}
```

Now that we have two functions Spring Cloud Stream won't just assume what bindings we want created so we need to go configure them in the `application.properties` file. Assuming we want to uppercase an incoming String and then reverse it we will add these properties to the file: 

```
spring.cloud.function.definition=uppercase|reverse
spring.cloud.stream.function.bindings.uppercasereverse-in-0=input
spring.cloud.stream.function.bindings.uppercasereverse-out-0=output
```

Positive
: Note that Spring Cloud Stream performs [Content Type Negotiation](https://cloud.spring.io/spring-cloud-static/spring-cloud-stream/current/reference/html/spring-cloud-stream.html#content-type-management) between each function so you could have a String output from one function and a POJO going into another as long as the framework knows how to deal with the Message Conversion. Read more about that in the [Reference Guide](https://cloud.spring.io/spring-cloud-static/spring-cloud-stream/current/reference/html/spring-cloud-stream.html#content-type-management). 

✅ We now have our function all wired up so go ahead and stop the app and restart it.     
✅ Navigate back to the "Try Me" menu in Solace Cloud (Refer to the steps in the "Test your Microservice" section if needed)     
✅ Add a subscription for "output" since that is what we called our output binding name. And publish a message to the "input" topic since that's what we called our input binding.     
✅ If you published "Hello world!" you should see that the subscriber received a message containing "!DLROW OLLEH" and your application printed the following to the terminal as it processed the message through the pipeline.  
```
Uppercasing: Hello world!
Reversing: HELLO WORLD!
```

🥳 Woohoo we have now created a Spring Cloud Stream app that uses a pipeline of functions to process incoming messages! 

## Takeaways + Next Steps
Duration: 0:02:00

✅ Hopefully this codelab showed you how easy it can be to create event-driven microservices using Spring Cloud Stream. Note that you didn't have to learn any messaging APIs as the Cloud Stream Binder abstracts them from you!   
✅ Learn how to generate Cloud Stream apps using AsyncAPI [here](https://codelabs.solace.dev/codelabs/design-to-code-workshop/#0).  
✅ Learn how to publish to dynamic topics using Spring Cloud Stream by a sample [here](https://github.com/SolaceSamples/solace-samples-spring/blob/master/cloud-stream-dynamic-destination-processor/src/main/java/com/solace/samples/spring/scs/DynamicDestinationProcessor.java).    

![solly_wave](img/solly_wave.webp)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
