"""
File which contains a python function to highlight specific amino acids in
@author: Jeremias Krause
@company: UKA Aachen (RWTH)
@mail: jerkrause@ukaachen.de
"""
import py3Dmol

def color_pdb(input_pdb:str,position:str):
    """
    Input Arguments : 
            input_pdb (str) -> path to .pdb file 
            position (str) -> protein position
    """
    with open(input_pdb) as pdbfile:
        pdb = "".join([x for x in pdbfile])
    view = py3Dmol.view(width=700, height=600)
    view.addModelsAsFrames(pdb)
    #Split loaded .pdb file into a list of lines
    splitted_pdb = pdb.split("\n")
    i=0
    for line in splitted_pdb:
        #Split each line into a list 
        splitted_pdb_line = line.split()
        if len(splitted_pdb_line) == 0 or splitted_pdb_line[0] != "ATOM":
            continue
        if splitted_pdb_line[5] == position:
            color = "cyan"
        else:
            color = "grey"
        #idx = int(splitted_pdb_line[1])

        view.setStyle({'model': -1, 'serial': i+1}, {"cartoon": {'color': color}})
        i += 1
    return view