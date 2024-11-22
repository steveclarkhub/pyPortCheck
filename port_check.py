import argparse 
import socket  #standard lib

def port_check(hostname, portno):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        con = s.connect_ex((hostname, portno))
    return con 

# connect_ex throws code (int) on exception instead of the exception
# code = tcp socket error codes. 0 = success. !0 = fail. 
# codes 100xx = windows, xx = *nix

# print(con)

parser = argparse.ArgumentParser(description="Process hostname and port.")
parser.add_argument('--hostname', type=str, default='8.8.8.8', help='The hostname to connect to (default: 8.8.8.8)')
parser.add_argument('--port', type=int, default='443', help='The port number on target server (default: 443)')
parser.add_argument('--file', type=str, help='path to the CSV file with a list of targets and ports')

args = parser.parse_args()
## test args
#print(type(args.hostname))
#print(args.hostname)
#print(type(args.port))
#print(args.port)

if args.file:
     print("file flag present")
     print(args.file,"is the path")
else:
    output = port_check(args.hostname,args.port)

    if output == 0:
        print("return code: ", output, "success")
    else:
        print("return code: ", output, "failure")


     

