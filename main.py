###############################
# Author:
# Vicente and MAL
# Code:
# This file containes the funtions in the files
# Coalescent_SeedBank.py, Coalescent_SeedBank_Sigma.py, 
# Coalescent_SeedBank_Process.py and Plots.py
# This is for easier use
###############################

import pandas as pd
import numpy as np
from scipy.stats import expon
from scipy.stats import beta
from scipy.stats import ks_2samp as ks
from scipy.stats import invweibull 
from numpy import log as ln
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import glob
import time
from tqdm import tqdm 

# This seed is to recreate the p-values that can be seen on the thesis
np.random.seed(1602)

from Coalescent_SeedBank.py import SeedBankC
from Coalescent_SeedBank_Sigma.py import SeedBankCSigma
from Coalescent_SeedBank_Process.py import SeedBankCProcess
from Plots.py import SBPlots

# Functions SeedBankC, SeedBankCSigma(), SeedBankCProcess(), and SBPlots(). Do not require
# any arguments; all requirements are shown as inputs.

