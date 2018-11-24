class SelectAtomGroup:
    def __init__(self, atoms):
        self.atoms = atoms

    def backbone(self):

        backbone = []

        for bond in self.atoms:
            if (bond.atom_1.element == 'C' or bond.atom_1.element == 'CA' or bond.atom_1.element == 'N') and \
                   (bond.atom_2.element == 'C' or bond.atom_2.element == 'CA' or bond.atom_2.element == 'N'):
                backbone.append(bond)

        return backbone

    def all_atoms(self):

        all_atoms = []

        for bond in self.atoms:
            all_atoms.append(bond)

        return all_atoms
