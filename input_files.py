import logging
import sys
from atom_bond_frame import Atom, Bond
from tools import Tools

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class InputFiles:
    def __init__(self, pdb_filename, psf_filename):
        self.pdb_filename = pdb_filename
        self.psf_filename = psf_filename

    def read_pdb(self):
        try:
            pdb_file = open(self.pdb_filename, 'r')
            a = []  # zmienna tmp
            for line in pdb_file:
                if "ATOM" in line:  # jesli linia zawiera slowo kluczowe atom
                    if 'TIP3W' in line:  # jesli linia zawiera TIP3W to przerwij
                        logging.info('Water was reached, scanning completed.')
                        break
                    else:
                        a.append(line.split(' '))  # dodaje linie do listy, rozdziela na tekst i spacje
            pdb_file.close()  # zamknij plik
            logging.info('File ' + self.pdb_filename + 'closed.')
            atom_list = [[] for i in range(len(a))]  # deklaracja listy list o dlugosci ilosci linii w pliku pdb
            for i in range(len(a)):
                for j in range(len(a[i])):
                    if a[i][j] == '':  # jesli element listy zawiera spacje nie rob nic
                        logging.info('Space found, line passed...')
                    else:
                        atom_list[i].append(a[i][j])  # jesli nie to dodaj
            return atom_list
        except FileNotFoundError as error:
            print(error.strerror)

    def create_atom_list(self):
        atom_list = self.read_pdb()
        atoms = []
        for i in range(len(atom_list)):
            atom = Atom(atom_list[i][1], atom_list[i][2], atom_list[i][3], atom_list[i][7], atom_list[i][8], atom_list[i][9])
            atoms.append(atom)

        return atoms

    def read_psf(self):
        can_print = False
        b = []
        try:
            psf_file = open(self.psf_filename, 'r')
            for line in psf_file:
                if "bonds\n" in line:
                    can_print = True
                elif "angles" in line:
                    can_print = False
                if can_print:
                    b.append(line.split(' '))
            psf_file.close()
            b.pop(0)
            bond_list = [[] for i in range(len(b))]

            for i in range(len(b)):
                for j in range(len(b[i])):
                    if b[i][j] == '':
                        logging.info('Space found, line passed...')
                    else:
                        bond_list[i].append(str.rstrip(b[i][j]))
            return bond_list

        except FileNotFoundError as error:
            print(error.strerror)

    def crete_bonds_list(self):
        b = self.read_psf()
        list_of_bonds = []
        atom_list = self.create_atom_list()
        for i in range(len(b)):
            if len(b[i]) % 2 == 0:
                for j in range(len(b[i])):
                    if j == 0:
                        atom_1 = Tools.find_atom(b[i][j], atom_list)
                        atom_2 = Tools.find_atom(b[i][j + 1], atom_list)
                        if atom_1 is not None and atom_2 is not None:
                            bond = Bond(atom_1, atom_2).create_bond()
                            list_of_bonds.append(bond)
                    else:
                        if ((j * 2) + 1) < len(b[i]):
                            atom_1 = Tools.find_atom(b[i][j * 2], atom_list)
                            atom_2 = Tools.find_atom(b[i][(j * 2) + 1], atom_list)
                            if atom_1 is not None and atom_2 is not None:
                                bond = Bond(atom_1, atom_2).create_bond()
                                list_of_bonds.append(bond)
            else:
                logging.info('The number of bonds is odd')
                break
        return list_of_bonds
