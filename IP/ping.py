import ping3
import pandas as pd

10
def IP(num):
    connected_ips = []
    if len(num) == 4:
        for i in range(100,201):
            ip = "10." + num[:2] + "." + num[2:] + "." + str(i)
            ip_response = ping3.ping(ip, timeout=0.2)
            if ip_response:
                connected_ips.append(ip)
    elif len(num) == 3:
            for i in range(100,201):
                ip = "10." + num[0] + "." + num[1:] + "." + str(i)
                ip_response = ping3.ping(ip, timeout=0.2)
                if ip_response:
                    connected_ips.append(ip)
    return connected_ips


def host_name(num):
    connected_hostnames = [] 
    if len(num) == 3:
        num = "00" + num
    elif len(num) == 4:
        num = "0" + num

    for i in range(1,7):
        tpv = '0' + str(i)
        hostname = "POS" + num + tpv + ".alseaeur.net"
        hostname_response = ping3.ping(hostname, timeout=0.2)
        if hostname_response:
            connected_hostnames.append(hostname)
    
    for i in range(50,61):
        tpv = str(i)
        hostname = "POS" + num + tpv + ".alseaeur.net"
        hostname_response = ping3.ping(hostname, timeout=0.2)
        if hostname_response:
            connected_hostnames.append(hostname)
        
    for i in range(90,96):
        tpv = str(i)
        hostname = "KDS" + num + tpv + ".alseaeur.net"
        hostname_response = ping3.ping(hostname, timeout=0.2)
        if hostname_response:
            connected_hostnames.append(hostname)
    return connected_hostnames
    



def host_ip(num):
    connected_hostnames = [] 
    if len(num) == 3:
        num = "00" + num
    elif len(num) == 4:
        num = "0" + num

    for i in range(1,7):
        tpv = '0' + str(i)
        hostname = "POS" + num + tpv + ".alseaeur.net"
        hostname_response = ping3.ping(hostname, timeout=0.2)
        if hostname_response:
            connected_hostnames.append(hostname)
    
    for i in range(50,61):
        tpv = str(i)
        hostname = "POS" + num + tpv + ".alseaeur.net"
        hostname_response = ping3.ping(hostname, timeout=0.2)
        if hostname_response:
            connected_hostnames.append(hostname)
        
    for i in range(90,96):
        tpv = str(i)
        hostname = "KDS" + num + tpv + ".alseaeur.net"
        hostname_response = ping3.ping(hostname, timeout=0.2)
        if hostname_response:
            connected_hostnames.append(hostname)        

    return connected_hostnames



