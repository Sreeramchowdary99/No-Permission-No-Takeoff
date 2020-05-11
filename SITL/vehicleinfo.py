import time
import dronekit_sitl

from dronekit import connect, VehicleMode,LocationGlobal,LocationGlobalRelative
def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """
    print ('Basic pre-arm checks')
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print (' Waiting for vehicle to initialise...')
        time.sleep(1)
    print ('Arming motors')
    # Copter should arm in GUIDED mode
    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed   = True
    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print (' Waiting for arming...')
        time.sleep(1)
    print ('Taking off!')
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print (' Altitude: ', vehicle.location.global_relative_frame.alt)
        #Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
            print ('Reached target altitude')
            break
        time.sleep(1)
print ('Start simulator (SITL)')
#sitl = dronekit_sitl.start_default()
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)
#vehicle.airspeed = 5 #m/s
#vehicle.groundspeed = 10 #m/s
arm_and_takeoff(100)
#a_location = LocationGlobalRelative(-34.364114, -149.166022,30)
a_location = LocationGlobalRelative(17.4325600, 78.3786881,30)
vehicle.simple_goto(a_location,groundspeed=10)
print ('Groundspeed: %s' % vehicle.groundspeed)
