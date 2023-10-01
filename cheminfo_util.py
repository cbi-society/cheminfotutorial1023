# utilfunction for cheminfo tutorial
from rdkit import Chem
from rdkit.Chem.MolStandardize import rdMolStandardize

from chembl_structure_pipeline import standardizer
from chembl_structure_pipeline import get_parent_mol
import chembl_structure_pipeline


# 01 data_prep
def prep_moleclue(mol):
    """
    @param mol: rdkit mol object
    @return tautomar canonicalized and standardized rdkit mol object
    """
    raise NotImplementedError()