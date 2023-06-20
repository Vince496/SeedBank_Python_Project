def SeedBankCProcess():
    Plants = int(input("Enter the number of active individuals: "))
    Seeds = int(input("Enter the number of inactive individuals: "))
    i = Plants
    j = Seeds
    C_1 =  int(input("Enter c_1: "))
    C_2 = int(input("Enter c_2: "))
    
    N = list()
    M = list()
    Actives = list()
    Inactives = list()
    Times = list()
    Events = list()
    
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
                Events.append("Activación")
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
                    Events.append("Coalescencia")
                else:
                    i -= 1
                    j += 1
                    Times.append(DTime)
                    Events.append("Desactivación")
        Actives.append(i)
        Inactives.append(j)
    
    
    df = pd.DataFrame()
    df["N"] = Actives
    df["M"] = Inactives
    df["Tiempos"] = Times
    df["Ocurrencia"] = Events
    
    df.to_csv(str(Plants)+'P'+str(Seeds)+'S_Seed-Bank_Process.csv', index = False)
    
