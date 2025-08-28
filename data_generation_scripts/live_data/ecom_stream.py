import asyncio
import random
import json
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

# PASTE YOUR CONNECTION STRING AND EVENT HUB NAME HERE
CONNECTION_STR = "Endpoint=sb://urbanprojecteventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=j5uSbtKez07rrKeeJbll+UlYVaEk4EpGA+AEhJQ0FFg="
EVENT_HUB_NAME = "ecom-clicks"

async def run():
    producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENT_HUB_NAME)
    async with producer:
        while True:
            event_data_batch = await producer.create_batch()
            user_id = random.randint(1, 100)
            pages = ["home", "products", "cart", "checkout"]
            event = {'user_id': user_id, 'page_viewed': random.choice(pages), 'timestamp': asyncio.get_event_loop().time()}
            event_data_batch.add(EventData(json.dumps(event)))

            await producer.send_batch(event_data_batch)
            print(f"Sent click: {event}")
            await asyncio.sleep(2) # Send a message every 2 seconds

asyncio.run(run())