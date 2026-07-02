from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing(as_frame=True)
df = data.frame
X = df[['MedInc','HouseAge','AveRooms']]
y = df['MedHouseVal']
# Split Dataset
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=7)
# Train model
model = LinearRegression()
model.fit(X_train,y_train)
# Make predictions
y_pred = model.predict(X_test)
# Evaluate model performance
mse = mean_squared_error(y_test,y_pred)
print("Linear Regression MSE: ",mse)
