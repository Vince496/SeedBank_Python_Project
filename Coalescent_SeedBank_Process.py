import pandas as pd
import numpy as np
from scipy.stats import expon

def SeedBankCProcess(Plants,Seeds,C_1,C_2):
    i = Plants
    j = Seeds
    
    Actives = list([Plants])
    Inactives = list([Seeds])
    Times = list([0])
    Events = list(["None"])
    
    Check = True
    
    while Check:
        if j > 0:
            if i > 1:
                lambda1 = (i*(i-1))/2
                lambda2 = i*C_1
                lambda3 = j*C_2
                CTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda1, size = 1))
                DTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda2, size = 1))
                ATime = np.float64(expon.rvs(loc = 0, scale = 1/lambda3, size = 1))
                if DTime > CTime and ATime > CTime:
                    i -= 1
                    Times.append(CTime)
                    Events.append("Coalescence")
                elif CTime > DTime and ATime > DTime:
                    i -= 1
                    j += 1
                    Times.append(DTime)
                    Events.append("Deactivation")
                else:
                    i += 1
                    j -= 1
                    Times.append(ATime)
                    Events.append("Activation")
            elif i == 1:
                lambda2 = i*C_1
                lambda3 = j*C_2
                DTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda2, size = 1))
                ATime = np.float64(expon.rvs(loc = 0, scale = 1/lambda3, size = 1))
                if ATime > DTime:
                    i -= 1
                    j += 1
                    Times.append(DTime)
                    Events.append("Deactivation")
                else:
                    i += 1
                    j -= 1
                    Times.append(ATime)
                    Events.append("Activation")
            else:
                lambda3 = j*C_2
                ATime = np.float64(expon.rvs(loc = 0, scale = 1/lambda3, size = 1))
                i += 1
                j -= 1
                Times.append(ATime)
                Events.append("Activation")
        else:
            if i == 1:
                break
            else:
                lambda1 = (i*(i-1))/2
                lambda2 = i*C_1
                CTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda1, size = 1))
                DTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda2, size = 1))
                if DTime > CTime:
                    i -= 1
                    Times.append(CTime)
                    Events.append("Coalescence")
                else:
                    i -= 1
                    j += 1
                    Times.append(DTime)
                    Events.append("Deactivation")
        Actives.append(i)
        Inactives.append(j)
    
    
    SeedBankProcess = pd.DataFrame()
    SeedBankProcess["N(t)"] = Actives
    SeedBankProcess["M(t)"] = Inactives
    SeedBankProcess["Times"] = Times
    SeedBankProcess["Events"] = Events
    SeedBankProcess.to_csv(str(Plants)+'P'+str(Seeds)+'S_SeedBank_Process.csv', index = False)
    return(SeedBankProcess)
