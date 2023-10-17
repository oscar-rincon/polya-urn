#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:22:50 2022

@author: hozkr
"""
import scipy

import scipy.special
import pandas as pd
import numpy as np 
import math
import matplotlib.pylab as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

data = pd.read_excel("Las_muertes_por_viruela_en_Suiza_ en_1877_1900.xlsx")
data=np.array(data)
nme=data[2:,0];nmu=data[2:,1];nmu14=data[2:,3];nmt=data[2:,4];nmt18=data[2:,5];nmt14=data[2:,6]
r=np.arange(0,61)
nmu=nmu[0:61]
nmu14=nmu14[0:61]

nme=nme[0:61]

h=sum(nmu*r)/288
a=((h-r)**2)*nmu
b=(sum(a)/287)
d1=(b/h)-1


r=np.arange(0,62)
h=5.5
d=15.9
rf=np.empty(62)
hdk=np.empty(62)
dk1d=np.empty(62)
P=np.zeros(61)

a=scipy.special.poch(h/d,1)

for i in range(61):

    rf[i]=1/math.factorial(i)
    hdk[i]=scipy.special.poch(h/d,i)
    dk1d[i]=(d**i)*((1+d)**(-(h/d)-i))
    P[i]=288*rf[i]*hdk[i]*dk1d[i]


plt.figure()
plt.plot(nme,nmu,'-',color="black")#graficando c1 vs c2
plt.plot(nme,nmu14,'-',color="green")#graficando c1 vs c2
plt.plot(nme,P,'-',color="red")#graficando c1 vs c2

#plt.plot(nme,nmt18,'--',color="black")#graficando c1 vs c2
#plt.plot(nme,nmt14,'-.',color="black")#graficando c1 vs c2
plt.xlabel(r"Meses")
plt.ylabel(r"Número de muertes")
#plt.xlim([0,60])
#plt.ylim([0,300])
plt.grid()
plt.show()


a1=scipy.stats.beta.fit(nmu)
#b1=scipy.stats.beta.pdf(nme, a1[0],a1[1])

