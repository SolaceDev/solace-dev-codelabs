author: Tal Avissar
summary: Trailblazer unusual db activity pattern demo
id: Trailblazer-unusual-db-activity
tags:
categories: attack
environments: Web
status: Published
feedback link: https://github.com/SolaceDev/solace-dev-codelabs/blob/master/markdown/Trailblazer-unusual-db-activity

# Trailblazer demo: Unusual db activity

## Overview

Duration: 0:05:00

Cloud Anomaly Detection
Trailblazer - An artificail inteligence agentless anomaly security engine that monitors cloud control plane api activity, detects threats, suspicious activities and abnormal behaviors.
Analyzing threat detections audit logs and tracking API sessions is no longer a challenge.
The Cloud Anomaly Detection feature does this work for you with zero human touch using unsupervised learming.


We want to explore and see detections (anomalies/incidents) from trailblazer anomaly engine related to Unusual Db activities such as dynamo db tables/databases.

From the same Principal (user, role, etc.) initiate API calls applying to multiple DB instances, engines, tables, snapshots, keyspaces and similar DBs-related resources (i.e. via RDS, DynamoDB, and other AWS DB services),
in roughly the same time (seconds), repeatedly over an extended period (roughly 15 minutes).
Persist an item to a DynamoDB table using Lambda function

This attack is using AWS Lambda function:
1. Contaminate dynamo db table with non relavant record rows
2. Scan dynamo db table for all data
3. Print data in table to sys log  :hushed:



## What you need: Prerequisites

Duration: 0:05:00

You need to have AWS Cloudformation account and access in order to run the cloud formation template.

There are two cloud formation template for each attack
1. Initialization phase cloud formation template which creates basic frofiling of anomaly engine on the suspected/inspected role
   The init phase should run at least for 24 hours before going into step 2

2. Attack demo cloud formation template which creates the actual attack using the role from step 1

### Roles configurations

> aside positive
> verify with your AWS admin you have the right permissions before running this CFT

> aside positive
> You will need user/role with the right permissions to run cloud formation templates


## Setting up the initialization phase in AWS Cloudformation

Duration: 0:10:00

The normal activity we set up is a lambda, which assumes a role and prints to the log.

### Steps to upload and run the CFT baseline

* Prerequists: make sure youre using the currect user with permission to run and create CF stack
* Navigate to CloudFormation > Stacks
* Click the Create Stack button
* Choose the option (with new resources)

Continuing choose the following options:
* Template is ready
* upload a template file
* Click the choose file button
* Choose the CFT-Trailblazer-Demo-Start-Unusual-DB-Activity.yaml
* Click the next button
* Enter unique descriptive stack name
* Click the next button
* check the checkbox of I acknowledge that AWS CloudFormation might create IAM resources
* Finish while click submit button

Wait for like 5 minutes until all resources are created

CFT needs to run for **at least 24 hours** to let Anomaly Engine getting solid base line profiles

After running the CFT you should see:
![Cloud formation after running](img/CFT.png)

Click the resources tab of the stack that ran the CFT you should see the following resources created in status CREATE_COMPLETE
- Event Bridge Rule
- Lambda function
- Lambda Role
- PermissionForLambdaEvent

![Resources created CFT](img/db-unusual-resources.png)

## Running the actual attack Cloud Formation table

The attack is a malicious lambda which uses the previous role,
the lambda starts to contiminate the db with useless data and scan the db to syslog.

> aside positive
> Before performing these steps verify that the baseline was run at least 24 hours before running CFT

Prepare your cloud formation in order to run db unusual activities attack

* Prerequists: make sure youre using the currect user with permission to run and create CF stack
* Navigate to CloudFormation > Stacks
* Click the Create Stack button
* Choose the option (with new resources)

Continuing choose the following options:
* Template is ready
* upload a template file
* Click the choose file button
* Choose the CFT-Trailblazer-Demo-Start-Unusual-DB-Activity.yaml
* Click the next button
* Enter unique descriptive stack name
* Click the next button
* Click the checkbox of I acknowledge that AWS CloudFormation might create IAM resources
* Click submit

## Verifying detection appear in ICS UI

Duration: 0:15:00

> aside negative
> After waiting for at least 15 minutes

Navigate to the ICS UI and refresh the page and perform the needed advanced filtering:
* Events Source=Rapid7

Verify you see detection of finding type
``` txt
API Activity: unusual change in count of unique actions
```

![threat findings](img/threatFindings.png)

## Remediation and recommendations
#### Social Engineering:
Preventing cyber social engineering involves a combination of education, awareness, and implementing security measures. Here are some strategies to help prevent cyber social engineering:
- Education and training
- Verify requests by contacting the supposed requester
- Use multi-factor authentication
- Use Strong passwords

#### Overpermissive Principles
To prevent overpermissive principles in AWS roles and users, regularly review IAM policies, adhere to the principle of least privilege, utilize IAM policy conditions, implement automated policy enforcement, and provide comprehensive training on IAM best practices.

#### Centralized Backups
Centralized backups consolidate data in one location, creating a single point of failure vulnerable to hardware issues or cyberattacks. In contrast, distributed backups spread data across multiple locations, enhancing resilience and reducing the risk of data loss.

## Demo removal
In order to remove the demo, follow these steps:
1. Log into the AWS account
2. Go to AWS CloudFormation
3. Delete CFT-Trailblazer-Demo-**Attack**-Start-Unusual-DB-Activity Cloud Formation Template
4. Delete CFT-Trailblazer-Demo-**Normal**-Base-Unusual-DB-Activity Cloud Formation Template


## Takeaways

Duration: 0:02:00

✅ Trailblazer created detection finding type of - unusual change in count of unique actions

✅ Trailblazer anomaly detection of resource name lambda.amazonaws.com

✅ Trailblazer created anomaly detection of resource name lambda.amazonaws.com

✅ Verify whether GuardDuty identified the attack and created detection ...

![Soly Image Caption](img/soly.gif)

Thanks for participating in this codelab! Let us know what you thought in the [Rapid7 Community Forum](https://rapid7.community/)! If you found any issues along the way we'd appreciate it if you'd raise them by clicking the Report a mistake button at the bottom left of this codelab.
