from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
import random

def new_map(num_elements, load_factor, prime=109345121):
    
    capacity = mf.next_prime(num_elements/load_factor)
    scale = random.randint(1, prime-1)
    shift = random.randint(0, prime-1)
    table = al.new_list()
    table["size"] = capacity
    current_factor = 0
    limit_factor = load_factor
    size = 0
    
    retorno = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": current_factor,
        "limit_factor": limit_factor,
        "size" : size
    }
    
    return retorno

def put(my_map, key, value):
    
    capacity = my_map['capacity']
    index = int(mf.hash_value(my_map, key))
    
    for i in range(capacity):
        pos = (index + i) % capacity
        entry = my_map['table'][pos]
        
        if entry is None:
            my_map['table'][pos] = me.new_map_entry(key, value)
            my_map['size'] += 1
            my_map['current_factor'] = my_map['size'] / capacity
            if my_map['current_factor'] > my_map['limit_factor']:
                mf.hash_value(my_map, key)
            return my_map
        elif me.get_key(entry) == key:
            me.set_value(entry, value)
            return my_map
    return my_map 