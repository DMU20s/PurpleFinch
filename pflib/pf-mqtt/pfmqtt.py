import base64
import paho.mqtt.publish as publish
import timeit


class Tx:
	"""MQTT transmitter class for PurpleFinch."""
	def __init__(self, topic, broker, key):
		self.topic = topic
		self.broker = broker
		self.key = key

	@staticmethod
	def pseudoencode(key, clear):
		enc = []
		for i in range(len(clear)):
			key_c = key[i % len(key)]
			enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
			enc.append(enc_c)
		return base64.urlsafe_b64encode("".join(enc).encode()).decode()

	def send(self, message):
		publish.single(self.topic, self.pseudoencode(self.key, message), hostname=self.broker)

	def send_unenc(self, message):
		publish.single(self.topic, message, hostname=self.broker)


