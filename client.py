import socket

host = socket.gethostname()
host = '192.168.43.124' #Host ip
port = 1234             # The same port as used by the server


while True:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((host, port))
   #receive data
   data = s.recv(1024)
   print(data.decode('utf-8'))

