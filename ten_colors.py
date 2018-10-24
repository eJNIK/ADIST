from pymol import preset, finish_launching, cmd
import pickle
from Tools import os
import sys


with open("frames.file", "rb") as f:
    list = pickle.load(f)
f.close()
os.remove('frames.file')

pymol_argv = ['pymol', '-q -x ']
finish_launching(pymol_argv)
cmd.util.performance(100)
cmd.set('defer_builds_mode', 10)
cmd.load(sys.argv[1], 'loaded_protein')
cmd.load_traj(sys.argv[2], 'loaded_protein')
cmd.remove('solvent')


for frame in list:
    cmd.frame(frame.number)
    for command in frame.commands_list:
            cmd.color(command.color_name, selection=command.atoms_to_color)

os.remove('ADIST.log')
