"""
File which contains a python function to highlight specific amino acids in
@author: Jeremias Krause
@company: UKA Aachen (RWTH)
@mail: jerkrause@ukaachen.de
"""
import py3Dmol

def color_pdb(input_pdb:str,position:str,highlight_colour:str,style:str,wildtype_pdb:str):
    """
    Input Arguments : 
            input_pdb (str) -> path to .pdb file 
            position (str) -> protein position
    """
    #Format position string (especially important if multiple positions were given)
    position = position.split(",")
    position = [x.strip() for x in position]


    with open(input_pdb) as pdbfile:
        pdb = "".join([x for x in pdbfile])

    with open(wildtype_pdb) as pdbfile2:
        pdb2 = "".join([x for x in pdbfile2])

    view = py3Dmol.view(height = 1100,width=1400,viewergrid=(1,2))
    view.addModelsAsFrames(pdb,viewer=(0,0))
    view.addModelsAsFrames(pdb2,viewer=(0,1))
    #Split loaded .pdb file into a list of lines
    splitted_pdb = pdb.split("\n")
    i=0
    if style == "cartoon_stick":
        for line in splitted_pdb:
            #Split each line into a list 
            splitted_pdb_line = line.split()
            if len(splitted_pdb_line) == 0 or splitted_pdb_line[0] != "ATOM":
                continue
            if splitted_pdb_line[5] in position:
                color = highlight_colour
                view.setStyle({'model': -1, 'serial': i+1}, {"stick": {'color': color}})
            else:
                color = "grey"
                view.setStyle({'model': -1, 'serial': i+1}, {"cartoon": {'color': color}})
            i += 1
    else:
        for line in splitted_pdb:
            #Split each line into a list 
            splitted_pdb_line = line.split()
            if len(splitted_pdb_line) == 0 or splitted_pdb_line[0] != "ATOM":
                continue
            if splitted_pdb_line[5] in position:
                color = highlight_colour
            else:
                color = "grey"
            view.setStyle({'model': -1, 'serial': i+1}, {style: {'color': color}})
            i += 1
    splitted_pdb = pdb2.split("\n")
    i=0
    if style == "cartoon_stick":
        for line in splitted_pdb:
            #Split each line into a list 
            splitted_pdb_line = line.split()
            if len(splitted_pdb_line) == 0 or splitted_pdb_line[0] != "ATOM":
                continue
            if splitted_pdb_line[5] in position:
                color = highlight_colour
                view.setStyle({'model': -1, 'serial': i+1}, {"stick": {'color': color}})
            else:
                color = "grey"
                view.setStyle({'model': -1, 'serial': i+1}, {"cartoon": {'color': color}})
            i += 1
    else:
        for line in splitted_pdb:
            #Split each line into a list 
            splitted_pdb_line = line.split()
            if len(splitted_pdb_line) == 0 or splitted_pdb_line[0] != "ATOM":
                continue
            if splitted_pdb_line[5] in position:
                color = highlight_colour
            else:
                color = "grey"
            view.setStyle({'model': -1, 'serial': i+1}, {style: {'color': color}})

    return view