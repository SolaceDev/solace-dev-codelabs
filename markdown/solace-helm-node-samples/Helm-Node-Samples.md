author: Paul Kondrat
summary: PubSub+ Node.js Samples using Helm / Kubernetes with a Desktop Windows Dev Environment
id: helm-node-samples
tags:
categories: Helm,, Kubernetes
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs

# PubSub+ Node.js Samples with Helm / Kubernetes

## Overview

Duration: 0:01:00

In a previous [CodeLab](https://codelabs.solace.dev/codelabs/helm-environment-setup) a desktop Kubernetes development environment was setup using Docker Desktop, Windows Subsystem for Linux, Helm and Visual Studio Code. That Codelab also used the environment to launch a dev instance of PubSub+ using the [PubSub+ Helm Charts](https://artifacthub.io/packages/search?page=1&ts_query_web=solace). This CodeLab will use the dev instance installed in the previous CodeLab to run some Node.js sample applications using Kubernetes and Helm.

## Step 1: Clone the Solace Node Sample Chart

Duration: 0:05:00

My colleague Ken Barr created a simple [chart](https://github.com/KenBarr/solace-node-sample) that launches the official Node image from Docker Hub, installs the Solace node.js API from NPM and clones the Solace node.js samples from github. To get started, clone the solace-node-sample repo from github. From your work directory execute the following command.

Note: If this is the first time using github from your WSL Ubuntu environment, you will need to setup your ssh keys to be able to authenticate with github.

```bash
git clone git@github.com:KenBarr/solace-node-sample.git
```

![Solace Node Sample Chart](./img/Annotation2020-05-04-192713.png)

The deployment.yaml file is where most of the work is done. In there you will see what looks a lot like a Kubernetes template however, there are some template functions surrounded by double braces scattered throughout. The Helm template functions can be used to insert strings extracted from the values.yaml file, do simple conditional formatting etc. You can find the details of the Helm template language in the [Helm docs](https://helm.sh/docs/chart_template_guide/). When you install a Helm chart, Helm will look at the templates, process all of the Helm template functions and render a Kubernetes template that is suitable for deployment.

Looking at the deployment.yaml file the key sequence is as follows:

```yaml
command:
  - sh
  - "-ec"
  - |
    apk update && apk upgrade && apk add --no-cache bash git openssh
    npm install solclientjs
    git clone https://github.com/SolaceSamples/solace-samples-nodejs
    cd solace-samples-nodejs
    npm init -y
    echo -e "#!/bin/bash\n node solace-samples-nodejs/src/basic-samples/TopicPublisher.js ws://{{.Values.psb.name}}:8008 publisher@default default" > publish.sh
    chmod +x publish.sh
    node src/basic-samples/TopicSubscriber.js ws://{{.Values.psb.name}}:8008 subscriber@default default
```

The fragment above does the following:

- Installs a few packages (bash, git and openssh)
- Installs the solace javascript api from npm (the base container image is the official node.js so, it comes with npm already installed)
- Clones the Solace node.js samples
- Writes out a shell script to publish a message
- Starts the subscriber

The code for the sample application that is going to run in the container can be found in [Solace Samples](https://github.com/SolaceSamples) on GitHub. The node.js samples are found in the [solace-samples-nodejs repo](https://github.com/SolaceSamples/solace-samples-nodejs). The container implements the [Publish/Subscribe](https://solace.com/samples/solace-samples-nodejs/publish-subscribe/) messaging pattern.

## Step 2: Install the Chart

Duration: 0:05:00

Before installing the chart, the values.yaml file needs to
be updated. In the previous step, you can see that the sample applications need the DNS ({{.Values.psb.name}}) name of the broker that the application is going to connect to. To get the dns name of the broker that was deployed in the previous code lab use the following command:

```bash
kubectl get services
```

![kubectl get services](./img/Annotation2020-05-04-192712.png)

Edit the values.yaml file and replace "MUST_SPECIFY_SERVICE_NAME" with the service name of the PubSub+ broker (in this case pubsubplus-dev-1587734193-pubsubplus-dev).

Now the chart is ready to be deployed. Change directory into the solace-node-samples and install the chart.

```bash
helm install solace-node-sample . -f values.yaml
```

![helm install solace-node-sample](./img/Annotation2020-05-04-192714.png)

## Step 3: Run the Node.js Sample Applications

Duration: 0:02:00

In this step we will use Visual Studio Code and the remote development extensions to attach to the node sample container and run the [sample applications](https://github.com/SolaceSamples/solace-samples-nodejs). If you haven't already done so, install the [Remote Development](https://code.visualstudio.com/docs/remote/remote-overview) extensions. Open a new Visual Studio Code window; the remote container extension unfortunately does not work with WSL at time of writing so, this will need to be done from Windows. Make sure that Kubectl is in your windows path (Docker Desktop should have done this during installation). Using the Kubernetes extension, right click on the "solace-node-sample" pod and select "Attach Visual Studio Code". This will open a new window inside the container using the Remote Container extension. Notice the in the bottom left corner of the new window it says "solace-node-sample".

![attach VSC](./img/Attach-VSC.png)

Split the terminal window and use the Remote Containers extension (click the remote containers icon on the left) to display the container logs by right clicking the container and selecting "Show Container Log".

![sample subscriber output](./img/VSC-Container-Log.png)

You can see that the subscriber application is running and ready to receive messages.

![sample subscriber output](./img/VSC-Container-Log2.png)

Execute the publish.sh script to publish a message and see that the messages was received by the subscriber app in the logs (the subscriber was started by the helm chart).

```bash
cd /
/solace-samples-nodejs/publish.sh
```

![sample publisher output](./img/VSC-Publish-Message.png)

## Takeaways

Duration: 0:04:00

In this codelab we have used the remote development capabilities of Visual Studio Code along with Helm and Kubernetes (supplied by Docker Desktop) to deploy some Solace sample applications. The sample applications were used to send and receive messages using a publish / subscribe messaging pattern. The Solace PubSub+ broker instance was deployed using the same environment in the [previous codelab](https://codelabs.solace.dev/codelabs/helm-environment-setup/).

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
