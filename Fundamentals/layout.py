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
