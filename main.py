from tabulate import tabulate
from display_intro import DisplayIntro
from forecast_calc import ForecastCalc
from weight_choose import WeightChoose
from forecast_plot import ForecastPlot

title = 'forecast Plot'
# generate the introduction on screen

display_intro = DisplayIntro()
display_intro.intro()

period = []

# get input from user
for i in range(4):
    print(i)
    n = i - 4
    p = float(input(f'Sales or volume from Months {n}: '))
    period.append(p)
print(period)

weight = WeightChoose()
weight.weight_choose()

# call routine for forecast calculation
forecast = ForecastCalc(period,
                        weight.weight_choose()
                        )

# return a list of forecast

# display the table on screen
table = [
    ['Period -4', period[0], weight.weight_choose()[3] * 100],
    ['Period -3', period[1], weight.weight_choose()[2] * 100],
    ['Period -2', period[2], weight.weight_choose()[1] * 100],
    ['Period -1', period[3], weight.weight_choose()[0] * 100],
    ['-----------', '-----------------------', '------------'],
    ['Period  1', round(forecast.forecast_calc()[0], 2)],
    ['Period  2', round(forecast.forecast_calc()[1], 2)],
    ['Period  3', round(forecast.forecast_calc()[2], 2)]
]

# append sales forecast to period list - from [0] to [3] - previous data and [4] to [6] - forecasted
for i in range(3):
    period.append(round(forecast.forecast_calc()[i],2))
print(period)


# create table and display on screen
headers = ["Period", "Realized / Forecasted", "Weight (%)"]
print(tabulate(table, headers, tablefmt="github"))


chart = ForecastPlot(title, period)
chart.plot_chart()

