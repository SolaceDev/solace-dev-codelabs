author: Supreet Mann
summary: This codelab will walk you through getting started with the Solace Schema Registry and the Solace SERDES Collection using the Solace Messaging API for Java (JCSMP) or with REST messaging.
id: schema-registry
tags:
categories: Solace
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/schema-registry

# Introduction to Solace Schema Registry using the Solace Messaging API for Java (JCSMP) and REST Messaging

## What you'll learn: Overview

Duration: 0:01:00

In today's data-driven world, ensuring data consistency and interoperability across different systems is crucial. This is where a schema registry comes into play. In this walkthrough, we'll explore how to use Solace Schema Registry with the Solace JCSMP API or REST applications, focusing on the JSON format for schema definition.

You'll learn about:

✔️ What a schema registry is and why it's important   
✔️ What a Serializer and Deserializer (SERDES) is and the role they play   
✔️ How to deploy and configure Solace Schema Registry using either Docker Compose or Kubernetes   
✔️ How to create and manage schema artifacts in Solace Schema Registry web console   
✔️ How to use schemas in your event-driven applications with Solace's JCSMP API or with REST messaging   
✔️ Best practices for schema evolution   

You can also check out our demo video covering the Solace Schema Registry here:

Video TBD


## What you need: Prerequisites

Duration: 0:01:00

1. A general understanding of [event-driven architecture (EDA) terms and concepts](https://docs.solace.com/#Messaging).
2. A locally running Solace Broker or a free trial account of Solace Cloud. Don't have one? [Sign up here.](https://console.solace.cloud/login/new-account)
    * Along with the connection information for the broker
3. Basic knowledge of [JSON schema format](https://json-schema.org/draft-07)
4. [Docker](https://docs.docker.com/get-started/get-docker/) installed on your system (for standalone deployment)
5. [Kubernetes](https://kubernetes.io/docs/tasks/tools/) with [Helm](https://helm.sh/docs/intro/install/) (for high availability deployments)
6. [Java Development Kit (JDK) version 11+](https://openjdk.org/) installed on your system
7. An IDE of your choice (e.g., IntelliJ IDEA, Eclipse, Visual Studio Code)
8. Download the provided GA tarball package named ```Schema-Registry-Beta-Package_(latest-version).zip``` that contains all the necessary pieces you will need. This is available on the [Solace Product Portal](https://products.solace.com/prods/Schema_Registry_Beta/) and unzip it to your preferred directory.

NOTE: If you cannot access the [Solace Product Portal](https://products.solace.com/prods/Schema_Registry_Beta/), please click the ```Report a mistake``` at the bottom left of the codelab and open an issue asking for access.
> aside positive
> This walkthrough uses Apicurio Registry for schema management, which we'll set up using Docker Compose.

## What Is A Schema Registry

Duration: 0:02:00

A schema registry is a central repository for managing and storing schemas. It helps ensure data consistency, enables data governance, and supports schema evolution. Here's why it's important:

1. **Data Consistency**: Ensures that producers and consumers agree on the data format.
2. **Interoperability**: Allows different systems to communicate effectively.
3. **Schema Evolution**: Supports versioning and compatibility checks as schemas change over time.
4. **Data Governance**: Centralizes schema management for better control and auditing.

## What Is A SERDEs

Duration: 0:02:00

A SERDES (Serializer/Deserializer) in the context of a schema registry is a component that handles two key functions:
1. **Serialization**: Converting data objects from their native format (like Java objects) into a binary format suitable for transmission or storage.
2. **Deserialization**: Converting the binary data back into its original format for processing.   

In a schema registry system, SERDES works closely with schemas to:
- Ensure data consistency during serialization/deserialization
- Validate that messages conform to the registered schema

For example:
- A serializer might take a Java object and convert it to binary format using a schema from the registry
- A deserializer would then use the same schema to correctly reconstruct the object from the binary data

This is a fundamental concept in message-based systems where data needs to be:
- Efficiently transmitted between different services
- Properly validated against defined schemas
- Correctly interpreted by different applications that might be written in different programming languages

> aside positive
> In this walkthrough, we'll use the Solace JSON Schema SERDES for Java along with the Solace Messaging API for Java (JCSMP) to serialize and deserialize messages in the JSON format.

## Setting up Solace Schema Registry with Docker

Duration: 0:06:00

We'll use Docker Compose to set up the Solace Schema Registry, for local development or standalone use cases with minimal resource and networking requirements. We've prepared a Docker Compose file that will launch an instance of the Solace Schema Registry and all the necessary components with a pre-defined configuration.

1. In these subsequent steps we will use the package that came from the downloaded tarball package from the prerequisites section. Navigate to the extracted folder called ```Schema-Registry-V1.0```. You should see the following files and folders:
<p align="center">
  <img src="img/SrBetaPackageFolderView.jpg" />
</p>


2. Open a terminal or command prompt window and navigate to the extracted location of the folder called ```solace-schema-registry-dist```.
3. Run the command ```for img in {docker-images}/*.tar.gz; do docker load -i "$img"; done``` to load docker images. For Window use this instead ```for %i in (docker-images\*.tar.gz \*.tar.gz) do docker load -i "%i"```.
4. You can make changes to the ```.env``` file to change things such as default login or ports. While using the built-in identity provider, we can leave everything to defaults for this codelab.

<p align="center">
  <img src="img/EnvFile.jpg" />
</p>

5. Run the following command and all the components will start up with the specified values configured: ```docker compose -f compose.yaml -f compose.nginx.yaml -f compose.nginx.for.embedded.yaml -f compose.embedded.yaml up -d```. 

6. Once the script is done running, you should now be able to go to your browser and navigate to ```localhost:8888``` which should re-direct you to the Solace Schema Registry login screen.

<p align="center">
  <img src="img/SrLoginEmpty.jpg" />
</p>

That's it, you have now installed an instance of the Solace Schema Registry with the Postgres storage option!

Alternatively, for enterprise-grade security features, Solace Schema Registry supports external identity providers. For that, make the necessary configurations in your IdP and set the environment variables in your ```.env``` file:

Insert image 

Run the following command ```docker compose -f compose.yaml -f compose.nginx.yaml -f compose.nginx.for.external.yaml -f compose.external.multiple.issuers.yaml up -d```.

## Setting up Solace Schema Registry with Kubernetes

Duration: 0:06:00

Alternatively, we can set up Solace Schema Registry on a Kubernetes cluster using Helm.

NOTE: You must have an existing Kubernetes cluster available (for example, Amazon EKS, Google GKE, Microsoft AKS, or an on-prem/self-managed cluster).

1. Configure ```kubectl``` to communicate with your cluster.
2. In this method of deployment also, we will use the package that came from the downloaded tarball package from the prerequisites section. Navigate to the extracted folder called ```Schema-Registry-V1.0```.
3. Open the commonad and run this command to load docker images at your preferred location:

```bash
export REGISTRY="your-registry.com/project"
for img in {docker-images}/*.tar.gz; do
  LOADED=$(docker load -i "$img" | grep "Loaded image:" | cut -d' ' -f3)
  NEW_NAME="$REGISTRY/$(basename "$img" .tar.gz)"
  docker tag "$LOADED" "$NEW_NAME"
  docker push "$NEW_NAME"
done
```

4. Install the CloudNative PostgreSQL Operator for database management:
```kubectl apply --server-side -f https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/release-1.26/releases/cnpg-1.26.0.yaml```.
5. Update a values.yaml file with your environment-specific configuration, database, authentication, ingress and TLS configuration:
Insert image
6. Install Solace Schema Registry using Helm: ```helm upgrade --install schema-registry ./solace-schema-registry```
7. Verify the deployment: ```kubectl get pods -n solace```

8. To access the deployed services, replace <ingress.hostNameSuffix> with the actual hostname or IP address you configured for your ingress: ```https://ui.<ingress.hostNameSuffix>```

## Creating and Registering Schemas

Duration: 0:04:00

Let's create a simple schema for a ```Clock-in-out``` event:

1. Open the Solace Schema Registry UI in your web browser by going to ```localhost:8888```.
2. Login with the predefined credentials for a developer. In this case the username is ```sr-developer``` and password is ```devPassword```.   

<p align="center">
  <img src="img/SrLogin.jpg" />
</p>

3. Click on ```Create artifact``` button. Once the dialogue opens enter the following as shown below:
    * Group Id: Leave it empty (default)
    * Artifact Id: Set to ```RetailMore/payroll```
    * Type: Set to ```JSON Schema```   

<p align="center">
  <img src="img/SrCreateArtifact.jpg" />
</p>
<p align="center">
  <img src="img/SrCreateArtifact1.jpg" />
</p>

4. We will skip the ```Artifact Metadata``` step as it is optional and will click ```Next```. 

5. For the "Version Content" section, copy the Avro schema from below and either paste directly or save it into a file and upload it and click ```Next``` when done. 
```json
{
  "namespace": "com.solace.samples.serdes.avro.schema",
  "type": "record",
  "name": "ClockInOut",
  "fields": [
    {
      "name": "region_code",
      "type": "string",
      "doc": "region code for clock in or out"
    },
    {
      "name": "store_id",
      "type": "string",
      "doc": "Store identifier"
    },
    {
      "name": "employee_id",
      "type": "string",
      "doc": "Employee ID for who clocked in or out"
    },
    {
      "name": "datetime",
      "type": {
        "type": "long",
        "logicalType": "timestamp-millis"
      },
      "doc": "Clock time"
    }
  ]
}
```  

<p align="center">
  <img src="img/SrCreateArtifact2.jpg" />
</p>

6. We will skip the ```Version Metadata``` step as it is optional and will simply click the ```Create``` button. 

7. Finally after you have successfully created the new schema you should see the following:   

<p align="center">
  <img src="img/SrCreateArtifactDone.jpg" />
</p>

You've now created and registered your first schema!

## Using Schemas with the Solace Messaging API for Java (JCSMP)

Duration: 0:10:00

Now, let's see how to use this schema in Java using the Solace Messaging API for Java (JCSMP):

1. Open a command window or terminal and clone this GitHub repository, and go to ```solace-samples-java-jcsmp```:
```git clone https://github.com/SolaceSamples/solace-samples-java-jcsmp```
```cd solace-samples-java-jcsmp```

NOTE: For winows users, use the ```gradlew.bat``` file instead of ```gradlew``` in the below steps.

2. Run the following command to build the sample on Windows ```./gradlew.bat build``` and . You should see a ```BUILD SUCCESSFUL``` message.          

3. Run the sample application and provide the broker connection details like so ```./gradlew.bat runHelloWorldJCSMPAvroSerde --args="localhost:55555 default default"```. 

This sample talks to the locally deployed Apicurio Schema Registry and retrieves the schema along with the schema ID. It will then do the following:

Configures the Serializer and Deserializer:
```java
// Create and configure Avro serializer and deserializer
        try (Serializer<GenericRecord> serializer = new AvroSerializer<>();
             Deserializer<GenericRecord> deserializer = new AvroDeserializer<>()) {

            serializer.configure(getConfig());
            deserializer.configure(getConfig());
```
```java
   /**
     * Returns a configuration map for the Avro serializer and deserializer.
     *
     * @return A Map containing configuration properties
     */
    private static Map<String, Object> getConfig() {
        Map<String, Object> config = new HashMap<>();
        config.put(SchemaResolverProperties.REGISTRY_URL, REGISTRY_URL);
        config.put(SchemaResolverProperties.AUTH_USERNAME, REGISTRY_USERNAME);
        config.put(SchemaResolverProperties.AUTH_PASSWORD, REGISTRY_PASSWORD);
        return config;
    }
```


Serializes the message payload and publishes the message to the connected broker on ```solace/samples``` destination with the serialized payload and schema ID:
```java
   // Create and populate a GenericRecord with sample data
            GenericRecord user = initEmptyUserRecord();
            user.put("name", "John Doe");
            user.put("id", "123");
            user.put("email", "support@solace.com");

            // Serialize and send the message
            BytesMessage msg = JCSMPFactory.onlyInstance().createMessage(BytesMessage.class);
            SerdeMessage.serialize(serializer, topic, msg, user);
            System.out.printf("Sending Message:%n%s%n", msg.dump());
            producer.send(msg, topic);
```

It will then receive the published message and deserialize it by looking up the schema ID and retrieving the schema and print it out to console:
```java
  // Set up the message consumer with a deserialization callback
            XMLMessageConsumer cons = session.getMessageConsumer(Consumed.with(deserializer, (msg, genericRecord) -> {
                System.out.printf("Got record: %s%n", genericRecord);
                latch.countDown(); // Signal the main thread that a message has been received
            }, (msg, deserializationException) -> {
                System.out.printf("Got exception: %s%n", deserializationException);
                System.out.printf("But still have access to the message: %s%n", msg.dump());
                latch.countDown();
            }, jcsmpException -> {
                System.out.printf("Got exception: %s%n", jcsmpException);
                latch.countDown();
            }));
            cons.start();
```

The sourcecode can be further looked at by opening the ```HelloWorldJCSMPAvroSerde.java``` file.

## Best Practices for Schema Evolution

Duration: 0:10:00

As your data model evolves, you'll need to update your schemas. Here are some best practices:

1. **Backward Compatibility**: Ensure new schema versions can read old data.
2. **Forward Compatibility**: Ensure old schema versions can read new data (ignoring new fields).
3. **Full Compatibility**: Aim for both backward and forward compatibility.
4. **Versioning**: Use semantic versioning for your schemas.
5. **Default Values**: Provide default values for new fields to maintain backward compatibility.
6. **Avoid Renaming**: Instead of renaming fields, add new fields and deprecate old ones.

When updating a schema in Apicurio Registry:

1. Create a new version of the existing schema.
2. Make your changes, following the best practices above.
3. Use the compatibility rule in the registry to ensure your changes don't break existing consumers.

## Takeaways

Duration: 0:02:00

✔️ Schema registries are crucial for maintaining data consistency in event-driven architectures.   
✔️ Apicurio Registry provides a powerful platform for managing schemas.   
✔️ Apache Avro is a popular choice for schema definition due to its compact binary format and schema evolution capabilities.   
✔️ Solace's JCSMP API can be used effectively with the Apicurio Registry for robust event-driven applications.   
✔️ Proper schema evolution practices ensure smooth updates without breaking existing systems.   
✔️ Using schemas in your applications helps catch data issues early and improves overall system reliability.   
✔️ More schema SERDEs will be made available in the future including JSON.

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
