
"""
Created on Wed Mar 22 18:39:18 2023

@author: kagan
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from scipy import integrate
from tkinter import *

class MyWindow:
    def __init__(self,win):
        self.lbl1 = Label(win, text = 'Hs[m]')
        self.lbl2 = Label(win, text = 'Tz[s]')
        self.lbl3 = Label(win, text = 'Wmin')
        self.lbl4 = Label(win, text = 'γ')
        self.lbl7 = Label(win, text = 'Wmax')
        self.lbl8 = Label(win, text = 'W Number')
        self.lbl9 = Label(win, text = 'M0')
        self.lbl10 = Label(win, text = 'M1')
        self.lbl11 = Label(win, text = 'M2')
        self.lbl12 = Label(win, text = 'M4')
        self.lbl13 = Label(win, text = 'MOMENTS')
        self.lbl14 = Label(win, text = '4m0^0.5 = ')
        self.lbl15 = Label(win, text = 'Non dimensional peak shape parameter γ ∈ [1,7]')
        self.lbl16 = Label(win, text = 'W Number = Number of Frequency Intervals')
        self.btn = Button(win, text = 'Calculate')
        self.btn2 = Button(win, text = 'Clean')
        self.t1=Entry(bd=1)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t7=Entry()
        self.t8=Entry()
        self.t9=Entry()
        self.t10=Entry()
        self.t11=Entry()
        self.t12=Entry()
        self.t13=Entry()
        self.lbl1.place(x=60, y=50)
        self.t1.place(x=100, y=50)
        self.lbl2.place(x=60, y=75)
        self.t2.place(x=100, y=75)
        self.lbl3.place(x=60,y=100)
        self.t3.place(x=100,y=100)
        self.lbl4.place(x=60,y=125)
        self.t4.place(x=100,y= 125)
        self.lbl7.place(x=250,y=100)
        self.t7.place(x=290,y=100)
        self.lbl8.place(x=440,y=100)
        self.t8.place(x=500,y=100)
        self.b1 = Button(win, text='Calculate', command=self.calc)
        self.b1.place(x=200, y=150)
        self.b2 = Button(win, text = 'Clear', command= self.clean)
        self.b2.place(x=300, y= 150)
        self.t9.place(x=100,y=250)
        self.lbl9.place(x=60,y=250)
        self.t10.place(x=100,y=275)
        self.lbl10.place(x=60,y=275)
        self.t11.place(x=100,y=300)
        self.lbl11.place(x=60,y=300)
        self.lbl12.place(x=60,y=325)
        self.t12.place(x=100,y=325)
        self.lbl13.place(x=140,y=225)
        self.t13.place(x=135,y=400)
        self.lbl14.place(x=60, y=400)
        self.lbl15.place(x=700, y=500)
        self.lbl16.place(x=700, y=520)
    def calc(self):
        self.t9.delete(0, 'end')
        self.t10.delete(0, 'end')
        self.t11.delete(0, 'end')
        self.t12.delete(0, 'end')
        Hs = float(self.t1.get())
        Tz = float(self.t2.get())
        w_min = float(self.t3.get())
        w_max = float(self.t7.get())
        no_w = int(self.t8.get())
        gamma = float(self.t4.get())
        w = np.linspace(w_min,w_max,no_w)
        A_gamma = 1 - 0.287*np.log(gamma)
        Tp = Tz / (0.6673+(0.05037*gamma)-(0.00623*gamma**2)+(0.0003341*gamma**3))
        Wp = 2*np.pi/Tp
        S_pm = (5/16)*((Hs**2*Wp**4)/(w**5))*np.exp((-5/4)*(w/Wp)**(-4))
        sigma = 0.09
        S_j = A_gamma*S_pm*gamma**(np.exp(-0.5*((w-Wp)/(sigma*Wp))**2))
        A= (123*Hs**2)/(Tz**4)
        B= 495/(Tz**4)
        S_ittc = (A / w**5 ) * np.exp(-B/w**4)
        fig = plt.figure(figsize=(6, 4), dpi=100)
        fig.patch.set_facecolor('lightgray')
        plt.plot(w, S_j, linestyle='-', color='blue', label='Johnswap')
        plt.plot(w, S_pm, linestyle='--', color='red', label='Pierson-Moskowitz')
        plt.plot(w, S_ittc, linestyle='-.', color='green', label='ITTC Spectra')
        plt.xlabel("Wave Frequency")
        plt.ylabel('S(w)')
        plt.legend()  
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.show()
        canvas = FigureCanvasTkAgg(fig, master = window)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas,window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=RIGHT)
        self.fig = fig
        self.canvas = canvas
        self.toolbar = toolbar
        m_0 = integrate.simps(S_j,w)
        m_1 = integrate.simps(S_j*w,w)        
        m_2 = integrate.simps(S_j*w**2,w)
        m_4 = integrate.simps(S_j*w**4,w)
        self.t9.insert(END, str(m_0))
        self.t10.insert(END, str(m_1))
        self.t11.insert(END, str(m_2))
        self.t12.insert(END, str(m_4))
        result = 4 * np.sqrt(m_0)
        self.t13.insert(END, str(result)) 
        error = abs(result - Hs) / Hs * 100
        if error <= 2.5:
            self.lbl14.config(text="Results are matched within a 2.5 percent error.")
        else:
            self.lbl14.config(text="Results are not in 2.5 percent error margin")
        self.lbl14.place(x=60,y=450)
        
    def clean(self):
        global restart
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)
        self.t9.delete(0, END)
        self.t10.delete(0, END)
        self.t11.delete(0, END)
        self.t12.delete(0, END)
        self.t13.delete(0, END)
        self.lbl14.config(text="")

        if self.fig and self.canvas and self.toolbar:
            self.fig.clear()
            self.canvas.draw()
            self.toolbar.pack_forget()  
            self.canvas.get_tk_widget().pack_forget() 

        self.restart = 1

window=Tk()
mywin=MyWindow(window)
window.title('Wave Spectra Calculator')
window.geometry("1280x600+10+10")
window.mainloop()



