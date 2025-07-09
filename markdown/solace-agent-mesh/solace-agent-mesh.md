author: Tamimi A
summary:
id: solace-agent-mesh
tags: 
categories: Solace, Agent Mesh, AI
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/solace-agent-mesh

# Getting started with Solace Agent Mesh over A2A

## What you'll learn: Overview

Duration: 0:05:00

## Introduction to the Solace Agent Mesh
Duration: 0:05:00


> aside negative
> This will appear in a yellow info box.


> aside positive
> This will appear in a green info box.

### What is Solace Agent Mesh?

### Key Components and Architecture

### Evolution of Event-Driven Architecture

### Key Benefits of Solace Agent Mesh

### Use Cases and Applications

### Resources
[Docs](https://solacelabs.github.io/solace-agent-mesh/docs/documentation/getting-started/introduction/)
<video id="_4IdRPBM2y8"></video>


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

## Solace Agent Mesh Components: Deep Dive
Duration: 0:05:00

### 1. Orchestrator
<video id="EAZcKkkfn-U"></video>

### 2. Agents
<video id="Sw3fKRcAbXo"></video>


### 3. Gateways
<video id="vZsdxAVW3Kg"></video>


### 4. Event Mesh

### 5. Plugins


### 6. Services & Tools
<video id="0_y5lDj7R8A"></video>


## Getting Started with Solace Agent Mesh
Duration: 0:05:00

### Prerequisites 

- Solace Event Broker
- Python 3.11+
- LLM Key

### Installation 

### Run

## Built-in Agents
Duration: 0:05:00

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


