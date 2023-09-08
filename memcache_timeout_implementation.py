from pymemcache.client.base import Client


client = Client(('localhost', 11211))


key = 'my_key_with_timeout'
value = 'my_value_with_timeout'
timeout = 60  
client.set(key, value, expire=timeout)


cached_value = client.get(key)
if cached_value is not None:
    print(f'Retrieved value within timeout: {cached_value.decode("utf-8")}')
else:
    print(f'Key "{key}" has expired or does not exist.')

# Sleep for more than the timeout duration soo that the data will be removed from cache
import time
time.sleep(timeout + 1)

# Try to retrieve the value again 
cached_value = client.get(key)
if cached_value is not None:
    print(f'Retrieved value after timeout: {cached_value.decode("utf-8")}')
else:
    print(f'Key "{key}" has expired or does not exist.')

# Close the connection
client.close()
