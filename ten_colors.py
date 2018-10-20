from pymol import preset, finish_launching, cmd
import pickle
import sys


class ColorCommand:
    def __init__(self, color_name, atoms_list):
        self.color_name = color_name
        self.atoms_list = atoms_list
        self.atoms_to_color = 'id ['

    def create_color_command(self):
        for atom_pair in self.atoms_list:
            self.atoms_to_color += atom_pair + ','
        self.atoms_to_color + ']'


with open("frames", "rb") as f:
    list = pickle.load(f)

pymol_argv = ['pymol', '-q -x ']
finish_launching(pymol_argv)
cmd.util.performance(100)
cmd.set('defer_builds_mode', 10)
cmd.load(sys.argv[1], 'loaded_protein')
cmd.load_traj(sys.argv[2], 'loaded_protein')
cmd.remove('solvent')


for frame in list:
    cmd.frame(frame.number)
    for key, value in frame.colors_command_list.items():
        if value:
            color_command = ColorCommand(key, value)
            color_command.create_color_command()
            cmd.color(color_command.color_name, selection=color_command.atoms_to_color)

