# Essentials for AWS

Its important to identify why you want to learn the service. 

Most IT firms use hardware to . Cloud computing enables firms (and individuals) to stop thinking about infrastructure as a hardware, and to use it instead as software. Cloud is not some esoteric concept, instead there are data centers (with each data center having thousands of servers) set up by AWS across 25 regions, with two or more data center in each region. More on it, later.  

AWS cloud is a set of resources that lets you quickly tear down and set up an infrastructure in a programmable way. The advantages of cloud computing includes: 
- Going global in minutes 
- Trade upfront expense for variable expense
- Benefit from massive economies of scale
- Stop guessing capacity 
- Increase speed and agility
- Stop spending money on running and maintaining data centers

____ has an interesting way to remember this. She uses ____ as an acronym to memorize. Do check out her linkedin learning course. 

## Breakdown of major services
Firewalls, ACLs, Administrators <-- Security --> Security groups, Network ACLs, AWS IAM
Router, Network pipeline, Switch <-- Networking --> Elastic Load Balancing, Amazon VPC
On-Premise servers <-- Servers --> AMI, Amazon EC2 instances 
DAS, SAN, NAS, RDBMS <-- Storage and databases --> Amazon EBS, Amazon S3, Amazon RDS

## Deployment Models 
There are three ways to implement AWS cloud: _On Premises_, _Hybrid_ and _on the Cloud_.  

## Data Centers
One or more data centers are also called Availability Zones, and in one region, multiple clusters of data centers (AZs) exists. For example: In Singapore ap-southeast-1, ap-southeast-1a and ap-southeast-1b.     
    - _AWS Outposts_: AWS Outposts provides hybrid/on-premises services 
    - _AWS Local Zones_: AWS Local Zones provides infrastructure and services closer to large metro cities where there is no AWS Region
    - _AWS Wavelength_: For 5G technology. 

## S3

## The three ways to get started
- AWS Management Console
- AWS Command Line Interface (AWS CLI)
- Software development kits (SDKs)


## The virtual server - EC2
- Elasticity
- Control 
- Flexibility 
- Integrated 
- Reliable 
- Secure 
- Inexpensive
- Easy

- On-Demand
- Reserved Instances
- Saving Plans
- Spot Instances

## Serverless computing with AWS Lambda
- Unmanaged services
- Managed services

### Lambda
- Fully managed compute service
- Runs stateless code
- Supports multiple languages 
- Runs your code on a schedule or in response to events (e.g changes to data in an Amazon S3 bucket or Amazon DynamoDB table)

_Use Cases_: Web applications, backends, data processing, chatbots, amazon alexa, IT automation

### Event Driven Architecture

From:
[image](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2021/02/01/Concept2.jpg)

To: 
[image2](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2021/02/01/Arch-Diagram2.jpg)

For more details, you can visit [here](https://aws.amazon.com/blogs/architecture/building-multi-partner-integration-on-aws-using-event-driven-architecture/). 


## ECS

## CloudWatch 
For maintaining logs

## S3 & Other storage options


### API Gateway
More on API Gateway can be found [here](https://aws.amazon.com/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker/).

### Elastic Load Balance:
Elastic Load Balancing automatically distributes incoming application traffic across multiple Amazon EC2 instances.

### EC2 Instance
An EC2 instance is like a remote computer running Windows or Linux and on which you can install whatever software you want, including a Web server running PHP code and a database server.

### Amazon S3
Amazon S3 is a storage service, typically used to store large binary files. Amazon also has other storage and database services, like RDS for relational databases and DynamoDB for NoSQL.

--------
### Amazon Rekognition
- Object and Scene Detection:
- Identifies objects and scenes
- provides confidence scores
- Uses object and scene detection to add features that search, filter, and curate large image libraries
- Facial Analysis (Face detection)
- Demographic data
- Facial Landmarks
- Image Quality
- Emotion expressed
- General Attributes
- Facial Pose
- Face Comparison
- e.g. Hotel: Identifying current guest or new guest
- Facial Recognition
