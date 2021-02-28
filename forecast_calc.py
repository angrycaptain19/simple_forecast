

class ForecastCalc:
    # responsable for calculate the forecast
    # input: data for the prior months and weights
    # output: sales forecast for 3 next 3 months
    def __init__(self, previous_month1, previous_month2, previous_month3, previous_month4, weight):
        self.previous_month1 = previous_month1
        self.previous_month2 = previous_month2
        self.previous_month3 = previous_month3
        self.previous_month4 = previous_month4
        self.weight = weight
        print(f'Weights: {self.weight}')

    def forecast_calc(self):
        pass
        # calculate the sales forecast for next 3 months
        # month 1
        self.forecast_m1 = (self.previous_month1 * self.weight[0] + self.previous_month2 * self.weight[1] + self.previous_month3 *
                            self.weight[2] + self.previous_month4 * self.weight[3]) / (
                                       self.weight[0] + self.weight[1] + self.weight[2] + self.weight[3])
        # month 2
        self.forecast_m2 = (self.forecast_m1 * self.weight[0] + self.previous_month1 * self.weight[1] + self.previous_month1 *
                            self.weight[2] + self.previous_month3 * self.weight[3]) / (
                                       self.weight[0] + self.weight[1] + self.weight[2] + self.weight[3])
        # month 3
        self.forecast_m3 = (self.forecast_m1 * self.weight[0] + self.forecast_m2 * self.weight[1] + self.previous_month1 *
                            self.weight[2] + self.previous_month2 * self.weight[3]) / (
                                       self.weight[0] + self.weight[1] + self.weight[2] + self.weight[3])
        return self.forecast_m1, self.forecast_m2, self.forecast_m3

