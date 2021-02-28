# module to input weight for moving averages
# the user should choose 3 options


class WeightChoose:

    def __init__(self):
        self.option = 'A'

    def weight_choose(self):

        print('Choose the weights\n')
        print('Option A:   Period -1 = 50%    Period -2 = 25%    Period -1 = 15%    Period -2 = 10%')
        print('Option B:   Period -1 = 40%    Period -2 = 30%    Period -1 = 20%    Period -2 = 10%')
        print('Option C:   Period -1 = 30%    Period -2 = 30%    Period -1 = 20%    Period -2 = 20%')

        self.option = input('Input the Letter from or option: ')

        if self.option[0].upper() == 'A':
            weight_values = (.5, .25, .15, .1)
            return weight_values

        elif self.option[0].upper() == 'B':
            weight_values = (.4, .3, .2, .1)
            return weight_values

        elif self.option[0].upper() == 'C':
            weight_values = (.3, .3, .2, .2)
            return weight_values

        else:
            print('\n *** You input a wrong letter ***')
            exit()
