
import os
import tkinter as tk
import matplotlib.pyplot as plt
from skrf import Network
from tkinter import filedialog


files =[]


root = tk.Tk()
root.withdraw()

for y in files: #loop for adding file paths
    file_path = filedialog.askopenfilename() #opens tkinter dialog box for operator to select the .s2p file
    files.append(file_path) #add the .s2p file path to the files list

for x in files: #loop for pulling pulling items from files list
    h = Network(os.path.basename(x)) #pulls just the file name from the entire file path stored in the files list and converts it to a network object
    h.s21.plot_s_db() #plots each network object (s21_dB)



plt.show() #plot all of the network object from above.

