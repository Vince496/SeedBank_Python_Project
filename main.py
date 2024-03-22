#############################################################################
# Author:
# Vicente and MAL
# Code:
# This file containes the funtions in the files
# Coalescent_SeedBank.py, Coalescent_SeedBank_Sigma.py, 
# Coalescent_SeedBank_Process.py and Plots.py
# This is for easier use
##############################################################################


# Import required functions
from Coalescent_SeedBank import SeedBankC
from Coalescent_SeedBank_Sigma import SeedBankCSigma
from Coalescent_SeedBank_Process import SeedBankCProcess
from Plots import SBPlots

# Define function parameters
num_plants = 10
initial_seeds = 0
activation_rate = 1
deactivation_rate = 1
num_iterations = 10

# Run simulations
seedbank_c = SeedBankC(num_plants, initial_seeds, deactivation_rate, 
                       activation_rate, num_iterations)
# This results in a csv like this:
#    NGamma  MGamma    TGamma  NTheta  MTheta    TTheta
# 0       1       1  0.759405       1       1  2.606253
# 1       3       1  0.326184       2       1  0.606984
# 2       6       1  0.100459       2       3  0.681716
# 3       8       1  0.031393       2       1  1.144467
# 4       4       1  0.177389       4       1  0.251287
# 5       1       1  0.977625       2       0  1.656141
# 6       4       1  0.253320       5       0  0.465251
# 7       9       1  0.008163       3       2  0.923082
# 8       5       1  0.067697       2       2  0.916792
# 9       3       1  0.167301       4       0  0.501972

seedbank_csigma = SeedBankCSigma(num_plants, initial_seeds, deactivation_rate, 
                       activation_rate, num_iterations)
# This results in a csv like this:
#    NGamma  MGamma    TGamma  NTheta  ...    TTheta  Nsigma  Msigma     TSigma
# 0       8       1  0.011498       3  ...  0.399689       1       0  13.652346
# 1       9       1  0.010063       3  ...  0.204304       1       0  11.792251
# 2       0       1  1.484018       1  ...  1.535702       1       0   1.535702
# 3       6       1  0.047282       2  ...  0.804284       1       0  11.075094
# 4       6       1  0.254474       4  ...  0.926500       1       0  15.470028
# 5       9       1  0.005737       5  ...  0.242726       1       0  12.091059
# 6       4       1  0.204347       3  ...  0.578725       1       0   7.169288
# 7       7       1  0.101355       8  ...  0.248332       1       0   3.317057
# 8       8       1  0.017099       5  ...  0.130401       1       0   3.032099
# 9       1       1  0.162788       2  ...  0.182460       1       0   3.986727

# Generate plots 
SBPlots(deactivation_rate, activation_rate)

# This file ask you to indicate the files you wanna use:
 
# Do you wanna use a seed? [y/n] "Input"
# set seed: "Input"
# We shall include the 10P0SSeedBank.csv file? [y/n] : "Input"
# We shall include the 10P0SSeedBankSigma.csv file? [y/n] : "Input"

print("Simulations completed. See generated plots.")


SeedBankCProcess(num_plants, initial_seeds, deactivation_rate, activation_rate)

# This results in a csv like this:
#      N(t)  M(t)     Times        Events
# 0      9     0  0.002069   Coalescence
# 1      8     0  0.003188   Coalescence
# 2      7     0  0.055631   Coalescence
# 3      6     0  0.049943   Coalescence
# 4      5     1  0.031999  Deactivation
# 5      4     1  0.035898   Coalescence
# 6      3     1  0.083938   Coalescence
# 7      2     2  0.210840  Deactivation
# 8      1     3  0.118292  Deactivation
# 9      0     4  0.028749  Deactivation
# 10     1     3  0.075810    Activation
# 11     2     2  0.616609    Activation
# 12     1     3  0.464129  Deactivation
# 13     2     2  0.161334    Activation
# 14     1     3  0.164597  Deactivation
# 15     2     2  0.272874    Activation
# 16     3     1  0.035160    Activation
# 17     2     2  0.075716  Deactivation
# 18     1     2  0.208690   Coalescence
# 19     0     3  0.601247  Deactivation
# 20     1     2  0.123612    Activation
# 21     2     1  0.073821    Activation
# 22     1     2  0.208647  Deactivation
# 23     2     1  1.417734    Activation
# 24     1     2  0.577575  Deactivation
# 25     2     1  0.156917    Activation
# 26     1     2  0.264542  Deactivation
# 27     0     3  0.072388  Deactivation
# 28     1     2  0.056920    Activation
# 29     2     1  0.315016    Activation
# 30     3     0  0.023642    Activation
# 31     2     0  0.107297   Coalescence
# 32     1     0  0.221540   Coalescence 




##############################################################################

