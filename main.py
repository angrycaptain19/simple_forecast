from tabulate import tabulate

from chart_upload import ChartUpload
from display_intro import DisplayIntro
from forecast_calc import ForecastCalc
from weight_choose import WeightChoose
from forecast_plot import ForecastPlot

title = 'Historical and Forecasted data by Period\n(Weighted Moving Average)'
# generate the introduction on screen

display_intro = DisplayIntro()
display_intro.intro()

period = []

# get input from user

for i in range(4):
    n = i - 4
    p = float(input(f'Enter data for the period {n}: '))
    period.append(p)

weight = WeightChoose()
weight.weight_choose()

# call routine for forecast calculation - it returns a list of forecast
forecast = ForecastCalc(period,
                        weight.weight_choose()
                        )

# display the table on screen
table = [
    ['Period -4', period[0], weight.weight_choose()[3] * 100],
    ['Period -3', period[1], weight.weight_choose()[2] * 100],
    ['Period -2', period[2], weight.weight_choose()[1] * 100],
    ['Period -1', period[3], weight.weight_choose()[0] * 100],
    ['-----------', '-----------------------', '------------'],
    ['Period  1', round(forecast.forecast_calc()[0], 2)],
    ['Period  2', round(forecast.forecast_calc()[1], 2)],
    ['Period  3', round(forecast.forecast_calc()[2], 2)],
    ['-----------', '-----------------------', '------------']
]

# append sales forecast to period list - from [0] to [3] - previous data and [4] to [6] - forecasted
for i in range(3):
    period.append(round(forecast.forecast_calc()[i],2))



# create table and display on screen
print('\nTable: Realized and Forecasted by Period - WMA methodology\n')
headers = ["Period", "Real.& Forecasted", "Weight (%)"]
print(tabulate(table, headers, tablefmt="github"))


chart = ForecastPlot(title, period)
chart.plot_chart()

# upload to clould base service - and return the URL
chart_share = ChartUpload()
chart_share.share()


print(f'\nThe plotted chart can be viewed on: {chart_share.share()}')
print('\nProgram End!!!')




