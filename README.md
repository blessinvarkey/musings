# aws-notes

# 1. Data Engineering

### Terminologies     
[S3](Fundamentals/S3-simple-storage-service.md) - Simple Storage Service   
ETL - Extract, Load, Transform  
EMR - Elastic Map Reduce    
Amazon Sagemaker    
Amazon FSx with Lustre       
Amazon Elastic File System   
Amazon EBS volumes   
Amazon Kinesis Data Streams   
Amazon Kinesis Video Streams  
Amazon Kinesis Data Firehose   
Amazon Kinesis Data Analytics   

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
Scatter plots      
Box plots      
Histograms      
Scatter matrix      
Correlation matrix      
Heatmaps      
Confusion matrix      

## 2.3 Analyze and visualize data    
### Terminologies    
Scaling   
Normalizing   
Dimensionality reduction      
Date formatting      
One-hot encoding      
Attribute Statistics    


