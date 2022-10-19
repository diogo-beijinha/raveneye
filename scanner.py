import getopt
import nmap
import sys


n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

ip_addr = None
port = None

# Get IP Address
for arg in sys.argv:
    if "--ip" in arg:
        ip_index = sys.argv.index(arg) + 1
        ip_addr = sys.argv[ip_index]
        print(ip_addr)

# Get Port
for arg in sys.argv:
    if "--port" in arg:
        port_index = sys.argv.index(arg) + 1
        port = sys.argv[port_index]
        print(port)


