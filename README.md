# California Housing Price Prediction using Exploratory Data Analysis (EDA) and Linear Regression

## Project Overview

This project explores the California Housing dataset using Exploratory Data Analysis (EDA) and builds a Linear Regression model to predict median house prices. The analysis focuses on understanding the dataset, visualizing relationships between variables, and training a predictive machine learning model.

## Dataset

The dataset was loaded using the `fetch_california_housing()` function from the `scikit-learn` library.

It contains information collected from the 1990 U.S. Census in California, with features such as:

* Median Income (`MedInc`)
* House Age (`HouseAge`)
* Average Rooms (`AveRooms`)
* Average Bedrooms (`AveBedrms`)
* Population (`Population`)
* Average Occupancy (`AveOccup`)
* Latitude (`Latitude`)
* Longitude (`Longitude`)

**Target Variable:**

* Median House Value (`MedHouseVal`)

## Technologies Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib
* Scikit-learn

## Exploratory Data Analysis (EDA)

To better understand the dataset, the following analyses were performed:

### Dataset Information

The `df.info()` method was used to:

* Inspect the dataset structure.
* View data types.
* Check for missing values.
* Determine the total number of observations and features.

### Descriptive Statistics

The `df.describe()` method was used to generate summary statistics, including:

* Mean
* Standard deviation
* Minimum and maximum values
* Quartiles (25%, 50%, and 75%)

These statistics helped identify the distribution and range of each numerical feature.

## Data Visualization

A **Seaborn Pairplot** was used to visualize relationships between variables.

The pairplot helped:

* Explore correlations between features.
* Observe data distributions.
* Identify potential linear relationships.
* Detect possible outliers.

## Machine Learning Model

After completing EDA, a **Linear Regression** model was built to predict median house values.

The workflow included:

1. Splitting the dataset into training and testing sets.
2. Training a Linear Regression model using the training data.
3. Making predictions on the test dataset.
4. Evaluating the model using regression performance metrics.

## Project Workflow

1. Load the California Housing dataset.
2. Convert the dataset into a Pandas DataFrame.
3. Perform exploratory data analysis using:

   * `df.info()`
   * `df.describe()`
4. Visualize feature relationships using Seaborn's `pairplot`.
5. Split the data into training and testing sets.
6. Train a Linear Regression model.
7. Generate predictions and evaluate model performance.

## Conclusion

This project demonstrates a complete introductory machine learning workflow, starting with data exploration, followed by visualization and predictive modeling. The EDA provided valuable insights into the dataset, while the Linear Regression model established a baseline for predicting California housing prices.

## Author

**Vedline Ochieng**
