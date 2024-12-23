import random #Importa la librerira de Random 
while True: # Aqui estariamos utilizando el While True Para que sea algo constante cuando llegue al final del codigo
    print("\n ---Bienvenido al Juego de la Carta---") #Hace una imprecion de pantalla con un salto de Linea
    name = input("Incerte su Usarname:") # Nombra la variable "name" dependiendo la infromacion que le ponga el usuario o dato
    print("Bienvenido de Nuevo:", name) # Imprime el nombre del usuario con la variable nombre utilizada anteriormente (name)

    continuar = input("Quieres Iniciar el juego? (s/n)") # Te pregunta si quieres Iniciar el juego si la respuesta es "Si" Comienza el juego si dice "No" se Termina el programa
    if continuar == "n"or continuar == "no": #Pregunta si dice no Acaba El programa
        print("Vuelva Pronto", name) # Imprime "Vuelva Pronto" y el nombre del usuario
        break # Termina el programa del bucle

    if continuar == "s" or continuar == "si": # Sirve para cuando el usuario dice que "Si" Vaya por este camino y siga con el programa
        print(name," Se esta iniciando el juego de cartas...") # Imprime tu Nombre y te dice que se esta ejecutando el programa
        card_cmd = random.randint (0,50) # Selecciona una Carta Random del 0-50
        print("El CMD a Elejido una carta:", card_cmd) # Imprime la carta random y dice que es carta del CMD ( Maquina )
        crd_select = input("Puse en Numero 0 Para Generar Su Carta:")   # Con la variavle "crd_select" dice que si quieres generar tu carta preciones 0
        crd_select = random.randint (0,50) # Genera una carta Random del 0-50
        print("Tu Carta es:", crd_select) # Imprime tu carta Generada alazar
        
        if crd_select > card_cmd: # Pregunta que si tu carta es mayor que la de tu oponente y si es mayor va con el siguiente print
            print("Me Ganaste :(") # Imprime que le Ganaste a la Computadora
            break # Finaliza el programa 
        elif crd_select < card_cmd:# Y so es menor va a seguir este camino y va a imprimir lo siguiente
            print("Te Gane :) ") # Imprime que te ha Ganado
            break # Finaliza el programa
        
#Jose Antonio Del Rio Cardona 