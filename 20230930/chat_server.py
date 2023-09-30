import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

with socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) as sock: # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        sock.sendto(data, addr)
