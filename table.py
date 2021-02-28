# module to create a table on screen
from forecast_calc import ForecastCalc


class Table(ForecastCalc):

    def __init__(self,
                 previous_month1,
                 previous_month2,
                 previous_month3,
                 previous_month4,
                 weight
                 ):
        ForecastCalc.__init__ (self, previous_month1)
        ForecastCalc.__init__ (self, previous_month2)
        ForecastCalc.__init__ (self, previous_month3)
        ForecastCalc.__init__ (self, previous_month4)
        self.previous_month2 = previous_month2
        self.previous_month3 = previous_month3
        self.previous_month4 = previous_month4
        self.weight = weight:

