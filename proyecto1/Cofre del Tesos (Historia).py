print("""
 ██████╗ ██████╗ ███████╗██████╗ ███████╗    ██████╗ ███████╗██╗         ████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗ 
██╔════╝██╔═══██╗██╔════╝██╔══██╗██╔════╝    ██╔══██╗██╔════╝██║         ╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔═══██╗
██║     ██║   ██║█████╗  ██████╔╝█████╗      ██║  ██║█████╗  ██║            ██║   █████╗  ███████╗██║   ██║██████╔╝██║   ██║
██║     ██║   ██║██╔══╝  ██╔══██╗██╔══╝      ██║  ██║██╔══╝  ██║            ██║   ██╔══╝  ╚════██║██║   ██║██╔══██╗██║   ██║
╚██████╗╚██████╔╝██║     ██║  ██║███████╗    ██████╔╝███████╗███████╗       ██║   ███████╗███████║╚██████╔╝██║  ██║╚██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝╚══════╝       ╚═╝   ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
                                                                                                                            
""")
print("Bienvenido hacia la isla del tesoro.\nTu mision es encontrar el tesoro.")

respuesta_1 = input("Estas cruzando la calle\nHacia Donde desea Ir? Derecha o Izquierda: ").lower()

if respuesta_1 == "izquierda":
    print("Caiste en un agujero.\nGame Over.")

elif respuesta_1 == "derecha":

    print("\nLlegaste hacia un lago. Hay una isla en el medio del lago.")
    respuesta_2 =  input("Escribe 'Esperar' para esperar un bote. Escribe 'Nadar' para nadar hacia la isla  ").lower()
    
    if respuesta_2 == "esperar":
        print("\nLlegaste a la isla del lago y hay 3 puertas. Una Roja, Una Amarilla y una azul.")
        respuesta_3 = input("¿Que color de la puerta deseas abrir? (Favor de escribir el color)").lower()

        if respuesta_3 == "rojo":
            print("\nLa habitacion estaba llena de fuego.\nGame Over.")
        elif respuesta_3 == "amarilla":
            print("\n¡Felicidades tu encontraste el tesoro!\n¡Tu Ganaste!")
        elif respuesta_3 == "azul":
            print("\nLa habitacion estaba llena de moustros.\nGame Over.")

        else:
            print("\nRespuesta no encontrada cerrando el juego...")
    else:
        print("\nFuiste Atacado por un Tiburon.\n Game Over.")
else:
    print("\nTerminando el juego...")