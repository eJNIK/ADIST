from pymol import cmd, finish_launching, preset
from atom_bond_frame import Atom, Frame, Bond
from Color import Color
from tools import Tools
import logging
import sys
from gui import OptionWindow
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# class PymolControl:
#     def __init__(self, pdb_file, dcd_file):
#         self.pdb_file = pdb_file
#         self.dcd_file = dcd_file
#
#     def run(self):
#         try:
#             finish_launching()
#             cmd.set('defer_builds_mode', 10)
#             cmd.load(self.pdb_file, 'loaded_protein')
#             cmd.load_traj(self.dcd_file, 'loaded_protein')
#             preset.publication(selection='all')
#             cmd.remove('solvent')  # usun wode
#             cmd.color('white', 'all')
#         except FileNotFoundError as error:
#             print(error.strerror)
#
#     def run_quite(self):
#         try:
#             pymol_argv = ['pymol', '-qc']
#             cmd.set('defer_builds_mode', 10)
#             cmd.load(self.pdb_file, 'loaded_protein')
#             cmd.load_traj(self.dcd_file, 'loaded_protein')
#             finish_launching()
#         except FileNotFoundError as error:
#             print(error.strerror)


class Frames:
    def __init__(self, residue):
        self.residue = residue

    @staticmethod
    def create_color_list(bonds):
        colors = {
            'density': [],
            'nitrogen': [],
            'lightblue': [],
            'bluewhite': [],
            'white': [],
            'paleyellow': [],
            'lightorange': [],
            'oxygen': [],
            'red': [],
            'ruby': []
        }

        for bond in bonds:

            colors[bond.color].append(bond.bond)

        return colors


# class RunAdist:
#     def __init__(self, frames):
#         self.frames = frames
#
#     def run_adist(self):
#
#         for frame in self.frames:
#             print(frame.number)
#             cmd.frame(frame.number)
#             for color in frame.colors_command_list:
#                 if len(frame.colors_command_list[color]) != 0:
#                     print(frame.colors_command_list[color])
