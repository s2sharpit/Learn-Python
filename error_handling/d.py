is_connected: bool = False

def connect_to_internet():    
    if not is_connected:
        # raise Exception('No Internet!')
        raise ConnectionError('No Internet!')
    else:
        print('Connected to the Internet!')

try:
    connect_to_internet()
except ConnectionError:
    print('There is no connection!')
except Exception as e:
    print(e)