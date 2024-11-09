# pyPortCheck

mvp: scan ip and port to find if port is open

- mvp+ take fqdns as well as IPs ("scanme.nmap.org", 22)
- mvp+ friendlier output than connect_ex socket codes
- mvp+ import csv of ips & ports
- mvp+ calculate time taken to respond

#### test output: port_check("8.8.8.8",53) = 0 
0 = success

10061 = (connection refused).

list of tcp socket codes used by connect_ex
https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/errno.h 
