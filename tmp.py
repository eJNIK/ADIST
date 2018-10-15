from pymol_control import *
from input_files import InputFiles
from select_residue import SelectResidue
from tools import Tools
from pymol_control import Frames
from pymol import cmd, finish_launching, preset

def frames_list(residue):
    frames = []

    for i in range((cmd.count_frames()) + 1):
        cmd.frame(i)
        bonds = []
        index = 0

        for bond in residue:
            d0 = residue[index].distance

            atom_1_coords = cmd.get_atom_coords('id ' + bond.atom_1.number)
            atom_2_coords = cmd.get_atom_coords('id ' + bond.atom_2.number)

            di = Tools.calculate_distance(atom_1_coords[0], atom_1_coords[1], atom_1_coords[2], atom_2_coords[0],
                                          atom_2_coords[1], atom_2_coords[2])

            atom_1 = Atom(bond.atom_1.number, bond.atom_1.element, bond.atom_1.residue, atom_1_coords[0],
                          atom_1_coords[1], atom_1_coords[2])
            atom_2 = Atom(bond.atom_2.number, bond.atom_2.element, bond.atom_2.residue, atom_2_coords[0],
                          atom_2_coords[1], atom_2_coords[2])

            delta_d_percent = Tools.distance_percent_change(d0, di)
            color = Color(delta_d_percent)

            new_bond = Bond(atom_1.create_atom(), atom_2.create_atom(), color.return_color())

            bonds.append(new_bond.create_bond())
            index += 1
        colors_command_list = Frames.create_color_list(bonds)
        frame = Frame(i, bonds, colors_command_list)
        frames.append(frame.create_frame())
    return frames


def ten_color(frames):
    for frame in frames:
        cmd.frame(frame.number)
        for key, value in frame.colors_command_list.items():
            if value:
                color_command = ColorCommand(key, value)
                color_command.create_color_command()
                cmd.color(color_command.color_name,
                          selection=color_command.atoms_to_color)

class ColorCommand:
    def __init__(self, color_name, atoms_list):
        self.color_name = color_name
        self.atoms_list = atoms_list
        self.atoms_to_color = 'id ['

    def create_color_command(self):
        for atom_pair in self.atoms_list:
            self.atoms_to_color += atom_pair + ','
        self.atoms_to_color + ']'




file_pdb = 'pdb.pdb'
file_psf = 'psf.psf'
file_dcd = 'dcd.dcd'

#input_files = InputFiles(file_pdb, file_psf)
#bonds = input_files.crete_bonds_list()
#select_residue = SelectResidue(bonds)
#backbone = select_residue.backbone()

#pymol_argv = ['pymol', '-qxiF'] #only window
finish_launching()

cmd.set('defer_builds_mode', 10)
cmd.util.performance(100)
cmd.load(file_pdb, 'loaded_protein')
cmd.load_traj(file_dcd, 'loaded_protein')
preset.ball_and_stick(selection='all')
cmd.remove('solvent')  # us
#frames = frames_list(backbone)
#ten_color(frames)
