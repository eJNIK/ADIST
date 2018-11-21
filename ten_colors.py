from pymol import finish_launching, cmd
import pickle
import os
import sys

with open("frames.file", "rb") as f:
    frame_list = pickle.load(f)
f.close()
os.remove('frames.file')


pymol_argv = ['pymol', '-q -x ']
finish_launching(pymol_argv)
start = input('Press any key to start')

cmd.load(sys.argv[1], 'loaded_protein')
cmd.load_traj(sys.argv[2], 'loaded_protein')

cmd.load('pdb.pdb', 'loaded_protein')
cmd.load_traj('dcd.dcd', 'loaded_protein')
cmd.util.performance(100)
cmd.set('defer_builds_mode', 10)
cmd.remove('solvent')


for frame in frame_list:
    cmd.set('state', frame.number)
    print('Frame ', frame.number)
    for command in frame.commands_list:
        cmd.color(command.color_name, selection=command.atoms_to_color)

