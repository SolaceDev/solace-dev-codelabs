# Advanced Event Mesh Adapter for SAP Integration Suite

## 1.0.0 (EA)

Early Access release for the Advanced Event Mesh Adapter.

### Installation

1. Follow the instructions in the [SAP documentation](https://help.sap.com/docs/integration-suite/sap-integration-suite/importing-custom-integration-adapter-in-cloud-foundry-environment#procedure) to upload and deploy this adapter.
2. Once the Adapter is uploaded and deployed in the intended Integration Suite Account, it should be available under Adapter Type as "PubSubPlusEA (Vendor: Solace)".

### Known Issues

* Topic subscriptions may need some characters to be HTML-encoded. e.g. Encode `>` as `%3E`.
* When `Acknowledgment Mode` is set to `Automatic On Exchange Complete`, the connected AEM broker must support NACKs (version 10.2.1 or greater).
