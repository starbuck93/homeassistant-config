#WIP
import time
import math
import sys

def updateState(previous,current,running):
	settings = {"device_class": "cold",  "friendly_name": "Is the AC Running"}
	if previous.state != current.state and math.fabs(float(previous.state)-float(current.state)) > .2: #if the absolute value delta is between 0 and 0.2 then we don't want to update the state to prevent false positives
		if previous.state > current.state: #air temp is falling
			print("::",current.state,"AC changed to ON")
			remote.set_state(api, 'binary_sensor.ac_boolean', new_state=True, attributes=settings) #call API to update the state of the sensor
		else : #air temp is rising,
			print("::",current.state,"AC changed to OFF")
			remote.set_state(api, 'binary_sensor.ac_boolean', new_state=False, attributes=settings) #call API to update the state of the sensor
	else:
		print(":: Delta < 0.2 ...",previous.state,current.state)


#setup
cold_ac_air_previous = hass.get('sensor.cold_ac_air') #get an initial reading
print(cold_ac_air_previous.state)
try:
	running = remote.get_state(api, 'binary_sensor.ac_boolean') #again, get an initial reading
except Exception:
	running = {"state": False} #assume it's off for the first run
try:
	print(":: Running?", running.state) #print it out
except Exception:
	pass
print(":: Initial reading:",cold_ac_air_previous.state)
print(":: Waiting for change...")


if len(sys.argv) > 1: #check for user input, and if so, call the function for the first run
	print(":: Got user input for previous:",sys.argv[1])
	cold_ac_air = remote.get_state(api, 'sensor.cold_ac_air') #because it's easier to just call the API again for this variable
	cold_ac_air_previous.state = sys.argv[1] #grab user input and name it something relevant
	updateState(cold_ac_air_previous,cold_ac_air,running.state) #call deciding funciton to update AC state
	cold_ac_air_previous = cold_ac_air #update that variable!

time.sleep(30) #wait 30 seconds to run the loop after gathering the first data point or updating based on user input


while True: #loop forever
	try: #https://stackoverflow.com/questions/730764/how-to-properly-ignore-exceptions
		try:
			running = remote.get_state(api, 'binary_sensor.ac_boolean') #again, get a new reading
		except Exception:
			pass #the variable exists so if it gets an update then great and if not we'll recycle data
		cold_ac_air = remote.get_state(api, 'sensor.cold_ac_air') #get that data!
		updateState(cold_ac_air_previous,cold_ac_air,running.state) #call deciding funciton to update AC state
		cold_ac_air_previous = cold_ac_air #update that variable!
		time.sleep(30) #wait 30 seconds and loop
	except Exception:
		time.sleep(30)
