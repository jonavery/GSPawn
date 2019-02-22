import os
import sys
import subprocess

os.chdir(sys.argv[1])

for f in os.listdir('.'):
    if os.path.isfile(f):
        subprocess.call(["python",r"C:\Users\jon\Documents\img_resizer.py",sys.argv[1]+"\\"+f])
        
