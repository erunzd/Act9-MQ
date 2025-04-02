# consumer.py (Receives Messages from ActiveMQ)
import stomp

BROKER_URL = 'localhost'
BROKER_PORT = 61613
QUEUE_NAME = '/queue/demo'

class Consumer(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        print(f"[Consumer] Received: {frame.body}")

# Connect to ActiveMQ
conn = stomp.Connection([(BROKER_URL, BROKER_PORT)])
conn.set_listener('', Consumer(conn))
conn.connect(wait=True)
conn.subscribe(destination=QUEUE_NAME, id=1, ack='auto')

print("[Consumer] Listening for messages. Press Ctrl+C to stop.")
try:
    while True:
        pass  # Keeps the script running to listen for messages
except KeyboardInterrupt:
    print("\n[Consumer] Stopped")
    conn.disconnect()