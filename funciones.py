import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta funciÃ³n devuelve la lista de palabras que empiezan por una letra que alfabÃ©ticamente estÃ¡ antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    resultado=[] # esta es la forma correcta, aqui se guarda siempre
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                # resultado = [] se inicializa cada iteración del bucle, por lo que solo
                # devolverá el último analizado
                resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta funciÃ³n inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    # Para actualizar un dict hay que utilizar dict.update({key:object}), no sirve hacerlo con []
    # como si fuera un array
    clients_list.update({
        nif: {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    })

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un nÃºmero de repeticiones, esta funciÃ³n selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        # Mismo error que antes. Se debe usar dict.update({key:object}) para añadir a un diccionario
        combinaciones.update({
            "repeticion"+str(i): []
            })
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            cartas_aleatorias.remove(carta)

    return combinaciones

    