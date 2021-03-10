
# Blog

Topics on AI, some old, some new. Mostly created while making AWS-ML notes.   

| Topics        | Keywords |
| ------------- | :------------- | 
| DALL-E | |
| [GNN: Graph Neural Network](https://dataflowr.github.io/website/modules/graph1/) | |
| [GPT-3 : Generative Pre-trained Transformer 3](posts/GPT-3.md) | unsupervised learning, language prediction model |
| NERF: Neural Radiance Fields | |
| Paradigms of Machine Learning |  |
| PLM: Pre-trained Languge Model | | 
| ResNet: Residual Neural Network | | 
| Single Shot Multibox Detector | |
|T5: Text-to-Text Transfer Transformer||

# Papers
|[Toward Fairness in AI for People with Disabilities](https://arxiv.org/abs/1907.02227)||


# aws notes
The following notes are part of my ongoing aws exploration. 

Machine learning is used when: 
- tasks cannot be adequately solved using a simple (deterministic), rule-based solution.   
- you need to handle large scale problems.  

### Steps involved 
| Topics        | Notes|
| ------------- |:------ |
| 1. Create a Sagemaker notebook instance     | |
| 2. Create a Jupyter notebook  | (Set session and role)   |
| 3. Download or retrieve the data.     | |
| 4. Process / Prepare the data. |  [Exploratory Data Analysis](posts/Exploratory-Data-Analysis.md)/ Split into train, test and validation  | 
| 5. Save locally and upload the processed data to S3.   | save locally and as test, train validation.csv |
| 6. Train the chosen model   | Container, Estimators, Hyperparameters, using [CreateTrainingJob API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html))     |
| 7. Test the trained model |       |
| 8. Deploy the endpoint | |
| 9. Use the model    |   (send test data to evaluate results)    |
| 10. Clean up      |   |



### Terminologies
AWS Sagemaker-> Notebook Instance-> ml.t2.medium (Instance type)-> Any S3 bucket with Sagemaker (IAM Role)->Start-> Select New (button on the left)->terminal

```
cd SageMaker
git clone https://github.com/..(repository link)
exit
```
session - A session is a special object that allows you to manage data in S3 and create and train any machine learning models.  
role - The role/IAM role defines how data is stored. Session documentation can be found [here](https://sagemaker.readthedocs.io/en/latest/session.html). 
[Simple Storage Service](posts/S3-simple-storage-service.md).   
Hyperparameter tuning - Parameters which define the model architecture are referred to as hyperparameters and the process of searching for the ideal model architecture is referred to as hyperparameter tuning.
### Case Studies
[Netflix](posts/Case-Studies.md) 



### AWS Supervised Learning Algorithms List 
* Regression & Binary/multi-class classification: Factorization Machines Algorithm, K-Nearest Neighbors (k-NN) Algorithm, Linear Learner Algorithm, XGBoost Algorithm   
* Time-series forecasting: DeepAR Forecasting Algorithm   

Full list of AWS Sagemaker's built in Algorithms can be found [here](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). 


### Terminologies    
**S3 Bucket** A bucket is a container for objects stored in Amazon S3. Every object is contained in a bucket. Buckets are the fundamental containers in Amazon S3 for data storage.     
**Elastic Load Balance** - Elastic Load Balance automatically distributes incoming application traffic across multiple Amazon EC2 instances.   
**EC2 instance - Elastic Compute Cloud** An EC2 instance is nothing but a virtual server in Amazon Web services terminology. It is a web service where an AWS subscriber can request and provision a compute server in AWS cloud.  
**AWS Lambda** - is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. In AWS Lambda, the code is executed based on the response of events in AWS services such as add/delete files in S3 bucket, HTTP request from Amazon API gateway, etc. However, Amazon Lambda can only be used to execute background tasks.    

# Step 1. Data Engineering

### Terminologies     
S3 - Simple Storage Service: is a storage service, typically used to store large binary files. Amazon also has other storage and database services, like RDS for relational databases and DynamoDB for NoSQL.     

ETL - Extract, Load, Transform  
EMR - Elastic Map Reduce    
Amazon Sagemaker    
Amazon FSx with Lustre       
Amazon Elastic File System   
Amazon EBS volumes   
Amazon Kinesis Data Streams  - low latency streaming ingest at scale from click streams    
Amazon Kinesis Video Streams -  
Amazon Kinesis Data Firehose -  () loads streams into S3, Redshift, Elastic Search and Splunk 
Amazon Kinesis Data Analytics - performs real-time analytics on streams using SQL  

### Difference between AWS Glue and AWS EMR    
AWS Glue is designed to operate flexible ETL operations for big data analytics as a serverless platform. Amazon EMR is used for ETL operations that have fixed requriements and are ideal for onsite platforms. AWS Glue is has more cost attached to it, since its serverless.    

### API vs Endpoint
API refers to the whole set of protocols that allows communication between two systems while an endpoint is a URL that enables the API to gain access to resources on a server.


# Step 2. Exploratory Data Analysis   
## 2.1 Prepare data for modeling
1. Sanatize and prepare data for modeling - Using descriptive statistics to understand data better   
2. Perform feature engineering   
3. Analyse and Visualise data for ML   
4. Standardize language and grammar   
5. Make sure the data is on the same scale (e.g. either in cm or km)   
6. Make sure a column doesn’t include multiple features (e.g. temperature, cost, time all in one column!)   
7. Clean the data based on any outliers that may exist (points in dataset that lie at an abnormal distance from other values)   
8. Missing data needs to be handled   

### Terminologies    
Overall statistics  
Multivariate statistics      
Attribute Statistics     
Dataset generation   
Data augmentation   
Descriptive statistics   
Informative statistics   
Handling missing values and outliers   


## 2.2 Feature Engineering
1. Binary *categorical variable*, such as the yes/no target variable, can be easily encoded into 1s and 0s   
2. For *ordinal variables*, a map function in Pandas can be used to convert the text into numerical values (N/A=0, Low = 5, Medium = 10, High = 20)   
3. *Categorical variable* can be converted to numerical value using a map function.    
4. For *nominal variables* like home type, instead of encoding it to a numerical data, one hot encoding is better.    
5. For *nummerical variables* 1,2,3 vs 1M, 100M etc, data can be scaled using: Mean/variance standardization, MinMax scaling, Maxabs scaling, Robust scaling, Normalizer   

### Terminologies    
Scaling   
Normalizing   
Dimensionality reduction      
Date formatting      
One-hot encoding      
Attribute Statistics    

## 2.3 Analyze and visualize data    

### Terminologies   
Scatter plots      
Box plots      
Histograms      
Scatter matrix      
Correlation matrix      
Heatmaps      
Confusion matrix      


