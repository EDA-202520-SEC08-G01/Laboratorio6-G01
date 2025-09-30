from DataStructures.List import list_node as ns


def new_list():
    return {"first": None, "last": None, "size": 0}


def is_empty(lst):
    return lst["size"] == 0


def size(lst):
    return lst["size"]


def add_first(lst, element):
    n = ns.new_single_node(element)
    if is_empty(lst):
        lst["last"] = n
    n["next"] = lst["first"]
    lst["first"] = n
    lst["size"] += 1
    return lst


def add_last(lst, element):
    n = ns.new_single_node(element)
    if is_empty(lst):
        lst["first"] = n
        lst["last"] = n
    else:
        lst["last"]["next"] = n
        lst["last"] = n
    lst["size"] += 1
    return lst


def first_element(lst):
    if is_empty(lst):
        raise Exception("Lista vacía")
    return lst["first"]["info"]


def last_element(lst):
    if is_empty(lst):
        raise Exception("Lista vacía")
    return lst["last"]["info"]


def get_element(lst, pos):
    if pos < 0 or pos >= lst["size"]:
        raise Exception("IndexError: fuera de rango")
    n = lst["first"]
    for i in range(pos):
        n = n["next"]
    return n["info"]


def remove_first(lst):
    if is_empty(lst):
        raise Exception("Lista vacía")
    n = lst["first"]
    lst["first"] = n["next"]
    if lst["first"] is None:
        lst["last"] = None
    lst["size"] -= 1
    return n["info"]


def remove_last(lst):
    if is_empty(lst):
        raise Exception("Lista vacía")
    if lst["first"] == lst["last"]:
        info = lst["last"]["info"]
        lst["first"] = None
        lst["last"] = None
        lst["size"] = 0
        return info
    n = lst["first"]
    while n["next"] != lst["last"]:
        n = n["next"]
    info = lst["last"]["info"]
    n["next"] = None
    lst["last"] = n
    lst["size"] -= 1
    return info


def delete_element(lst, pos):
    if pos < 0 or pos >= lst["size"]:
        raise Exception("IndexError: fuera de rango")
    if pos == 0:
        remove_first(lst)
        return lst

    prev = lst["first"]
    for i in range(pos - 1):
        prev = prev["next"]

    target = prev["next"]
    prev["next"] = target["next"]

    if target is lst["last"]:
        lst["last"] = prev

    lst["size"] -= 1
    return lst


def insert_element(lst, element, pos):
    if pos < 0 or pos > lst["size"]:
        raise Exception("IndexError: fuera de rango")
    if pos == 0:
        return add_first(lst, element)
    if pos == lst["size"]:
        return add_last(lst, element)
    node = ns.new_single_node(element)
    prev = lst["first"]
    for i in range(pos - 1):
        prev = prev["next"]
    node["next"] = prev["next"]
    prev["next"] = node
    lst["size"] += 1
    return lst


def is_present(lst, element, cmp_function):
    n = lst["first"]
    index = 0
    while n is not None:
        if cmp_function(element, n["info"]) == 0:
            return index
        n = n["next"]
        index += 1
    return -1


def change_info(lst, pos, new_info):
    if pos < 0 or pos >= lst["size"]:
        raise Exception("IndexError: fuera de rango")
    n = lst["first"]
    for i in range(pos):
        n = n["next"]
    n["info"] = new_info
    return lst


def exchange(list, pos1, pos2):
        if not(0 <= pos1 <= size(list) and 0 <= pos2 <= size(list)):
            raise Exception('IndexError: list index out of range') # esto esta en la documentacion de DISC - Data Structures btw x3
        if is_empty(list):
            raise Exception("Error: Indexación fuera de rango -> No se puede borrar elementos si no existe ninguno que borrar.")
        enc_p1_prev = list["first"]
        enc_p2_prev = list["first"]
        for i in range(pos1-1):
            enc_p1_prev = enc_p1_prev["next"]
        for i in range(pos2-1):
            enc_p2_prev = enc_p2_prev["next"]
        
        p1 = enc_p1_prev["next"]
        p2 = enc_p2_prev["next"]
        
        if p1["next"]==None:
            p1["next"] = p2["next"]
            p2["next"] = None
        elif p2["next"]==None:
            p2["next"] = p1["next"]
            p1["next"] = None
        
        enc_p2_prev["next"] = p1
        enc_p1_prev["next"] = p2
        return list

def sub_list(list, pos, num_elements):
    if not(0 <= pos <= size(list)):
            raise Exception('IndexError: list index out of range') # esto esta en la documentacion de DISC - Data Structures btw x3
    if is_empty(list):
            raise Exception("Error: Indexación fuera de rango -> No se puede borrar elementos si no existe ninguno que borrar.")
    sub_list = new_list()
    ini_lista = list["first"]
    for i in range(pos):
        ini_lista = ini_lista["next"]
    
    sub_list["first"] = ini_lista
    sub_list["last"] = list["last"]
    sub_list["size"] = num_elements
    return sub_list
    
def default_sort_criteria(element_1, element_2):
   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def insertion_sort(my_list, sort_crit):
    n = size(my_list)
    for i in range(1, n):
        key = get_element(my_list, i)
        j = i - 1
        while j >= 0 and not sort_crit(get_element(my_list, j), key):
            change_info(my_list, j + 1, get_element(my_list, j))
            j -= 1
        change_info(my_list, j + 1, key)

    return my_list

def shell_sort(list, sort_crit):
    n = size(list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = get_element(list, i)
            j = i
            while j >= gap and not sort_crit(get_element(list, j - gap), temp):
                change_info(list, j, get_element(list, j - gap))
                j -= gap
            change_info(list, j, temp)
        gap //= 2

    return list

def selection_sort(my_list,sort_crit):
    s = size(my_list)
    for i in range(s - 1):
        mejor = i
        for j in range(i + 1, s):
            if sort_crit(get_element(my_list, j),get_element(my_list, mejor)):
                mejor = j
        if mejor != i:
            change_info(my_list, i, mejor)
        
    return my_list 

def merge_sort(list, sort_crit):
    if list["size"] <= 1:
        return list

    mid = list["size"] // 2
    left = sub_list(list, 0, mid)
    right = sub_list(list, mid, list["size"] - mid)

    left_sorted = merge_sort(left, sort_crit)
    right_sorted = merge_sort(right, sort_crit)

    return merge(left_sorted, right_sorted, sort_crit)


def merge(left, right, sort_crit):
    merged = new_list()
    i = j = 0

    while i < left["size"] and j < right["size"]:
        if sort_crit(get_element(left, i), get_element(right, j)):
            add_last(merged, get_element(left, i))
            i += 1
        else:
            add_last(merged, get_element(right, j))
            j += 1

    while i < left["size"]:
        add_last(merged, get_element(left, i))
        i += 1

    while j < right["size"]:
        add_last(merged, get_element(right, j))
        j += 1

    return merged

def concatenar(list1, list2):
    # Concatena dos listas y retorna la nueva lista.
    retorno = new_list()
    for element in list1:
        add_last(retorno, element) # copia todos los elementos de list1
    for element in list2:
        add_last(retorno, element) # dsps copia todos los elementos de list2

    return retorno

def quick_sort(list, sort_crit):
    
    n = size(list)
    if n <= 1:
        return list
    
    pivote = get_element(list, 0) # -> El primer elemento es el pivote del quick sort

    # 3 particiones: menores, mayores, iguales al pivote
    antes_pivote = new_list()
    dsps_pivote = new_list()
    iguales = new_list()

    # En este ciclo se llenan las 3 particiones en dependencia de su relación con el pivote
    for i in range(n):
        curr = get_element(list, i)
        if curr == pivote:
            add_last(iguales, curr)
        elif sort_crit(curr, pivote):
            add_last(antes_pivote, curr)
        else:
            add_last(dsps_pivote, curr)


    # Se ordenan recursivamente las particiones de antes y después. Como iguales = pivote, iguales ya está ordenada (todos son el mismo elemento/número)
    antes_pivote_sort = quick_sort(antes_pivote, sort_crit)
    dsps_pivote_sort = quick_sort(dsps_pivote, sort_crit)

    # Se concatenan las 3 particiones y se retorna la lista ordenada: antes -> iguales -> después
    return concatenar(concatenar(antes_pivote_sort, iguales), dsps_pivote_sort)