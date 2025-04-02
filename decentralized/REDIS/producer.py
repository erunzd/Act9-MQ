import redis
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

stream_name = "mystream"

for i in range(5):
    message = {"event": "user_signup", "user_id": str(i)}
    r.xadd(stream_name, message)
    print(f"Published: {message}")
    time.sleep(2)  # Simulating event intervals
