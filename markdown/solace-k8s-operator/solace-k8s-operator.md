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

* First to build operators you will need [golang](https://golang.org/doc/install) with compatible compiler.
* [Next install the operator-sdk](https://sdk.operatorframework.io/docs/install-operator-sdk/) which can be done as a simple binary download or built locally.
* [Helm](https://helm.sh/docs/intro/install/) is required to create initial packaging, 
* Finally configure the helm values.yaml to suite your target environment.  In this example I am installing a Highly Available cluster in minikube which would be good for development testing including failure and retry conditions:
```
cd ~/<git_workspace>; git clone git@github.com:SolaceProducts/pubsubplus-kubernetes-quickstart.git

cd pubsubplus-kubernetes-quickstart; 
vi pubsubplus/values.yaml   
  redundancy: true
  size: dev
  usernameAdminPassword: <password>

helm package pubsubplus/  
```
The result of the package command will produce pubsubplus-2.1.2.tgz

## Create an Operator
Duration: 0:20:00

Now that you have a helm package configured the way you want, use this to create the operator with the following workflow:
* Create a new operator project using the SDK Command Line Interface (CLI)
* Add existing Helm chart for use by the operator's reconciling logic
* Use the SDK CLI to build and generate the operator deployment manifests
### Create a new operator project and add existing Helm chart
```
cd ~/<go_workspace>/src;
operator-sdk new pubsubplus-operator --type=helm --helm-chart=<absolute_path>/<git_workspace>/pubsubplus-kubernetes-quickstart/pubsubplus-2.1.2.tgz
```
The output of the "new" command shows what files are being created:
```
INFO[0000] Creating new Helm operator 'pubsubplus-operator'.
INFO[0000] Created helm-charts/pubsubplus
INFO[0000] Generating RBAC rules
WARN[0000] The RBAC rules generated in deploy/role.yaml are based on the chart's default manifest. Some rules may be missing for resources that are only enabled with custom values, and some existing rules may be overly broad. Double check the rules generated in deploy/role.yaml to ensure they meet the operator's permission requirements.
INFO[0000] Created build/Dockerfile
INFO[0000] Created watches.yaml
INFO[0000] Created deploy/service_account.yaml
INFO[0000] Created deploy/role.yaml
INFO[0000] Created deploy/role_binding.yaml
INFO[0000] Created deploy/operator.yaml
INFO[0000] Created deploy/crds/charts.helm.k8s.io_v1alpha1_pubsubplus_cr.yaml
INFO[0000] Generated CustomResourceDefinition manifests.
INFO[0000] Project creation complete.
```
At this point the pubsubplus [custom resource definition, crd](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions) has been created.  This definition can be loaded into the target cluster.
```
kubectl apply -f deploy/crds/charts.helm.k8s.io_pubsubplus_crd.yaml
```
Validate the crd loads into Kubernetes
```
kubectl get crd
NAME                            CREATED AT
pubsubplus.charts.helm.k8s.io   2020-04-28T20:21:30Z
```
### Use the SDK CLI to build and generate the operator deployment manifests
The build command creates a container image with the operator/[custom resource, cr](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). In this example I tagged the container suitable to push into my personal dockerhub account: kenbarr.
```
operator-sdk build kenbarr/pubsubplus-operator:v0.0.2
```
The output of the "build" shows new container image being built and pushed into local docker.
```
INFO[0000] Building OCI image kenbarr/pubsubplus-operator:v0.0.2
Sending build context to Docker daemon  76.29kB
Step 1/3 : FROM quay.io/operator-framework/helm-operator:v0.15.1
 ---> 450a3ca2d02d
Step 2/3 : COPY watches.yaml ${HOME}/watches.yaml
 ---> Using cache
 ---> 9d7dfeb65ddd
Step 3/3 : COPY helm-charts/ ${HOME}/helm-charts/
 ---> 435ddaefa627
Successfully built 435ddaefa627
Successfully tagged kenbarr/pubsubplus-operator:v0.0.2
INFO[0000] Operator build complete.
```

The new image can be seen loaded locally
```
docker images

REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
kenbarr/pubsubplus-operator                v0.0.2              435ddaefa627        14 minutes ago      174MB
```
(Optional) Push newly built operator into container repo, here I am using personal dockerhub
```
docker push  kenbarr/pubsubplus-operator:v0.0.2
```
```the push refers to repository [docker.io/kenbarr/pubsubplus-operator]
857870fbcbfe: Pushed                                                   6e6a6b67e101: Layer already exists                                                                                      b496b494f6f9: Layer already exists                             9fd48ecc1227: Layer already exists                                                                                      0141daa77f22: Layer already exists                             27cd2023d60a: Layer already exists                                                                                      4b52dfd1f9d9: Layer already exists                     v0.0.2: digest: sha256:199c815d49f59e3e8cad16133fc799a88cda61a3c051470334811430d116b044 size: 1779
```

## Test the operator
Duration: 0:20:00

The next steps are to deploy and test the new operator
* Modify the operator deployment to use the newly created image
* Deploy the operator
* Create a new Solace cluster with the operator

Edit the opertor.yaml file to point at the newly created operator container image.
```
vi deploy/operator.yaml
      containers:
        - name: pubsubplus-operator
          # Replace this with the built image name
          image: kenbarr/pubsubplus-operator:v0.0.1 
```
Ensure roles are correct to create custom service account.  Ensure these lines exist in deploy/role.yaml
```
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - rolebindings
  - roles
  verbs:
  - '*'
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - '*'
```

Deploy the operator with specific service account and role binding.
```
kubectl apply -f deploy/service_account.yaml
kubectl apply -f deploy/role.yaml
kubectl apply -f deploy/role_binding.yaml
kubectl apply -f deploy/operator.yaml
```

You can verify the operator container is deployed and running.
``` 
$ kubectl get deployment
NAME                 DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
pubsubplus-operator       1         1         1            1           1m

kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
pubsubplus-operator-5889cf85c-446kb   1/1     Running   0          3m36s
```
Finally run the operator to start the Solace cluster
```
kubectl apply -f deploy/crds/charts.helm.k8s.io_v1alpha1_pubsubplus_cr.yaml
```

Validate the Solace brokers are live and ready.
```
kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
example-pubsubplus-pubsubplus-0       1/1     Running   0          96s
example-pubsubplus-pubsubplus-1       1/1     Running   0          96s
example-pubsubplus-pubsubplus-2       1/1     Running   0          95s
pubsubplus-operator-5889cf85c-446kb   1/1     Running   0          3m36s
```
Go on the primary broker with node ordinal 0 and validate "Redundancy Status" = "Up".  This means that all the brokers are syncronized and ready to recieve messages.
```
kubectl exec -it example-pubsubplus-pubsubplus-0 cli
```
```
example-pubsubplus-pubsubplus-0> show redundancy

Configuration Status     : Enabled
Redundancy Status        : Up
Operating Mode           : Message Routing Node
Switchover Mechanism     : Hostlist
Auto Revert              : No
Redundancy Mode          : Active/Standby
Active-Standby Role      : Primary
Mate Router Name         : examplepubsubpluspubsubplus1
ADB Link To Mate         : Up
ADB Hello To Mate        : Up
```
Finally get the name of the loadbalancing Service that fronts the Solace cluster.  This will be the name used be applications connect to Solace. 
```
kubectl get services
NAME                                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                                                                                                                                                                   AGE
example-pubsubplus-pubsubplus             LoadBalancer   10.97.76.97     <pending>     2222:31348/TCP,8080:31717/TCP,1943:32170/TCP,55555:32597/TCP,55003:30106/TCP,55443:32318/TCP,8008:31054/TCP,1443:32713/TCP,5672:32610/TCP,1883:30046/TCP,9000:31317/TCP   5m4s
```


Using the test application found [here](https://github.com/KenBarr/solace-node-sample) to test, we see successful send and receipt of messages.

```
[21:13:32]
*** Subscriber to topic "tutorial/topic" is ready to connect ***
[21:13:32] Connecting to Solace message router using url: ws://example-pubsubplus-pubsubplus:8008
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

```
kubectl delete -f deploy/crds/charts.helm.k8s.io_v1alpha1_pubsubplus_cr.yaml
kubectl delete -f deploy/operator.yaml
kubectl delete -f deploy/role_binding.yaml
kubectl delete -f deploy/role.yaml
kubectl delete -f deploy/service_account.yaml
kubectl delete -f deploy/crds/charts.helm.k8s.io_pubsubplus_crd.yaml
```
Note: this will not automatically delete the persistent volumes.
```
kubectl get pvc
kubectl delete -R pvc <no-longer-needed-pvc>
```
