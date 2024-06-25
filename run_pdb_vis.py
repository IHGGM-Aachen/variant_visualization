"""
File used to run the CNVizard, a streamlit app that visualizes germline-copy-number-variants
@author: Jeremias Krause / Matthias Begemann / Florian Kraft
@company: UKA Aachen (RWTH)
@mail: jerkrause@ukaachen.de
"""


import streamlit as st
import pandas as pd
import py3Dmol
from Color_function import highlight_AA
import os
import ipywidgets as widgets
from stmol import showmol

st.set_page_config(layout="wide", page_title="PDB Visualizer")
#Title of App
st.title("PDB Visualizer")
#General Description
st.markdown("This is a streamlit webapp which visualizes pdb files")

cwd = os.getcwd()
esm_input_folder = str(cwd) + "/esm_files/"
alphafold_input_folder = str(cwd) + "/alphafold_files/"


st.sidebar.title("About")
st.sidebar.markdown("This streamlit webapps highlights the position of genetic variants in their corresponding 3-D protein structure")

#The sidebar additionally enables the user to select a candigene (which will be loaded from the previously candi_annotation_folder)
st.sidebar.subheader("Model Selection")
#Declare streamlit selection object 
selected_model = st.sidebar.radio("Please select the desired Model",["alphafold","esmfold"])

if selected_model == "alphafold":
    input_folder = alphafold_input_folder
else:
    input_folder = esm_input_folder

cols_filter = st.columns(3)
selected_variant = cols_filter[0].multiselect("variant",os.listdir(input_folder),max_selections=1)
position = str(cols_filter[1].text_input("Protein Position"))
highlight_colour = str(cols_filter[2].text_input("highlight colour", value="cyan"))

cols_rotation = st.columns(3)
x = int(cols_rotation[0].number_input("x-axis", value=100))
y = int(cols_rotation[1].number_input("y-axis", value=30))
z = int(cols_rotation[2].number_input("z-axis", value=40))

style = st.selectbox("Select stlye",["stick","cartoon","sphere","cartoon_stick"])

if len(selected_variant)!=0:
    st.write("selected variant file " + selected_variant[0])
    input_pdb = input_folder+selected_variant[0]
    view = highlight_AA.color_pdb(input_pdb,position,highlight_colour,style)
    view.rotate(x,"x")
    view.rotate(y,"y")
    view.rotate(z,"z")
    view.zoomTo()
    showmol(view,height = 500,width=800)

