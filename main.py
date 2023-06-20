#############################################################################
# Author:
# Vicente and MAL
# Code:
# This file containes the funtions in the files
# Coalescent_SeedBank.py, Coalescent_SeedBank_Sigma.py, 
# Coalescent_SeedBank_Process.py and Plots.py
# This is for easier use
##############################################################################


from Coalescent_SeedBank import SeedBankC
from Coalescent_SeedBank_Sigma import SeedBankCSigma
from Coalescent_SeedBank_Process import SeedBankCProcess
from Plots import SBPlots


# This seed is to recreate the p-values that can be seen on the thesis
np.random.seed(1602)

# Functions: SeedBankCSigma( Plants , Seeds , C_1 , C_2 , iterations )
#            SeedBankCProcess( Plants , Seeds , C_1 , C_2 )
#            SeedBankC( Plants , Seeds , C_1 , C_2 , iteration )
#            SBPlots() 
#            The SBplots function read the files on the folder and all 
#            requirements are shown as inputs.
##############################################################################

