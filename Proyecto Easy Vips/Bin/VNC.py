import os
from tkinter import *
import subprocess
import AVEC2


def conectuvnc(list2): #VNC
    print(list2)
    print(".....")
    IP=list2[3]
    #IP = re.sub(r'\b0+(\d)', r'\1', list2[3])
    passwd="AcPe7@1t"
    port="5900"
    subprocess.Popen(r"UVNC\vncviewer.exe -autoscaling -encoding tight -compresslevel 8 -quality 3 -8greycolors -connect "+IP+":"+port+" -password "+passwd)
    #subprocess.Popen(r"UVNC\vncviewer.exe -connect "+IP+":"+port+" -quickoption 4 -password "+passwd)
    #os.system(r"UVNC\vncviewer.exe -connect "+IP+":"+port+" -quickoption 4 -password "+passwd)

def ping(list2):
    print(list2)
    print(".....")
    IP=list2[3]
    #IP = re.sub(r'\b0+(\d)', r'\1', list2[3])
    #os.system(r"UVNC\vncviewer.exe -connect "+IP+":6000 -quickoption 4 -password "+passwd)
    os.system("start cmd /c ping "+IP+" -t")

