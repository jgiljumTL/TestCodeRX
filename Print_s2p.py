

import tkinter as tk
import matplotlib.pyplot as plt
from skrf import Network
from tkinter import filedialog


files =["RX25AF_U01283_VNA_N_BWL=0,00_BWH=0,00_GC=1,50_00.s2p","RX25AF_U00840_VNA_N_BWL=2,70_BWH=2,70_GC=2,20_00.s2p"]

#t = Network("RX25AF_U01283_VNA_N_BWL=0,00_BWH=0,00_GC=1,50_00.s2p")
#r = Network("RX25AF_U00840_VNA_N_BWL=2,70_BWH=2,70_GC=2,20_00.s2p")

root = tk.Tk()
root.withdraw()



file_path = filedialog.askopenfilename()

for x in files:
    h = Network(x)
    h.s21.plot_s_db()


#t.s21.plot_s_db() #Plot only s21 parameter
#r.s21.plot_s_db()

plt.show()

