author: Tamimi
summary:
id: terraform-modules
tags: terraform
categories: terraform, solace
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/terraform-modules

# Solace Terraform Modules

## Unpacking the Power of Modules
Duration: 0:10:00

![Solace Terraformm Modules](./img/TF+Solace.png)

[Terraform modules](https://developer.hashicorp.com/terraform/language/modules) are a way to organize and reuse code in your Terraform configurations. They allow you to encapsulate a group of resources and their configuration into a single, reusable unit. This helps in managing infrastructure as code more efficiently, promoting DRY (Don't Repeat Yourself) principles, and making your Terraform codebase more manageable and scalable.

Terraform modules are versatile tools that can be used to define reusable configurations for various aspects of infrastructure. Let's say you want to abstract a broker queue or topic endpoint or an endpoint template configuration, or a rest delivery point configuration, or even broker VPN, authentication and authorization configuration then a module would be a perfect fit for this. 

### Benefits of using Terraform Modules

Like all things DRY, Terraform Modules has a lot of benefits including: 
1. Reusability - Modules can be reused across different projects and environments, saving time and effort. For instance, if you have a standard broker setup that you use in multiple environments, you can encapsulate this configuration into a module and use it wherever needed 

1. Consistency - Using modules ensures that best practices and standards are consistently applied across your infrastructure reducing the risk of misconfigurations and enhances security

1. Manageability - Breaking down complex infrastructure into smaller, manageable pieces makes it easier to understand and maintain. Each module can be developed, tested, and debugged independently, leading to more reliable infrastructure

1. Encapsulation - By exposing only the necessary inputs and outputs, modules encapsulate the details of the underlying resources. This abstraction simplifies the use of complex resources, making the overall configuration cleaner and more user-friendly.

1. Collaboration - Teams can work on different modules independently, enabling parallel development and faster delivery

Even tho Terraform modules promote best practices, enhance collaboration, and make your infrastructure more scalable and maintainable, it is critical to keep in mind the drawbacks from the introduced complexity to manage and handle these modules. By understanding both their benefits and potential drawbacks, you can effectively leverage Terraform modules to build robust and efficient infrastructure.

## Essential Terraform Modules Concepts
Duration: 0:10:00

Before talking about the new Solace PubSub+ Terraform Modules, lets cover some key concepts of Terraform Modules

### Module Structure

1. Root Module: This is the main module, typically the directory where terraform init is run. It serves as the entry point for defining the overall infrastructure

1. Child Modules: These are modules called by the root module or other modules. These child modules can be referenced by the root module or even by other modules, promoting a hierarchical and organized approach to managing complex infrastructure setups. This structure allows for efficient reuse, easier management, and greater modularity in your Terraform codebase

### Module Composition

1. Input Variables: Allow you to pass different values to the module, making it flexible and adaptable to various environments and use cases

1. Output Values: Allow you to expose specific values from the module facilitating the integration and reuse of these outputs in other parts of your configuration. 

1. Resources: The actual infrastructure components that the module will manage.

1. Local Values: Intermediate values used within the module for simplification and readability.

> aside positive
> This comprehensive approach to module composition ensures that your Terraform configurations are both robust and easy to maintain.

### Module Sources

Terraform module sources provide various options for sourcing modules, enhancing flexibility and collaboration in managing infrastructure. Modules can be sourced from local file paths, allowing you to use modules stored on your local machine or within your organization's internal network. Versioned repositories, such as GitHub or Bitbucket, enable you to maintain modules in a version-controlled environment, facilitating collaborative development and easy updates. The Terraform Registry offers a vast collection of publicly available modules, such as the [Solace Pubsub+ Terraform Modules](https://registry.terraform.io/namespaces/SolaceProducts), that can be readily used, promoting best practices and reducing development time.

Additionally, modules can be sourced from URLs, providing a way to directly reference modules hosted on web servers or other remote locations. These diverse sourcing options make it easy to integrate, reuse, and manage Terraform modules across different environments and teams.

## Solace PubSub+ Terraform Modules
Duration: 0:10:00

As of July 2024, Solace has released 10 modules that are a combination of the following five: 

1. `client module` - The Client module represents a client user entity, either a client username or authorization group.

1. `jndi module` - The JNDI module provides a wrapper for a JMS connection factory event broker object. More specifically, this module enables an application team member to create a connection factory object in the JNDI store of an event broker with minimal insight into all of the necessary Solace configuration components by only providing the resource-specific information.

1. `queue_endpoint module` - This feature simplifies the establishment of queues and endpoints by encompassing many of their potential dependencies as a single resource. The Queue Endpoint module represents a durable event broker endpoint to publish to, or consume from. In addition, it can also represent an endpoint template.

1. `rest_delivery module` - The Rest Delivery module represents REST delivery point (RDP), REST consumer, and queue binding configuration. More specifically, this module enables an application team member to create an RDP that connects to a consumer (for example, a public cloud) with minimal insight into all of the necessary Solace configuration components by only providing the resource-specific information.

1. `service module` - The Service module encapsulates Message VPN-level service configuration, including protocols, authentication and authorization settings, and resource limits. It defines and makes ACL and client profiles available for use.

## Example Usage

There are multiple ways the Solace PubSub+ Terraform Modules could be used, depending on the conventions followed by your team. One potential common practice is to reference the module in your `main.tf` file as follows: 

```
module "exclusive_queue" {
  # update with the module location
  source = "SolaceProducts/queue-endpoint/solacebroker"

  msg_vpn_name  = "default"
  endpoint_type = "queue"
  endpoint_name = "testEQ"

  # permission "consume" enables a messaging client to connect, read and consume messages to/from the queue
  permission = "consume"

  # access_type "exclusive" is the default queue access type. While it has been specified here for clarity, it is not strictly required.
  access_type = "exclusive"

  # ingress and egress are enabled by default in the module, no need to enable here
  # ingress_enabled = true
  # egress_enabled = true
}

output "provisioned_queue" {
  value       = module.exclusive_queue.queue
  description = "The provisioned queue resource"
}

```
With the following providers.tf file 

```
terraform {
  required_providers {
    solacebroker = {
      source = "registry.terraform.io/solaceproducts/solacebroker"
    }
  }
}

# Configure the Solace provider
provider "solacebroker" {
  username = var.semp_username
  password = var.semp_password
  url      = var.solace_url
}
```

run the following:
```
terraform init
terraform apply
```

And observe a couple of things:
1. Terraform will install the `solacebroker` provider defined in the `providers.tf` file
1. Terraform will install the `exclusive_queue` module defined in the `main.tf` file and configure it based on the input variables defined
1. Terraform will apply the configuration on the target broker


> aside positive 
> For a list of Solace Modules visit this page [https://registry.terraform.io/namespaces/SolaceProducts](https://registry.terraform.io/namespaces/SolaceProducts)

## Takeaways
Duration: 0:07:00

✅ Terraform modules are helpful for code reuse and scalability   
✅ Keep an eye on the solace community and the Solace terraform registry for the latest updates on the SolaceTerraform Modules    

To participate in the discussion on the Solace Community, feel free to comment on [this discussion post](https://solace.community/discussion/3515/solace-terraform-appliance-provider-modules-declarative-semp-now-generally-available)

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
