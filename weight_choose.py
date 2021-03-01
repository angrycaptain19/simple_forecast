# module to input weight for moving averages
# the user should choose 3 options


class WeightChoose:

    def __init__(self):
        self.option = 'A'

        print('Choose one option for the period weights\n')
        print('Option A:   Period -1 = 50%   Period -2 = 25%   Period -1 = 15%   Period -2 = 10%')
        print('Option B:   Period -1 = 40%   Period -2 = 30%   Period -1 = 20%   Period -2 = 10%')
        print('Option C:   Period -1 = 30%   Period -2 = 30%   Period -1 = 20%   Period -2 = 20%')

        self.option = input('Input the option letter: ').upper()

    def weight_choose(self):

        if self.option == 'A':
            weight_values = (.5, .25, .15, .1)
            return weight_values

        elif self.option == 'B':
            weight_values = (.4, .3, .2, .1)
            return weight_values

        elif self.option == 'C':
            weight_values = (.3, .3, .2, .2)
            return weight_values

        else:
            print('\n *** You input an invalid letter ***')
            exit()

