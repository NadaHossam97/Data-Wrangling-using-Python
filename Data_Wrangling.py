import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot
import seaborn as sns
from ucimlrepo import fetch_ucirepo 


adult = pd.read_csv(".\\adult.csv", header=0)

#handling missing values:

# replace "?" to NaN
adult.replace("?", np.nan, inplace = True)

# Check if there are any missing values in the entire dataset
missing_before_replacement = adult.isnull().sum()

# Print the missing values for each column
print("Missing values after replacement in each column:")
print(missing_before_replacement)

# Replace missing values in 'workclass' with the most frequent value
most_frequent = adult['workclass'].mode()[0]  # Get the mode
adult['workclass']=adult['workclass'].fillna(most_frequent)  # Replace missing values

# Replace missing values in 'Occupation' with the most frequent value
most_frequent = adult['occupation'].mode()[0]  # Get the mode
adult['occupation']=adult['occupation'].fillna(most_frequent)  # Replace missing values

# Replace missing values in 'native-country' with the most frequent value
most_frequent = adult['native-country'].mode()[0]  # Get the mode
adult['native-country']=adult['native-country'].fillna(most_frequent)  # Replace missing values

# Check if there are any missing values in the entire dataset
missing_after_replacement = adult.isnull().sum()

# Print the missing values for each column
print("Missing values after replacement in each column:")
print(missing_after_replacement)

#Data Normalization to range from 0 to 1 
adult['age']=adult['age']/adult['age'].max()
adult['fnlwgt']=adult['fnlwgt']/adult['fnlwgt'].max()
adult['education-num']=adult['education-num']/adult['education-num'].max()
adult['capital-gain']=adult['capital-gain']/adult['capital-gain'].max()
adult['capital-loss']=adult['capital-loss']/adult['capital-loss'].max()
adult['hours-per-week']=adult['hours-per-week']/adult['hours-per-week'].max()

#Creating dummies for categorical varibales
dummies=pd.get_dummies(adult,columns=['workclass','education','marital-status','occupation','relationship','race','sex'])



