# generate a forecast plot based on results
# save to a file

import matplotlib.pyplot as plt
import matplotlib
import os

class ForecastPlot:


    def __init__(self, title, period):
        self.title = title
        self.period = period
        self.x_period = [-4, -3, -2, -1, 0, 1, 2]

    # will plot the chat
    # input prior sales and forecasted sales (y axis)
    # Months -4 to +3 (X axis)
    # output: plot a chart and save into a file
    def plot_chart(self):

        # define the bar color for the chart
        bar_color = ['#6ba05e',
                     '#6ba05e',
                     '#6ba05e',
                     '#6ba05e',
                     '#a5cec8',
                     '#a5cec8',
                     '#a5cec8'
                     ]

        fig, ax = plt.subplots()
        ax.bar(self.x_period, self.period, color=bar_color)
        #ax.axvspan(-.5,3, facecolor='#2ca02c', alpha = .1)
        fig.suptitle(self.title,
                     fontsize=11,
                     fontstyle='italic'
                     )
        ax.set(xlabel='Periods (n)', ylabel='Realized / Forecasted'
               )


        # save the plot in 'files' directory
        # change the directory
        working_dir = os.getcwd()

        # save the file
        fig.savefig(working_dir + '/file/'+ 'Forecast_WMA.png',
                    dpi = 100,
                    transparent=True
                    )

        plt.show()



