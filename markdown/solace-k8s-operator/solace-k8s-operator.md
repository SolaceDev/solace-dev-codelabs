author: Ken Barr
summary: How to build a Solace PubSub+ Kubernetes Operator
id: solace-k8s-operator
tags: iguide
categories: Kubernetes
environments: Web
status: Draft
feedback link: https://github.com/SolaceProducts/pubsubplus-kubernetes-quickstart
analytics account: UA-3921398-10

# How to build a Solace PubSub+ Kubernetes Operator

## Overview

Duration: 0:05:00

The kubernetes [Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator) is exactly what it sounds like.  It is code or automation that acts like the set of runbooks a human operator of an application would use to deploy, monitor, troubleshoot, upgrade and decommission an application.  The operator can do these functions because it has a deep understanding of the application it is operating on and knowns if the application is functioning correctly.

When Solace first introduced a Kubernetes solution back in the days of Kubernetes 1.5 and 1.6, Operator concepts where very much in flux.  For this reason, we based our Solution on Helm to do initial deployments and rolling upgrades and config-maps as the glue that binds together the highly available cluster of brokers together. But today Kubernetes Operators are far more prevalent and stable.  They make extending Kubernetes behaviour to manage stateful applications like event brokers and databases possible via custom resource and custom resource definitions. So for organizations that manage their deployments through custom resources and operators a Solace operator would be useful, here is why.  

All Kubernetes deployments are a collection of resources. Services, Persistent Volumes, Secrets, Pods, are example of basic resources that are composed together to make up a deployment.  With a Solace custom resources as defined in an operator, then a Solace highly available cluster could also be used as another resource to compose a deployment.  Its life cycle tied to the deployment and maintained within the deployment.  It would be possible for example to upgrade brokers and applications in one operation.

The easiest first step toward a Solace Operator is to wrap the existing Helm charts and Kubernetes templates into an operator based with the Operator SDK.  So, lets see how to do that.

## Environment Setup

Duration: 0:15:00

* Prerequisite is functional access to Kubernetes 1.16+.
* First to build operators you will need [golang](https://golang.org/doc/install) with compatible compiler.
* [Next install the operator-sdk](https://sdk.operatorframework.io/docs/) Minimum version is 1.0.0.
* [Next install Helm](https://helm.sh/docs/intro/install/) which is required to create initial packaging.
* Finally add Solace charts to your helm repo:

``` sh
$ helm repo add solacecharts https://solaceproducts.github.io/pubsubplus-kubernetes-quickstart/helm-charts
```

## Create an Operator

Duration: 0:20:00

Now that you have the Solace defined helm chart, use this to create the operator with the following workflow:

* Create a new operator project using the SDK Command Line Interface (CLI)
* Correct for permissions and passwords
* Use the SDK CLI to build and generate the operator deployment manifests

### Create a new operator project and add existing Helm chart

``` sh
$ cd ~/"<go_workspace>"/src;
$ mkdir pubsubplus-ha-operator
$ cd pubsubplus-ha-operator
$ operator-sdk init --plugins=helm.sdk.operatorframework.io/v1 --domain=solace.com --helm-chart=solacecharts/pubsubplus-ha
```

You will recieve this warning and need to take action:

``` sh
WARN[0000] "The RBAC rules generated in config/rbac/role.yaml are based on the chart's default manifest. Some rules may be missing for resources that are only enabled with custom values, and some existing rules may be overly broad. Double check the rules generated in config/rbac/role.yaml to ensure they meet the operator's permission requirements."
```

Ensure roles are correct to modify pod lables.  Ensure these line exist in config/rbac/role.yaml

``` sh
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["patch"]
```

### Build the operator and deploy

Install the CRD

``` sh
$ make install

/"<go_workspace>"/src/pubsubplus-ha-operator/bin/kustomize build config/crd | kubectl apply -f -
customresourcedefinition.apiextensions.k8s.io/pubsubplushas.charts.solace.com created
```

Define docker repo and imager name:

``` sh
$ export IMG="<docker_repo>"/pubsubplus-ha-operator:v0.0.1
```

Build the operator container and push to docker repo:

``` sh
$ make docker-build docker-push IMG=$IMG
```

Deploy the operator container:

``` sh
$ make deploy IMG=$IMG

cd config/manager && /<go_workspace>/src/pubsubplus-ha-operator/bin/kustomize edit set image controller=<docker_repo>/pubsubplus-ha-operator:v0.0.1
/<go_workspace>/src/pubsubplus-ha-operator/bin/kustomize build config/default | kubectl apply -f -
namespace/pubsubplus-ha-operator-system created
customresourcedefinition.apiextensions.k8s.io/pubsubplushas.charts.solace.com unchanged
role.rbac.authorization.k8s.io/pubsubplus-ha-operator-leader-election-role created
clusterrole.rbac.authorization.k8s.io/pubsubplus-ha-operator-manager-role created
clusterrole.rbac.authorization.k8s.io/pubsubplus-ha-operator-proxy-role created
clusterrole.rbac.authorization.k8s.io/pubsubplus-ha-operator-metrics-reader created
rolebinding.rbac.authorization.k8s.io/pubsubplus-ha-operator-leader-election-rolebinding created
clusterrolebinding.rbac.authorization.k8s.io/pubsubplus-ha-operator-manager-rolebinding created
clusterrolebinding.rbac.authorization.k8s.io/pubsubplus-ha-operator-proxy-rolebinding created
service/pubsubplus-ha-operator-controller-manager-metrics-service created
deployment.apps/pubsubplus-ha-operator-controller-manager created
```

Validate the controller is running

``` sh
$ kubectl get deployment --namespace pubsubplus-ha-operator-system
NAME                                        READY   UP-TO-DATE   AVAILABLE   AGE
pubsubplus-ha-operator-controller-manager   1/1     1            1           2m50s
```

Validate the crd loads into Kubernetes

``` sh
$ kubectl get crd
NAME                              CREATED AT
pubsubplushas.charts.solace.com   2020-08-17T22:53:03Z
```

## Test the operator

Duration: 0:20:00

The next steps create a Solace HA cluster using the newly deployed operator:

* Modify the sample configuaration to include Solace admin password
* Create a new Solace cluster with the operator

Edit the opertor.yaml file to set admin password

``` sh
$ vi config/samples/charts_v1alpha1_pubsubplusha.yaml
  solace:
    redundancy: true
    size: prod100
    usernameAdminPassword: "<new admin password>"
```

Finally run the operator to start the Solace cluster

``` sh
$ kubectl apply -f config/samples/charts_v1alpha1_pubsubplusha.yaml
```

Validate the Solace brokers are live and ready.

``` sh
$ kubectl get pods
NAME                                     READY   STATUS    RESTARTS   AGE
pubsubplusha-sample-pubsubplus-ha-0       1/1     Running   0          96s
pubsubplusha-sample-pubsubplus-ha-1       1/1     Running   0          96s
pubsubplusha-sample-pubsubplus-ha-2       1/1     Running   0          95s
```

Go on the primary broker with node ordinal 0 and validate "Redundancy Status" = "Up".  This means that all the brokers are syncronized and ready to recieve messages.

``` sh
kubectl exec -it pubsubplusha-sample-pubsubplus-ha-0 cli

pubsubplusha-sample-pubsubplus-ha-0> show redundancy

Configuration Status     : Enabled
Redundancy Status        : Up
Operating Mode           : Message Routing Node
Switchover Mechanism     : Hostlist
Auto Revert              : No
Redundancy Mode          : Active/Standby
Active-Standby Role      : Primary
Mate Router Name         : pubsubplushasamplepubsubplusha1
ADB Link To Mate         : Up
ADB Hello To Mate        : Up
```

Get the name of the loadbalancing Service that fronts the Solace cluster.  This will be the name used be applications connect to Solace.

``` sh
kubectl get services
NAME                                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                                                                                                                                                                   AGE
pubsubplusha-sample-pubsubplus-ha        LoadBalancer   10.97.76.97     <pending>     2222:31348/TCP,8080:31717/TCP,1943:32170/TCP,55555:32597/TCP,55003:30106/TCP,55443:32318/TCP,8008:31054/TCP,1443:32713/TCP,5672:32610/TCP,1883:30046/TCP,9000:31317/TCP   5m4s
```

Using the test application found [here](https://github.com/KenBarr/solace-node-sample) to test, we see successful send and receipt of messages.

``` sh
[21:13:32]
*** Subscriber to topic "tutorial/topic" is ready to connect ***
[21:13:32] Connecting to Solace message router using url: ws://pubsubplusha-sample-pubsubplus-ha:8008
[21:13:32] Client username: subscriber
[21:13:32] Solace message router VPN name: default
[21:13:32] Press Ctrl-C to exit
[21:13:32] === Successfully connected and ready to subscribe. ===
[21:13:32] Subscribing to topic: tutorial/topic
[21:13:32] Successfully subscribed to topic: tutorial/topic
[21:13:32] === Ready to receive messages. ===
[21:17:40] Received message: "Sample Message", details:
Destination:                            [Topic tutorial/topic]
Class Of Service:                       COS1
DeliveryMode:                           DIRECT
Binary Attachment:                      len=14
  53 61 6d 70 6c 65 20 4d    65 73 73 61 67 65          Sample.Message
```

From here you should be able to stress the cluster be deleting nodes,(in public clouds), or pods and watch the Solace HA cluster heal itself.

## Delete the operator

Duration: 0:02:00

Finally, to clean up and remove Solace HA cluster, the operator and the CRD.

``` sh
kubectl delete -f config/samples/charts_v1alpha1_pubsubplusha.yaml
make undeploy

```

Note: this will not automatically delete the persistent volumes.

``` sh
kubectl get pvc
kubectl delete -R pvc <no-longer-needed-pvc>
```
