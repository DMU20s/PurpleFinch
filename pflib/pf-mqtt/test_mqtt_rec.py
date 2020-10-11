import paho.mqtt.client as mqtt
import json

class MyMQTTClass(mqtt.Client):

	def on_message(self, mqttc, obj, msg):
		print(msg.payload.decode("UTF-8"))
		my_json = msg.payload.decode('utf8').replace("'", '"')
		data = json.loads(my_json)
		s = json.dumps(data, indent=4, sort_keys=True)
		print(s)

	def run(self):
		self.connect("mqtt.eclipse.org", 1883, 60)
		self.subscribe("pfgs/rnd", 0)

		rc = 0
		while rc == 0:
			rc = self.loop()
		return rc


mqttc = MyMQTTClass()
rc = mqttc.run()
