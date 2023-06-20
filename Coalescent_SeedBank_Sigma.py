def SeedBankCSigma():
    Plants = int(input("Enter the number of active individuals: "))
    Seeds = int(input("Enter the number of inactive individuals: "))
    iterations = int(input("Enter the number of iterations: "))
    
    C_1 = int(input("Enter c_1: "))
    C_2 =int(input("Enter c_2: "))1
    
    NGamma = list()
    MGamma = list()
    TGamma = list()
    NTheta = list()
    MTheta = list()
    TTheta = list()
    NSigma = list()
    MSigma = list()
    TSigma = list()
    
    
    pbar = tqdm(total=iterations)
    for l in range(iterations):
        i = Plants
        j = Seeds
        Time = np.float64(0)
        Check_1 = True
        Check_2 = True
        Check_3 = True
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
        
        
        while Check_2 == 1:
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
    
        while Check_3:
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
                        Time += CTime
                    elif CTime > DTime and ATime > DTime:
                        i -= 1
                        j += 1
                        Time += DTime
                    else:
                        i += 1
                        j -= 1
                        Time += ATime
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
                else:
                    lambda3 = j*C_2
                    AT = np.float64(expon.rvs(loc = 0, scale = 1/lambda3, size = 1))
                    i += 1
                    j -= 1
                    Time += ATime
            else:
                if i == 1:
                    Check_3 = False
                else:
                    lambda1 = (i*(i-1))/2
                    lambda2 = i*C_1
                    CTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda1, size = 1))
                    DTime = np.float64(expon.rvs(loc = 0, scale = 1/lambda2, size = 1))
                    if DTime > CTime:
                        i -= 1
                        Time += CTime
                    else:
                        i -= 1
                        j += 1
                        Time += DTime
        
        NSigma.append(i)
        MSigma.append(j)
        TSigma.append(Time)
        time.sleep(1)
        pbar.update(1)
    
        
        
    pbar.close()
    
    df=pd.DataFrame()
    df["NGamma"] = NGamma
    df["MGamma"] = MGamma
    df["TGamma"] = TGamma
    df["NTheta"] = NTheta
    df["MTheta"] = MTheta
    df["TTheta"] = TTheta
    df["Nsigma"] = NSigma
    df["Msigma"] = MSigma
    df["TSigma"] = TSigma
    df.to_csv(str(Plants)+"P"+str(Seeds)+"S"+'SeedBankSigma.csv', index = False)
