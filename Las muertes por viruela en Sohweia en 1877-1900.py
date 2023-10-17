#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 06:39:56 2022

@author: hozkr
"""
import pandas as pd
import numpy as np 
import math
import matplotlib.pylab as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')
plt.rcParams["font.size"] = 16


data = pd.read_excel("Las_muertes_por_viruela_en_Suiza_ en_1877_1900.xlsx")
data=np.array(data)
nme=data[2:,0];nmu=data[2:,1];nmt=data[2:,4];nmt18=data[2:,5];nmt14=data[2:,6]
plt.figure()
plt.plot(nme,nmt,'.',color="black")#graficando c1 vs c2
plt.plot(nme,nmt18,'--',color="black")#graficando c1 vs c2
plt.plot(nme,nmt14,'-.',color="black")#graficando c1 vs c2
plt.xlabel(r"Meses")
plt.ylabel(r"Número de muertes")
plt.xlim([0,60])
plt.ylim([0,300])
plt.grid()
plt.show()
#-----------------------------------------------------------------------------
h=5.5
d=14.2
mt=288
#r=np.arange(0,62)
pr=np.empty(mt)
r=0
#p=288*((h**r)*(np.exp(-h)))/math.factorial(r)
#p=round(p,1)

p=288*((1+d)**(-h/d)*(1/math.factorial(r)))#*(h/(1+d)))
p=round(p,1)
pt=1
for i in range(1):
    pt=pt*(h+i*d)
    #pr[i]=288*((1/math.factorial(i))*(h+i*d)*((1+d)**(-(h/d)-i)))
    
    pr=288*((1/math.factorial(i))*pt*((1+d)**(-(h/d)-i)))
#pr=round(pr,1)

#a=sum(nme*nmu)/285
#p=np.empty(len(r))
#for i in range(len(r)):
#    p[i]=288*((h**r[i])*(np.exp(h)))/math.factorial(r[i])
#p=((h**r)(np.exp(h)))/math.factorial(r)


