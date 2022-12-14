import getopt
import sys
from port_scan import port_scanning

def get_params():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if "-h" in opts:
        print("Usage: python raveneye.py -i <ip_address> -p <port>")
    else:
        if "-i" in opts:
            ip_loc = opts.index("-i")
            ip_addr = str(args[ip_loc])
        else:
            "No IP Address inserted! Scanning all hosts.."
            ip_addr = "all"
        
        if "-p" in opts:
            port_loc = opts.index("-p")
            ports = str(args[port_loc])
        else:
            ports = "1-443"
            print("No Port inserted! Scanning all ports..")
        
        port_scanning(ip_addr, ports)

get_params()