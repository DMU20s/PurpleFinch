from pfmqtt import Tx
from random import randrange
from time import sleep
import json

t = Tx("pfgs/rnd", "mqtt.eclipse.org", "lol")
# t.send("test")
# t.send_unenc("test")


while True:
	sleep(1)
	data = {
		"values": {
			"val0": randrange(1, 100),
			"val1": randrange(1, 100),
			"val2": randrange(1, 100),
			"val3": randrange(1, 100),
			"val4": randrange(1, 100),
			"val5": randrange(1, 100),
			"val6": randrange(1, 100),
			"val7": randrange(1, 100),
			"val8": randrange(1, 100),
			"val9": randrange(1, 100)
		}
	}
	t.send_unenc(json.dumps(data))
