def SeedBankC():
    Plants = int(input("Enter the number of active individuals: "))
    Seeds = int(input("Enter the number of inactive individuals: "))
    iterations = int(input("Enter the number of iterations: "))
    C_1 = 1 = int(input("Enter c_1: "))
    C_2 = 1 = int(input("Enter c_2 "))
    NGamma = []
    MGamma = []
    TGamma = []
    NTheta = []
    MTheta = []
    TTheta = []
    
    
    pbar = tqdm(total=iterations)
    for l in range(iterations):
        time.sleep(1)
        pbar.update(1)
        i = Plants
        j = Seeds
        Time = np.float64(0)
        Check_1 = True
        Check_2 = True
    
        while Check_1: 
            if i > 1:
                lambda1 = (i*(i-1))/2
                lambda2 = i*C_1
                CTime = np.float64(expon.rvs(loc=0, scale=1/lambda1, size=1))
                DTime = np.float64(expon.rvs(loc=0, scale=1/lambda2, size=1))
                if DTime > CTime:
                    i -= 1
                    Time += CTime 
                else:
                    i -= 1
                    j += 1
                    Time += DTime
                    Check_1 = False
            else:
                lambda2 = i*C_1
                DTime = np.float64(expon.rvs(loc=0, scale=1/lambda2, size=1))
                Time += DTime
                i -= 1
                j += 1
                Check_1 = False
                
        NGamma.append(i)
        MGamma.append(j)
        TGamma.append(Time)
    
    
        while Check_2:
            if i > 1: 
                lambda1 = (i*(i-1))/2
                lambda2 = i*C_1
                lambda3 = j*C_2
                CTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda1, size = 1))
                DTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda2, size = 1))
                ATime = np.float64(expon.rvs(loc = 0, scale = 1/lambda3, size = 1))
                if DTime > CTime and ATime > CTime:
                    i -= 1
                    Time += CTime
                elif CTime > DTime and ATime > DTime:
                    i -= 1
                    j += 1
                    Time += DTime
                else:
                    i += 1
                    j -= 1
                    Time += ATime
                    Check_2 = False
            elif i == 1: 
                lambda2 = i*C_1
                lambda3 = j*C_2
                DTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda2, size = 1))
                ATime = np.float64(expon.rvs(loc = 0, scale = 1/lambda3, size = 1))
                if ATime > DTime:
                        i -= 1
                        j += 1
                        Time += DTime
                else:
                    i += 1
                    j -= 1
                    Time += ATime
                    Check_2 = False
            else: 
                lambda3 = j*C_2
                ATime = np.float64(expon.rvs(loc = 0, scale = 1/lambda3, size = 1))
                i += 1
                j -= 1
                Time += ATime
                Check_2 = False
        NTheta.append(i)
        MTheta.append(j)
        TTheta.append(Time)     
    pbar.close()
    
    df = pd.DataFrame()
    df["NGamma"] = NGamma
    df["MGamma"] = MGamma
    df["TGamma"] = TGamma
    df["NTheta"] = NTheta
    df["MTheta"] = MTheta
    df["TTheta"] = TTheta
    
    df.to_csv(str(Plants)+'P'+str(Seeds)+'S'+'SeedBank.csv', index = False)
