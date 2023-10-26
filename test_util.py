import unittest
import cheminfo_util
from rdkit import Chem

class TestCheminfo_util(unittest.TestCase):
    def test_prep_mol1(self):
        mol = Chem.MolFromSmiles("C1=CC(=O)NC=C1")
        stdmol = cheminfo_util.prep_moleclue(mol, canon_taut=True)
        self.assertEqual(Chem.MolToSmiles(stdmol),"O=c1cccc[nH]1")
     
    def test_prep_mol2(self):
        mol = Chem.MolFromSmiles("CC(=O)[O-].[Na+]")
        stdmol = cheminfo_util.prep_moleclue(mol, get_large_frag=True)
        self.assertEqual(Chem.MolToSmiles(stdmol),"CC(=O)O")

if __name__=="__main__":
    unittest.main()