from .inputs import *


paciente_maximos = 100

def opciones(mensaje:str):
    opcion_valida = get_int(mensaje,1, 9, 5)
    
    return opcion_valida


def formato_paciente(id,nombre_validado, apellido_validado, edad_validado, altura_validado, peso_validado, dni_validado, grupo_sanguineo_validado) -> dict:
    if None in[nombre_validado, apellido_validado,edad_validado,altura_validado,peso_validado,dni_validado,grupo_sanguineo_validado]:
        return None
        
    else:
        paciente_creado = {"id":id, 
                           "nombre":nombre_validado, 
                           "apellido":apellido_validado, 
                           "edad": int(edad_validado),
                           "altura":int(altura_validado),
                           "peso": float(peso_validado),
                           "dni":int(dni_validado),
                           "grupo sanguineo":grupo_sanguineo_validado
                           }

    return paciente_creado

def crear_paciente(id:int) -> dict:

    nombre_validado = validar_caracteres("Ingrese su nombre: ")

    apellido_validado = validar_caracteres("Ingrese su apellido: ")
    
    edad_validado = get_int("Ingrese su edad: ", 1, 120, 3)
    
    altura_validado = get_int("Ingrese su altura: ", 30, 230, 3)

    peso_validado = get_float("Ingrese su peso: ", 10, 300, 3)
    
    dni_validado = validar_formato_dni(get_int("El DNI tiene que ser mayor a 4.000.000: ", 4000000, 99999999, 3))
        
    grupo_sanguineo_validado = validar_grupo_sanguineo("Ingrese su tipo sanguineo: ")
    
    paciente = formato_paciente(id, nombre_validado, apellido_validado, edad_validado, altura_validado, peso_validado, dni_validado, grupo_sanguineo_validado)
    
    if paciente:
        return paciente
    else:
        return print("ERROR: no se pudo dar de algo el paciente")


    
def agregar_paciente(pacientes:list, ids_asignados):

    if len(pacientes) < paciente_maximos + 1:
        if ids_asignados:
            nuevo_id = max(ids_asignados) + 1
        else:
            nuevo_id = 1        
        
        paciente_creado = crear_paciente(nuevo_id)
        print("pacientes",paciente_creado)
        if paciente_creado:
            pacientes.append(paciente_creado)
            ids_asignados.add(nuevo_id)
        
        return print("Paciente dado de alta con exito")
    else:
        return print("ERROR: no se puede agregar mas de 50 pacientes" )  
    
    
            
def menu_modificar_paciente(id_paciente):
    """Menu para modificar los datos de un paciente.

    Este menú permite al usuario modificar los datos de un paciente específico,
    como el nombre, apellido, edad, altura, peso, DNI y grupo sanguíneo.

    Args:
        id_paciente (dict): Diccionario que representa al paciente que se va a modificar.

    Example:
        # Ejemplo de uso:
        paciente = {"nombre": "Juan", "apellido": "Pérez", "edad": 30, "altura": 175, "peso": 70, "dni": "12345678", "grupo sanguineo": "A+"}
        menu_modificar_paciente(paciente)
    """
    bandera_seguir = True
    
    while bandera_seguir:
        opcion = opciones("1. Ingresar nombre a cambiar\n2. Ingrese apellido a cambiar\n3.La edad a cambiar\n4.Ingrese la altura a cambiar\n5.Ingrese el peso a cambiar:\n6. Ingrese el DNI a cambiar\n7.Ingrese el grupo sanguineoa cambiar\n8.salir\n elija una opcion:")
        
        match opcion:
            case 1:
                nombre_validado = validar_caracteres("Ingrese el nombre: ")
                
                id_paciente["nombre"] = nombre_validado    
                
            case 2:

                apellido_validado = validar_caracteres("Ingrese el apellido: ")

                id_paciente["apellido"] = apellido_validado
                
            case 3:
                edad_validado = get_int("Ingrese su edad: ", 1, 120, 3)

                id_paciente["edad"] = edad_validado
            case 4:

                altura_validado = get_int("Ingrese su altura: ", 30, 230, 3)
                
                id_paciente["altura"] = altura_validado
                
            case 5:
                peso_validado = get_float("Ingrese su peso: ", 10, 300, 3)

                id_paciente["peso"] = peso_validado          
            case 6:
                dni_validado = get_int("El DNI tiene que ser mayor a 4.000.000: ",4000000, 100000000, 3 )

                id_paciente["dni"] = dni_validado
            case 7:
                grupo_sanguineo_validado = validar_grupo_sanguineo("Ingrese su tipo sanguineo: ")

                id_paciente["grupo sanguineo"] = grupo_sanguineo_validado
            case 8:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    print("Cambios guardados con exito")
                    bandera_seguir = False        
                else:
                    bandera_seguir = True  
            case _:
                print("ERROR: elija una opcion")
                
def eliminar_paciente(clave:str, valor:int,diccionario:dict):
    """Elimina un paciente del diccionario según una clave y un valor especificados.

    Esta función busca un paciente en el diccionario que coincida con el valor proporcionado
    para la clave especificada y lo elimina del diccionario.

    Args:
        clave (str): La clave del diccionario que se utilizará para buscar al paciente.
        valor (int): El valor que se utilizará para comparar con la clave y encontrar al paciente.
        diccionario (dict): El diccionario que contiene a los pacientes.

    Returns:
        str: Un mensaje indicando si el paciente fue eliminado exitosamente.

    Example:
        # Ejemplo de uso:
        pacientes = [{"nombre": "Juan", "edad": 30}, {"nombre": "María", "edad": 25}]
        eliminar_paciente("nombre", "Juan", pacientes)
    """
    for paciente in diccionario:
        if paciente[clave] == valor:
            diccionario.remove(paciente)
            return print("Empleado eliminado de forma exitosa")
            
            
    return print("no se eliminó el paciente")



                    
