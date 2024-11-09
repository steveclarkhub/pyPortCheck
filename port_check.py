import socket  #standard lib

def port_check(hostname, portno):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        con = s.connect_ex((hostname, portno))
    # s.sendall(b"Hello, world")
    # data = s.recv(1024)
    return con 

# connect_ex throw a code on exception instead of the exception itself
# code = tcp socket error codes. 0 = success 

# print(con)

output = port_check("45.33.32.156",80)
print(output)
