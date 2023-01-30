import os
import subprocess
import sqlite3
import csv
import socket
import ipaddress

def insertincsv(il,ln,tp,hn,ip):

    with open('inventariocsvsort.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=';')

        fieldnames = [il,ln,tp,hn,ip]
        print(fieldnames)
        writer.writerow(fieldnames)


FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
filename = "scanresult.txt"
IPrange = "10.1.4.1-253"
args = "advanced_ip_scanner_console.exe /r:"+IPrange +" /f:"+ filename
print('Escaneando local')
subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)


outfile = open("scanip.csv", "w") 
for line in open("scanresult.txt", "r"): 
    if line.startswith('alive') and not line.startswith('alive |  |'):
        print(line)
        outfile.write(line.replace(" | ",";")) # write in new file
outfile.close() 

with open('scanip.csv') as file:
    #writer = csv.writer('inventariocsvsort.csv', delimiter=',')
    data = csv.reader(file, delimiter=';')
    #data = []
    data = sorted(data, key = lambda row: ipaddress.IPv4Address(row[4]))
    #print(data[1])
    #writer.writerows(data)
    for row in data:
        print(row)
        insertincsv(row[0],row[1],row[2],row[3],row[4])

print('Fin del scan')
