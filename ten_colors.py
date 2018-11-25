from pymol import finish_launching, cmd
import pickle
import os
import sys
import subprocess
import time

with open("frames.file", "rb") as f:
    frame_list = pickle.load(f)
f.close()
os.remove('frames.file')


pymol_argv = ['pymol', '-q -x ']
finish_launching(pymol_argv)

cmd.load(sys.argv[1], 'loaded_protein')
cmd.load_traj(sys.argv[2], 'loaded_protein')

cmd.util.performance(100)
cmd.set('defer_builds_mode', 10)
cmd.remove('solvent')

for frame in frame_list:
    try:
        CapsLock_status = subprocess.getoutput('xset q | grep Caps')[21:24]
        if CapsLock_status == 'on ':
            print('Frame ', frame.number)
            cmd.set('state', frame.number)
            for command in frame.commands_list:
                cmd.color(command.color_name, selection=command.atoms_to_color)
        elif CapsLock_status == 'off':
            print('Wait for CapsLock...')
            time.sleep(10)
            CapsLock_status = 'on '
    except KeyboardInterrupt:
        break
