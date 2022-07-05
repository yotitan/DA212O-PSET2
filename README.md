[![DA212O-PSET2 CI](https://github.com/yotitan/DA212O-PSET2/actions/workflows/main.yml/badge.svg)](https://github.com/yotitan/DA212O-PSET2/actions/workflows/main.yml)

# DA212O-PSET2
## Boston Housing Price Regression

Dagshub repo: https://dagshub.com/yotitan/DA212O-PSET2

The Boston Housing Dataset is a derived from information collected by the U.S. Census Service concerning housing in the area of Boston MA. The following describes the dataset columns:

<ul>
<li>CRIM - per capita crime rate by town</li>
<li>ZN - proportion of residential land zoned for lots over 25,000 sq.ft.</li>
<li>INDUS - proportion of non-retail business acres per town.</li>
<li>CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)</li>
<li>NOX - nitric oxides concentration (parts per 10 million)</li>
<li>RM - average number of rooms per dwelling</li>
<li>AGE - proportion of owner-occupied units built prior to 1940</li>
<li>DIS - weighted distances to five Boston employment centres</li>
<li>RAD - index of accessibility to radial highways</li>
<li>TAX - full-value property-tax rate per $10,000</li>
<li>PTRATIO - pupil-teacher ratio by town</li>
<li>B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town</li>
<li>LSTAT - % lower status of the population</li>
<li>MEDV - Median value of owner-occupied homes in $1000's</li>
</ul>

The dataset was initially loaded using sklearn.datasets.load_boston, but now it is being tracked as .csv file using DVC.

We are trying to predict MEDV using other features.

For this, we have used Standard Scaler to normalize input features followed by fitting a Ridge Regression model.

DVC has been used to track raw data and setup a pipeline.
![image](https://user-images.githubusercontent.com/33491154/177386826-6f4ff921-a5f7-4275-bc6a-5e7d0055ba79.png)

MLFlow has been used to store instances of trained models.
![image](https://user-images.githubusercontent.com/33491154/177386913-0cd4ae8b-6342-4b73-9a29-bea55473f457.png)

Most of the development was done using Cloud9 on an AWS EC2 instance.
![image](https://user-images.githubusercontent.com/33491154/177388317-32e10e59-191d-4a63-b457-277fd3350b55.png)
