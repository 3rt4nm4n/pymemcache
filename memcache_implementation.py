from pymemcache.client.base import Client

def cache_input(user_id, value_to_cache):
    client = Client(('localhost', 11211))
    client.set(user_id, value_to_cache)
    client.close()

def is_input_cached(user_id):
    client = Client(('localhost', 11211))
    cached_value = client.get(user_id)
    if cached_value is not None:
        client.close()  
        return True
    else:
        client.close()  
        return False

for i in range(0,3): # Run the code block below 3 times to see if caching works
    user_id = "12345678" 
    if is_input_cached(user_id):
        print(f'Value for input "{user_id}" is cached.')
    else:
        value_to_cache = 'value_for_user_id'  
        cache_input(user_id, value_to_cache)
        print(f'Value for input "{user_id}" is not cached, but it is cached now.')

Client(('localhost', 11211)).flush_all()
Client(('localhost', 11211)).close()