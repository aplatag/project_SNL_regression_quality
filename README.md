# Simple No Linear Regression:
<div align="justify">
An analysis of the quality of the regression is carried out.
First, simple linear regression assumptions are implemented. The assumption of outliers is made by eliminating samples whose absolute value of standardized and studentized residuals is greater than 3. The assumption of normality is carried out with the Shapiro-Wilk statistical test. The Breusch-Pagan statistical test is used for homoscedasticity. The Durbin-Watson test is used for the assumption of independence and the F test for linearity.
Regarding the quality of the simple linear regression, the dynamic range is calculated as the difference of the highest and lowest value of the response variable y. The sensitivity is obtained from ordinary least squares (OLS). The resolution is known through the statistical method of ANOVA to determine if there is a significant difference between the two consecutive values of the variable to be predicted with the smallest difference. Cross validation with k=10 and rmse as a metric is used to calculate accuracy.
</div>

<p align="center">
    <img src="https://raw.githubusercontent.com/aplatag/project_SNL_regression_quality/main/img/RlinealMW.jpeg" alt="methodology" 
     width="500" >
</p>
<div align="center">
Figure 1. Flowchart of the proposed methodology.
</div>


## Table of Contents
- [Simple No linear regression assumptions](#simple-No-linear-regression-assumptions)
- [Simple No linear regression quality](#simple-No-linear-regression-quality)
- [Database structure](#database-structure)
- [Installation](#installation)
- [Code example](#code-example)



## Simple No linear regression assumptions

1.  **Outlier**: The term anomaly indicates that there is data that deviates significantly from the rest.
2. **Normality**: refers to the normal distribution of errors or residuals.
3. **Homoscedasticity**:  is another simple linear regression assumption and indicates whether the variance of the residuals is the same across different groups in the database.
4. **Independence**:  refers to the absence of temporal correlation between residuals.


## Simple No linear regression quality

1.	**Dynamic range**: is defined as the range of values of the variable to be predicted within which linearity exists.
2.	**Maximum Sensitivity**: is defined as the maximum value of the change in the variable to be predicted with respect to the predictor.
3.	**Resolution**: is the ability of the measurement system to faithfully detect and indicate small changes in the characteristics of the measurement result.
4.	**Accuracy**: is the degree of agreement between the result of a measurement and a true value of the measurand.

## Database structure
<div align="justify">
The "snl_exp_regression_quality" program works with two databases. The first database contains all repetitions for the variable X (see Figure 2(a)), and the second database contains all repetitions for the variable Y (see Figure 2(b)). Figure 2 illustrates an example of how to organize the data to use the program effectively.
</div>


<p align="center">
    <img src="https://raw.githubusercontent.com/aplatag/project_SNL_regression_quality/main/img/example_dataset.png" alt="database" width="500" >
</p>
<div align="center">
Figure 2. Example: (a) database for X, and (b) database for Y.
</div>

## Installation

Instructions on how to install the project. For example:
```bash

pip install snl-exp-regression-quality
```
## Code example
For instance, the following code can be executed in Google Colab. Simply copy and paste it into a new Colab notebook.
```bash

#--------------------------------------------------------------------------------------------------
# 1): Load libraries:
#--------------------------------------------------------------------------------------------------
from snl_regression_quality.snl_regression import SnlRegression
from snl_regression_quality.modules.methods.reading_data import ReadingData


#--------------------------------------------------------------------------------------------------
# 2): Initialization of input parameters:
#--------------------------------------------------------------------------------------------------

path_x_dataset = 'data_X.csv'
path_y_dataset = 'data_Y.csv'
significance_level = 0.05

# Uncomment a Single Model to Run:

#model_form = "concave_increasing"
#model_form= "convex_increasing"
#model_form = "convex_decreasing" 
model_form= "concave_decreasing"

#--------------------------------------------------------------------------------------------------
# 3): Load and read data:
#--------------------------------------------------------------------------------------------------

x_values,y_values ,x_mean, y_mean = ReadingData(path_x_dataset,path_y_dataset,example=True).run()

#--------------------------------------------------------------------------------------------------
# 4): execute code:
#--------------------------------------------------------------------------------------------------

SnlRegression(x_values,y_values,x_mean,y_mean,model_form,significance_level).run()


```




        