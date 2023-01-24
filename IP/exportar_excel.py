import pandas as pd
import ping
import socket

def guardar(num):
    connected_ips = ping.IP(num)
    connected_hostnames = ping.host_name(num)

    print("IPs conectadas:")
    for ip in connected_ips:
        print(ip)

    print("hostnames conectadas:")
    for hostname in connected_hostnames:
        print(hostname)

    common_connections = {}
    for ip in connected_ips:
        for hostname in connected_hostnames:
            try:
                host_ip = socket.gethostbyname(hostname)
                if host_ip in connected_ips:
                    common_connections[hostname] = host_ip
            except:
                pass
    df = pd.DataFrame.from_dict(common_connections, orient='index', columns=['IP'])
    df['hostname'] = df.index
    df.to_excel("resultados.xlsx", columns = ['hostname','IP'], index=False)
    return df

