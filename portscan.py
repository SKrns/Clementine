from socket import *
from sys import argv

def first():
    for port in range(30,200):
        try:
            s= socket.socket()
            print("[+] Attempting to connect : "+str(port))
            s.connect(('163.44.165.68', port))
            banner = s.recv(1024)
            if banner:
                print("[+] Port "+str(port)+"open : "+str(banner))
            elif banner==b'':
                print("[+] Port "+str(port)+"open : no.")
            s.close()
        except: pass


if(len(argv)<3):
    print("Usage : %s [TARGET] [PORT]" % argv[0])
    print("Usage : %s [TARGET] [START_PORT] [END_PORT]" % argv[0])
    exit()

def check_port(target,start,end):

    for i in range(start,end+1):
        s=socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.1)

        try:
            s.connect((target,i))
            print("[+][+][+] %d port is using now" % i)
        except:
            print("[+] %d port is open" % i)

        s.close()
    print("done")
    exit()

if(len(argv)==3):
    check_port(argv[1],int(argv[2]),int(argv[2]))
else:
    check_port(argv[1],int(argv[2]),int(argv[3]))
