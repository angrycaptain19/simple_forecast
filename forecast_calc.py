# Module to perform the forecast calculations

class ForecastCalc:
    # responsable for calculate the forecast
    # input: data for the prior months and weights
    # output: sales forecast for 3 next 3 months
    def __init__(self,
                 period,
                 weight
                 ):
        self.previous_month1 = period[3]
        self.previous_month2 = period[2]
        self.previous_month3 = period[1]
        self.previous_month4 = period[0]
        self.weight = weight
        self.forecast_m1 = 0
        self.forecast_m2 = 0
        self.forecast_m3 = 0

    def forecast_calc(self):

        # calculate the sales forecast for next 3 months
        # month 1
        self.forecast_m1 = (self.previous_month1 * self.weight[0] + self.previous_month2 * self.weight[1]
                            + self.previous_month3 * self.weight[2] + self.previous_month4 * self.weight[3])\
                           /\
                           ( self.weight[0] + self.weight[1] + self.weight[2] + self.weight[3])
        # month 2
        self.forecast_m2 = (self.forecast_m1 * self.weight[0] + self.previous_month1 * self.weight[1]
                            + self.previous_month1 * self.weight[2] + self.previous_month3 * self.weight[3])\
                           / \
                           (self.weight[0] + self.weight[1] + self.weight[2] + self.weight[3])
        # month 3
        self.forecast_m3 = (self.forecast_m1 * self.weight[0] + self.forecast_m2 * self.weight[1] +
                            self.previous_month1 * self.weight[2] + self.previous_month2 * self.weight[3])\
                           /\
                           (self.weight[0] + self.weight[1] + self.weight[2] + self.weight[3])


        return self.forecast_m1, self.forecast_m2, self.forecast_m3

