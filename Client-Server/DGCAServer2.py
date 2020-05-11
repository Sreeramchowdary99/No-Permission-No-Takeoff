import socket               

s = socket.socket()        
host = '192.168.137.134'# ip of raspberry pi 
port = 12346       
s.connect((host, port))
# cmd = '(0,0,0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,-34.364114, 149.166022, 30)'
n=int(input('choose between 1=RTL & 2=CMD: '))
if n==1:
    cmd = 'RTL'

if n==2:
    cmd = 'LAND'

    
#cmd = 'LAND'
s.sendall(cmd.encode())
s.close()
