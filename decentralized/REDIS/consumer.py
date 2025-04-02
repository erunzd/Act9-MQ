import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

stream_name = "mystream"
last_id = "0"  # Start from the beginning

print("Consumer started. Listening for messages...")

while True:
    messages = r.xread({stream_name: last_id}, count=1, block=0)
    for stream, msg_list in messages:
        for msg_id, msg_data in msg_list:
            print(f"Received: {msg_data}")
            last_id = msg_id  # Update last ID to continue reading
