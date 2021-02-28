from tabulate import tabulate
from display_intro import DisplayIntro
from forecast_calc import ForecastCalc
from weight_choose import WeightChoose

from forecast_plot import ForecastPlot


# generate the introduction on screen

display_intro = DisplayIntro()
display_intro.intro()

# get input from user
previous_month1 = float(input('Sales or volume from Months -1: '))
previous_month2 = float(input('Sales or volume from Months -2: '))
previous_month3 = float(input('Sales or volume from Months -3: '))
previous_month4 = float(input('Sales or volume from Months -4: '))

weight = WeightChoose()
weight_choose = weight.weight_choose()

# call routine for forecast calculation
forecast = ForecastCalc(previous_month1,
                        previous_month2,
                        previous_month3,
                        previous_month4,
                        weight_choose)

# return a list of forecast
#print(forecast.forecast_calc())

# display the table on screen

table = [
         ['Period -4', previous_month4, weight.weight_choose()[3]],
         ['Period -3', previous_month3, weight.weight_choose()[2]],
         ['Period -2', previous_month2, weight.weight_choose()[1]],
         ['Period -1', previous_month1, weight.weight_choose()[0]],
         ['Period  1', forecast.forecast_calc()[0]],
         ['Period  2', forecast.forecast_calc()[1]],
         ['Period  3', forecast.forecast_calc()[2]]
        ]

headers = ["Period", "Realized / Forecasted", "Weight"]
print(tabulate(table, headers, tablefmt="github"))





