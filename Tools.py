from math import sqrt
from datetime import datetime
import csv
import os
from sys import maxsize, argv, exit
import matplotlib.pyplot as plt
import logging


logger = logging.basicConfig(filename='ADIST.log', filemode='w', level=logging.DEBUG, format='%(asctime)s- %(levelname)s - %(message)s')


class Tools:

    @staticmethod
    def calculate_distance(x_1, y_1, z_1, x_2, y_2, z_2):
        distance = sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2) + ((z_2 - z_1) ** 2))
        return distance

    @staticmethod
    def find_atom(value, data_set):
        for i, atom in enumerate(data_set):
            if atom.number == value:
                return atom

    @staticmethod
    def export_to_file(frames):
        if not os.path.exists('data'):
            os.makedirs('data')
        with open('data/distances_' + datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.csv', 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Frame number, atom 1, atom 2, distance, color'])
            for frame in frames:
                for bond in frame.bonds_list:
                    writer.writerow([frame.number, bond.atom_1.number, bond.atom_2.number, bond.distance])
        csv_file.close()


    @staticmethod
    def distance_percent_change(d0, di):
        delta_d_pr = ((di - d0) / d0) * 100
        return delta_d_pr

    @staticmethod
    def plot(frames, atom1, atom2):
        delta_d_list = []
        for frame in frames:
            for bond in frame.bonds_list:
                if bond.atom_1.number == str(atom1) and bond.atom_2.number == str(atom2):
                    plot_title = 'atom ' + bond.atom_1.number + '(' + bond.atom_1.element + ')' + ' and ' + 'atom ' + \
                                 bond.atom_2.number + '(' + bond.atom_2.element + ')'
                    if frame.number == 0:
                        d0 = bond.distance
                    delta_d_list.append(Tools.distance_percent_change(d0, bond.distance))
        plt.plot(delta_d_list, 'ro')

        plt.title('Distance between ' + plot_title)
        plt.xlabel('Frames')
        plt.ylabel('Delta d(%)')
        plt.figure(figsize=(50, 50))
        plt.show()
