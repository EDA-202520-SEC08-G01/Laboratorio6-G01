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
    for i in range(table["size"]):
        key = "key"
        value = "value"
        entrada = me.new_map_entry(key, value)
        al.add_first(table, entrada)
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

def is_available(table, pos):
   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):
   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail


def find_slot(my_map, key, hash_value):
    capacity = my_map['capacity']
    index = int(mf.hash_value(my_map, key)) if hash_value is None else hash_value
    
    for i in range(capacity):
        pos = (index + i) % capacity
        entry = my_map['table'][pos]
        if entry is None:
            return (False, pos)
        if me.get_key(entry) == key:
            return (True, pos)
    return (False, -1)

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

def size(my_map):
    return my_map["size"]

def rehash(my_map):
    """
    Redimensiona la tabla de hash cuando se supera el factor de carga.
    """
    old_table = my_map['table']
    old_capacity = my_map['capacity']
    new_capacity = mf.next_prime(2 * old_capacity)
    new_prime = mf.next_prime(new_capacity + 1)  
    my_map['prime'] = new_prime
    my_map['scale'] = random.randint(1, new_prime - 1)
    my_map['shift'] = random.randint(0, new_prime - 1)
    
    for entry in old_table:
        if entry is not None:
            put(my_map, me.get_key(entry), me.get_value(entry))

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
                rehash(my_map)
            return my_map
        elif me.get_key(entry) == key:
            me.set_value(entry, value)
            return my_map
    return my_map