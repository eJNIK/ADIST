from range_key_dict import RangeKeyDict
from Tools import logger, maxsize, logging
import yaml


class Color:
    def __init__(self, delta_pr):
        self.delta_pr = delta_pr

    def return_color(self):
        try:
            try:
                config = yaml.load(open('conffig.yaml'))
                logging.info('Configuration load from file')

                colors_set = RangeKeyDict({
                    (int(config['density']['bottom_range']), int(config['density']['top_range'])): 'density',
                    (int(config['nitrogen']['bottom_range']), int(config['nitrogen']['top_range'])): 'nitrogen',
                    (int(config['marine']['bottom_range']), int(config['marine']['top_range'])): 'marine',
                    (int(config['lightblue']['bottom_range']), int(config['lightblue']['top_range'])): 'lightblue',
                    (int(config['bluewhite']['bottom_range']), int(config['bluewhite']['top_range'])): 'bluewhite',
                    (int(config['white']['bottom_range']), int(config['white']['top_range'])): 'white',
                    (int(config['paleyellow']['bottom_range']), int(config['paleyellow']['top_range'])): 'paleyellow',
                    (int(config['lightorange']['bottom_range']), int(config['lightorange']['top_range'])): 'lightorange',
                    (int(config['oxygen']['bottom_range']), int(config['oxygen']['top_range'])): 'oxygen',
                    (int(config['red']['bottom_range']), int(config['red']['top_range'])): 'red',
                    (int(config['ruby']['bottom_range']), int(config['ruby']['top_range'])): 'ruby',

                })

                return colors_set[self.delta_pr]

            except FileNotFoundError as err:

                logging.warning('Configuration with name ' + err.filename + ' not found, default settings chosen.')
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
            return 'green'


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


color = Color(14)
print(color.return_color())