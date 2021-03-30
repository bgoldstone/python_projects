import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('muhlenberg.edu', 443))
cmd = 'GET https://muhlenberg.edu/ HTTP/1.1\n\n'.encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
my_socket.close()