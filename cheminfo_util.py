# utilfunction for cheminfo tutorial
from rdkit import Chem
from rdkit.Chem.MolStandardize import rdMolStandardize

from chembl_structure_pipeline import standardize_mol
from chembl_structure_pipeline import get_parent_mol
import chembl_structure_pipeline


# 01 data_prep
# Mainはコメントアウトしている方をActiveにする
'''
def prep_moleclue(mol):

    raise NotImplementedError()
'''

def prep_moleclue(mol, canon_taut=True, get_large_frag=True):
    """
    @param mol: rdkit mol object
    @return tautomar canonicalized and standardized rdkit mol object
    """
    molprops = mol.GetPropsAsDict()
    if mol.HasProp('_Name'):
        molname = mol.GetProp('_Name')
    else:
        molname = ""
    if canon_taut:
        mol = rdMolStandardize.CanonicalTautomer(mol)
    std_mol = standardize_mol(mol)
    parent_mol, exclude= get_parent_mol(std_mol)
    if exclude:
        return None
    if get_large_frag:
        lfc = rdMolStandardize.LargestFragmentChooser()
        uc = rdMolStandardize.Uncharger()
        parent_mol = lfc.choose(parent_mol)
        parent_mol = uc.uncharge(parent_mol)
    for k,v in molprops.items():
        parent_mol.SetProp(k, str(v))
    parent_mol.SetProp('_Name', molname)
    return parent_mol
