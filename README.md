# variant visualization
A small jupyter notebook which is used to highlight variant .pdb files using py3dmol

# Setup
1. **Clone this repository and change directory:**
   ```sh
   git clone https://github.com/jerkrause/variant_visualization
   cd variant_visualization
   ```
2. **Create a conda environment and activate it:**
   ```sh
   conda create -n pdb_visualizer python=3.11.9
   conda activate pdb_visualizer
   ```
3. **Install requirements:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the streamlit application:**
   ```sh
   streamlit run run_pdb_vis.py
   ```