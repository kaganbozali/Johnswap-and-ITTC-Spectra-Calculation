# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:02:13 2022

@author: Oğuz Kağan Bozali
"""
#Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#Main Dimensions
Hs = 1.5
Tz = 5.5
gamma = np.linspace(1.5,6.5,6)
A_gamma = 1 - 0.287*np.log(gamma)
Tp = Tz / (0.6673+(0.05037*gamma)-(0.00623*gamma**2)+(0.0003341*gamma**3))
Wp = np.pi*2/Tp
w = np.linspace(0.1,2.5,300)
sigma = []
for i in range(len(gamma)):
    for j in range(len(w)):
        if Wp[i]>=w[j]:
            sigma.append(0.07)
        else:
            sigma.append(0.09)
sigma = np.array(sigma)
sigma = np.split(sigma,len(gamma))
#Pierrson Moskowitz and Johnswap Spectrum
S_pm = []
S_johnswap = []
for i in range(len(gamma)):
    S_pm.append((5/16)*((Hs**2*Wp[i]**4)/(w**5))*np.exp((-5/4)*(w/Wp[i])**(-4)))
    S_johnswap.append(A_gamma[i]*S_pm[i]*gamma[i]**(np.exp(-0.5*((w-Wp[i])/(sigma[i]*Wp[i]))**2)))
S_johnswap = np.array(S_johnswap)
# Plot
for i in range(len(gamma)):
    plt.plot(w,S_johnswap[i],c='k')
    plt.xlabel('w,(rad/s)')
    plt.ylabel('S(w),m2/rad')
plt.legend()
plt.grid()
#plt.show()
#plt.savefig('Johnswap.jpg',dpi=1000)
#Moments Calculation
m_0 = []
m_1 = []
m_2 = []
for i in range(len(gamma)):
    m_0.append(integrate.simpson(S_johnswap[i],w))
    m_1.append(integrate.simpson(S_johnswap[i]*w,w))
    m_2.append(integrate.simpson(S_johnswap[i]*w**2,w))
if False:
    plt.plot(w,S_johnswap[2],label='S(w)')
    plt.plot(w,S_johnswap[2]*w,label='wS(w)')
    plt.plot(w,S_johnswap[2]*w**2,label=' w^2S(w)')
    plt.xlabel('w,(rad/s)')
    plt.ylabel('S(w),m2/rad')
    plt.grid()
    plt.legend()
    plt.savefig('a.jpg',dpi=1000)
    plt.show()
#ITTC
A= (123*Hs**2)/(Tz**4)
B= 495/(Tz**4)
S_ittc = (A / w**5 ) * np.exp(-B/w**4)
m_0_ITTC = integrate.simpson(S_ittc,w)
plt.plot(w,S_ittc,label='ITTC')
plt.legend()
plt.savefig('ITTC',dpi=1000)
