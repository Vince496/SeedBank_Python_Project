# Vicente's Undergraduate Thesis Project: SeedBank Model Simulation and Verification

This repository contains the Python code for my undergraduate thesis titled "Análisis de Convergencia en el Coalescente Seed-Bank: una aplicación del Método Monte Carlo" (Convergence Analysis in the Seed-Bank Coalescent: A Monte Carlo Application). The code simulates the SeedBank model and statistically verifies theoretical results on seedbank tree lengths.

**Project Structure:**

* **CSV Folder:** Stores CSV files used to generate the thesis's graphs. These files contain raw data for visualizations.
* **Example Plots Folder:** Demonstrates how the `plots.py` script works. It includes plots generated from all CSV files in the `CSV Folder`.
* **pvalues.csv:** The file contains the p-values shown in my thesis, for your reference, which were obtained with the seed 1602. 
* **Coalescent_SeedBank.py:** Core script implementing simulations for the Kingman phase and Kingman phase with freezing.
* **Plots.py:** Generates plots from simulation results. It takes data and creates visualizations for exploration and analysis.
* **Coalescent_Seed-Bank_Sigma.py:** Simulates the complete coalescent tree, encompassing the entire model (from seed dispersal to coalescence). It builds upon `Coalescent_SeedBank.py`.
* **Coalescent_Seed-Bank_Process.py:** Simulates a single complete coalescent tree, saving all intermediate steps. This allows detailed tracking of the model's evolution for further analysis or debugging.

**Required Libraries:**

* pandas
* numpy
* scipy
* time
* tqdm
* matplotlib
* statsmodels
* glob









