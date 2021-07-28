author: Dennis Brinley
summary: Deploy KEDA and Scale a Kubernetes Deployment by Monitoring a Solace PubSub+ Queue
id: keda-solace-queue
tags: keda, kubernetes, scale, scaler, scaling, autoscaler, solace, pubsub, event, broker, queue, message, messaging, msgCount, msgSpoolSize, scaledobject, trigger, triggerauthentication
categories: KEDA
environments: Web
status: Draft
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/keda-solace-queue

# Scale a Kubernetes Deployment using KEDA with Solace PubSub+ Event Queues

## Introduction

Duration: 0:05:00

The purpose of this CodeLab is to provide an introduction to Kubernetes Event-Driven Autoscaler (KEDA) and the Solace PubSub+ Event Broker Queue Scaler. [KEDA](https://keda.sh) is a [CNCF](https://www.cncf.io) sandbox project (current as of this writing). It's purpose is to augment the capability of the native [Kubernetes Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/). It does this by providing an interface for HPA to retrieve custom metric values that can be used for scaling. The [Solace PubSub+ Event Broker Queue Scaler](http://need-ref) defines an interface that allows KEDA to scale applications based on Solace Queues, specifically the current ***Message Count*** and ***Message Spool Usage***. Based on the values of these metrics, KEDA and HPA can scale target Deployments, Jobs, and Stateful Sets in response to fluctuating demand. The instructions in this CodeLab will provide a practical guide to using KEDA and the Solace Event Queue Scaler with Solace Event Brokers.

## What you'll learn

Duration: 00:02:00

In the course of this CodeLab, you will learn:
- How to install KEDA to your Kubernetes Cluster
- The basics of how KEDA works with Kubernetes Horizonal Pod Autoscaler (HPA)
- How to configure KEDA to scale an application based on a Solace PubSub+ Event Broker Queue
- How to scale an Application based on message backlog (message count) on a queue
- How to scale an Application based on the message spool usage (resources utilized) on a queue
- How to Manage HPA behavior using KEDA Configuration

## Prerequisites

Duration: 0:10:00

### Proficiencies
This Codelab assumes that you have at least minimum proficiency with:
- Kubernetes, including command line administration using `kubectl` command
- Solace PubSub+ Event Broker
- Messaging system concepts

### Desktop Software
You must have following command line tools available to complete the CodeLab. Links are provided to respective web sites if you need to complete installation.
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/quickstart/)

### Kubernetes
Access to a Kubernetes cluster is required to complete the Codelab
- Size Requirements?
- Administrative Access (Define? Create/Deploy)

## What you'll do

Duration: 0:15:00

### Install Software
We will use **Helm** to install software to your Kubernetes cluster. **Helm** charts (coded instructions for installation) are available in public repositories.
- KEDA - We will use **Helm** to deploy the KEDA software to the Kubernetes cluster in `namespace=keda`
- Solace PubSub+ Event Broker (Dev Mode) - We will install a small scale Event Broker to complete the lab in `namespace=solace`

### Create Deployments
We will create the following objects on the Kubernetes cluster in `namespace=solace`:
- **kedalab-helper** - Kubernetes **Pod** that will be created for the purpose of running configuration scripts and to publish messages.
- **solace-consumer** - Kubernetes **Deployment** that we will scale using KEDA and the Solace Queue Scaler.

### Configure KEDA to Scale the solace-consumer Deployment
These objects define the KEDA configuration and will be created in `namespace=solace`:
- **kedalab-scaled-object** - KEDA **ScaledObject** informs KEDA that a Scaler (Solace Scaler for this Codelab) will be applied to our deployment
- **kedalab-solace-secret** - Kubernetes **Secret** with encoded credentials for the admin ID to connect to the Solace SEMP endpoint of our broker
- **kedalab-trigger-auth** - KEDA **TriggerAuthentication**; bridges a KEDA **ScaledObject** configuration to a Kubernetes **Secret**

### Publish Messages and Observe!
- We will use SDK-Perf utility, provided for you on **kedalab-helper** pod, to publish messages to our broker.
- Based upon the message backlogs that we create, we will observe how KEDA scales the **solace-consumer** deployment

Positive
: Let's Get Started!

## Install KEDA

Duration: 0:15:00

You will need to install KEDA if it is not already available on your cluster. Instructions here are reproduced from the [KEDA Web site](https://keda.sh/docs/2.3/deploy/). Please refer to the KEDA site if you wish to use a deployment method other than Helm to install KEDA.

Negative
: If KEDA was already installed to your cluster and you intend to use it to complete the CodeLab:<br>_It may be necessary to update the installation OR uninstall keda and re-install it if the Solace Scaler is not available in your installed version of KEDA. The Solace Scaler is available in KEDA core starting with version 2.4_

### Install KEDA Using Helm

1. Add Helm repo (if not already added)
    ```bash
    helm repo add kedacore https://kedacore.github.io/charts
    ```
2. Update Helm repo
    ```bash
    helm repo update
    ```
3. Install KEDA Using the Helm chart:
    ```bash
    kubectl create namespace keda
    helm install keda kedacore/keda --namespace keda
    
    ## ***IMPORTANT*** Use the following until KEDA 2.4 release is available.
    ## * The Solace Scaler will not be available in the KEDA images
    ##   until v2.4 is GA!
    ## * The command below will pull the image from a private registry
    ##   instead of the ghcr.io/kedacore registry.
    ## * Note: The keda namespace must be created as above
    helm install keda kedacore/keda --namespace keda --set image.keda.repository=docker.io/dennisbrinley/keda --set image.keda.tag=main --set image.metricsApiServer.repository=docker.io/dennisbrinley/keda-metrics-apiserver --set image.metricsApiServer.tag=main
    ```
4. Check your installation
    ```bash
    ## Make sure that the deployments/pods are Ready!
    kubectl get deployments -n keda
    kubectl get pods -n keda
    ```

## Install Solace PubSub Event Broker

Duration: 0:15:00

Follow the instructions to install a Solace PubSub+ Event Broker to your Kubernetes cluster. The broker will be installed to a namespace called `solace`. The broker will be created with an administrative user=**admin** and password=**KedaLabAdminPwd1**. We will configure the broker subsequently in the next section.

1. Add Helm repo
    ```bash
    helm repo add solacecharts https://solaceproducts.github.io/pubsubplus-kubernetes-quickstart/helm-charts
    ```
2. Update Helm repo
    ```bash
    helm repo update
    ```
3. Create `solace` namespace
    ```bash
    kubectl create namespace solace
    ```
4. Install the temporary broker
    ```bash
    ##  This installation will use ephemereal storage, which means if pod is shut down and restored, the configuration will be lost.
    helm install kedalab solacecharts/pubsubplus-dev --namespace solace --set solace.usernameAdminPassword=KedaLabAdminPwd1 --set storage.persistent=false
    ```
    ```bash
    ##  Use the following command instead of the previous one if you want to keep the Solace broker beyond the time spent on the code lab:
    ##  helm install kedalab solacecharts/pubsubplus-dev --namespace solace --set solace.usernameAdminPassword=KedaLabAdminPwd1
    ```
5. Wait and Verify
    ```
    ## Command will hold until the pod = kedalab-pubsubplus-dev-0 is ready for use
    ## Note: This make take up to a minute if you execute immediately after deploying the broker
    kubectl wait -n solace --for=condition=Ready --timeout=120s pod/kedalab-pubsubplus-dev-0
    
    ## Then, double-check:
    kubectl get statefulsets -n solace kedalab-pubsubplus-dev -o wide
    kubectl get pods -n solace kedalab-pubsubplus-dev-0 -o wide
    ```
6. **OPTIONAL** - You can connect to the broker and inspect the installation using a web browser. The installed broker will have the default configuration. (We haven't configured it yet)
    - First, you'll need to obtain the service IP Address for the broker:
    ```bash
    kubectl get services -n solace kedalab-pubsubplus-dev
    ## *** OR ***
    kubectl get services -n solace kedalab-pubsubplus-dev -o jsonpath="{.status.loadBalancer.ingress[0].ip}"
    ```
    - Next, use the IP Address in a web browser to navigate to the Solace Console:
    ```
    http://[service-external-ip-address]:8080
    ## e.g. http://34.199.88.200:8080
    ```
    - Enter the username and password: **admin/KedaLabAdminPwd1**
    - You should be connected to the Solace PubSub+ Event Broker

## Deploy Apps and Configure Solace PubSub+ Event Broker

Duration: 0:20:00

After these steps are complete, we will have a configured Solace Event Broker, our kedalab-helper pod will be available, and the solace-consumer will be ready to process messages.

### Create kedalab-helper Pod
The kedalab-help pod contains configuration scripts and tools we need to complete the lab. We will create it on our Kubernetes cluster.

1. Navigate from the lab root directory to the configs directory:
```bash
cd ./configs
```
2. Apply the kedalab-helper.yaml file to the cluster to create the pod:
```bash
kubectl apply -f kedalab-helper.yaml
```
3. Verify that the pod is created and ready:
```bash
kubectl get pods -n solace
##  OUTPUT
##  ------
##  NAME                               READY   STATUS        RESTARTS   AGE
##  kedalab-helper                     1/1     Running       0          45s
##  (and others)
```

### Configure Solace PubSub+ Event Broker
Next, we'll execute a script included on kedalab-helper to configure our Solace PubSub+ Event Broker with the objects necessary for the code lab. Execute the following command to configure the Event Broker:
```bash
kubectl exec -n solace kedalab-helper -- ./config/config_solace.sh
```

Positive
: If you completed optional step #6 above in [Install Solace PubSub Event Broker](#install-solace-pubsub-event-broker), then you can view the results of the configuration script: Refresh the screen to observe the configured VPN and associated objects. If you navigate to the queue `SCALED_CONSUMER_QUEUE1`, you can view the attached consumers. Initially zero, this list will grow and shrink as we publish messages with KEDA configured.

### Create solace-consumer Deployment
The Solace PubSub+ Event Broker should be created and configured prior to completing this step. Create the `solace-consumer` deployment by executing the following steps:
1. Navigate from the lab root directory to the configs directory (if you're not already there):
```bash
cd ./configs
```
2. Apply the solace-consumer.yaml file to the cluster to create the deployment:
```bash
kubectl apply -f solace-consumer.yaml
```
3. Verify that the consumer is deployed and ready
```bash
kubectl get deployments -n solace
kubectl get pods -n solace
```

Positive
: Note that there should be one replica of the `solace-consumer` pod running at this point. We are now ready to proceed with using KEDA to scale the solace-consumer deployment!

## Review KEDA ScaledObject Configuration

Duration: 0:15:00

A KEDA ScaledObject provides the core configuration for KEDA. This section explains the 

We are going to apply a file called `scaledobject-complete.yaml` to the Kubernetes cluster. This file contains a KEDA **ScaledObject**, **TriggerAuthentication** _and_ a Kubernetes **Secret** to manage credentials. The ScaledObject is shown in the exerpt below. (Elipses are in horizontalPodAutoscalerConfig, indicating that section is eliminated from the reproduction).

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name:      kedalab-scaled-object
  namespace: solace
spec:
  scaleTargetRef:
    apiVersion:    apps/v1
    kind:          Deployment
    name:          solace-consumer
  pollingInterval:  5
  cooldownPeriod:  10
  minReplicaCount:  0
  maxReplicaCount: 10
  advanced:
    horizontalPodAutoscalerConfig:
       ...                     ## Removed for brevity
  triggers:
  - type: solace-event-queue
    metadata:
      solaceSempBaseURL:       http://kedalab-pubsubplus-dev.solace.svc.cluster.local:8080
      messageVpn:              keda_vpn
      queueName:               SCALED_CONSUMER_QUEUE1
      messageCountTarget:      '20'
      messageSpoolUsageTarget: '1'
    authenticationRef:
      name: kedalab-trigger-auth
```

The ScaledObject:
- References a specific deployment, in this example: `spec.scaleTargetRef.name=solace-consumer`
- Is declared in `namespace=solace`, the same namespace as the solace-consumer
- Declares at least one or more `triggers`

The following table describes important KEDA ScaledObject configuration parameters.

|Field Name|Codelab Value|Impact|
|----|:--:|------------------|
|pollingInterval|_5_|KEDA will poll the Solace SEMP API every 5 seconds|
|cooldownPeriod|_10_|This is the period in seconds that must elapse before KEDA will scale the application from 1 replica to zero replicas|
|minReplicaCount|_0_|If there are no messages on the queue, then our solace-consumer deployment will scale to zero replicas|
|maxReplicaCount|_10_|KEDA/HPA may scale the solace-consumer deployment up to 10 replicas|

Positive
: We will discuss the `horizonalPodAutoscalerConfig` in our last exercise.

### Solace Event Queue Trigger
Let's inspect the `triggers:` section of the ScaledObject. The trigger type is specified as `solace-event-queue`. The fields contained in the trigger configuration shown here _are specific to a Solace Event Queue scaler._ Other trigger types interface with different technology and logically have different requirements. The Solace Event Queue Scaler uses the SEMP API to obtain metrics from the broker. Therefore, we expect that then information necessary to connect to SEMP is required.

The `solaceSempBaseURL`, `messageVpn`, and `queueName` form a path to the queue we'll use for scaling the Deployment. Note the fields called out in the following table and their impact on the scaling operation. 

|Field Name|Codelab Value|Impact|
|----|:--:|------------------|
|solaceSempBaseURL|_SEMP URL_|Solace SEMP Endpoint in format: `<protocol>://<host-or-service>:<port>`|
|messageVpn|_keda\_vpn_|Message VPN hosted on the Solace broker|
|queueName|_SCALED\_CONSUMER\_QUEUE1_|The name of the queue being monitored|
|messageCountTarget|_20_|The average number of messages desired per replica.|
|messageSpoolUsageTarget|_1_|Value in Megabytes; The average spool usage desired per replica|

Negative
: **AT LEAST** one of `messageCountTarget` or `messageSpoolUsageTarget` is required. If both values are present, the metric value resulting in the higher desired replicas will be used. (Standard KEDA/HPA behavior)

Positive
: You can find more information about the [Solace Event Queue Trigger](https://keda.sh/docs) on the KEDA web site.

### Metric Target Values
Target values, `messageCountTarget` and `messageSpoolUsageTarget` for the Solace Queue Scaler, represent the _maximum_ value desired per replica for the metric. From the Kubernetes HPA Documentation, the computation is expressed as:
```
desiredReplicas = ceil[currentReplicas * ( currentMetricValue / desiredMetricValue )]
```
Using `messageCountTarget` as an example. The target value for the lab is 20.
- If the average number (per active replica) of messages on the queue backlog is greater than this value, then the deployment will scale up to more replicas. For example, if there are 44 messages on the queue and two active replicas (mean average = 22), then the target deployment will scale up to 3 replicas to meet the demand (_observed_ 22 msg/replica > 20 msg/replica _desired_)
- If the current replica count is zero, and the messageCount is 1, then the application will scale to 1 replica

**Based on this configuration, we can expect that the Deployment will scale:**
- To zero replicas if there are no messages on the input queue for more than 10 seconds
- To a maximum of 10 replicas.
- To 10 replicas if `messageCount` from SEMP > 180 messages on the queue when it is polled.
- To 10 replicas if the `messageSpoolUsage` from SEMP > 9 Megabytes

Positive
: Note that HPA has no ability to scale from 0 -> 1 or from 1 -> 0 replicas. This is done by KEDA.

### KEDA Trigger Authentication

Note that the Trigger record in the ScaledObject depicted above specifies `authenticationRef.name=kedalab-trigger-auth`. This reference points to a KEDA TriggerAuthentication record. The contents are shown below. The TriggerAuthentication maps authentication parameters to the Solace Trigger. In this case, the parameters are mapped to a Kubernetes Secret called `kedalab-solace-secret`. The `username` and `password` will be used to authenticate to the Solace SEMP RESTful API.

```yaml
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: kedalab-trigger-auth
  namespace: solace
spec:
  secretTargetRef:
    - parameter:   username
      name:        kedalab-solace-secret
      key:         SEMP_USER
    - parameter:   password
      name:        kedalab-solace-secret
      key:         SEMP_PASSWORD
```

Positive
:  **TriggerAuthentication** You can find more information about **TriggerAuthentication** records on the KEDA Web site: [KEDA Authentication](https://keda.sh/docs/2.3/concepts/authentication/)

## Create KEDA ScaledObject with Solace Queue Trigger

Duration: 0:15:00

### Pre-Flight Check
At this point, the following statements should all be **true**:
- KEDA is installed
- Solace PubSub+ Event Broker is installed _and_ configured for the Codelab
- kedalab-helper Pod is created and ready to accept commands
- solace-consumer Deployment is created _and_ there is 1 active replica (pod)

**OPTIONAL** - We can verify these conditions with the following commands:
```bash
kubectl get deployments -n keda
## Result: keda-metrics-apiserver, keda-operator READY

kubectl get pods -n solace
## Result: kedalab-helper, kedalab-pubsubplus-dev-0, and solace-consumer-[identifiers] listed
```

### Apply the KEDA ScaledObject
_And Secret + TriggerAuthentication!_ We will apply the ScaledObject to the cluster and observe the Deployment scale to zero replicas.

1. We will use a separate terminal window to watch KEDA scale the application. Open a new terminal window and execute one of the following commands. These commands will check the status of the deployment or the replica pods continuously.
```bash
##  Watch the solace scaler deployment
kubectl get deployment solace-consumer -n solace -w

##  OR Watch the solace scaler pods
kubectl get pods -n solace -w

##  (You can also open two separate terminal windows and do both)
```
2. In your main terminal window, make sure you are in the configs/ directory and execute the command:
```bash
kubectl apply -f scaledobject-complete.yaml
```
3. You should observe the replicas scale to zero pods after a few seconds. You can observe the activity in one of your terminal windows where you have an active watch `-w` option, or execute `kubectl get deployments solace-consumer -n solace`
4. View the HPA (Horizontal Pod Autoscaler) entry - When a ScaledObject is created for KEDA, KEDA creates a scaler in the Horizonal Pod Autoscaler (HPA). We can check the HPA entry with the following command.
```bash
kubectl get hpa -n solace
```
5. **OPTIONAL** - In your watch window, press Control-C to stop the command from watching the deployment or pod replicas and return to a command prompt. (Or you can leave this command active for the next exercise)

### Recap: Create KEDA ScaledObject with Solace Queue Trigger
In this exercise we checked our readiness and then created a KEDA ScaledObject. We verified that the ScaledObject was created and active by watching the solace-consumer Deployment scale to zero replicas, and by checking the HPA entry.

Positive
: There should be 0 replicas of the solace-consumer running in the Kubernetes cluster at this point!

## Scale Deployment on Queue Message Count

Duration: 0:20:00

We will publish messages to the queue of sufficient volume that KEDA and HPA will scale the solace-consumer Deployment to 10 replicas.

### Execute Steps: Scale on Message Count
1. Watch KEDA scale the application. _(Skip this step if the watch is already active.)_ 
Open a separate terminal window and execute one of the following commands. These commands will check the status of the deployment or the replica pods continuously. (When we publish messages, we can watch the deployment replicas scale up and down while this command is active.)
```bash
##  Watch the solace scaler deployment (less noisy)
kubectl get deployment solace-consumer -n solace -w

##  OR Watch the solace scaler pods
kubectl get pods -n solace -w

##  (You can also open two separate terminal windows and do both)
```
2. Publish Messages - We will use SDK-Perf (Java Command-Line app) to write messages to the queue read by the solace-consumer application. At this point, there should be no active instances of the solace-consumer application. We will publish 400 messages to the queue at a rate of 50 messages per second. Each message will have a 256 byte payload. On your command line, enter:
```bash
kubectl exec -n solace kedalab-helper -- ./sdkperf/sdkperf_java.sh -cip=kedalab-pubsubplus-dev:55555 -cu consumer_user@keda_vpn -cp=consumer_pwd -mr 50 -mn 400 -msx 256 -mt=persistent -pql=SCALED_CONSUMER_QUEUE1
#### ******* CREATE SCRIPT FOR THIS?
```
3. Observe Scaling - View the the scaling of solace-consumer deployment in the command line window Upon publication of our messages. We expect:
    - KEDA will detect that the application should be active and scale the application to 1 replica.
    - Horizontal Pod Autoscaler will then take over and scale the application to 10 replicas.
    - When the messages have finished processing, HPA will reduce the total replicas to 1.
    - KEDA scales the application zero replicas
4. OPTIONAL - In your watch window, press Control-C to stop the command from watching the deployment or pod replicas and return to a command prompt. (Or you can leave this command active for the next exercise)

Positive
: You can repeat Step 2, Publish Messages, as many times as you like and review the results. You can also modify the `sdkperf` command options to see the effects if you are familiar with the tool. The command `kubectl exec -n solace kedalab-helper -- ./sdkperf/sdkperf_java.sh -h` will display the options.

### Recap: Scale on Message Count
We published messages to the consumer input queue hosted on our Solace Broker. We observed KEDA and HPA scale the application based on the message count from 0 to 10 replicas, and back down to 0 replicas after the input queue was cleared.

Positive
: The solace-consumer should have scaled back down from its maximum of 10 back down to 0 replicas

## Scale Deployment on Queue Message Spool Size

Duration: 0:15:00

In the last exercise, we scaled based on message count. In this exercise, we will scale the deployment to 10 replicas based on message spool usage. We will publish 50 messages to the queue at a rate of 10 messages per second. Each message will have a size of 4 megabytes per message so that KEDA and HPA will scale the solace-consumer Deployment to 10 replicas. (4 megabytes = 4 * 1024 * 1024 = 4194304 bytes) Our scaler configuration indicates a size of 1 megabyte, so the message spool size > (9 megabytes + 1 byte) will cause our deployment to scale to 10 replicas. Recall that messages will be read as the solace-consumer deployment scales up. So the highest number of replicas we can expect resulting from message count is 5. However. the existance of 3 4 Mbyte messages on the message spool when the queue is polled via SEMP will result in a 12 megabyte backlog. So the deployment should scale to the maximum of 10 replicas given our target value of 1 megabyte per replica.

### Execute Steps: Scale on Message Spool Size
1. Watch KEDA scale the application. _(Skip if the watch is already active.)_ 
Open a separate terminal window and execute one of the following commands. These commands will check the status of the deployment or the replica pods continuously. (When we publish messages, we can watch the deployment replicas scale up and down while this command is active.)
```bash
##  Watch the solace scaler deployment (less noisy)
kubectl get deployment solace-consumer -n solace -w

##  OR Watch the solace scaler pods
kubectl get pods -n solace -w

##  (You can also open two separate terminal windows and do both)
```
2. Publish Messages - We will use SDK-Perf (Java Command-Line app) to write messages to the queue read by the solace-consumer application. At this point, there should be no active instances of the solace-consumer application. We will publish 50 messages to the queue at a rate of 10 messages per second. Each message will have a 4194304 byte (4 megabyte) payload. On your command line, enter:
```bash
kubectl exec -n solace kedalab-helper -- ./sdkperf/sdkperf_java.sh -cip=kedalab-pubsubplus-dev:55555 -cu consumer_user@keda_vpn -cp=consumer_pwd -mr 10 -mn 50 -msx 4194304 -mt=persistent -pql=SCALED_CONSUMER_QUEUE1
#### ******* CREATE SCRIPT FOR THIS?
```
3. Observe Scaling - View the the scaling of solace-consumer deployment in the command line window Upon publication of our messages. We expect:
    - KEDA will detect that the application should be active and scale the application to 1 replica.
    - Horizontal Pod Autoscaler will then take over and scale the application to 10 replicas.
    - When the messages have finished processing, HPA will reduce the total replicas to 1.
    - KEDA scales the application zero replicas
4. OPTIONAL - In your watch window, press Control-C to stop the command from watching the deployment or pod replicas and return to a command prompt. (Or you can leave this command active for the next exercise)

### Recap: Scale on Message Spool Size
We published messages to the consumer input queue hosted on our Solace Broker. We observed KEDA and HPA scale the application based on the message spool size from 0 to 10 replicas, and back down to 0 replicas after the input queue was cleared.

Positive
: The solace-consumer should have scaled back down from its maximum of 10 back down to 0 replicas

### Modify HPA Behavior

Duration: 0:20:00

In this exercise, we will modify the KEDA ScaledObject to adjust the Horizonal Pod Autoscaler settings. The settings will be adjusted so that HPA can increase and decrease the number of desired replicas by a maximum of two pods in an interval of ten seconds. The number (or percentage) of pods can be controlled in this manner, as well as the interval at which pods are scaled. In this way, we can control how quickly replicas are added or removed from our deployment in order to prevent undesirable churn or _flapping_ of replicas as observed metrics fluctuate. See [Kubernetes Horizonal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) for more details.

### Initial HPA Behavior Configuration
Consider the following excerpt from the ScaledObject (this section was elipsized in the earlier excerpt). This is the configuration that was used in the excercises we just completed. It specifies that HPA is permitted to scale down 100 _Percent_ of the maximum pods in a 10 second period; and to scale up a maximum of 10 _Pods_ in a 10 second period (The maximum number of replicas is 10). The `stabilizationWindowSeconds` is zero and therefore has no effect. Effectively, this means that HPA can fully scale up from 1 to 10 pods or down from 10 to 1 pods in a ten second period.

```yaml
horizontalPodAutoscalerConfig:
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 0
      policies:
      - type:          Percent
        value:         100
        periodSeconds: 10
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type:          Pods
        value:         10
        periodSeconds: 10
      selectPolicy:    Max
```

### Updated HPA Behavior Configuration
We will update the configuration to reflect the following exerpt.
```yaml
horizontalPodAutoscalerConfig:
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 30
      policies:
      - type:          Pods
        value:         5
        periodSeconds: 10
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type:          Pods
        value:         2
        periodSeconds: 10
```
Given this configuration, we expect that two replicas may created and up to 5 may be removed during a 10 second period. In addition, _scaleDown_ has `stabilizationWindowSeconds=30` seconds. This parameter allows us to smooth out the scaling curve so that HPA is not constantly scaling up and down due to localized fluctuations in observed metric values. From the Kubernetes HPA documentation:
>When the metrics indicate that the target should be scaled down the algorithm looks into previously computed desired states and uses the highest value from the specified interval.

Therefore, the highest desired replica count computed over a window of the last 30 seconds will be used when scaling down.

### Execute Steps: Updated HPA Behavior Configuration
1. Watch KEDA scale the application. _(Skip if the watch is already active.)_ 
Open a separate terminal window and execute one of the following commands. These commands will check the status of the deployment or the replica pods continuously.
```bash
kubectl get deployment solace-consumer -n solace -w
```
2. Update the ScaledObject to adjust the HPA Behavior to our updated configuration. _This update also contains the TriggerAuthentication and Secret figuration.
```bash
kubectl apply -f scaledobject-complete-hpa.yaml
```
3. Publish Messages - We will publish messages a load of messages as before: 400 messages total at a rate of 50 messages per second.
```bash
kubectl exec -n solace kedalab-helper -- ./sdkperf/sdkperf_java.sh -cip=kedalab-pubsubplus-dev:55555 -cu consumer_user@keda_vpn -cp=consumer_pwd -mr 50 -mn 400 -msx 256 -mt=persistent -pql=SCALED_CONSUMER_QUEUE1
```
4. Observe Scaling - View the the scaling of solace-consumer deployment in the command line window Upon publication of our messages. We expect:
    - KEDA will detect that the application should be active and scale the application to 1 replica.
    - Horizontal Pod Autoscaler will then take over and scale the application, incrementing by 2 replicas at a time (It may not reach the maximum of 10 replicas).
    - The maximum replica count reached will hold longer than necessary to process all of the messages due to the `stabilizationWindowSeconds=30` setting on _scaleDown_
    - When the messages have finished processing and the stabilization window expires, HPA will scale down to 1 replica, decrementing by a maximum of 5 at a time.
    - KEDA scales the application zero replicas
5. In your watch window, press Control-C to stop the command from watching the deployment or pod replicas and return to a command prompt.

### Recap: Updated HPA Behavior Configuration
In this exercise we modified the HPA configuration in our scaled object. Then we published messages and observed effects, showing that we can control the increment and rate at which replicas are created and destroyed. And we observed how the stabilization window can be used to smooth out scaling over time due to temporary spikes in metric values.

## Clean Up

Duration: 0:15:00

Execute the following steps to remove the components from your cluster as desired.

1. On a command line, navigate to the `[codelab-root]/configs` directory (if you're not already there):
```bash
cd ./configs
```
2. Delete the scaled KEDA Scaled Object and verify (Deletes the ScaledObject, TriggerAuthentication, and Secret)
```bash
kubectl delete -f scaled-object.yaml -n solace
kubectl get scaledobjects -n solace
```
3. Delete the solace-consumer Deployment and verify
```bash
kubectl delete -f solace-consumer.yaml -n solace
kubectl get deployments -n solace
```
4. Delete the kedalab-helper Pod and verify
```bash
kubectl delete -f kedalab-helper.yaml
kubectl get pods kedalab-helper -n solace
```
5. Delete the Solace PubSub+ Event Broker (If Desired)
```bash
helm uninstall kedalab --namespace solace
kubectl get statefulsets -n solace
```
6. Delete the `solace` namespace (assuming it is empty).
```bash
kubectl get pods,services,scaledobjects,secrets,triggerauthentications -n solace
kubectl delete namespace solace
```
7. If desired, delete KEDA from the cluster
```bash
helm uninstall keda --namespace keda
```
8. If the last step is complete, then delete the `keda` namespace
```bash
kubectl delete namespace keda
```

## Conclusion
In the course of this CodeLab you learned how to install KEDA. And you learned how to configure KEDA to use the Solace Event Queue Scaler to scale deployments.

### Takeaways
✅ Scale one of your own applications using your own broker.
✅ The scaler is still experimental: At a minimum, TLS must be added to make it operational (on our TODO list)
✅ Look for Blogs and Updates about KEDA and the Solace Event Queue Scaler on Solace Community!

### References

- [KEDA Web Site](https://keda.sh)
- [KEDA - Solace PubSub+ Event Broker Queue Scaler](https://keda.sh/docs/2.4/scalers/solace-event-queue/)
- [KEDA GitHub Project](https://github.com/kedacore/keda)
- [Kubernetes Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

Positive
: Thank you for trying Solace-KEDA CodeLab! We hope you found it informative.

![Soly Image Caption](img/soly.gif)
