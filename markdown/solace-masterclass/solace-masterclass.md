author: HariRangarajan-Solace
summary: This codelab describes the whole technical hands-on part of the Solace Masterclass session
id: solace-masterclass
tags: Solace-Masterclass, Java, Springboot
categories:
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/solace-masterclass

# Solace Masterclass

## What you'll learn: Overview

![Solace Masterclass](img/Solace-masterclass.jpeg)

This code lab contains the technical hands on section of the **Solace Masterclass : Implementing Event-Driven-Architectures**
The participants of this masterclass will be implementing this code lab in the Strigo virtual machine provided as a part of the masterclass session.
The Strigo virtual machine contains all the software packages required for implementing the hands on codelab. 

The agenda of the hands-on is as below :

* Use case introduction
* Event Portal design import
* Publish-Subscribe pattern flow
  * Generate AsyncAPI specification from Event Portal
  * Code generation using AsyncAPI code generator
  * Implement business code logic 
  * Implement version control, CI/CD workflow and Event Portal updates
  * Link applications to runtime environments and modelled event mesh (MEM)
* Request-Reply pattern flow
  * Generate AsyncAPI specification from Event Portal
  * Code generation using AsyncAPI code generator
  * Implement business code logic
  * Implement version control, CI/CD workflow and Event Portal updates
  * Link applications to runtime environments and modelled event mesh (MEM) 
* Boot up Confluent Kafka local broker and integrate with Solace cloud


## 1. Use case introduction
As a part of the event storming session earlier you would have discussed and brainstormed on few use cases. In this brain storming you have identified systems, events and processes involved in the flow(s) and also 
designed the topic taxonomy following Solace best practices and recommendations.

In the hands-on section of this masterclass, you can choose one of the below industry domains :

1. Retail
2. Banking

and follow it for implementing. Due to time limit considerations, we will be implementing only a selected subset of the whole design. 

## 2. Event Portal design

The Event Portal is a cloud-based tool that simplifies the design of your event-driven architecture (EDA). With the Event Portal, you can:
* Define and track relationships between applications in a highly decoupled EDA.
* Easily create and manage events using a user-friendly GUI.

In summary, the Event Portal streamlines event management, making it an essential part of your EDA toolkit.

### Step 1 : Import Postman objects
In the virtual machine box provided to you for this masterclass session, a Github repository has been checked out. 
- Navigate to the folder : <mark>**Solace-masterclass/Postman-collection**</mark> 
- Start Postman application
- Import the file with the name **Establish Environment for Event Portal.postman_collection.json** as a Postman collection as shown below
![postman-collection-import.png](img/postman-collection-import.png)
- Once imported, you should be able to see a Postman collection as below :
![collection-imported.png](img/collection-imported.png)
- Similarly, import the file with the name **Environment Definition.postman_environment.json** as a Postman environment as shown below
![Postman-environment-import.png](img/Postman-environment-import.png)
- Once imported, you should be able to see a Postman environment as below :
![environment-imported.png](img/environment-imported.png)

### Step 2 : Create Event Portal token
Follow the steps detailed in the link over here : [Creating an API Token](https://docs.solace.com/Cloud/ght_api_tokens.htm#Create)
Make sure that you enable the following permissions during the process :
- Event Portal 2.0
  - Designer  - Read and Write
  - Runtime Event Manager - Read and Write
  - API Management / Dev Portal - Read and Write
- Event Portal - Read and Write
- Environments - Read and Write
- Account Management - Read and Write

**Keep this token safe as it will not be available again**

### Step 3 : Import Event Portal design
- Open the Postman **environment** that you had imported earlier.
- Paste the token created earlier into the Current value column of the **api_key** variable.
- Change the value of the variable **epSampleDomain** to refer to the industry that you want to work with for the course of this hands-on excercise. You can choose any of the below values :
  - Retail Industry : `retail`
  - Banking industry : `acme-bank`
![ep-token-setup.png](img/ep-token-setup.png)
- Open the Postman **collection** that you had imported earlier.
- Choose the **Training Environment Definition** from the dropdown
- Click on the **Runs** tab and then **Run Collection** button as below : 
![collection-execution.png](img/collection-execution.png)
- Click on the **Run Establish Demo Environment** button on the right side without changing any of the scripts or order as below :
![run-collection.png](img/run-collection.png)
- Once the script has finished execution, switch over to the Solace Cloud Console and Open Event Portal. You should be able to see the objects from your selected industry as below : 
  - Retail industry : 
    ![retail-domain-ep.png](img/retail-domain-ep.png)
  - Banking industry :
    ![banking-industry.png](img/banking-industry.png)
    
- Explore the various EDA artefacts like schemas, events, applications, their relationships and dependencies.

## 3.a. Retail Industry : Publish-Subscribe pattern flow

### Generate AsyncAPI specification from Event Portal
### Code generation using AsyncAPI code generator
### Implement business code logic
### Implement version control, CI/CD workflow and Event Portal updates
### Link applications to runtime environments and modelled event mesh (MEM)
### Test with sample feed

## 3.b. Retail Industry :  Request-Reply pattern flow

### Generate AsyncAPI specification from Event Portal
### Code generation using AsyncAPI code generator
### Implement business code logic
### Implement version control, CI/CD workflow and Event Portal updates
### Link applications to runtime environments and modelled event mesh (MEM)
### Test with sample feed

## 4.a. Banking Industry : Publish-Subscribe pattern flow

### Generate AsyncAPI specification from Event Portal
### Code generation using AsyncAPI code generator
### Implement business code logic
### Implement version control, CI/CD workflow and Event Portal updates
### Link applications to runtime environments and modelled event mesh (MEM)
### Test with sample feed

## 4.b. Banking Industry :  Request-Reply pattern flow

### Generate AsyncAPI specification from Event Portal
### Code generation using AsyncAPI code generator
### Implement business code logic
### Implement version control, CI/CD workflow and Event Portal updates
### Link applications to runtime environments and modelled event mesh (MEM)
### Test with sample feed

## 5. Solace and Kafka integration

## 6. Takeaways and benefits

![Soly Image Caption](img/soly.gif)

Thanks for participating in this code lab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
