author: Tamimi A
summary:
id: solace-agent-mesh
tags: 
categories: Solace, Agent Mesh, AI
environments: Web
status: Publish 
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/solace-agent-mesh

# Getting started with Solace Agent Mesh over A2A

## What you'll learn: Overview

In this codelab, you'll gain a foundational understanding of the [Solace Agent Mesh](https://solacelabs.github.io/solace-agent-mesh/docs/documentation/getting-started/introduction/). You'll explore the architecture, key components, and benefits of the Solace Agent Mesh, learning how it enables scalable, event-driven communication between AI agents and services. The introduction covers the evolution of event-driven architectures and highlights real-world use cases where agent mesh technology can be applied.

You'll dive into the details of the [A2A Protocol](https://a2a-protocol.org/latest/), discovering its design principles, core concepts, and how it standardizes agent communication for interoperability and extensibility. You'll also learn about the [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) and how it works with A2A to build and deploy advanced AI agents.

You'll then dive into the [Solace AI Connector](https://github.com/SolaceLabs/solace-ai-connector), a powerful tool designed to seamlessly integrate AI capabilities into your event-driven architecture, enabling you to create efficient pipelines that process events from your event mesh using AI and other components.

By the end of this codelab, you'll be equipped to get started with Solace Agent Mesh, including installation prerequisites, running built-in agents, and connecting external services through MCP. You'll understand how to develop custom agents, leverage plugins and tools, and build multi-agent systems that harness the power of event mesh and standardized protocols for robust, collaborative AI solutions.

![SAM Arch](img/SAM_arch.png)

Duration: 0:05:00

## Introduction to the Solace Agent Mesh
Duration: 0:15:00

### Problem statement
Building effective agentic systems presents a complex challenge that extends far beyond simply deploying AI models. AI Agents are siloed that operate in isolation, and are unable to effectively communicate or share capabilities across organizational boundaries. By definition and design, Agents are inherently domain-specific, designed to excel in narrow use cases but struggling to collaborate or leverage expertise from other specialized agents, creating fragmented AI ecosystems that fail to realize their collective potential.

To make intelligent decisions and respond to dynamic conditions, agentic systems must rely on event-driven actions that flow into the organization. While solving the core AI challenge represents only 20% of the effort, the remaining 80% involves the much more complex task of connecting AI models to the disparate data sources, legacy systems, APIs, and organizational knowledge that exist across isolated silos—making data accessibility and integration the true bottleneck in delivering practical AI value

> aside negative
> Without a framework like Solace Agent Mesh, connecting AI systems to siloed data sources can be extremely complex, requiring custom integration code and creating maintenance challenges.

### What is Solace Agent Mesh?

Solace Agent Mesh is a comprehensive open-source framework that empowers developers to build sophisticated, distributed AI systems. On a high level, Agent mesh provides developers with the following:

**Core Communication & Protocol**

- **Standardized A2A (Agent-to-Agent) Protocol**: A unified communication standard that enables seamless interaction between AI agents, regardless of their underlying implementation or deployment location
- **Event-Driven Architecture**: Built on the Solace Event Broker for asynchronous, scalable, and resilient agent communication
- **Topic-Based Routing**: Intelligent message routing that enables agents to discover and communicate with each other dynamically
- **Session Management**: Persistent conversation context across multi-turn interactions and complex workflows

**Data Integration & Connectivity**

- **Real-World Data Source Integration**: Pre-built connectors and tools to seamlessly connect AI agents to databases, APIs, file systems, and enterprise applications
- **Universal Gateway Support**: Multiple interface types including REST APIs, WebSockets, webhooks, and direct event mesh integration
- **Enterprise System Compatibility**: Native integration with HR systems (BambooHR, Workday), CRMs (Salesforce), collaboration tools (Confluence, Jira), and identity providers
- **Streaming Data Processing**: Real-time event processing capabilities for handling live data streams and IoT sensor feeds
- **Multi-Protocol Support**: Connect to systems using HTTP, MQTT, AMQP, WebSocket, and custom protocols

**Workflow Orchestration & Management**

- **Complex Workflow Orchestration**: Coordinate sophisticated multi-agent workflows with dependency management and parallel execution
- **Task Decomposition**: Automatically break down complex requests into manageable subtasks for specialized agents
- **Result Aggregation**: Intelligent collection and synthesis of results from multiple agents into cohesive responses
- **Error Handling & Recovery**: Built-in retry logic, circuit breakers, and graceful degradation for robust production deployments
- **Workflow Templates**: Pre-configured workflow patterns for common use cases like data analysis, document processing, and customer service

**Extensibility & Plugin Architecture**

- **Modular Plugin System**: Easily extend functionality through a rich ecosystem of community and commercial plugins
- **Custom Agent Development**: Comprehensive tools and templates for building domain-specific agents with specialized capabilities
- **Gateway Plugins**: Create custom external interfaces for unique integration requirements
- **Service Provider Plugins**: Standardized abstractions for integrating with backend systems and data sources
- **Tool Framework**: Extensible tool system that allows agents to perform actions and interact with external services

**AI Model & Provider Support**

- **Multi-Model Compatibility**: Support for all major AI providers including OpenAI, Anthropic, Google, Azure OpenAI, and local models
- **Model Abstraction**: Switch between different AI models without changing agent logic
- **Provider Failover**: Automatic failover between AI providers for high availability
- **Cost Optimization**: Intelligent model selection based on task complexity and cost considerations
- **Custom Model Integration**: Support for proprietary and fine-tuned models through flexible provider interfaces

**Development Tools & Framework**

- **Comprehensive CLI**: Full-featured command-line interface for project creation, management, and deployment
- **Configuration Management**: YAML-based configuration system with environment variable support and validation
- **Development Environment**: Hot-reload capabilities, debugging tools, and comprehensive logging for efficient development
- **Testing Framework**: Built-in testing utilities for unit testing, integration testing, and end-to-end workflow validation
- **Documentation Generation**: Automatic API documentation and configuration reference generation

**Security & Enterprise Features**

- **Multi-Authentication Support**: JWT, OAuth, API keys, and custom authentication mechanisms
- **Role-Based Access Control**: Fine-grained permissions and authorization for agents and resources
- **Identity Service Integration**: Seamless integration with enterprise identity providers and HR systems
- **Audit Trail**: Comprehensive logging and monitoring for compliance and security auditing
- **Data Encryption**: End-to-end encryption for data in transit and at rest

**Monitoring & Observability**

- **Real-Time Metrics**: Comprehensive performance monitoring with custom dashboards and alerting
- **Distributed Tracing**: End-to-end request tracing across the entire agent mesh
- **Health Monitoring**: Automatic health checks and status reporting for all components
- **Performance Analytics**: Detailed insights into agent performance, resource utilization, and workflow efficiency
- **Log Aggregation**: Centralized logging with correlation IDs for easy debugging and troubleshooting

**Scalability & Performance**

- **Horizontal Scaling**: Easily scale individual agents or entire agent meshes based on demand
- **Load Balancing**: Automatic distribution of tasks across multiple agent instances
- **Resource Management**: Intelligent resource allocation and optimization for optimal performance
- **Caching Strategies**: Built-in caching mechanisms for frequently accessed data and computations
- **Async Processing**: Non-blocking, asynchronous operations for maximum throughput

**Deployment & Operations**

- **Multi-Environment Support**: Seamless deployment across development, staging, and production environments
- **Container-Ready**: Docker and Kubernetes support for modern containerized deployments
- **Cloud-Native**: Native support for AWS, Azure, GCP, and hybrid cloud deployments
- **Infrastructure as Code**: Terraform and CloudFormation templates for automated infrastructure provisioning
- **CI/CD Integration**: Built-in support for continuous integration and deployment pipelines

**Use Case Enablement**

- **Conversational AI**: Build sophisticated chatbots and virtual assistants with multi-turn conversation support
- **Document Processing**: Automated document analysis, extraction, and processing workflows
- **Data Analytics**: Complex data analysis and reporting across multiple data sources
- **Customer Service**: Intelligent customer support systems with escalation and knowledge management
- **Business Process Automation**: End-to-end automation of complex business workflows
- **IoT & Real-Time Processing**: Real-time processing and analysis of IoT sensor data and events

**Developer Experience**

- **Rich Documentation**: Comprehensive guides, tutorials, and API references
- **Community Support**: Active community forums, Discord channels, and regular office hours
- **Example Projects**: Ready-to-run examples and templates for common use cases
- **Migration Tools**: Utilities for migrating existing AI applications to the SAM framework
- **IDE Integration**: Extensions and plugins for popular development environments

This comprehensive feature set makes Solace Agent Mesh the ideal choice for developers looking to build production-ready, scalable AI applications that can seamlessly integrate with existing enterprise infrastructure while providing the flexibility to grow and evolve with changing requirements.
> aside positive
> Solace Agent Mesh follows an event-driven architecture that decouples components, allowing them to be developed, deployed, and scaled independently.

### Key Components and Architecture

Solace Agent Mesh consists of several interconnected components that work together to create a distributed, event-driven ecosystem of collaborative AI agents.

1. **Solace Event Broker**
The central messaging backbone that provides intelligent topic-based routing, fault-tolerant delivery, and horizontal scaling for all Agent-to-Agent (A2A) protocol communications across the entire system.

2. **Gateways**
External interface bridges that translate diverse protocols (HTTP, WebSockets, Slack) into standardized A2A messages while handling authentication, authorization, and session management for outside systems.

3. **Agents**
Specialized AI processing units built on Google's Agent Development Kit that provide domain-specific intelligence, self-register for dynamic discovery, and access comprehensive tool ecosystems for complex task execution.

4. **Solace AI Connector**
The universal runtime environment that hosts and manages the complete lifecycle of all system components while bridging Google ADK capabilities with Solace event infrastructure through YAML-driven configuration.

5. **Google Agent Development Kit (ADK)**
The core AI framework that powers individual agents with LLM interactions, conversation memory management, artifact processing capabilities, and an extensible tool integration system.

6. **A2A Protocol & Agent Registry**
The standardized communication protocol and service discovery mechanism that enables seamless interaction, dynamic routing, and lifecycle management across all mesh components.

7. **Backend Services & Tools**
The foundational infrastructure layer providing multi-provider LLM access, extensible integrations for custom tools and APIs, persistent data storage, and cloud-native artifact management services.

> aside negative
> Without proper planning and understanding of the component roles, you might create overly complex architectures or miss opportunities to leverage the full power of the distributed agent ecosystem.


This workshop will help you understand how to leverage Solace Agent Mesh for your own AI applications, whether you're an AI enthusiast experimenting with new models or an enterprise developer building production systems.

### Resources

For more information and a deep dive on the Solace Agent Mesh, you can check out this video series 
<video id="_4IdRPBM2y8"></video>

## Use Cases and Applications
Duration: 0:05:00

Solace Agent Mesh is versatile and can be applied to various domains:

1. **Customer Service Augmentation**:
   - Intelligent chatbots that can access multiple backend systems
   - Real-time response generation based on customer data and history
   - Seamless handoff between AI agents and human agents

2. **Supply Chain Optimization**:
   - Monitoring and analyzing events across the supply chain
   - Predictive maintenance and inventory management
   - Automated decision-making based on real-time data

3. **Financial Services**:
   - Fraud detection through pattern analysis across multiple data streams
   - Personalized financial advice based on customer portfolio and market events
   - Regulatory compliance monitoring and reporting

4. **Healthcare**:
   - Patient monitoring and alert generation
   - Clinical decision support by accessing medical records and research data
   - Healthcare workflow optimization

5. **Smart Cities**:
   - Traffic management through real-time data analysis
   - Utility optimization based on usage patterns
   - Emergency response coordination

> aside positive
> By building on Solace Agent Mesh, you can focus on creating domain-specific agent intelligence rather than spending time on integration and communication infrastructure.


## Google Agent-to-Agent Protocol (A2A)
Duration: 0:07:00

The Agent-to-Agent (A2A) Protocol is Google's standardized communication protocol designed to enable seamless interaction between AI agents, regardless of their underlying implementation or hosting environment. It provides a common language for agents to discover each other, exchange information, delegate tasks, and collaborate on complex problems. This document explores the A2A protocol in detail, including its design principles, components, and implementation approaches.

> aside positive
> A2A is an open-source protocol, available for any developer or organization to implement. This open nature fosters a rich ecosystem of interoperable agents across different platforms and frameworks.

### Core Concepts

The A2A Protocol is built around several foundational concepts that define its structure and behavior:

#### Protocol Design Principles

A2A was designed with the following principles in mind:

1. **Standardization**: Provide a common interface for agent communication
2. **Interoperability**: Enable agents from different systems to work together
3. **Extensibility**: Support evolving agent capabilities
4. **Asynchronicity**: Handle long-running tasks and parallel operations
5. **Discoverability**: Allow agents to find and understand each other's capabilities
6. **Security**: Implement robust authentication and authorization

These principles ensure that A2A serves as a reliable foundation for building multi-agent systems.

#### Agent Cards

Agent Cards are metadata structures that describe an agent's capabilities, allowing other agents and systems to discover and understand how to interact with them. Key components include:

1. **Name**: A unique identifier for the agent
2. **Description**: A human-readable explanation of the agent's purpose
3. **Capabilities**: The specific tasks the agent can perform
4. **Input/Output Formats**: The data structures the agent expects and produces
5. **Authentication Requirements**: Security information for accessing the agent

Agent Cards are published to discovery endpoints, making them available to other agents in the ecosystem.

> aside negative
> Always validate Agent Cards from external sources, as malicious actors could potentially publish misleading Agent Cards to trick systems into inappropriate delegations.

#### Tasks

Tasks represent the work that agents perform. They include:

1. **Task ID**: A unique identifier for tracking
2. **Input**: The information provided to the agent
3. **Context**: Additional information about the task environment
4. **Artifacts**: Files or binary data associated with the task
5. **Delegation Path**: Information about how the task was routed

Tasks follow a lifecycle from creation through processing to completion or failure.

#### Events

Events represent the state changes and progress updates that occur during task execution:

1. **Status Updates**: Progress information about ongoing tasks
2. **Artifact Updates**: Notifications about new or modified files
3. **Error Events**: Information about failures or issues
4. **Completion Events**: Signals that a task has finished

Events enable asynchronous monitoring of task progress, which is essential for long-running operations.

#### Artifacts

Artifacts are files or binary data that agents can exchange:

1. **Content**: The actual data (text, image, audio, etc.)
2. **Metadata**: Information about the artifact (type, creation time, etc.)
3. **Versioning**: Tracking changes to artifacts over time
4. **References**: Ways to refer to artifacts across the system

Artifacts enable agents to share rich, structured data beyond simple text messages.

> aside positive
> The A2A Protocol continues to evolve with the needs of the agent ecosystem. 

### Where to learn more 

The Agent-to-Agent (A2A) Protocol provides a standardized foundation for building interconnected AI agent systems. By enabling discovery, task delegation, and asynchronous communication, A2A facilitates the creation of sophisticated multi-agent workflows that can tackle complex problems through collaboration.

As the ecosystem of AI agents continues to grow, A2A offers a common language that allows these agents to work together seamlessly, regardless of their underlying implementation or hosting environment. This interoperability is key to unlocking the full potential of agent-based AI systems.

To learn more about A2A, navigate to the [A2A Documentation](https://a2aproject.github.io/A2A/latest/)

## Agent Development Kit (ADK)
Duration: 0:05:00

Google's Agent Development Kit (ADK) offers developers a comprehensive framework to build, evaluate, and deploy sophisticated AI agents with minimal friction. ADK provides the essential building blocks—from LLM integration and tool execution to session management and artifact handling—that enable both conversational and non-conversational agents capable of complex reasoning, planning, and task execution. 

The A2A Protocol works seamlessly with Google's Agent Development Kit (ADK):

1. **ADK A2A Tools**: Built-in tools for A2A communication
2. **Protocol Translation**: Converting between ADK events and A2A messages
3. **Agent Deployment**: Exposing ADK agents through A2A endpoints
4. **Multi-Agent Systems**: Building networks of ADK agents communicating via A2A

For more information on ADK integration, see the [ADK documentation](https://google.github.io/adk-docs/).

## Getting Started with Solace Agent Mesh
Duration: 0:05:00

### Prerequisites 

- [Optional] [Solace Event Broker](https://solace.com/products/event-broker/software/getting-started/)
- Python 3.11+
- LLM Key

### Installation 

#### Create and activate a Python virtual environment

MacOS/Linux
```
mkdir solace-agent-mesh-demo
cd solace-agent-mesh-demo
python3 -m venv venv
source venv/bin/activate
```
Windows
```
venv/Scripts/activate
```

> aside positive
> Note: on a Linux machine, depending on the distribution you might need to `apt-get install python3-venvinstead`. Alternatively, you can use `pyenv` to manage multiple versions of python

#### Install the Solace Agent Mesh Community Edition

```
pip install https://github.com/SolaceDev/solace-dev-codelabs/raw/master/markdown/solace-agent-mesh/solace_agent_mesh-1.0.0-py3-none-any.whl

```

### Initialize Solace Agent Mesh

> aside positive 
> To use the solace agent mesh, you can activate it by typing `solace-agent-mesh` or simply `sam`

In the newly created directory, initialize a new instance of an agent mesh project

```
sam init
```
You will then be presented with the following output 
```
Initializing Solace Application Project...
Would you like to configure your project through a web interface in your browser? [Y/n]:

```
Press `Y` and proceed with the frontend initialize interface

![SAM Init](img/saminit.png)

From here, choose option 1: "Get started quick" to spin up an instance of the Agent Mesh without the Solace Broker   

In this tutorial, we will choose to configure the agent mesh without the Solace Broker which will use in-memory queues. 

> aside negative
> Note that The simple setup with the recommended setup is not meant for production ready development and proof of concept project that require high performance and multiple Agentic workflow interactions

![SAM provider](img/aiprovider.png)

Select the following:

- LLM Provider: Google Gemini
- LLM API Key: `Insert Key Here`
- LLM Model Name: `Choose model name`

Review and Initialize

![SAM final](img/finalinit.png)

### Run Solace Agent Mesh

Now back to your terminal and execute the following command

```
sam run
```
![SAM Intro](img/samintro.png)

Viola! You are up and running with the Solace Agent Mesh!

## Built-in Agents
Duration: 0:05:00

As mentioned earlier, Agents are specialized processing units built around Google's ADK. They provide domain-specific knowledge and capabilities and can operate independently and be deployed separately.

In Solace Agent Mesh, there are multiple ways to write an agent:
1. Using built-in templates,
1. via MCP, or 
1. custom built

Adding new agent could be done in one of the following ways
1. Using cli command `sam add agent` 
1. Using the GUI


Lets go ahead and add a general purpose agent

In this tutorial we will be using the GUI. To spin up the agent building interface, execute this command from your terminal

```
sam add agent --gui
```

![SAM final](img/addagentinit.png)

Fill in the required fields as per the screenshot below. 

Use the following prompt in the `Instructions` section

```


```


## Connecting Google Maps via MCP
Duration: 0:05:00

## Connecting Google Search via MCP
Duration: 0:05:00

## A2A Agents
Duration: 0:05:00

## Custom Agents
Duration: 0:05:00

## Next Steps
Duration: 0:05:00

## Takeaways

Duration: 0:07:00

✅ < Fill IN TAKEAWAY 1>   
✅ < Fill IN TAKEAWAY 2>   
✅ < Fill IN TAKEAWAY 3>   

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Solace Community Forum](https://solace.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.


