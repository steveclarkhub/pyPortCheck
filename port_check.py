# std lib
import argparse 
import socket  
import csv

def port_check(servername, portno):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        con = s.connect_ex((servername, portno))
    return con 

# connect_ex throws tcp socket err code (int). 0 = success. !0 = fail. 
# Codes 100xx = MS Windows, xx = Nix, MacOS

parser = argparse.ArgumentParser(description="Process hostname and port.")
parser.add_argument('-s', '--servername', type=str, default='8.8.8.8', help='The server to connect to (default: 8.8.8.8)')
parser.add_argument('-p', '--port', type=int, default='443', help='The port number on target server (default: 443)')
parser.add_argument('-f', '--file', type=str, help='path to CSV. Format: arbitrary name, fqdn or ip, port')

args = parser.parse_args()
# test args: #1 print(type(args.hostname)) #2 print(args.hostname) 
# #3 print(type(args.port)) #4 print(args.port)

if args.file:
     print("file flag present")
     print(args.file,"is the path")
     with open (args.file, mode='r') as csv_import:
        csv_readobj = csv.DictReader(csv_import) # ordered dictionary
        line_ct = 0
        for row in csv_readobj:
            if line_ct == 0:
                print(f'Column Names are {", ".join(row)}')
                # w/o join, get a dict dump {'k':'v', 'k':'v', 'k':'v',}
                line_ct +=1
            else:
                targ,p = row["Tcp_Target"],int(row["Port"])
                result = (port_check(targ,p))
                # test vals print(port_check(targ,p)) & print(targ,p)
                if result == 0:
                    print(f'{row["Resource"]} ({row["Tcp_Target"]}) SUCCEEDS at port {row["Port"]}')
                else:
                    print(f'{row["Resource"]} ({row["Tcp_Target"]}) FAILS to respond at port {row["Port"]}')
                line_ct +=1
else:
    output = port_check(args.servername,args.port)
    if output == 0:
        print("return code: ", output, "success")
    else:
        print("return code: ", output, "failure")


     

