import nmap
from dir_scan import directory_scanning


def port_scanning(ip_addr, ports):
    scan_dirs = False
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
                    scan_dirs = True
    
                if proto == "21":
                    pass
                    # TEST FTP ANONYMOUS CONNECTION HERE
                if proto == "445": #SMB sometimes uses port 139(implement later)
                    pass
                    # TEST SMB ANONYMOUS CONNECTION HERE

    if scan_dirs == True:
        dir_option = input("HTTP port open! Would you like to enumerate directories? (Y/N)")
        if dir_option == "Y" or dir_option == "y":
            directory_scanning(ip_addr)
