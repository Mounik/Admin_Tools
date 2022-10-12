import socket

for ping in range(1,254):
    address = "192.168.1." + str(ping)
    socket.setdefaulttimeout(1)
    
    try:
        hostname, alias, addresslist = socket.gethostbyaddr(address)

    except socket.herror:
        hostname = None
        alias = None
        addresslist = address

    print(addresslist, '=>', hostname)