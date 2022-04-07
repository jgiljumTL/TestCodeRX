
import os
import tkinter as tk
import matplotlib.pyplot as plt
from skrf import Network
from tkinter import filedialog
from tkinter import *


files =[]
run = 1

root = tk.Tk()
root.withdraw()

while run == 1: #loop for adding file paths
    file_path = filedialog.askopenfilename() #opens tkinter dialog box for operator to select the .s2p file
    #my_btn = Button(root, text="Close", command=exit)

    if file_path == "":
        run = 0
    else:
        run = 1

    files.append(file_path) #add the .s2p file path to the files list



for x in files: #loop for pulling pulling items from files list
    if x == "":
        break
    else:
        h = Network(x) #pulls just the file name from the entire file path stored in the files list and converts it to a network object
        h.s21.plot_s_db() #plots each network object (s21_dB)



plt.show() #plot all of the network object from above.

