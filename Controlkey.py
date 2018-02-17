
#Juan Pablo Elizarraraz Oliva
#A01632031
#
#
#
#
#****************************************************************************
# Imported functions, classes and methods
#****************************************************************************
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

#****************************************************************************
#   Method Name     : set_velocity_body
#
#
#****************************************************************************

def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

#****************************************************************************
#For arming the drone and telling you when it is done
#
#****************************************************************************
def arm_and_takeoff(TargetAltitude):
    print ("Executing Takeoff")

    while not drone.is_armable:
        print ("Vehicle is not armable, waiting....")
        time.sleep(1)

    print("Ready to arm")
    drone.mode = VehicleMode("GUIDED")
    drone.armed = True

    while not drone.armed:
        print("waiting for arming...")     
        time.sleep(1)

    print ("Ready for takeoff, taking off...")
    drone.simple_takeoff(TargetAltitude)

    while True:
        Altitude = drone.location.global_relative_frame.alt 
        print("Altitude: ", Altitude)
        time.sleep(1)

        if Altitude >=TargetAltitude * 0.95:
            print("Altitude reached")
            break
                



#### your code here #####

#****************************************************************************
# The following commands are for the drone to know what to do when an arrow key is pressed
#****************************************************************************
def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r': 
            drone.mode = VehicleMode("RTL")
            ### Add your code for what you want to happen when you press r #####
            
    else: #-- non standard keys
        if event.keysym == 'Up': set_velocity_body(drone, -5,0,0)
            ### add your code for what should happen when pressing the up arrow ###
        elif event.keysym == 'Down': set_velocity_body(drone, 5,0,0)
            ### add your code for what should happen when pressing the down arrow ###
        elif event.keysym == 'Left': set_velocity_body(drone, 0,5,0)
            ### add your code for what should happen when pressing the Left arrow ###
        elif event.keysym == 'Right': set_velocity_body(drone, 0,-5,0)
            ### add your code for what should happen when pressing the Right arrow ###

#****************************************************************************
#   For connecting and for the altitude
#
#****************************************************************************

### add your code to connect to the drone here ###
drone = connect('127.0.0.1:14551', wait_ready=True)
#Take off to 10 m altitude
arm_and_takeoff(10)
 
# Read the keyboard with tkinter
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()
drone.close()