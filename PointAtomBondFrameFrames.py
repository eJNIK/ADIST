from Tools import Tools


class Point:
    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z


class Atom:
    def __init__(self, number, element, residue, x, y, z):
        self.number = number
        self.element = element
        self.residue = residue
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def create_atom(self):
        atom = Atom(self.number, self.element, self.residue, self.x, self.y, self.z)
        atom.number = self.number
        atom.element = self.element
        atom.residue = self.residue
        atom.coord = Point(self.x, self.y, self.z)
        atom.coord.x = self.x
        atom.coord.y = self.y
        atom.coord.z = self.z

        return atom


class Bond:
    def __init__(self, atom_1, atom_2, color=None):
        self.atom_1 = atom_1
        self.atom_2 = atom_2
        self.color = color

    def create_bond(self):
        bond = Bond(self.atom_1, self.atom_2, self.color)
        bond.atom_1 = self.atom_1
        bond.atom_2 = self.atom_2
        bond.distance = Tools.calculate_distance(self.atom_1.x, self.atom_1.y, self.atom_1.z, self.atom_2.x, self.atom_2.y, self.atom_2.z)
        bond.bond = str(self.atom_1.number + ',' + self.atom_2.number)

        if self.color:
            bond.color = self.color
        else:
            bond.color = 'white'
        return bond


class Frame:
    def __init__(self, number, bonds_list, colors_command_list):
        self.number = number
        self.bonds_list = bonds_list
        self.colors_command_list = colors_command_list

    def create_frame(self):
        frame = Frame(self.number, self.bonds_list, self.colors_command_list)
        frame.number = self.number
        frame.bonds_list = self.bonds_list
        frame.colors_command_list = self.colors_command_list

        return frame


class CommandFrame:
    def __init__(self, number, commands_list):
        self.number = number
        self.commands_list = commands_list

    def create_frame(self):
        frame = CommandFrame(self.number, self.commands_list)
        frame.number = self.number
        frame.commands_list = self.commands_list

        return frame


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

