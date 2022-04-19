import socket
import os
from ip import IP

# host to listen on
HOST = '192.168.1.15'

def main():
# create raw socket, bin to public interface
    print( "create raw socket, bin to public interface" )
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))

# include the IP header in the capture
    print( "include the IP header in the captureinclude the IP header in the capture" )
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# read one packet
    print( "read one packet" )
    ip = IP( sniffer.recvfrom(65565)[0] )
    print( ip._fields_ )
    #print(sniffer.recvfrom(65565))

# if we're on Windows, turn off promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()
