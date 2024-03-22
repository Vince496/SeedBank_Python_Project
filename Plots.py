
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



def SBPlots(c_1,c_2):
    gammagrid = np.linspace(0,1, 100000)
    thetagrid = np.linspace(0,12, 100000)
    frgrid = np.linspace(0,100, 100000)
    
    # The following seed is for replicating the p-values found in the thesis
    # "Análisis de Convergencia en el Coalescente Seed-Bank: 
    #  una aplicación del Método Monte Carlo"
    # np.random.seed(1602) 
    # In Scipy, the invweibull function and the Fréchet function are synonyms.
    seed_res = input("Do you wanna use a seed? [y/n]: ")
    if "y" in seed_res or "Y" in seed_res :
        np.random.seed(int(input("set seed: ")))
        controltheta = expon(scale = .5).cdf(thetagrid)
        controlgamma = beta(a = 2 , b = 1).cdf(gammagrid)
        controlfr = invweibull(c=1,scale = 4).cdf(frgrid)
    else:
        controltheta = expon(scale = .5).cdf(thetagrid)
        controlgamma = beta(a = 2 , b = 1).cdf(gammagrid)
        controlfr = invweibull(c=1,scale = 4).cdf(frgrid)
        
    gammaks=beta.rvs(a=2*c_1,b=1,size=800,loc=0)
    tethaks=expon.rvs(scale=1/(2*c_1*c_2),loc=0,size=800)
    frks=invweibull.rvs(c=1,scale=4*c_1*c_2,loc=0,size=800)
    csv_fil = glob.glob("*.csv")
    pk = list()    
    pnk = list()
    pt = list()    
    pnt = list()
    plants = list()
    csv_files = list()
    csv_index = list()
    csv_sigma_index = list()
    csv_sigma = list()
    for file in csv_fil:
        resp = input('We shall include the '+ str(file) +' file? [y/n] : ')
        if 'y' in resp or 'Y' in resp: 
            csv_index.append(int( str(file).split("P")[0] ) )
            csv_files.append(file)
            if 'Sigma' in file:
                csv_sigma.append(file)
                csv_sigma_index.append(int( str(file).split("P")[0] ) )
    mapping = {file: index for file, index in zip(csv_index,csv_files)}
    csv_files = [index for _, index in sorted(mapping.items())]
    csv_index.sort()
    mapping2 = {file: index for file, index in zip(csv_sigma_index,csv_sigma)}
    csv_sigma = [index for _, index in sorted(mapping2.items())]
    
    green = np.array([0.0, 1.0, 0.0])
    red = np.array([1.0, 0.0, 0.0])
    n = len(csv_index)+1
    rgb = []
    for i in range(n):
        color = tuple((1 - i/(n-1)) * green + (i/(n-1)) * red)
        rgb.append(color)
    
    unos = np.ones(1000)
    gridunos = np.linspace(0,1000,100000)
    ECTunos = ECDF(unos)
    PECTunos = ECTunos(gridunos)
    
    graficas = (['NGamma', 'TGamma', 'NTheta', 'MTheta', 'TTheta','TSigma'])
    
    
    for grafica in graficas:
        if not grafica == 'TSigma':
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6) )
            for file in csv_files:
                df_aux = pd.read_csv(file)
                col = rgb[csv_index.index(int(file.split("P")[0] ))]
                file = int( str(file).split("P")[0] )
                if grafica == 'NGamma':
                    aux = df_aux.NGamma/int(file)
                    k = ks(aux,gammaks)
                    file = str(file)+" iterations: "+str(len(aux))
                    pnk.append(k.pvalue) 
                    plants.append(file.split(" ")[0])
                if grafica == 'TGamma':
                    aux = 1/((int(file)/2)*df_aux.TGamma+1)
                    k = ks(aux,gammaks)
                    file = str(file)+" iterations: "+str(len(aux))
                    pk.append(k.pvalue) 
                if grafica == 'NTheta':
                    aux = df_aux.NTheta/ln(int(file))
                    k = ks(aux,frks)
                    file = str(file)+" iterations: "+str(len(aux))
                    pnt.append(k.pvalue)
                    ax.set_xlim(0,100)
                if grafica == 'MTheta':
                    aux = df_aux.MTheta/(2*ln(int(file)))
                    file = str(file)+" iterations: "+str(len(aux))
                if grafica == 'TTheta':
                    aux = df_aux.TTheta*ln(int(file))
                    k = ks(aux,tethaks)
                    file = str(file)+" iterations: "+str(len(aux))
                    pt.append(k.pvalue)
                grid = np.sort(aux.unique())
                ECT = ECDF(aux)
                PECT = ECT(grid)
                ax.plot(grid, PECT,color =col ,label= str(file))
            if grafica == 'MTheta':
                plt.plot(gridunos, PECTunos ,"blue",label = "1" )
                ax.set_xlim(0,1.2)
                ax.set_title(r"$M_n(\theta_n)/(2c_1 \log n)$")
            if grafica == 'TTheta':
                plt.plot(thetagrid, controltheta ,color ="blue",label = "T" )
                ax.set_title(r"$\theta_n \log n$")
                ax.set_xlim(0,6)
            if grafica == 'NTheta':
                plt.plot(frgrid, controlfr ,"blue",label = "Z" )
                ax.set_title(r"$N(\theta_n)/(\log n)$")
            if "TGamma" == grafica:
                plt.plot(gammagrid, controlgamma ,color ="blue",label = "Y" )
                ax.set_title(r"$1/(\frac{n}{2}\gamma_n+1)$")
            if "NGamma" == grafica:
                plt.plot(gammagrid, controlgamma ,color ="blue",label = "Y" )
                ax.set_title(r"$N_n(\gamma_n)/n$")
            ax.legend();
            plt.savefig(grafica+".pdf")
            if grafica == 'NGamma':
                fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6) )
                for file in csv_files:
                    df_aux = pd.read_csv(file)
                    col = rgb[csv_index.index(int(file.split("P")[0] ))]
                    file = int( str(file).split("P")[0] )
                    aux = df_aux.NGamma/int(file)
                    grid = np.sort(aux.unique())
                    ECT = ECDF(aux)
                    PECT = ECT(grid)
                    resta = abs(PECT - beta.cdf(grid,a=2,b=1))
                    ax.plot(grid, resta,color =col, label= str(file))
                ax.set_title(r"$|N_n(\gamma_n)/n - Y|$")
                ax.set_xlabel('Grid empirical')
                plt.axhline(y = 0,color='black')
                ax.legend();
                plt.savefig("Dif" + str(grafica)+".pdf")
            if grafica == 'TGamma':
                fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6) )
                for file in csv_files:
                    df_aux = pd.read_csv(file)
                    col = rgb[csv_index.index(int(file.split("P")[0] ))]
                    file = int( str(file).split("P")[0] )
                    aux = 1/((int(file)/2)*df_aux.TGamma+1)
                    grid = np.sort(aux.unique())
                    ECT = ECDF(aux)
                    PECT = ECT(grid)
                    resta = abs(PECT - beta.cdf(grid,a=2,b=1))
                    ax.plot(grid, resta,color =col, label= str(file))
                ax.set_title(r"$|1/(\frac{n}{2}\gamma_n+1) - Y|$")
                ax.set_xlabel('Grid empirical')
                plt.axhline(y = 0,color='black')
                ax.legend();
                plt.savefig("Dif" + str(grafica)+".pdf")
            if grafica == 'TTheta':
                fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6) )
                for file in csv_files:
                    df_aux = pd.read_csv(file)
                    col = rgb[csv_index.index(int(file.split("P")[0] ))]
                    file = int( str(file).split("P")[0] )
                    aux = df_aux.TTheta*ln(int(file))
                    grid = np.sort(aux.unique())
                    ECT = ECDF(aux)
                    PECT = ECT(grid)
                    resta = abs(PECT - expon.cdf(grid,scale = .5))
                    ax.plot(grid, resta,color =col, label= str(file))
                ax.set_title(r"$|\theta_n \log n - T|$")
                ax.set_xlabel('Grid empirical')
                plt.axhline(y = 0,color = 'black')
                ax.legend();
                plt.savefig("Dif" + str(grafica)+".pdf")
            if grafica == 'NTheta':
                fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6) )
                for file in csv_files:
                    df_aux = pd.read_csv(file)
                    col = rgb[csv_index.index(int(file.split("P")[0] ))]
                    file = int( str(file).split("P")[0] )
                    aux = df_aux.NTheta/ln(int(file))
                    grid = np.sort(aux.unique())
                    ECT = ECDF(aux)
                    PECT = ECT(grid)
                    resta = abs(PECT - invweibull.cdf(grid,scale = 4,c=1))
                    ax.plot(grid, resta,color =col , label= str(file))
                ax.set_title(r"$|N(\theta_n)/(\log n) - Z$|")
                ax.set_xlabel('Grid empirical')
                ax.set_xlim(0,100)
                plt.axhline(y = 0,color ='black')
                ax.legend();
                plt.savefig("Dif" + str(grafica)+".pdf")
        else:
            if len(csv_sigma)==0:
                print("No file with sigma observations")
            else:
                fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6) )
                for file in csv_sigma:
                    df_aux = pd.read_csv(file)
                    col = rgb[csv_index.index(int(file.split("P")[0] ))]
                    file = int( str(file).split("P")[0] )
                    aux = df_aux.TSigma
                    aux = aux/ln(ln(file))
                    grid = np.sort(aux.unique())
                    ECT = ECDF(aux)
                    PECT = ECT(grid)
                    file = str(file)+" iterations: "+str(len(aux))
                    ax.plot(grid, PECT,color = col, label=str(file))
                plt.plot(gridunos, PECTunos ,color ="blue",label = "1" )
                ax.set_xlim(0,max(grid))
                ax.set_title(r'$\sigma_n/\log \log n$')
                ax.legend();
                plt.savefig('TSigma.pdf')
                plt.show();
    pvalues = pd.DataFrame({
    "N" : plants,
    r"$1/(\frac{n}{2}\gamma_n+1)$": pk,
    r"$N_n(\gamma_n)/n$": pnk,
    r"$\theta_n \log n$": pt,
    r"$N(\theta_n)/(\log n)$": pnt
    })
    pvalues["N"] = pvalues["N"].astype(int)
    pvalues = pvalues.sort_values(by='N', ascending=True)
    pvalues.to_csv("pvalues.csv")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    n = pvalues["N"].astype(str)
    y1 = pvalues[r"$1/(\frac{n}{2}\gamma_n+1)$"]
    y2 = pvalues[r"$N_n(\gamma_n)/n$"]
    ax.plot(n, -np.log(y1), label=r"$1/(\frac{n}{2}\gamma_n+1)$")
    ax.plot(n, -np.log(y2), label=r"$N_n(\gamma_n)/n$")
    ax.set_xlabel("Size population")
    ax.set_ylabel("-log(pvalue)")
    ax.legend()
    ax.set_title("Logaritmic transformation of p-values")
    fig.savefig("gamma_pvalues.pdf")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    n = pvalues["N"].astype(str)
    y1 = pvalues[r"$\theta_n \log n$"]
    y2 = pvalues[r"$N(\theta_n)/(\log n)$"]
    ax.plot(n, -np.log(y1), label=r"$\theta_n \log n$")
    ax.plot(n, -np.log(y2), label=r"$N(\theta_n)/(\log n)$")
    ax.set_xlabel("N")
    ax.set_ylabel("-log(pvalue)")
    ax.legend()
    ax.set_title("Logaritmic transformation of p-values")
    fig.savefig("theta_pvalues.pdf")
    




