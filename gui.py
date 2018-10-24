from PyQt5.QtWidgets import QPushButton, QWidget, QComboBox, QLabel, QCheckBox, QLineEdit, QProgressBar


class LoadFileWindow(QWidget):
    def __init__(self, parent=None):
        super(LoadFileWindow, self).__init__(parent)

        self.label_buttons = QLabel(self)
        self.label_buttons.setText('Load files')
        self.label_buttons.move(170, 30)

        self.pdb_btn = QPushButton('Load PDB file', self)
        self.pdb_btn.resize(200, 40)
        self.pdb_btn.move(100, 50)

        self.psf_btn = QPushButton('Load PSF file', self)
        self.psf_btn.resize(200, 40)
        self.psf_btn.move(100, 100)

        self.dcd_btn = QPushButton('Load DCD file', self)
        self.dcd_btn.resize(200, 40)
        self.dcd_btn.move(100, 150)

        self.label_combo = QLabel(self)
        self.label_combo.setText('Select residue')
        self.label_combo.move(150, 230)

        self.residue_cb = QComboBox
        self.combo = QComboBox(self)
        self.combo.addItem('Backbone')
        self.combo.resize(200, 40)
        self.combo.move(100, 250)

        self.next_btn = QPushButton('Next', self)
        self.next_btn.resize(100, 40)
        self.next_btn.move(280, 400)


class OptionWindow(QWidget):
    def __init__(self, parent=None):
        super(OptionWindow, self).__init__(parent)

        self.label_buttons = QLabel(self)
        self.label_buttons.setText('Select one option')
        self.label_buttons.move(140, 30)

        self.file_check = QCheckBox(self)
        self.file_check.move(120, 80)
        self.label_file = QLabel(self)
        self.label_file.setText('Save to file')
        self.label_file.move(150, 80)

        self.chart_check = QCheckBox(self)
        self.chart_check.move(120, 120)
        self.label_chart = QLabel(self)
        self.label_chart.setText('Create chart')
        self.label_chart.move(150, 120)

        self.atom_1_input = QLineEdit(self)
        self.atom_1_input.move(120, 140)
        self.atom_2_input = QLineEdit(self)
        self.atom_2_input.move(120, 165)

        self.atom_1_label = QLabel(self)
        self.atom_1_label.move(70, 145)
        self.atom_1_label.setText('Atom 1')

        self.atom_2_label = QLabel(self)
        self.atom_2_label.move(70, 165)
        self.atom_2_label.setText('Atom 2')

        self.run_btn = QPushButton('Run!', self)
        self.run_btn.resize(100, 40)
        self.run_btn.move(280, 400)

        self.back_btn = QPushButton('Back', self)
        self.back_btn.resize(100, 40)
        self.back_btn.move(20, 400)

        self.ten_colors_check = QCheckBox(self)
        self.ten_colors_check.move(120, 220)
        self.label_ten_colors = QLabel(self)
        self.label_ten_colors.setText('10 Colors')
        self.label_ten_colors.move(150, 220)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 280, 20)
        self.progress.move(60, 320)


class ProcessingWindow(QWidget):
    def __init__(self, parent=None):
        super(ProcessingWindow, self).__init__(parent)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 280, 20)
        self.progress.move(50, 45)

        self.new_btn = QPushButton('New inputs', self)
        self.new_btn.resize(90, 40)
        self.new_btn.move(10, 100)

        self.run_btn = QPushButton('Run!', self)
        self.run_btn.resize(90, 40)
        self.run_btn.move(150, 100)

        self.back_btn = QPushButton('Back', self)
        self.back_btn.resize(90, 40)
        self.back_btn.move(280, 100)
