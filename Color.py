from range_key_dict import RangeKeyDict
from Tools import logger, maxsize, logging


class Color:
    def __init__(self, delta_pr, config):
        self.delta_pr = delta_pr
        self.config = config

    def return_color(self):
        if self.config:
            try:
                colors_set = RangeKeyDict({
                    (float(self.config['density']['bottom_range']), float(self.config['density']['top_range'])): 'density',
                    (float(self.config['nitrogen']['bottom_range']), float(self.config['nitrogen']['top_range'])): 'nitrogen',
                    (float(self.config['marine']['bottom_range']), float(self.config['marine']['top_range'])): 'marine',
                    (float(self.config['lightblue']['bottom_range']), float(self.config['lightblue']['top_range'])): 'lightblue',
                    (float(self.config['bluewhite']['bottom_range']), float(self.config['bluewhite']['top_range'])): 'bluewhite',
                    (float(self.config['white']['bottom_range']), float(self.config['white']['top_range'])): 'white',
                    (float(self.config['paleyellow']['bottom_range']), float(self.config['paleyellow']['top_range'])): 'paleyellow',
                    (float(self.config['lightorange']['bottom_range']), float(self.config['lightorange']['top_range'])): 'lightorange',
                    (float(self.config['oxygen']['bottom_range']), float(self.config['oxygen']['top_range'])): 'oxygen',
                    (float(self.config['red']['bottom_range']), float(self.config['red']['top_range'])): 'red',
                    (float(self.config['ruby']['bottom_range']), float(self.config['ruby']['top_range'])): 'ruby',

                })

                return colors_set[self.delta_pr]

            except KeyError as error:
                logging.error('Value:' + str(error) + ' out of range!')
                return 'white'

        else:
            try:
                default_colors_set = RangeKeyDict({
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

                return default_colors_set[self.delta_pr]

            except KeyError as error:
                logging.error('Value:' + str(error) + ' out of range!')
                return 'white'


class ColorCommand:
    def __init__(self, color_name, atoms_list):
        self.color_name = color_name
        self.atoms_list = atoms_list
        self.atoms_to_color = 'id ['

    def create_color_command(self):
        for atom_pair in self.atoms_list:
            self.atoms_to_color += atom_pair + ','
        self.atoms_to_color = self.atoms_to_color[:-1]
        self.atoms_to_color += ']'
