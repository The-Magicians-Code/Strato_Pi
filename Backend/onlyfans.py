# Exclusive porn for fans only
def tempstat():
	with open('/sys/class/stratopifan/sys_temp/temp', 'r') as status:
		temperature = round(int(status.read().strip())/100.0, 2)
	print(f"Temperature: {temperature}°C")
