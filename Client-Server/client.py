import socket
from dronekit import connect, VehicleMode
import time
import dronekit_sitl
s = socket.socket()
host = '192.168.137.134' #ip of raspberry pi
port = 12346
s.bind((host, port))
connection_string = "/dev/ttyACM0"
baud_rate = 115200
#vehicle = connect(connection_string,baud=baud_rate, wait_ready=True)
vehicle = connect('tcp:192.168.137.102:5763',wait_ready=True)
s.listen(5)
print ('listening for command')
while True:
   c, addr = s.accept()
   print ('Got connection from',addr)
   cmd = str(c.recv(1024))
   print (cmd)
   vehicle.mode = cmd
   c.close()
