#================================================================================================
from snl_regression_quality.snl_regression import SnlRegression
from snl_regression_quality.modules.methods.reading_data import ReadingData
#=================================================================================================

#--------------------------------------------------------------------------------------------------
# 1): Initialization of input parameters:
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
# 2): Load and read data:
#--------------------------------------------------------------------------------------------------

x_values,y_values ,x_mean, y_mean = ReadingData(path_x_dataset,path_y_dataset,example=True).run()

#--------------------------------------------------------------------------------------------------
# 3): execute code:
#--------------------------------------------------------------------------------------------------

SnlRegression(x_values,y_values,x_mean,y_mean,model_form,significance_level).run()

