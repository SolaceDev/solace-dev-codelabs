
author: ChristianHoltfurth
summary: Prerequisites : This code lab walks the participant through the prerequisites to the experience of using SAP AEM to event enable their SAP ecosystem and workflows
id: sap-aem-int-prerequisites
tags: SAP, AEM, Event Portal, SAP BTP, CAPM, CPI, Cloud Integration
categories:
environments: Web
status: Hidden
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/sap-aem-int-prerequisites

# Event Enable SAP Using SAP Advanced Event Mesh - Prerequisites

Overall Duration: 0:41:00

## What you'll learn: Overview

Duration: 0:01:00

Prerequisites.
Topics covered :
- Prerequisites for participating in the Advanced Event Mesh Rapid Pilot Workshops

## What you need: Prerequisites

Duration: 0:10:00

As part of the workshop we will be deploying a couple of event driven scenarios in **your** environment.
Please note that in order to participate you will need to be ready to use the following services in your own landscape:
- SAP Integration Suite, advanced event Mesh
- SAP Integration Suite
- SAP Build Workzone, standard edition
- SAP Workflow Management
- SAP Business Application Studio
- SAP Cloud Foundry
- Asapio Cloud Integration with Advanced Event Mesh or Solace connector

Follow this guide if you are looking for details on how to complete these prerequisites.

>aside negative Please note hat you will also need some people/colleagues that have access to these services to follow along with the workshop.

In addition it is advised to have some people from your organisation in the workshop that have some knowledge/experience with these services as it will help with following along the instructions

## Requesting an Asapio Cloud Integration Trial license

Duration: 0:10:00

Asapio are offering free 30-day trials for those participating in the AEM Rapid Pilot workshops. Please click on the link below and request a trial license for the Asapio Cloud Integrator + Advanced Event Mesh or Solace connector.

[Request Asapio Trial license](https://protect-us.mimecast.com/s/g1YTCR6nxjIrnKJri9FGqr?domain=asapio.com/)


## Starting Services in SAP BTP

Duration: 0:10:00

TODO: explain steps.

## Testing Connectivity/Access to AEM

Duration: 0:05:00

The AEM broker UI runs on a non-standard web port per default. This can sometimes cause access issues when enterprises are tightly controlling internet access and forcing everything through an internet/http proxy.
If that is the case in your enterprise, please request a rule to to be added to allow access to hosts running on `*.messaging.solace.cloud:943` (on port 943).

Alternatively you can switch the ports of the broker service when you are starting those during the workshop to have the UI run on standard port 443. You will just have to swap our web messaging port to a different port then (e.g. 943 - if you just want to swap those two.)

You can test if your enterprise is blocking access to non-standard ports by clicking on the following link:

[AEM broker UI](https://mr-connection-qhgik3f2ezp.messaging.solace.cloud:943/)

If you see a login screen, you're good!
If not, check with your security team to allow access as described above!

## Takeaways

Duration: 0:05:00

✅ If you have completed all the prerequisites in this lab, then you should be good to go for our AEM Rapid Pilot workshop! <br>
✅ Congratulations and looking forward to seeing you there!<br>

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
