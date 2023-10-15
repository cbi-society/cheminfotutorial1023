# utilfunction for cheminfo tutorial
from rdkit import Chem
from rdkit.Chem.MolStandardize import rdMolStandardize

from chembl_structure_pipeline import standardize_mol
from chembl_structure_pipeline import get_parent_mol
import chembl_structure_pipeline


# 01 data_prep
def prep_moleclue(mol, canon_taut=True, get_large_frag=True):
    """
    @param mol: rdkit mol object
    @param cannon_taut: canonicalize tautomer, default=True
    @param get_large_frag: get large fragment, default=True
    @return tautomar canonicalized and standardized rdkit mol object
    """
    # 処理を行った分子は新しいオブジェクトになるのでもともとの化合物が持っているプロパティを事前に取得し付与します。
    molprops = mol.GetPropsAsDict()
    # _Nameプロパティは上記の処理では取得できないので別途処理します。
    if mol.HasProp('_Name'):
        molname = mol.GetProp('_Name')
    else:
        molname = ""
    if canon_taut:
        mol = # ToDo 互変異整体の標準化オプションがTrueの場合の処理を書きましょう
    std_mol = # ToDo molを正規化しましょう
    parent_mol, exclude = #ToDo 親分子（本体）を取るメソッドを書きましょう
    if exclude:
        # 除外金属を持つ分子は処理しないのでNoneを返します。
        return None
    if get_large_frag:
        lfc = rdMolStandardize.LargestFragmentChooser()
        uc = rdMolStandardize.Uncharger()
        parent_mol = lfc.choose(parent_mol)
        parent_mol = uc.uncharge(parent_mol)
    # parent_molに元々の分子が保持していたプロパティを付与します。
    # 電荷や、分子量などは変わる可能性があります。今回の処理では影響はないですがご注意ください。
    for k,v in molprops.items():
        parent_mol.SetProp(k, str(v))
    parent_mol.SetProp('_Name', molname)
    raise parent_mol

