import pandas as pd

data_file = pd.read_csv('tvmarketing.csv')


# Checking the data for different scenario

data_file.head()
data_file.tail()
data_file.info()
data_file.shape
data_file.describe()

# Importing seaborn for data visualise

import matplotlib as plt
import seaborn as sns

sns.pairplot(data_file)
             




