author: Jamieson Walker
summary:
id: explore-dmr
tags:
categories: solace,dmr
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/explore-dmr/explore-dmr.md


# DMR (Event Mesh) Exploration Procedures

## Objectives
Duration: 0:05:00

### Prerequisites
1. 2+ Solace PubSub+ Brokers deployed in environments where they are visable to each other over a network. 
2. Access to the Solace Broker WebUI for all Brokers via administrator credentials. 

<aside class=“positive”> A note on security: The brokers must be secured with a TLS certificate. </aside>

If you do not meet both of these requirements please use the following resources to setup and configure Solace PubSub+ Brokers.
* [Solace Broker CodeLab](https://codelabs.solace.dev/codelabs/get-started-basics/index.html)
* [Solace Cloud Trial](https://console.solace.cloud/login/new-account)
* [Solace PubSub+ Getting Started](https://solace.com/products/event-broker/software/getting-started/)
<br>

This codelab will lay the groundwork for a Solace based Event Mesh by setting up a Dynamic Message Routing (DMR) link between two stand alone brokers.  These brokers can be running in Docker or on Solace Cloud, in any cloud environment.  Then we will explore how events are propagated across a DMR link.  Setup publishers and Subscribers to each of the brokers in our Event Mesh in order to see events publish to one broker be dynamically routed to the other brokers in our Event Mesh where there are active subscribers. 

### Learning Objectives:
 ⬜️ Setup a DMR link between two Solace Brokers  
 ⬜️ Publish and Subscribe to DMR enabled topics with Try Me  
 ⬜️ Publish and Subscribe to DMR enabled topics with SDKPerf 
<br><br>

### Resulting Architecture:
![DMR Exploration Topics](img/DMR_Exploration.png)

## Setting up DMR with the Solace Broker WebUI
Duration: 0:18:00

**What is a Solace Event Mesh Powered by DMR**

If you have not heard about Solace Dynamic Message Routing (DMR) or Event Mesh here is a quick refresher: An event mesh is like a super-efficient highway system for data that allows event data to flow only to parts of the mesh where that event is needed. This occurs dynamically, meaning that new event types can be added any time, and new interests in events can also be registered, immediately changing the flow of events in real time. Event Brokers that make up the mesh can be running in any environment (data center, private cloud, public cloud, or combination), and are configured to dynamically route data from producing applications to consuming applications without forcing those applications to know about one another, or how they connect to the mesh.

![event-mesh-solution.gif](img/event-mesh-solution.gif)

### Connecting Solace Brokers via DMR

1. Navigate to the Broker WebUI and Login

2. Create a new Cluster
    <br><aside class=“positive”>❗️If you are on a Solace Cloud Broker a cluster ia automatically defined. If you are using Solace Software Brokers you will have to define a cluster for the broker. </aside><br>
Select Cluster from the left Solace menu then select Create New Cluster

![Create New Cluster](img/create_cluster.jpeg)

3. Define cluster: Set Name, provide cluster password, confirm cluster password, turn off client certificate authentication, continue.

![Define Cluster Parameters](img/define_cluster.jpeg)

4. If you are defining a cluster on the PubSub+ Standard Docker container you will likely get a warning about the spool side being too small.  You can bypass the warning with no reprocussions, unless you are moving large amounts of data between brokers. 

![Spool Size Too Small](img/SpoolSizeTooSmall.png)
[Expand Spool Size Allocation](https://docs.solace.com/Messaging/Guaranteed-Msg/System-Level-Msg-Spool-Config.htm#Config-Max-Spool)

5. After a few seconds you will see your new cluster status change to Up

![Cluster Up](img/clusterUp.png)


<aside class=“positive”> ♻️ At this point repeat the Cluster Creation steps on each Software instance of Solace PubSub+ broker that you wish to connect into the Event Mesh. Then continue to the next step </aside>


6. Create an External DMR link between clusters: 
    Right Click on the Cluster Summary page and Select "Create External Link"
    ![Right Click to Create](img/rightClickCreate.png)
    Or
    Switch from the "Summary" tab to the "External Links" tab and press "+ Click to Connect"
    ![External Link Click to Connect](img/ExternalLinkClickToConnect.png)

7. Select the Remote Broker you would like to link to:
    Provide broker URL, Admin Username and Admin Password (Note: This is not your cluster password but instead a broker Admin username and password).
    ![Solace Remote Broker](img/remoteBroker.png)
    Or Login with Solace Cloud by providing your Solace cloud Username and Password. You can also connect with a [Solace Cloud Token](https://docs.solace.com/Cloud/ght_api_tokens.htm)
    ![Solace Cloud Broker Login](img/SolaceCloudLogin.png)

8. Select Message VPNs to bridge:
    From the left side drop down menu select the desired Local Message VPN you wish to bridge.
    From the right side drop down menu select the desired Remote Message Service you would like to bridge.
    <br><aside class=“positive”> The term Message VPN and Service may appear seemingly interchangeably, the concept of message VPNs do not exist on our Cloud Brokers so instead we call the cloud brokers Services. </aside>
    ![Select Message VPNs](img/SelectVPNs.png)

9. Bypass Spool Size Warning (again):
    If you are using a Docker Solace Software Broker and you did not alter your spool size earlier you will have to bypass another spool size warning
    ![Again Spool Size Warning](img/againSpoolSizeWarning.png)

10. Configure connection parameters:
    Select if you would like the local broker or the remote broker to initiate the DMR link, you would select once side vs the other if there were inbound firewall rules between brokers. For example if the local broker was hosted in a company internet and the remote broker was hosted on the Solace Cloud.
    Also provide the Remote Cluster Password and Local Cluster Password. These passwords were set in step 3 when you defined cluster parameters for each broker. 
    Finally click "Create Link and Test Connection"
    ![Configure Connection Parameters](img/configureConnectionParameters.png)

11. Wait for Link and Test:
    The broker will now attempt to establish a link with the specified DMR Link mate.  Then once the connection is negotiated the brokers will run bi-directional communication tests.
    ![Wait for Link and Test](img/waitForLinkAndTest.png)

12. Successful DMR Link:
    After communication tests we will have a successful DMR Link.  
    <br> If you encounter an error please review a DMR troubleshooting steps to determine how to correct the error and build a successful DMR Link between brokers
    ![Successful DMR Link](img/successfulLink.png)

<aside class=“positive”>At this point if you would like to include more than 2 brokers in your Event Mesh repeat steps 6 to 12 for each additional broker you wish to include in the mesh.  <br>Note that events will not traverse N brokers to reach a desired broker so you have to form a direct DMR Link between each and every broker for form a full Event Mesh</aside>

### Conclusion
In the previous steps we have provisioned a cluster on each broker to prepare them to participate in an Event Mesh.  Then we created a DMR link between the brokers to form the Event Mesh.  Events will now be intelligently and Dynamically Routed from the Solace PubSub+ brokers where they are produced to the broker where there are interested subscribers. Continue to learn how we can explore the behavior of events over a DMR Link. 

## Exploration DMR with “Try Me” tab
Duration: 0:02:00

The Solace Try Me Tab is small CodePen application which was created to provide a simple way of publishing and subscribing to Solace topics and queues.  The application produces and consumes WebSocket (WS) events to Solace PubSub+ brokers over a network.  Thus is it not required that the Try Me tool be used to connect to a local broker, however the tooling is setup to make connecting to the "local" Solace Broker effortless. Using the Try Me tool you can explore the following Solace features:
* Publish Direct Messages
* Publish Persistent Messages
* Publish to topics
* Publish directly to queues
* Subscribe to Solace topics
* Subscribe to Solace queues
* Subscribe to Solace topics using Solace wild cards
* Experience Solace Broker translate different message protocols (requires the use of Try Me and an additional publisher or subscriber).

<br>

**In the next section we will explore how using the Try Me tool to Publish and Subscribe only to a single individual Solace Broker will allow us to obtain events from any accessible topic published to any of the Solace Brokers connected to our Solace DMR Event Mesh.** 


The Solace Try Me Tab is small CodePen application which was created to provide a simple way of publishing and subscribing to Solace topics and queues.  The application produces and consumes WebSocket (WS) events to Solace PubSub+ brokers over a network.  Thus is it not required that the Try Me tool be used to connect to a local broker, however the tooling is setup to make connecting to the "local" Solace Broker effortless. Using the Try Me tool you can explore the following Solace features:
* Publish Direct Messages
* Publish Persistent Messages
* Publish to topics
* Publish directly to queues
* Subscribe to Solace topics
* Subscribe to Solace queues
* Subscribe to Solace topics using Solace wild cards
* Experience Solace Broker translate different message protocols (requires the use of Try Me and an additional publisher or subscriber).

<br>

**In the next section we will explore how using the Try Me tool to Publish and Subscribe only to a single individual Solace Broker will allow us to obtain events from any accessible topic published to any of the Solace Brokers connected to our Solace DMR Event Mesh.** 
<br>🆘!!!Maybe here I should include some topic architecture for 2 brokers that will allow you to see the DMR Event Mesh in action?

## Setting up and running "Try Me"
Duration: 0:10:00

**Option A: For your local (on-premise) broker**

1. Navigate to your on-premise broker WebUI and Login
    
    ![onpremise broker webUI](img/Untitled.png)
    
2. Select the Message VPN you wish to use
    
    ![onpremise message vpn](img/Untitled_1.png)
    
3. Select“Try Me” tab on the left side bar menu inside of the WebUI
    
    ![onpremise try me](img/Untitled_2.png)
    
4. Populate with your on-premise broker details into the Publisher side, unless you are running the broker on your local machine you will likely have to change the “Broker URL”, “Client Username” and “Client Password”. You may also have to change the “Message VPN” depending on your setup. 
    
    ![onpremise publisher populate](img/Untitled_3.png)
    
5. Select the “Connect” button on the Publisher side of “Try Me”.
    
    ![onpremise publisher connect](img/Untitled_4.png)
    
6. Select the “Connect” button on the Subscriber side of “Try Me” as well.  The connection details will carry over from the Publisher side unless you expand the drop down menu, uncheck the “Same as Publisher” option and modify them.
    
    ![onpremise subscriber connect](img/Untitled_5.png)
    
7.  Now we can customize our Publish topic, Delivery Mode and Message Content and Publish messages directly to our local (on-premise) broker. 
    
    ![onpremise topics](img/Untitled_6.png)
    
8. We can also subscribe to any topics that we would like on the right side by changing the subscribe field and pressing “Subscribe”. The topic can be one that is published to our local broker or published to any other broker in the DMR (Event Mesh) that your user has access to.
Do not forget about our [Solace wild cards](https://docs.solace.com/Messaging/Wildcard-Charaters-Topic-Subs.htm) here 
<br>
    `* is a single level wild card: example/topic/with/a/*/wildcard`
<br>
    `> is a multi level wild card: example/topic/>`
   
    
    ![Untitled](img/Untitled_7.png)

**Option B: For your Solace Cloud Brokers**

1. Log into Solace Cloud
    
    ![cloud login](img/Untitled_8.png)
    
2. Select the Service you would like to test. Remember that the service must already be DMR linked to the other services you want to experiment with.
    
    ![cloud service select](img/Untitled_9.png)
    
3. Navigate to the “Try Me!” Tab along the top of the services web page
    
    ![cloud try me](img/Untitled_10.png)
    
4. On Solace Cloud the Service connection details should already be correctly populated and you can simply click “Connect” on the Publisher side.  However if that does not work you can select “show advanced settings” to manually configure “Broker URL” “Client Username” “Client Password” and “Message VPN”
    
    ![cloud publisher connect](img/Untitled_11.png)
    
5. On the Subscriber side you can also simply select “Connect”. However if that does not work you can select “show advanced settings” to manually configure “Broker URL” “Client Username” “Client Password” and “Message VPN”
    
    ![cloud subscriber connect](img/Untitled_12.png)
    
6. Now we will specify a unique publish topic on the Publisher side of the “Try Me!” tab and begin publishing events to our cloud broker
    
    ![cloud tryme topics](img/Untitled_13.png)
    
7. We can also subscribe to any topics that we would like on the right side by changing the subscribe field and pressing “Subscribe”. The topic can be one that is published to our local broker or published to any other broker in the DMR(Event Mesh) that your user has access to.
Do not forget about our [Solace wild](https://docs.solace.com/Messaging/Wildcard-Charaters-Topic-Subs.htm) cards here:
<br>
    `* is a single level wild card: sample/topic/with/a/*/wildcard`
<br>
    `> is a multi level wild card: sample/topic/>`

    
![cloud add subscriptions](img/Untitled_14.png)

    
<aside class=“positive”>💡 In this screen grab you can see that we are subscribed to a topic that is being published to a topic on a different Solace Broker which is in a DMR link (Event Mesh) with this broker. Thus requiring that DMR route the event from that other broker to this cloud broker when events are published.</aside> 

### Seeing Events flow across the DMR (Event Mesh):

Now that we have created publishers and subscribers via the “Try Me” tabs on our different DMR linked (Event Mesh) brokers we can start publishing events and watch them flow between brokers.  Experiment with “Try Me” subscriptions to only local topics, remote topics and combinations of both to get a better understanding of how Solace is Dynamically Routing messages between brokers.

## Exploration DMR with SDKPerf tool
Duration: 0:02:00

Obtain the SDKPerf Solace Performance testing tool from our downloads page here: [https://solace.com/downloads/](https://solace.com/downloads/) at the bottom of the page.  You can select from your desired flavor or the testing tool.  

![Solace SDKPerf Downlad](img/solaceSDKPerfDownload.png)

Check out general SDKPerf documentation here: [https://docs.solace.com/API/SDKPerf/SDKPerf.htm](https://docs.solace.com/API/SDKPerf/SDKPerf.htm)

And additional command line argument options here: [https://docs.solace.com/API/SDKPerf/Command-Line-Options.htm](https://docs.solace.com/API/SDKPerf/Command-Line-Options.htm)

<aside class=“positive”>💡 I will be using the Solace SDKPerf_java tool on a unix based system for this example.  All of the flavors behave similarly with different underlying protocols. </aside>

## Running SDKPerf
Duration: 0:10:00

Navigate to the unpacked directory of your recently downloaded SDKPerf tool in the terminal of your choice.  When you list the contents of the directory you should see some libraries and in the case of the java tool: `sdkperf_java.sh` and `sdkperf_java.bat`.  We will use these scripts to execute the tool. 

List of common SDKPerf flags

```
-cip= <- the ip address(host name) and port of the broker we wish to connect to 
-cu=  <- userid and message vpn we wish to connect as seperated by @
-cp=  <- password for the user we are connecting as
-ptl= <- publish topic list, the topics we want to publish to separeated by ,
-stl= <- list of topics we want to subscribe to separated by a ,
-mn=  <- integer for the number of messages we want to publish
-mr=  <- integer for the rate at which we want to publish or subscribe in msg/sec

```

### Create SDKPerf Publisher to Broker A on topic `sample/broker/a`

```
./sdkperf_java.sh -cip=localhost:55554 -cu=admin@default -cp=admin -ptl=sample/broker/a -mn=100 -mr=1
```

![sdkperf publisher](img/Untitled_15.png)

### Create SDKPerf Publisher to Broker B on topic `sample/broker/b`

```
./sdkperf_java.sh -cip=mr-6d275srp5ae.messaging.solace.cloud:55555 -cu=solace-cloud-client@jamiesontest -cp=vkkveu1ublk5ekl4mffh7uvmf -ptl=sample/broker/b -mn=100 -mr=1
```

![sdkperf publisher 2](img/Untitled_16.png)

### Create SDKPerf Subscriber to Broker A on topic `sample/broker/b`

```
./sdkperf_java.sh -cip=localhost:55554 -cu=admin@default -cp=admin -stl=sample/broker/b
```

![sdkperf subscriber](img/Untitled_17.png)

### Create SDKPerf Subscriber to Broker B on topic `sample/broker/a`

```
./sdkperf_java.sh -cip=mr-6d275srp5ae.messaging.solace.cloud:55555 -cu=solace-cloud-client@jamiesontest -cp=vkkveu1ublk5ekl4mffh7uvmf -stl=sample/broker/a
```

![sdkperf subscriber 2](img/Untitled_18.png)

## Conclusion
Duration: 0:02:00

✅ Setup a DMR link between two Solace Brokers   
✅ Publish and Subscribe to DMR enabled topics with Try Me   
✅ Publish and Subscribe to DMR enabled topics with SDKPerf    

We prepared Solace PubSub+ Event Brokers to participate in an Event Mesh by provisioning a cluster on each broker.  Then we connected those brokers together with DMR Links to create an Event Mesh.  After creating our Event Mesh we explored two different ways of easily publishing and subscribing to Solace topics.  Using these two methods and Solace Brokers that are connected into a DMR Event Mesh you can create a suite of publishers and subscribers on each broker in the Event Mesh.  By experimenting with the topics each subscriber SDKPerf tool or “Try Me” tool is advertising a subscription to you can see how events are dynamically routed between brokers that are DMR linked.  

As a final note you can also cause a broker in the DMR Event Mesh to have advertise a topic subscription by creating a queue on the broker and subscribing to a topic that is being published to a different broker in the DMR Event Mesh.  But keep in mind that the subscriptions in these queues will be a more static subscription so unless you delete the queue or its subscription the events will always be passed to that broker to be stored on the queue.

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
