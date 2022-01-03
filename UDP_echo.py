import socket, time

UDP_IP = "192.168.0.11"                     # Static IP address of the machine on which this script is running
UDP_PORT = 5005                             # Assuming that both the devices communicate over the same port 

DEST_IP = "192.168.0.10"                    # IP address of the Nucleo 

sock = socket.socket(socket.AF_INET,        # Internet
                     socket.SOCK_DGRAM)     # UDP
sock.bind((UDP_IP, UDP_PORT))
message = 1

while True:
    sock.sendto(str(message), (DEST_IP, UDP_PORT))
    print("Sent {} from host".format(message))
    data, addr = sock.recvfrom(1024)        # max buffer size is set to 1024 bytes
    print("Received {} from address {}".format(data, addr[0]))
    message += 1
    time.sleep(2)                           # sleep for 2 seconds
