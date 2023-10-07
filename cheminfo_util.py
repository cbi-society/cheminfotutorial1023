# utilfunction for cheminfo tutorial
from rdkit import Chem
from rdkit.Chem.MolStandardize import rdMolStandardize

from chembl_structure_pipeline import standardize_mol
from chembl_structure_pipeline import get_parent_mol
import chembl_structure_pipeline


# 01 data_prep
def prep_moleclue(mol, canon_taut=True, get_large_farg=True):
    """
    @param mol: rdkit mol object
    @param cannon_taut: canonicalize tautomer, default=True
    @param get_large_frag: get large fragment, default=True
    @return tautomar canonicalized and standardized rdkit mol object
    """
    raise NotImplementedError()

