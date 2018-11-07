import obd
import time

connection = obd.Async()

rpm = 0
speed = 0

# a callback that prints every new value to the console
def new_rpm(r):
	global rpm
	rpm = int(r.value.magnitude)

def new_speed(s):
	global speed
	speed = int(s.value.magnitude*.621371)

connection.watch(obd.commands.RPM, callback=new_rpm)
connection.watch(obd.commands.SPEED, callback=new_speed)


connection.start()

# the callback will now be fired upon receipt of new values
while True:
	print("RPM: %s\tSPEED: %s" %(str(rpm),str(speed)))
	time.sleep(0.01)
# time.sleep(5)
connection.stop()
