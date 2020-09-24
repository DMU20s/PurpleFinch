import base64
#import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


class Tx:
	"""MQTT transmitter class for PurpleFinch."""
	def __init__(self, topic, broker, key, message):
		self.topic = topic
		self.broker = broker
		self.key = key
		self.message = message

	def encode(self, key, clear):
		enc = []
		for i in range(len(clear)):
			key_c = key[i % len(key)]
			enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
			enc.append(enc_c)
		return base64.urlsafe_b64encode("".join(enc).encode()).decode()

	def send(self, message):
		publish.single(self.topic, self.encode(self.key, self.message), hostname=self.broker)


print(Tx.__doc__)

transmitter = PfMqttTx("lolcake/1", "broker.hivemq.com", "keykeykey", "")
transmitter.send("keykey")
