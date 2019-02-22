import os
import sys
import subprocess

os.chdir(sys.argv[1])

for f in os.listdir('.'):
    if os.path.isfile(f):
        subprocess.call(["python","C:\Users\jon\Documents\img_resizer.py",f,1000])
        
