import os 
import re
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print(type(dir_path))
s1 = dir_path.split('\\')
s1 = re.split(r'[\\/]', dir_path)
print(s1)

from tkinter import filedialog
dir = filedialog.askdirectory()
print(dir)
# split(r'[,;]', string)
s = re.split(r'[\\/]', dir)
print(s)