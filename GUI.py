from PyQt5.QtWidgets import QPushButton, QWidget, QComboBox, QLabel, QCheckBox, QLineEdit, QProgressBar
from PyQt5.QtGui import QPainter, QColor
import yaml


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
        self.label_combo.setText('Select atom group')
        self.label_combo.move(130, 230)

        self.residue_cb = QComboBox
        self.combo = QComboBox(self)
        self.combo.addItem('Backbone')
        self.combo.addItem('All')
        self.combo.resize(200, 40)
        self.combo.move(100, 250)

        self.next_btn = QPushButton('Next', self)
        self.next_btn.resize(100, 40)
        self.next_btn.move(280, 400)


class OptionWindow(QWidget):
    def __init__(self, parent=None):
        super(OptionWindow, self).__init__(parent)

        try:
            self.config = self.config = yaml.load(open('config.yaml'))
        except FileNotFoundError:
            self.config = None

        self.label_buttons = QLabel(self)
        self.label_buttons.setText('Select one option')
        self.label_buttons.move(140, 30)

        self.label_buttons = QLabel(self)
        self.label_buttons.setText('Ranges used in this run:')
        self.label_buttons.move(120, 365)

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
        self.run_btn.move(280, 800)

        self.back_btn = QPushButton('Back', self)
        self.back_btn.resize(100, 40)
        self.back_btn.move(20, 800)

        self.ten_colors_check = QCheckBox(self)
        self.ten_colors_check.move(120, 220)
        self.label_ten_colors = QLabel(self)
        self.label_ten_colors.setText('10 Colors')
        self.label_ten_colors.move(150, 220)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 280, 20)
        self.progress.move(60, 320)

        self.density_label = QLabel(self)
        self.density_label.move(120, 400)
        if self.config:
            self.density_label.setText('Density (' + str(self.config['density']['bottom_range']) + ','
                                       + str(self.config['density']['top_range']) + ')')
        else:
            self.density_label.setText('Density  (-inf,20)')

        self.nitrogen_label = QLabel(self)
        self.nitrogen_label.move(120, 440)
        if self.config:
            self.nitrogen_label.setText('Nitrogen (' + str(self.config['nitrogen']['bottom_range']) + ','
                                        + str(self.config['nitrogen']['top_range']) + ')')
        else:
            self.nitrogen_label.setText('Nitrogen  (-20, -15)')

        self.marine_label = QLabel(self)
        self.marine_label.move(120, 475)
        if self.config:
            self.marine_label.setText('Marine (' + str(self.config['marine']['bottom_range']) + ','
                                      + str(self.config['marine']['top_range']) + ')')
        else:
            self.marine_label.setText('Marine  (-15, -10)')

        self.lightblue_label = QLabel(self)
        self.lightblue_label.move(120, 510)
        if self.config:
            self.lightblue_label.setText('Lightblue (' + str(self.config['lightblue']['bottom_range']) + ','
                                         + str(self.config['lightblue']['top_range']) + ')')
        else:
            self.lightblue_label.setText('Lightblue  (-10, -5)')

        self.bluewhite_label = QLabel(self)
        self.bluewhite_label.move(120, 545)
        if self.config:
            self.bluewhite_label.setText('Bluewhite (' + str(self.config['bluewhite']['bottom_range']) + ','
                                         + str(self.config['bluewhite']['top_range']) + ')')
        else:
            self.bluewhite_label.setText('Bluewhite  (-5, 0)')

        self.white_label = QLabel(self)
        self.white_label.move(120, 580)
        if self.config:
            self.white_label.setText('White (' + str(self.config['white']['bottom_range']) + ',' + str(
                self.config['white']['top_range']) + ')')
        else:
            self.white_label.setText('White  (0, 5)')

        self.paleyellow_label = QLabel(self)
        self.paleyellow_label.move(120, 615)
        if self.config:
            self.paleyellow_label.setText('Paleyellow (' + str(self.config['paleyellow']['bottom_range']) + ','
                                          + str(self.config['paleyellow']['top_range']) + ')')
        else:
            self.paleyellow_label.setText('Paleyellow  (5, 10)')

        self.lightorange_label = QLabel(self)
        self.lightorange_label.move(120, 650)
        if self.config:
            self.lightorange_label.setText('Lightorange (' + str(self.config['lightorange']['bottom_range']) + ','
                                           + str(self.config['lightorange']['top_range']) + ')')
        else:
            self.lightorange_label.setText('Lightorange  (10, 15)')

        self.oxygen_label = QLabel(self)
        self.oxygen_label.move(120, 685)
        if self.config:
            self.oxygen_label.setText('Oxygen (' + str(self.config['oxygen']['bottom_range']) + ',' + str(
                self.config['oxygen']['top_range']) + ')')
        else:
            self.oxygen_label.setText('Oxygen  (15, 20)')

        self.red_label = QLabel(self)
        self.red_label.move(120, 715)
        if self.config:
            self.red_label.setText('Red (' + str(self.config['red']['bottom_range']) + ',' + str(
                self.config['red']['top_range']) + ')')
        else:
            self.red_label.setText('Red  (20, 25)')

        self.ruby_label = QLabel(self)
        self.ruby_label.move(120, 750)
        if self.config:
            self.ruby_label.setText('Ruby (' + str(self.config['ruby']['bottom_range']) + ',' + str(
                self.config['ruby']['top_range']) + ')')
        else:
            self.ruby_label.setText('Ruby  (25, inf)')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor.fromRgbF(0.1, 0.1, 0.6))
        qp.drawRect(60, 400, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.2, 0.2, 1.0))
        qp.drawRect(60, 435, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.0, 0.5, 1.0))
        qp.drawRect(60, 470, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.75, 0.75, 1.0))
        qp.drawRect(60, 505, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.85, 0.85, 1.0))
        qp.drawRect(60, 540, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 1.0, 1.0))
        qp.drawRect(60, 575, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 1.0, 0.5))
        qp.drawRect(60, 610, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 0.8, 0.5))
        qp.drawRect(60, 645, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 0.3, 0.3))
        qp.drawRect(60, 680, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 0, 0))
        qp.drawRect(60, 710, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.6, 0.2, 0.2))
        qp.drawRect(60, 745, 25, 25)





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


class ConfigWindow(QWidget):
    def __init__(self, parent=None):
        super(ConfigWindow, self).__init__(parent)
        try:
            self.config = self.config = yaml.load(open('config.yaml'))
        except FileNotFoundError:
            self.config = None

        self.density_label = QLabel(self)
        self.density_label.move(50, 20)
        if self.config:
            self.density_label.setText('Density (' + str(self.config['density']['bottom_range']) + ','
                                       + str(self.config['density']['top_range']) + ')')
        else:
            self.density_label.setText('Density  (-inf,20)')

        self.nitrogen_label = QLabel(self)
        self.nitrogen_label.move(50, 55)
        if self.config:
            self.nitrogen_label.setText('Nitrogen (' + str(self.config['nitrogen']['bottom_range']) + ','
                                        + str(self.config['nitrogen']['top_range']) + ')')
        else:
            self.nitrogen_label.setText('Nitrogen  (-20, -15)')

        self.marine_label = QLabel(self)
        self.marine_label.move(50, 90)
        if self.config:
            self.marine_label.setText('Marine (' + str(self.config['marine']['bottom_range']) + ','
                                      + str(self.config['marine']['top_range']) + ')')
        else:
            self.marine_label.setText('Marine  (-15, -10)')

        self.lightblue_label = QLabel(self)
        self.lightblue_label.move(50, 125)
        if self.config:
            self.lightblue_label.setText('Lightblue (' + str(self.config['lightblue']['bottom_range']) + ','
                                    + str(self.config['lightblue']['top_range']) + ')')
        else:
            self.lightblue_label.setText('Lightblue  (-10, -5)')

        self.bluewhite_label = QLabel(self)
        self.bluewhite_label.move(50, 160)
        if self.config:
            self.bluewhite_label.setText('Bluewhite (' + str(self.config['bluewhite']['bottom_range']) + ','
                                         + str(self.config['bluewhite']['top_range']) + ')')
        else:
            self.bluewhite_label.setText('Bluewhite  (-5, 0)')

        self.white_label = QLabel(self)
        self.white_label.move(50, 195)
        if self.config:
            self.white_label.setText('White (' + str(self.config['white']['bottom_range']) + ',' + str(
                self.config['white']['top_range']) + ')')
        else:
            self.white_label.setText('White  (0, 5)')

        self.paleyellow_label = QLabel(self)
        self.paleyellow_label.move(50, 230)
        if self.config:
            self.paleyellow_label.setText('Paleyellow (' + str(self.config['paleyellow']['bottom_range']) + ','
                                          + str(self.config['paleyellow']['top_range']) + ')')
        else:
            self.paleyellow_label.setText('Paleyellow  (5, 10)')

        self.lightorange_label = QLabel(self)
        self.lightorange_label.move(50, 265)
        if self.config:
            self.lightorange_label.setText('Lightorange (' + str(self.config['lightorange']['bottom_range']) + ','
                                           + str(self.config['lightorange']['top_range']) + ')')
        else:
            self.lightorange_label.setText('Lightorange  (10, 15)')

        self.oxygen_label = QLabel(self)
        self.oxygen_label.move(50, 300)
        if self.config:
            self.oxygen_label.setText('Oxygen (' + str(self.config['oxygen']['bottom_range']) + ',' + str(
                self.config['oxygen']['top_range']) + ')')
        else:
            self.oxygen_label.setText('Oxygen  (15, 20)')

        self.red_label = QLabel(self)
        self.red_label.move(50, 335)
        if self.config:
            self.red_label.setText('Red (' + str(self.config['red']['bottom_range']) + ',' + str(
                self.config['red']['top_range']) + ')')
        else:
            self.red_label.setText('Red  (20, 25)')

        self.ruby_label = QLabel(self)
        self.ruby_label.move(50, 370)
        if self.config:
            self.ruby_label.setText('Ruby (' + str(self.config['ruby']['bottom_range']) + ',' + str(
                self.config['ruby']['top_range']) + ')')
        else:
            self.ruby_label.setText('Ruby  (25, inf)')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor.fromRgbF(0.1, 0.1, 0.6))
        qp.drawRect(10, 15, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.2, 0.2, 1.0))
        qp.drawRect(10, 50, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.0, 0.5, 1.0))
        qp.drawRect(10, 85, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.75, 0.75, 1.0))
        qp.drawRect(10, 120, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.85, 0.85, 1.0))
        qp.drawRect(10, 155, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 1.0, 1.0))
        qp.drawRect(10, 190, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 1.0, 0.5))
        qp.drawRect(10, 225, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 0.8, 0.5))
        qp.drawRect(10, 260, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 0.3, 0.3))
        qp.drawRect(10, 295, 25, 25)

        qp.setBrush(QColor.fromRgbF(1.0, 0, 0))
        qp.drawRect(10, 330, 25, 25)

        qp.setBrush(QColor.fromRgbF(0.6, 0.2, 0.2))
        qp.drawRect(10, 365, 25, 25)
