import nmap
from dir_scan import directory_scanning

dir_scan = False

def port_scanning(ip_addr, ports):
    nm = nmap.PortScanner()
    nm.scan(ip_addr, ports)
    nm.command_line()
    nm.scaninfo()
    nm.all_hosts()
    nm[ip_addr].hostname()
    nm[ip_addr].state()
    nm[ip_addr].all_protocols()
    nm[ip_addr]['tcp'].keys()
    nm[ip_addr].has_tcp(22)
    nm[ip_addr].has_tcp(23)
    try:
        nm[ip_addr]['tcp'][22]
        nm[ip_addr].tcp(22)
        nm[ip_addr]['tcp'][22]['state']
    except:
        pass

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            #lport.sort()
            for port in lport:
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                if proto == "80" or proto == "8080":
                    dir_scan = True
    
    if dir_scan == True:
        directory_scanning(ip_addr)
