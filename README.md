# pyPortCheck

Utility that scans host/fqdn/ip + tcp port to find if port accepts connections

- mvp+ import csv of ips & ports
- mvp+ calculate time taken to respond

#### test output: port_check("8.8.8.8",53) = 0 
tcp socket codes:
61 / 10061 = connection refused, Linux, Windows

list of tcp socket codes used by connect_ex
https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/errno.h 
