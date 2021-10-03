import os
from tkinter import filedialog
a = Directory= filedialog.askdirectory()
#a = os.path.getsize('/home/kamy/test.txt')
f = open("fcdir.txt", "w")
f.write(a)
f.close()
os.system("ruby fcdir.rb")