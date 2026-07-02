import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
# Performing EDA
data = fetch_california_housing(as_frame=True)
df = data.frame
# Inspect data
print(df.info())
print(df.describe())
# Visualize relationships
sns.pairplot(df,vars=['MedInc','AveRooms','HouseAge','MedHouseVal'])
plt.show()
# Check for missing values
print("Missing Values:\n",df.isnull().sum())

