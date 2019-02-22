"""
Simple Linear Regression 
@author Amin Abbasnejad
"""
import numpy as np
import bigfloat as bg
from numpy.linalg import norm
from sklearn import linear_model
from sklearn.cluster import KMeans

# Splitting the data

train_data, test_data = sales.random_split(.8,seed=0)

Simple linear regression algorithm - Part 1

# To calculate the intercept and the slope of the regression line

# x is the input and y is the output
def simple_linear_regression(x, y):
    
    # compute the sum of input and output
    sum = x + y
    
    # compute the product of the output and the input and its sum
    product = x * y
    sum_of_product = product.sum()
    
    # compute the squared value of the input and its sum
    x_squared = x * x
    sum_x_squared = x_squared.sum()
    
    # use the formula for the slope
    numerator = sum_of_product - ((x.sum() * y.sum()) / x.size())
    denominator = sum_x_squared - ((x.sum() * x.sum()) / x.size())
    slope = numerator / denominator
    
    # use the formula for the intercept
    intercept = y.mean() - (slope * x.mean())
    
    return (intercept, slope)
	
"""We can test that our function works by passing it something where we know the answer.
 In particular we can generate a feature and then put the output exactly on a line:
 output = 1 + 1*input_feature then we know both our slope and intercept should be 1"""

 test_feature = graphlab.SArray(range(5))
test_output = graphlab.SArray(1 + 1*test_feature)
(test_intercept, test_slope) =  simple_linear_regression(test_feature, test_output)
print test_feature
print test_output
print "Intercept: " + str(test_intercept)
print "Slope: " + str(test_slope)


#So now it works let's build a regression model for predicting price based on sqft_living

sqft_intercept, sqft_slope = simple_linear_regression(train_data['sqft_living'], train_data['price'])

print "Intercept: " + str(sqft_intercept)
print "Slope: " + str(sqft_slope)

#Simple linear regression algorithm - Part 2

#To calculate the predicted output

def get_regression_predictions(input_feature, intercept, slope):
    # calculate the predicted values:
    predicted_values = intercept + (slope * input_feature)
    return predicted_values
	
# What is the predicted price for a house with 2650 sqft?

my_house_sqft = 2650
estimated_price = get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope)
print "The estimated price for a house with %d squarefeet is $%.2f" % (my_house_sqft, estimated_price)

# Residual Sum of Squares	

#RSS is the sum of the squares of the residuals which is the difference between the predicted output and the true output.

def get_residual_sum_of_squares(input_feature, actual_output, intercept, slope):
    # First get the predictions
    predicted_output = intercept + (slope * input_feature)

    # then compute the residuals (since we are squaring it doesn't matter which order you subtract)
    residuals = actual_output - predicted_output

    # square the residuals and add them up
    residuals_squared = residuals * residuals
    residual_sum_squares = residuals_squared.sum()

    return(residual_sum_squares)


rss_prices_on_sqft = get_residual_sum_of_squares(train_data['sqft_living'], train_data['price'], sqft_intercept, sqft_slope)
print 'The RSS of predicting Prices based on Square Feet is : ' + str(rss_prices_on_sqft)

# Function to predict the squarefeet of a house from a given price

def inverse_regression_predictions(output, intercept, slope):
    # solve output = intercept + slope*input_feature for input_feature. Use this equation to compute the inverse predictions:
    estimated_feature = (output - intercept) / slope
    return estimated_feature

# What is the estimated square-feet for a house costing $800,000?

my_house_price = 800000
estimated_squarefeet = inverse_regression_predictions(my_house_price, sqft_intercept, sqft_slope)
print "The estimated squarefeet for a house worth $%.2f is %d" % (my_house_price, estimated_squarefeet)	

#Estimate house price from no. of bedrooms

# Estimate the slope and intercept for predicting 'price' based on 'bedrooms'
bedrm_intercept, bedrm_slope = simple_linear_regression(train_data['bedrooms'], train_data['price'])
print "Intercept: " + str(bedrm_intercept)
print "Slope: " + str(bedrm_slope)

# Test Linear Regression Algorithm for Square feet and Bedrooms Model

# Which model (square feet or bedrooms) has lowest RSS on TEST data?

# Compute RSS when using bedrooms on TEST data:
get_residual_sum_of_squares(test_data['sqft_living'], test_data['price'], sqft_intercept, sqft_slope)	

# Compute RSS when using squarefeet on TEST data:
get_residual_sum_of_squares(test_data['bedrooms'], test_data['price'], bedrm_intercept, bedrm_slope)