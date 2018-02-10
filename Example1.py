from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#Defining the altitude
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


#Vehicle Connection
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)

drone.airspeed = 10 
#WavePoints, the points to where the drone will fly
print("On my way to point 1 ...")
Punto_01 = LocationGlobalRelative (20.736864, -103.456317, 20)
drone.simple_goto(Punto_01)
time.sleep (20)
print("On my way to point 2 ...")
Punto_02 = LocationGlobalRelative (20.737674, -103.456572, 20)
drone.simple_goto(Punto_02)
time.sleep (20)
print("On my way to point 3 ...")
Punto_03 = LocationGlobalRelative (20.736992, -103.457159, 20)
drone.simple_goto(Punto_03)
time.sleep (20)
print("Now back home")
drone.mode = VehicleMode("RTL")
time.sleep (20)

#The level of the battery
print("The battery voltage is:")
print (drone.battery.voltage) 

#For landing the drone
def LandDrone():
	print ("Landing")
	drone.mode = VehicleMode ("LAND")
	while True:
		Altitude = drone.location.global_relative_frame.alt 
		print("Altitude: ", Altitude)
			

		if Altitude <= 0:
			print("Landed")
			break

		time.sleep (10)

arm_and_takeoff(20)
#LandDrone()(We have RTL)