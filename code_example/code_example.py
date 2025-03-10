#================================================================================================
import matplotlib.pyplot as plt 

from snl_regression_quality.modules.methods.reading_data import ReadingData
from snl_regression_quality.modules.methods.scaling_data import ScalingData
from snl_regression_quality.modules.methods.remove_outlier import OutlierData
from snl_regression_quality.modules.metrics.calculate_assumptions import Assumptions
from snl_regression_quality.modules.metrics.calculate_quality import Quality
from snl_regression_quality.modules.methods.user_messages_initial import initial_message
#=================================================================================================

initial_message()

#--------------------------------------------------------------------------------------------------
# 1): Load and read data:
#--------------------------------------------------------------------------------------------------

path_x_dataset = 'dataP11NOX.csv'
path_y_dataset = 'dataP11NOY.csv'


x_values,y_values ,x_mean, y_mean = ReadingData(path_x_dataset,path_y_dataset,example=True).run()


#--------------------------------------------------------------------------------------------------
# 2): standardization
#--------------------------------------------------------------------------------------------------

x_scaling, y_scaling = ScalingData(x_mean, y_mean ).run()

#--------------------------------------------------------------------------------------------------
# 3): remove_outlier
#--------------------------------------------------------------------------------------------------

        
#model_form = "concave_increasing"
#model_form= "convex_increasing"
model_form= "concave_decreasing"
#model_form = "convex_decreasing" 

x_deescalated, y_deescalated, indexes = OutlierData(model_form,x_scaling, y_scaling,x_mean, y_mean).run()

# plt.plot(x_descalated, y_deescalated, 'o', color ='blue', label ="optimized data")
# plt.plot(x_descalated, y_mean[indexes], 'o', color ='red', label ="data Without Outliers")
# plt.legend()
# plt.show()

#--------------------------------------------------------------------------------------------------
# 3): calculate Assumptions:
#--------------------------------------------------------------------------------------------------

significance_level = 0.05
enable_assumptions = Assumptions(y_mean,indexes,y_deescalated,significance_level).run()
  
#--------------------------------------------------------------------------------------------------
# 3): calculate Quality:
#--------------------------------------------------------------------------------------------------

Quality(y_values,x_mean,y_mean,indexes,x_deescalated,y_deescalated,significance_level,model_form).run()

