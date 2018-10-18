from range_key_dict import RangeKeyDict
from Tools import logger, maxsize, logging


class Color:
    def __init__(self, delta_pr):
        self.delta_pr = delta_pr

    def return_color(self):
        try:
            colors_set = RangeKeyDict({
                (-(maxsize), -20): 'density',
                (-20, -15): 'nitrogen',
                (-15, -10): 'marine',
                (-10, -5): 'lightblue',
                (-5, 0): 'bluewhite',
                (0, 5): 'white',
                (5, 10): 'paleyellow',
                (10, 15): 'lightorange',
                (15, 20): 'oxygen',
                (20, 25): 'red',
                (25, maxsize): 'ruby',

            })

            return colors_set[self.delta_pr]

        except KeyError as error:
            logging.error('Value:' + str(error) + ' out of range!')
            return 'white'
