# producer.py (Sends Messages to ActiveMQ)
import stomp
import time

BROKER_URL = 'localhost'
BROKER_PORT = 61613
QUEUE_NAME = '/queue/demo'

class Producer:
    def __init__(self):
        self.conn = stomp.Connection([(BROKER_URL, BROKER_PORT)])
        self.conn.connect(wait=True)
    
    def send_message(self, message):
        print(f"[Producer] Sending: {message}")
        self.conn.send(destination=QUEUE_NAME, body=message)
    
    def close(self):
        self.conn.disconnect()

if __name__ == "__main__":
    producer = Producer()
    for i in range(5):
        producer.send_message(f"Message {i + 1}")
        time.sleep(1)
    producer.close()
    print("[Producer] Messages Sent")