author: Aaron Lee
summary: Learn how to configure a Solace PubSub+ broker to accept any incoming REST requests, and convert them into event-driven pub/sub messages
id: solace-event-enable-rest
tags: patterns,howto
categories: REST,Solace,Java
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/solace-event-enable-rest/solace-event-enable-rest.md
analytics account: UA-3921398-10


# How to Event-Enable your REST Architecture with Solace PubSub+


## Introduction
Duration: 0:02:00

#### > Do you use **REST-over-HTTP** (`GET`, `POST`, etc.) for application communication??  Read on!

In traditional microservice applications, the primary form of communication is often REST-over-HTTP.  However, this can be limiting as:

 - REST archictecture is client-to-server (not bidirectional)
 - REST-over-HTTP is point-to-point (only one URL destination)
 - HTTP is a synchronous/blocking protocol (waiting for 200 OK)

Modern applications are embracing **publish-subscribe** communication as a way to enable **event-driven** architectures.

 - But how to migrate?
 - How to integrate?
 - Is it possible to combine both traditional REST interaction with efficient pub/sub communication??

Positive
: **YES IT IS**, using the **Solace PubSub+ Event Broker!**

### What you'll build

![asdf](gfx/build.png)


### What you'll learn
- How to configure the Solace PubSub+ broker to accept incoming REST requests
- How to configure the Solace broker to pass incoming REST requests straight though, similar to a proxy, using a Rest Delivery Point (RDP)
- How to utilize the publish-subscribe pattern to allow easy access to multiple copies of the same data
- How to build a Solace messaging application to consume and respond to incoming REST requests











## Prerequisites & Assumptions
Duration: 0:02:00

- It is assumed you have a basic understanding of what a Solace PubSub+ event broker is, and what it does.
- You have access (and _admin_ access) to a Solace PubSub+ broker. This can either be a hardware appliance, the software broker, or a Solace Cloud service instance.  (See below)
- cURL, Postman, or other REST utility that will allow the injection of REST-over-HTTP requests.
- (optional) A REST-enabled webserver, web application, or microservice that can accept incoming REST (GET, POST, etc.) requests, and generate a response. If not, the tuorial will use an available [Postman test server](https://postman-echo.com).
- (optional) The Solace Java (JCSMP), JavaScript, C#, JMS, or other messaging API, which can be found at either [solace.com/downloads](https://solace.com/downloads) or [github.com/solacesamples](https://github.com/solacesamples).

Negative
: **Note:** this tutorial assumes that you are using the `default` Message VPN on the software broker. If not (e.g. hardware appliance, Solace Cloud, or just a different VPN), ensure you substitute the proper VPN name, username, etc. as you progress through this tutorial.

### Free Solace Access!

 - [Sign up for a free Solace Cloud service (50 connections)](https://console.solace.cloud/login/new-account)
 - [Download the free feature-complete Standard Edition software broker](https://solace.com/downloads/)
 - [Quickstart Video for Solace PubSub+ Docker container](https://youtu.be/s2n5V-IXCaM)











## Overview of Sections: A, B, and C
Duration: 0:02:00

This tutorial will walk though a number of steps to configure the Solace PubSub+ broker to be used in REST Gateway mode, as well as code examples using the Solace JCSMP (or other) API for building a request-reply backend messaging application.

### Starting Configuration

 - In the beginning, you have a client making a REST reqeust to a backend REST server. (We'll use a free one if you don't have one available).
![asdf](gfx/flow_01.png)

### Part A

 - First, we configure and test the Solace PubSub+ broker to ensure it is receiving REST requests. Solace will convert the incoming requests to messages for testing.
![asdf](gfx/flow_02.png)

### Part B

 - Next, configure all the necessary "outbound" REST components in the Solace broker to allow the REST request to reach the backend REST API, and respond.  This allows Solace to essentially be a REST proxy.
![asdf](gfx/flow_03.png)

### Part C

 - Finally, configure a "sniffer" messaging application to listen to the REST request/reply flow through Solace broker, using the publish-subscribe pattern. Could be very useful for logging, diagnostics, or audit.
![asdf](gfx/flow_04.png)

 - Configure a messaging application to replace/extend/complement the backend REST server,  allowing a REST-to-pub/sub conversion within the Solace broker.
![asdf](gfx/flow_05.png)













## Three Options for Config Management
Duration: 0:03:00

You can (generally) configure the Solace PubSub+ broker using three different methods; this section provides a very brief outline of those.

Each section of this CodeLab that performs a configuration step on the Solace broker will include all three options.

Negative
: **Note:** do _not_ perform all 3 configuration options, just choose 1 for each section.

For any configuration management, you will need a username/password with either admin or read/write level privileges.                                                                                                                      

### PubSub+ Manager GUI

The PubSub+ Manager for Solace brokers is a web GUI, usually accessed on port 8080 on the software broker, port 80 of the management plane of the hardware appliance, or via the Solace Cloud console and clicking on "Manage Service" in the top right. (It is a replacement for SolAdmin, if you know that that is).

Positive
: **Tip:** throughout the PubSub+ Manager, by clicking on any configuration item or attribute, a "Tip" will show on the right-hand side of the screen describing the object. Built-in help!

![alt-text-here](gfx/tips.png)


### SEMP Management API

All of the commands and capabilities within the PubSub+ Manager can also be accomplished programmatically via the RESTful **Solace Element Management Protocol** (SEMP) API. For more information on the SEMP API, please consult the following links:

 - [SEMPv2 Swagger Reference Documentation](https://docs.solace.com/API-Developer-Online-Ref-Documentation/swagger-ui/config/index.html)
 - [SEMP User Guide](https://docs.solace.com/SEMP/Using-SEMP.htm)


### Command Line Interface (CLI)

The Solace **Command Line Interface** (CLI) can be reached by one of the following methods (as appropriate):

- Software broker, SSH to port 2222, and login with the admin username/password
- Software broker running as Docker container: `sudo docker exec -it <container-name> cli`
- Software broker running as machine image: login to the machine image, then: `solacectl cli`
- Hardware appliance: login to port 22 of the management VRF

Note that `show` commands can be run anywhere in CLI, from any "level".  But configuration commands must be executed in a specific order.

I've also included a lot of double-quotes `"` in the CLI commands for completeness... but you almost never need to use them. FYI. (Just never put a space in any object name!!)

 - [Solace CLI Reference Documentation](https://docs.solace.com/Solace-CLI/Using-Solace-CLI.htm)
 - [Get Started with CLI (blog)](https://solace.com/blog/getting-started-solos-cli/)












## Part A - Objective
Duration: 0:00:00

#### Recall:

 - First we configure and test the Solace PubSub+ broker to ensure it is receiving REST requests. Solace will convert the incoming requests to messages for testing.

![asdf](gfx/flow_02.png)













## [A] Verify/Assign REST Port
Duration: 0:03:00

In this first section, we will verify what port has been configured (if any) to allow incoming REST requests to your particular Message VPN. If using the `default` Message VPN on the software broker, this section can be skipped.

Negative
: **Note:** if creating a new Message VPN, you must configure a new/different port than one used by the `default` Message VPN, 9000. Each VPN needs different ports for REST connectivity.

Negative
: **Note:** if using **Docker** for Windows, Docker for Mac, or using `bridge` networking mode with Docker on Linux, the new port must be added to the container's list of published ports (`-p <new-port>`) when the container is first instantiated (i.e. new ports are not automatically exposed).



### PubSub+ Manager

Login to the PubSub+ GUI Manager, then select your Message VPN:
![alt-text-here](gfx/port_mgr1.png)

Select "Services" from the Message VPN's menu items:
![alt-text-here](gfx/port_mgr2.png)

Scroll down to the section on REST and verify the port is configured and enabled:
![alt-text-here](gfx/port_mgr3.png)


### SEMP

To view the incoming REST port, perform the following (replace `default` with your Message VPN name, and user credentials as appropriate):

```
curl -u admin:admin http://localhost:8080/SEMP/v2/config/msgVpns/default?select=serviceRest*
```

And the response should look something like:

```
{
    "data":{
        "serviceRestIncomingMaxConnectionCount":100,
        "serviceRestIncomingPlainTextEnabled":true,        <----
        "serviceRestIncomingPlainTextListenPort":9000,     <----
        "serviceRestIncomingTlsEnabled":true,
        "serviceRestIncomingTlsListenPort":9443
        "serviceRestMode":"messaging",
        "serviceRestOutgoingMaxConnectionCount":100
    },
    "links":{},
    "meta":{
        "request":{
            "method":"GET",
            "uri":"http://localhost:8080/SEMP/v2/config/msgVpns/default?select=serviceRestIncoming*"
        },
        "responseCode":200
    }
}
```

To configure the incoming port and enable it using SEMP, perform the following 2 commands. First, shutdown the port:

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default \
  -X PATCH \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "serviceRestIncomingPlainTextEnabled": false }'
```

Then change the port number and re-enable it:

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default \
  -X PATCH \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "serviceRestIncomingPlainTextListenPort": 9001,
        "serviceRestIncomingPlainTextEnabled": true }'
```


### CLI

Perform the following `show` command in CLI.  Look for the line with `REST` and an `N` in the S(ecure) column for the port to use.  If the broker has a server certificate installed, you may use port in the line below (9443 in this case).

Note that `solace>` is simply the prompt, ignore that.  
```
solace> show message-vpn default service

// snip //
Service TP  S C VRF    Port A O Failed Reason
------- --- --- ----- ----- --- ------------------------------
SMF     TCP N N MsgBB 55555 U U
SMF     TCP N Y MsgBB 55003 U U
SMF     TCP Y N MsgBB 55443 U D No Cert
REST    WEB N - MsgBB  9000 U U              <----
REST    WEB Y - MsgBB  9443 U D No Cert
SMF     WEB N - MsgBB    80 U U
SMF     WEB Y - MsgBB   443 U D No Cert
MQTT    TCP N - MsgBB  1883 U U
MQTT    TCP Y - MsgBB  8883 U D No Cert
// snip //
```

To configure a different port (e.g. if you are using a different Message VPN) and enable it, enter the following CLI commands in this exact order:

```
home
enable
  config
    message-vpn "default"
      service rest
        incoming
          plain-text shutdown
          listen-port 9001
          no plain-text shutdown
          exit
```


### Solace Cloud

If using Solace Cloud, from within the console for your Solace Cloud instance, select "Connect":
![alt-text-here](gfx/port_sc1.png)                                                                                                                                

Scroll down to the section on REST and verify the username, password, port, and URL:
![alt-text-here](gfx/port_sc2.png)













## [A] Enable REST (Micro)Gateway Mode
Duration: 0:03:00

In this section, we will switch the REST mode for our Message VPN from _Messaging_ (the default) to _Gateway_. Microgateways allow Solace PubSub+ event brokers to act as HTTP load balancers, or simple API gateways between RESTful API clients and RESTful API service providers. Learn more about Microgateways [here](https://docs.solace.com/Overviews/Microgateway-Concepts/Microgateways-Overview.htm)


### PubSub+ Manager

Inside the "Services" menu of the Message VPN, either click "Edit" in the top-right, or double-click the Service Mode:
![alt-text-here](gfx/rest_mode_mgr1.png)

Select _Gateway_ from the drop-down list, and click "Apply":
![alt-text-here](gfx/rest_mode_mgr2.png)


### SEMP

Change to `gateway` with just one command:

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default \
  -X PATCH \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "serviceRestMode": "gateway" }'
```

To verify, use the previous GET command:
```
curl -u admin:admin http://localhost:8080/SEMP/v2/config/msgVpns/default?select=serviceRest*
```

```
{
    "data":{
        "serviceRestIncomingMaxConnectionCount":100,
        "serviceRestIncomingPlainTextEnabled":true,
        "serviceRestIncomingPlainTextListenPort":9000,
        "serviceRestIncomingTlsEnabled":true,
        "serviceRestIncomingTlsListenPort":9443,
        "serviceRestMode":"gateway",                       <----
        "serviceRestOutgoingMaxConnectionCount":100
    },
    "links":{},
    "meta":{
        "request":{
            "method":"GET",
            "uri":"http://localhost:8080/SEMP/v2/config/msgVpns/default?select=serviceRest*"
        },
        "responseCode":200
    }
```


### CLI

Set the Message VPN into REST `gateway` mode with the following CLI commands. If continuing from the previous CLI command and are still at the `rest` level, simply enter the last line.

```
home
enable
  config
    message-vpn "default"
      service rest
        mode gateway
```

```
solace> show message-vpn default

Message VPN:                         default
Configuration Status:                Enabled
Local Status:                        Up
Distributed Cache Management:        Enabled
SSL to plain text downgrade allowed: No
REST mode:                           Gateway     <----
Total Local Unique Subscriptions:    9
// snip //
```













## [A] Test REST Connectivity
Duration: 0:06:00

Now that the Message VPN on the Solace broker has been configured for REST Gateway mode, let's verify that REST requests are reaching the broker.


### Inject a REST Request

Using cURL, Postman, or another REST program, inject a REST `GET` request to the broker on the correct port, using any path you'd like.

Negative
: **Note:** the following is not a "management" command, and therefore the **username**, **password**, and **port** are different than the SEMP commands seen thus far. This would be a _client username_ that you create for the Message VPN.
 
For example:
```
curl -u default:default http://localhost:9000/test -v
```

And you should see a response similar to the following:

```
<solace-error-response>
<code>404</code>
<reason><![CDATA[No Subscription Match]]></reason>
<detail><![CDATA[
No subscription matching topic "GET/test"           <----
]]></detail>
<internal-use>1:7633</internal-use>
</solace-error-response>
```

Which means that it is reaching the broker, however there is nowhere to route this incoming request as there are no listeners currently configured.

Positive
: **Recall:** in `gateway` mode, incoming REST requests are "pre-pended" with the REST VERB.  So a GET request for path `test` becomes a Solace message with topic `GET/test`


### Consuming the Incoming REST Request

As a test, to simply receive the incoming REST request, let's use the "Try Me!" test app built into the PubSub+ Manager:


Click on "Try Me!" on the left-hand menu:
![alt-text-here](gfx/tryme_mgr1.png)

Click on "Connect" for the Subscriber on the right:
![alt-text-here](gfx/tryme_mgr2.png)

Enter the subscription `GET/>` into the text field, and click "Subscribe".  Recall: the `>` wildcard in Solace is a multi-level wildcard. This subscription will receive anything that is a "GET" request.
![alt-text-here](gfx/tryme_mgr3.png)

Resubmit the REST request from before, and it should pop up as a message on the Subscriber's received messages:
![alt-text-here](gfx/tryme_mgr4.png)

Positive
: Hooray!!


### How about POST requests?

In the Subscriber application's subscription text field, try entering `POST/>` as a subscription.  Then, submit a different REST request to see how it appears:

```
curl -u default:default -X POST http://localhost:9000/hello/world -d '{"body":"hello world!!","status":"great"}' -v
```
![alt-text-here](gfx/tryme_mgr5.png)

Positive
: Awesome!!














## Part B - Objective
Duration: 0:00:00

#### Recall:


 - Next, configure all the necessary "outbound" REST components in the Solace broker to allow the REST request to reach the backend REST API, and respond.  This allows Solace to essentially be a REST proxy.

![asdf](gfx/flow_03.png)














## [B] Prepare for Outbound REST Pass-Through                                                                                                                                                                          
Duration: 0:03:00

For the Solace broker to act as a "pass-through" for REST requests in MicroGateway mode, we need to configure some additional "outbound" components on the broker.

- **A REST Delivery Point (RDP):** this is the "parent" object which contains all the necessary configuration for sending outbound REST requests from the Solace broker
- **A persistent Queue:** each RDP is bound to one or more queues from which it receives messages 
- **A REST Consumer:** this defines where/how the outbound request will be sent, essentially the destination 

The remainder of this tutorial will use a Postman API test server to generate a response to a HTTP GET request. If you have another API endpoint available to you that you'd like to use, please feel free.


### Test Server Details

 - **Host:** postman-echo.com
 - **Port:** 80
 - **Authentication:** none

[Postman Echo Documentation](https://docs.postman-echo.com/?version=latest)

We will use the GET API to receive a response. The response will consist of some JSON, including any parameters that are passed with the URL.  E.g.:

```
curl 'http://postman-echo.com:80/get?hello=world&solace=cool'
```

Should result in the following response (pretty-printed for visibility):

```
{
  "args": {
    "hello": "world"
    "solace": "cool",
  },
  "headers": {
    "x-forwarded-proto": "https",
    "host": "postman-echo.com",
    "accept": "*/*",
    "user-agent": "curl/7.58.0",
    "x-forwarded-port": "80"
  },
  "url":"https://postman-echo.com/get?hello=world&solace=cool"
}
```










## [B] Create a New Queue 
Duration: 0:04:00

When sending an outbound REST request, we need to configure a **Queue** to (temporarily) store the message before it gets sent out from the RDP.

Negative
: **Note:** if creating a _new_ Message VPN, remember that the VPN's `max-spool-quota` size defaults to **0MB**. So when creating a new Message VPN, you must also increase the spool quota for your new VPN.


### PubSub+ Manager

Click on "Queues" on the left-hand menu:
![alt-text-here](gfx/q_mgr1.png)

Click on "+ Queue" in the top-right to create a new queue:
![alt-text-here](gfx/q_mgr2.png)

Enter a name for your new queue. E.g. `q_rest_get`.  Click "Create":
![alt-text-here](gfx/q_mgr3.png)

Adjust any of the default attributes if you wish (e.g. message quota / queue size), although probably unnecessary.  Click "Apply":
![alt-text-here](gfx/q_mgr4.png)

Click on the newly created queue to view it:
![alt-text-here](gfx/q_mgr5.png)

Click on "Subscriptions":
![alt-text-here](gfx/q_mgr6.png)

Click on "+ Subscription" in the top-right to add a new subscription(s):
![alt-text-here](gfx/q_mgr7.png)

Add the subscription `GET/>` for the queue to attract _any_ HTTP GET requests to the queue. Click "Create":
![alt-text-here](gfx/q_mgr8.png)

Negative
: **Note:** if you'd like to use another HTTP verb -- e.g. HTTP POST -- then enter a different/another subscription here: e.g. `POST/>` or restrict it to just the path you want: `GET/query`)

You can read more about Wilecard Topic Subscriptions [here](https://docs.solace.com/PubSub-Basics/Wildcard-Charaters-Topic-Subs.htm)


### SEMP

Create a new queue:

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default/queues \
  -X POST \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "queueName": "q_rest_get",
        "accessType": "exclusive",
        "maxMsgSpoolUsage": 100,
        "permission": "consume",
        "ingressEnabled": true,
        "egressEnabled": true }'
```

Add a subscription to it:

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default/queues/q_rest_get/subscriptions \
  -X POST \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "subscriptionTopic": "GET/>" }'
```


### CLI

```
home
enable
  config
    message-spool message-vpn "default"
      create queue "q_rest_get"
      access-type exclusive
      permission all consume
      max-spool-usage 100
      subscription topic "GET/>"
      no shutdown
      exit
    end

show queue q_rest_get detail
```












## [B] Create a REST Delivery Point (RDP)
Duration: 0:05:00

Next, we need to create a new **Rest Delivery Point** (RDP) and bind it to the new queue.


### PubSub+ Manager

Click on "Client Connections" on the left-hand menu:
![alt-text-here](gfx/rdp_01.png)

Click on "REST" in the top menu:
![alt-text-here](gfx/rdp_02.png)

Click on "+ REST Delivery Point" in the top-right to create a new RDP:
![alt-text-here](gfx/rdp_03.png)

Enter a name for your new RDP. E.g. `rdp_get`.  Click "Create":
![alt-text-here](gfx/rdp_04.png)

**Enable** the RDP. Click "Apply":
![alt-text-here](gfx/rdp_05.png)

Click on the new RDP to view it:
![alt-text-here](gfx/rdp_06.png)

Click on "Queue Bindings" in the top menu:
![alt-text-here](gfx/rdp_07.png)

Click on "+ Queue Binding" in the top-right to create a new binding:
![alt-text-here](gfx/rdp_08.png)

Enter the name of your new queue to bind to this RDP, E.g. `q_rdp_get`. Click "Create":
![alt-text-here](gfx/rdp_09.png)

Click "Apply":
![alt-text-here](gfx/rdp_10.png)



### SEMP

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default/restDeliveryPoints \
  -X POST \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "restDeliveryPointName": "rdp_get",
        "enabled": true}'

```

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default/restDeliveryPoints/rdp_get/queueBindings \
  -X POST \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "queueBindingName": "q_rest_get" }'
```

### CLI


```
home
enable
  config
    message-vpn "default"
      rest
        create rest-delivery-point "rdp_get"
          create queue-binding "q_rest_get"
          exit
        no shut

show message-vpn default rest rest-delivery-point * detail
```










## [B] Configure a REST Consumer                                                                                                                                                                                       
Duration: 0:05:00

The final configuration step on the Solace broker to allow the REST request to pass-through is the **REST Consumer**.  This is where the destination server/host is specified.  

Negative
: **Note:** if you want to point the REST Consumer to a different REST API endpoint than the example `postman-echo.com`, you will amend some configuration settings in this section (e.g. authentication: basic, username/password).


### PubSub+ Manager                                                                                                                                                                                                

From within the newly created RDP, click on "REST Consumers" in the top menu:
![alt-text-here](gfx/rc_01.png)

Click on "+ REST Consumer" in the top-right to create a new consumer:
![alt-text-here](gfx/rc_02.png)

Enter a name for your new consumer. E.g. `rc_get`.  Click "Create":
![alt-text-here](gfx/rc_03.png)

Enable the REST Consumer, and add the remote **host**, **port**, and any authentication required by the downstream REST server. In this example, the host is `postman-echo.com` and the port is `80`. Toggle the enable option and click "Apply"
![alt-text-here](gfx/rc_04.png)

Refresh the screen, and ensure the REST Consumer reports an Operational State of **Up**:
![alt-text-here](gfx/rc_05.png)                                                                                                                                                                                                             


### SEMP

One single SEMP API command will create and configure the REST Consumer:

```
curl http://localhost:8080/SEMP/v2/config/msgVpns/default/restDeliveryPoints/rdp_get/restConsumers \
  -X POST \
  -u admin:admin \
  -H "Content-type:application/json" \
  -d '{ "restConsumerName": "rc_get",
        "authenticationScheme": "none",
        "remoteHost": "postman-echo.com",
        "remotePort": 80,
        "tlsEnabled": false,
        "enabled": true }'


```

Make sure that it is reporting a good state, using the Monitor SEMP API:

```
curl -u admin:admin http://localhost:8080/SEMP/v2/monitor/msgVpns/default/restDeliveryPoints/rdp_get/restConsumers
```

```
{
    "data":[
        {
            "authenticationHttpBasicUsername":"",
// snip //
            "restConsumerName":"rc_get",
            "restDeliveryPointName":"rdp_get",
            "retryDelay":3,
            "tlsCipherSuiteList":"default",
            "tlsEnabled":false,
            "up":true                 <----
        }
    ],
// snip //
```


### CLI

If continuing from the preious CLI command, and are still inside the `rest-delivery-point` level, start at line 7.

```
home
enable
  config
    message-vpn "default"
      rest
        rest-delivery-point "rdp_get"
          create rest-consumer "rc_get"
            authentication auth-scheme none
            remote host "postman-echo.com"
            remote port 80
            no shut
```

You should now see something that looks like:

```
solace> show message-vpn default rest rest-consumer * detail

REST Consumer Name:                  rc_get
REST Delivery Point:                 rdp_get
Message VPN:                         default
Admin State:                         Enabled       <----
Operational State:                   Up            <----

Last Failure:
  Reason:                            Shutdown
  Time:                              Jan 30 2020 09:27:20 UTC
Last Conn Failure:
  Local Endpoint:                    N/A
  Remote Endpoint:                   N/A
  Reason:                            Unknown Connect Event
  Time:                              Jan 30 2020 09:24:49 UTC
Local:
  Interface:
Remote:
  Host:                              postman-echo.com
  Port:                              80
  SSL:                               No
  Outgoing Connections (up):         3       <----
  Outgoing Connections (configured): 3       <----
```

Positive
: Yay!











## [B] Test one more time!
Duration: 0:03:00

Now that the configuration is done, let us test using _almost_ the same cURL command from before, except replacing the `postman-echo.com` host and port with the Solace broker's REST port, and adding client username & password as required:

```
curl -u default:default 'http://localhost:9000/get?hello=world&solace=cool'
```
And the output should look like:
```
{
  "args": {
    "hello": "world",
    "solace": "cool"
  },
  "headers": {
    "x-forwarded-proto": "https",
    "host": "postman-echo.com",
    "accept": "*/*",
    "solace-delivery-mode": "Non-Persistent",
    "solace-message-id": "ID:Solace-b7603db440727f09",
    "solace-reply-wait-time-in-ms": "FOREVER",
    "solace-time-to-live-in-ms": "30000",
    "user-agent": "curl/7.58.0",
    "x-forwarded-port": "80"
  },
  "url": "https://postman-echo.com/get?hello=world&solace=cool"
}
```
Note the additional headers.  But the original requesting client (cURL in this case) is unaffected.














## Part C - Objective
Duration: 0:00:00

#### Recall:

 - Finally, configure a "sniffer" messaging application to listen to the REST request/reply flow through Solace broker, using the publish-subscribe pattern. Could be very useful for logging, diagnostics, or audit.

![asdf](gfx/flow_04.png)


 - Configure a messaging application to replace/extend/complement the backend REST server,  allowing a REST-to-pub/sub conversion within the Solace broker.

![asdf](gfx/flow_05.png)












## [C] Configuring a "Sniffer" App
Duration: 0:04:00

Just like we did on the last step of Section A, use the **Try Me!** functionality of the PubSub+ Manager to "snoop" or "sniff" the messages going through Solace:

Enter the subscriptions `GET/>` and `#P2P/*/#rest*/>` into the subscription text field. The 2nd subscription will receive all point-to-point replies for REST requests.
![alt-text-here](gfx/proxy_tryme1.png)

Re-run the same cURL command from the previous section:

```
curl -u default:default 'http://localhost:9000/get?hello=world&solace=cool'
```

Verify cURL still receives a response, but note that you can **also** see the request and reply in the Subscriber window:
![alt-text-here](gfx/proxy_tryme2.png)

Positive
: Similarly, you could configure a Java, C, JavaScript, C#, etc. client application using Solace APIs to receive the exact same messages by subscribing to the exact same topics.

This shows that you can have an application passively receive **a copy of all REST request-reply traffic** as it moves through the broker, **without impacting the original actors**. This functionality could be very useful for logging, diagnostics, or audit.














## [C] Building a Replier Messaging App
Duration: 0:15:00

### (AKA Who Needs a REST Server??)

Now that we have verified that the REST MicroGateway feature is passing through the various REST requests, let's take a look at some sample/example code to generate a response using a messaging topic consumer.

The following section assumes you are using the Solace Java JCSMP API, which is availalbe at our [Samples GitHub repo](https://github.com/SolaceSamples/solace-samples-java). However, the modifications and concepts apply to other Solace APIs and other messaging APIs (JMS, C, C#, JavaScript, etc.).  Other APIs are available on https://github.com/solacesamples/

Positive
: For a video guide on how to download, setup, run, and configure the Solace Java Samples, check out these videos: [Solace Java Samples Part 1](https://www.youtube.com/watch?v=eTcmeLzkFN8&list=PLY1Ks8JEfJR5H6LMgs6EJ_SYcDf3IZsjd&index=5) and [Solace Java Samples Part 2](https://www.youtube.com/watch?v=14yUT5pdyBk&list=PLY1Ks8JEfJR5H6LMgs6EJ_SYcDf3IZsjd&index=4)


### Shutdown the RDP

Negative
: Using PubSub+ Manager, CLI, or SEMP: shutdown or disable the RDP to prevent parallel flows from occuring.


### Make a Replier App

Take a look at the [Basic Replier (source code)](https://github.com/SolaceSamples/solace-samples-java/blob/master/src/main/java/com/solace/samples/BasicReplier.java) sample application.  We are going to modify it slightly.

1. Change the topic subscription from `tutorial/requests` to `GET/>`, approximately line 50. (Could be any REST verb, using wildcards or not)
1. Inside the `onReceive()` callback method (approximately line 75), replace the line `reply.setText(text);` with the following, for something more interesting/dynamic:

```
    try {
        reply.setText("Your path was: "+request.getProperties().getString("JMS_Solace_HTTP_target_path_query_verbatim"));
    } catch (Exception e) {
        reply.setText(text);
    }
```

1. Just after the new `try { }` block, before the reply message is sent as a response to the request, add the following lines:

```
System.out.println(request.dump());  // prints the request message to the console
reply.setApplicationMessageId(request.getApplicationMessageId());  // needed for correlation
```

1. Run the application, and pass in the required arguments: `hostname username@vpn-name [password]`.  E.g.:

```
BasicReplier localhost default@default
```

1. Resubmit the original REST GET request, and you should see following printed to the console of the BasicReplier app:

```
BasicReplier initializing...
Jan 27, 2020 6:22:00 PM com.solacesystems.jcsmp.protocol.impl.TcpClientChannel call
INFO: Connecting to host 'orig=localhost, host=localhost' (host 1 of 1, smfclient 2, attempt 1 of 1, this_host_attempt: 1 of 1)
Jan 27, 2020 6:22:01 PM com.solacesystems.jcsmp.protocol.impl.TcpClientChannel call
INFO: Connected to host 'orig=localhost, host=localhost' (smfclient 2)
Listening for request messages on topic GET/> ... Press enter to exit

Received request, generating response
Destination:                            Topic 'GET/get'
AppMessageID:                           ID:Solace-d2dc2510dbfe295a
Priority:                               0
Class Of Service:                       USER_COS_1
DeliveryMode:                           DIRECT
Message Id:                             7
ReplyTo:                                Topic '#P2P/v:aa-local-broke/#rest-e135cb328ef67649/GET/get'
TimeToLive:                             30000
User Property Map:                      4 entries
      Key 'JMS_Solace_HTTP_field_Accept' (String): */*
      Key 'JMS_Solace_HTTP_field_User-Agent' (String): curl/7.58.0
      Key 'JMS_Solace_HTTP_method' (String): GET
      Key 'JMS_Solace_HTTP_target_path_query_verbatim' (String): get?hello=world&solace=cool
```

1. And at the end of the cURL console, you should see the returned payload of "Sample response":

```
> curl -u default:default http://localhost:9000/test -v
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 9000 (#0)
* Server auth using Basic with user 'default'
> GET /test HTTP/1.1
> Host: localhost:9000
> Authorization: Basic ZGVmYXVsdDpkZWZhdWx0
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Length: 15
< Solace-Client-Name: #rest-55e4631320167e61
< Solace-Message-ID: ID:Solace-bf11a8964cec2d0e
<
* Connection #0 to host localhost left intact
Your path was: get?hello=world&solace=cool              <----
```

Positive
: Success!!


### HTTP Response Codes

1. For more advanced HTTP response codes, add the following to the sample code, just before the reply message is sent:

```
 SDTMap props = JCSMPFactory.onlyInstance().createMap();
 try {
        props.putShort("JMS_Solace_HTTP_status_code",(short)403);
        props.putString("JMS_Solace_HTTP_reason_phrase","declined");
 } catch (SDTException e) {
        // won't happen here
        e.printStackTrace();
 }
 reply.setProperties(props);
```

1. Restart the Basic Replier, resubmit the REST GET request, and you should see something that looks the following:

```
$ curl -u default:default http://localhost:9000/test -v
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 9000 (#0)
* Server auth using Basic with user 'default'
> GET /test HTTP/1.1
> Host: localhost:9000
> Authorization: Basic ZGVmYXVsdDpkZWZhdWx0
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 403 declined                               <----
< Content-Length: 15
< Solace-Client-Name: #rest-e135cb328ef67649
< Solace-Message-ID: ID:Solace-d2dc2510dbfe295a
<
* Connection #0 to host localhost left intact
Your path was: get?hello=world&solace=cool
```

Positive
: Great Success!!



### Shared Subscriptions

One very useful feature of Solace for this type backend service is **Shared Subscriptions**.  It allows multiple applications to all subscribe to the same subscription _group_, and the Solace broker will round-robin deliver the incoming request/message to only one of the consumers within the group.  




## Conclusion, Discussion, Best Practices, Links

Thanks for making it this far! :-D

### What we've covered

 - Configured the Solace broker to act as a REST proxy
 - Snooped the messages as they have gone through Solace
 - Built a messaging application to replace/extend/complement the functionality of the REST endpoint

### Some Thoughts

 - RDPs can be bound to more than one queue.
 - Good practice to have different types of requests (e.g. GET, POST) go to different queues... then they can be serviced differently by more/less consumer threads/connections for differing levels of service.
 - Create a 2nd queue, RDP, and REST Conusmer to have two copies of the REST request getting sent out. Cheap/lazy/easy way for added redundancy.
 - The replacement messging application can either use Direct messaging (like it did in this tutorial), or Guaranteed messaging by using a queue.
 - The [Shared Subscriptions feature](https://docs.solace.com/PubSub-Basics/Direct-Messages.htm#Shared) might be useful for application redundancy / load-balancing, if using Direct messaging.

### Useful Links

[Solace REST Message Encoding](https://docs.solace.com/RESTMessagingPrtl/Solace-REST-Message-Encoding.htm#_Ref393979969)

[Solace REST Component Map](https://docs.solace.com/PubSub-ConceptMaps/Component-Maps.htm#REST2)

[All about Solace Wildcards](https://docs.solace.com/PubSub-Basics/Wildcard-Charaters-Topic-Subs.htm)

[Solace REST Multi-Protocol Integration](https://docs.solace.com/Overviews/REST-Messaging-Concepts/Multi-Protocol-Integration.htm)

[Solace REST Message Correlation](https://docs.solace.com/RESTMessagingPrtl/Solace-REST-Message-Encoding.htm#2.2.6.1)


#### Thanks!

Thanks for reading my tutorial!  Aaron@Solace
