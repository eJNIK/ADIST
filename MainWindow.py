from InputFiles import InputFiles
from SelectResidue import SelectResidue
from Tools import Tools, logger, logging
from Color import Color, ColorCommand
from PointAtomBondFrameFrames import Atom, Frames, Frame, Bond, CommandFrame
import pymol2
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot
from gui import LoadFileWindow, OptionWindow
import subprocess
import pickle
import os.path


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.file_pdb = ''
        self.file_psf = ''
        self.file_dcd = ''
        self.file_frames = ''
        self.setGeometry(50, 50, 400, 450)

        self.setWindowTitle('ADIST')
        self.start_load_file_window()

    def start_load_file_window(self):
        self.load_file = LoadFileWindow(self)
        self.setCentralWidget(self.load_file)
        self.load_file.pdb_btn.clicked.connect(self.file_load_click)
        self.load_file.psf_btn.clicked.connect(self.file_load_click)
        self.load_file.dcd_btn.clicked.connect(self.file_load_click)
        self.load_file.next_btn.clicked.connect(self.start_option_window)
        self.show()

    def start_option_window(self):
        self.option = OptionWindow(self)
        self.setCentralWidget(self.option)
        self.option.back_btn.clicked.connect(self.start_load_file_window)
        self.option.run_btn.clicked.connect(self.run_option)
        self.show()

    @pyqtSlot()
    def run_option(self):
        if self.file_pdb and self.file_psf and self.file_dcd:
            input_files = InputFiles(self.file_pdb, self.file_psf)
            bonds = input_files.crete_bonds_list()
            select_residue = SelectResidue(bonds)
            backbone = select_residue.backbone()

            self.p1 = pymol2.PyMOL()
            self.p1.start()

            self.p1.cmd.util.performance(100)
            self.p1.cmd.set('defer_builds_mode', 10)
            self.p1.cmd.load(self.file_pdb, 'loaded_protein')
            self.p1.cmd.load_traj(self.file_dcd, 'loaded_protein')
            self.p1.cmd.remove('solvent')
            self.frames_list = self.create_frames_list(backbone)
            self.p1.stop()

            if self.option.file_check.isChecked():
                if self.frames_list:
                    Tools.export_to_file(self.frames_list)
                    QMessageBox.information(self, 'ADIST', 'CSV file created!')
                    logging.info('CSV file created!')

            if self.option.chart_check.isChecked():
                if self.frames_list:
                    atom_1 = self.option.atom_1_input.text()
                    atom_2 = self.option.atom_2_input.text()

                    if atom_1.isdigit() and atom_2.isdigit():

                        Tools.plot(self.frames_list, atom_1, atom_2)
                        QMessageBox.information(self, 'ADIST', 'Plot created!')
                        logging.info('Plot created!')

            if self.option.ten_colors_check.isChecked():
                if self.frames_list:
                    self.comand_frames = self.create_commands_list(self.frames_list)
                    with open("frames.file", "wb") as f:
                        pickle.dump(self.comand_frames, f, pickle.HIGHEST_PROTOCOL)
                        f.close()
                    if os.path.isfile('frames.file'):
                        logging.info('File dropped')

                    QMessageBox.information(self, 'ADIST', 'Done, watch result in PyMOL')
                    subprocess.call(['python', 'ten_colors.py', self.file_pdb, self.file_dcd, 'frames.file'])

                else:
                    QMessageBox.critical(self, 'Error', 'File not found!')
                    logging.error('File not found')
        else:
            QMessageBox.critical(self, 'Error', 'None file selected!')
            logging.error('None file selected')

    def file_load_click(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        if '.pdb' in path:
            self.file_pdb = path
        elif '.psf' in path:
            self.file_psf = path
        elif '.dcd' in path:
            self.file_dcd = path
        elif 'frames.file' in path:
            self.file_frames = path
        else:
            QMessageBox.critical(self, 'Error', 'Wrong file extension')
            logging.error('Wrong file extension')

    def create_frames_list(self, residue):
        frames = []
        completed = 0
        self.option.progress.setRange(0, self.p1.cmd.count_frames() + 1)
        for i in range((self.p1.cmd.count_frames()) + 1):
            completed += 1
            self.option.progress.setValue(completed)
            self.p1.cmd.frame(i)
            logging.info('Processing frame number ' + str(i) + '...')

            bonds = []
            index = 0

            for bond in residue:
                d0 = residue[index].distance

                atom_1_coords = self.p1.cmd.get_atom_coords('id ' + bond.atom_1.number)
                atom_2_coords = self.p1.cmd.get_atom_coords('id ' + bond.atom_2.number)

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

    def create_commands_list(self, frames):
        comands_frames = []
        completed = 0
        self.option.progress.setRange(0, len(frames))

        for frame in frames:
            comands_list = []
            completed += 1
            self.option.progress.setValue(completed)
            for key, value in frame.colors_command_list.items():
                if value:
                    color_command = ColorCommand(key, value)
                    color_command.create_color_command()
                    comands_list.append(color_command)
            command_frame = CommandFrame(frame.number, comands_list)
            comands_frames.append(command_frame)
        return comands_frames
