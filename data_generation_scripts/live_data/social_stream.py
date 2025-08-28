import asyncio
import random
import json
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

# PASTE YOUR CONNECTION STRING AND EVENT HUB NAME HERE
CONNECTION_STR = "Paste your connection string key""
EVENT_HUB_NAME = "social-mentions"

async def run():
    producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENT_HUB_NAME)
    async with producer:
        while True:
            event_data_batch = await producer.create_batch()
            sentiments = ["I love my new Urban Threads jacket!", "The shipping was so fast from Urban Threads.", "Urban Threads quality has gone down.", "Can anyone recommend Urban Threads jeans?"]
            event = {'author': f'user_{random.randint(100,999)}', 'message': random.choice(sentiments), 'timestamp': asyncio.get_event_loop().time()}
            event_data_batch.add(EventData(json.dumps(event)))

            await producer.send_batch(event_data_batch)
            print(f"Sent mention: {event}")
            await asyncio.sleep(5) # Send a message every 5 seconds


asyncio.run(run())
