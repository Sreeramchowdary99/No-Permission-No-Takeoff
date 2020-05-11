from firebase import firebase
from dronekit import connect, VehicleMode
import time
import dronekit_sitl

firebase = firebase.FirebaseApplication('https://npnt-acf2d.firebaseio.com/',None)


connection_string = "/dev/ttyACM0"
baud_rate = 115200

from datetime import datetime
now=datetime.now()

#--- Now that we have started the SITL and we have the connection string (basically the ip and udp port)...

print(">>>> Connecting with the UAV <<<")
vehicle = connect(connection_string,baud=baud_rate, wait_ready=True)     #- wait_ready flag hold the program untill all the parameters are been read (=, not .)

#-- Read information from the autopilot:
#- Version and attributes
vehicle.wait_ready('autopilot_version')

while True:
    latitude = str(vehicle.location.global_relative_frame.lat)
    longitude = str(vehicle.location.global_relative_frame.lon)
    altitude = str(vehicle.location.global_relative_frame.alt)
    time = str(now)
    result = firebase.post('/users/',{'latitude':latitude,'longitude':longitude})
    #result = firebase.post('/users',{"type":"feature",
      #                     "geometry":{
     #                          "type":"point",
     #                          "coordinates":[latitude,longitude]}})
    #result1 = firebase.post('/time/', time)
    #result2 = firebase.post('/velocity/', vehicle.velocity)

    print(result)
    #print(result1)
    #print(result2)
