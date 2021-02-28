from typing import Tuple

from display_intro import DisplayIntro
from forecast_calc import ForecastCalc
from forecast_plot import ForecastPlot

# generate the introduction on screen
display_intro = DisplayIntro()
display_intro.intro()

# get input from user
previous_month1 = float(input('Sales or volume from Months -1: '))
previous_month2 = float(input('Sales or volume from Months -2: '))
previous_month3 = float(input('Sales or volume from Months -3: '))
previous_month4 = float(input('Sales or volume from Months -4: '))

# define the weight
weight = (50, 30, 10, 10)

# call routine for forecast calculation
forecast = ForecastCalc (previous_month1,previous_month2,previous_month3, previous_month4, weight)
print(forecast.forecast_calc())




























