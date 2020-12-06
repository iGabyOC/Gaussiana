#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hp240
"""
#Gaussiana
import matplotlib.pyplot as plt
import numpy as np
import math as mt

def Gaussiana(x,s,m):
    a=(1/(s*(mt.sqrt(2*np.pi))))
    b=np.exp(-( (x-m)**2 / ( 2.0 * s**2 ) ) )
    Gauss=a*b
    return Gauss

x_valores=np.arange(-6,10,0.1)
m1=3
s1=1
m2=0
s2=0.5
m3=2
s3=3

s4=2
m4=1
s5=6
m5=3

plt.plot(x_valores,Gaussiana(x_valores,s1,m1), color='turquoise', label='μ=3, σ=1')
plt.plot(x_valores,Gaussiana(x_valores,s2,m2), color='deeppink', label='μ=0, σ=0.5')
plt.plot(x_valores,Gaussiana(x_valores,s3,m3), color='purple', label='μ=2, σ=3')
#Cambios git
plt.plot(x_valores,Gaussiana(x_valores,s4,m4), color='green')
plt.plot(x_valores,Gaussiana(x_valores,s5,m5), color='yellow')



plt.legend(loc=1)
plt.title('Gaussiana')
plt.xlabel('X')
plt.ylabel('Gμ,σ(X)')
plt.show()