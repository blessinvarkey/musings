# aws-notes

List of AWS Sagemaker's built in Algorithms can be found [here](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). 

### Terminologies     
Elastic Load Balance - Elastic Load Balance automatically distributes incoming application traffic across multiple Amazon EC2 instances.   
EC2 instance - Elastic Compute Cloud    

# 1. Data Engineering

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

### Difference between EC2 and AWS Lambda    

### Difference between AWS Glue and AWS EMR    
AWS Glue is designed to operate flexible ETL operations for big data analytics as a serverless platform. Amazon EMR is used for ETL operations that have fixed requriements and are ideal for onsite platforms. AWS Glue is has more cost attached to it, since its serverless.    


# 2. Exploratory Data Analysis   
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


