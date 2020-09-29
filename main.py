from pflib.pfmqtt import Tx

if __name__ == '__main__':
    t = Tx("lolcake/1", "broker.hivemq.com", "keykeykey", "")
    t.send("vacuums")
