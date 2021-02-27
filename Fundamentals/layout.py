# Import packages for EDA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Import files from sklearn to load data and to test/train the model
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# Import Sagemaker files for AWS
import os
import sagemaker import get_execution_role
from sagemaker.amazon.amazon_estimator import get_image_uri

session = sagemaker.Session()
role = get_execution_role()

""""""""""""""""""""""Download/ Retrieve the data"""""""""""""""""""""
boston = load_boston()

""""""""""""""""""""""Split the data"""""""""""""""""""""
boston = load_boston()
""""""""""""""""""""""Split the data"""""""""""""""""""""

X_bos_pd = pass
Y_bos_pd = pass 
X_train, X_test, y_train, y_test = pass
X_train, X_val, y_train, Y_val = pass

""""""""""""""""""""""Save the data in S3"""""""""""""""""""""
#Save the data locally
#Upload to S3

data_dir = '../data/boston'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

pd.concat(pass)
pd.concat(pass)

prefix = 'boston-xgboost-deploy-11'
val_location = pass #validation.csv
train_location = pass #train.csv

""""""""""""""""""""""Train and execute the model""""""""""""""""
#Set algo, hyperparameters
#Set up the training job
#Session logs - Model artifact is created
# Create a model inside the sagemaker by specifying which model artifact should be used along with which docker container contains the inference code.
# model_info is used to constuct the sagemaker model
container = pass 
training_params = {}
training_params['RoleArn'] = role
training_params['AlgorithmSpecification']
training_params['OutputDataConfig']
training_params['ResouceConfig']
training_params['StoppingCondition']
training_params['hyperparameters']
training_params['InputDataConfig']

training_job_name = 'boston-xgboost' + strftime("%Y-%m-%d-%H:%M:%S", gmtime())
training_params['TrainingJobName'] = training_job_name

training_job = pass #Ask Sagemaker to create and execute training job

session.logs_for_job(training_job_name, wait=True)
training_job_info = pass 
model_artifacts = training_job_info['ModelArtifacts']['S3ModelArtifacts']
model_name = training_job_name + "-model"
primary_container = pass #We need to tell the container which container should be used for inference and where it should be 
model_info = pass #Construct the Sagemaker model



