import random

def manos(opcion):
    if opcion == 0:
        #Primeras Opciones:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
              """)
    
    elif opcion == 1:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
              """)
    
    elif opcion == 2:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
              """)
def versus():
    #Empates:
    if respuesta == 0 and respuesta_computadora == 0:
        print("""
            _______           _______
        ---'   ____)         (____   '---
              (_____)       (_____)
              (_____)       (_____)
              (____)         (____)
        ---.__(___)           (___)__.---
                   Roca VS Roca
                      Empate
              """)
    elif respuesta == 1 and respuesta_computadora == 1:
        print("""
             _______                     _______
        ---'    ____)____           ____(____   '----
                   ______)         (______
                  _______)         (_______
                 _______)           (_______
        ---.__________)                (_________.---
                        Papel VS Papel
                            Empate
              """)
       
    elif respuesta == 2 and respuesta_computadora == 2:
        print("""
            _______                      _______
        ---'   ____)____            ____(____   '---
                  ______)          (______
               __________)        (__________
              (____)                    (____)
        ---.__(___)                      (___)__.---
                     Scissor vs Scissor
                           Empate
              """)
    
    #Variaciones:
    #Piedra:
    elif respuesta == 0 and respuesta_computadora == 1:
        print("""
            _______                 _______
        ---'   ____)           ____(____   '----
              (_____)         (______
              (_____)         (_______
              (____)           (_______
        ---.__(___)                (_________.---  
              
                     Roca vs Papel
                       Perdiste :(
              """)
    
    elif respuesta == 0 and respuesta_computadora == 2:
        print("""
            _______                 _______
        ---'   ____)           ____(____   '---
              (_____)         (______
              (_____)        (__________
              (____)               (____)
        ---.__(___)                 (___)__.---
                    Roca vs tijera
                       Ganaste :)
              """)
    #Papel:
    elif respuesta == 1 and respuesta_computadora == 0:
        print("""
             _______               _______
        ---'    ____)____         (____   '---
                   ______)       (_____)
                  _______)       (_____) 
                 _______)         (____)
        ---.__________)            (___)__.---
                    Papel vs Roca
                       Ganaste :)
              """)

    elif respuesta == 1 and respuesta_computadora == 2:
        print("""
             _______                     _______
        ---'    ____)____           ____(____   '---
                   ______)         (______
                  _______)        (__________
                 _______)               (____)
        ---.__________)                   (___)__.---
                        Papel vs Tijera
                           Perdiste :(
              """) 
    #Tijeras:   
    elif respuesta == 2 and respuesta_computadora == 0:
        print("""
            _______                       _______
        ---'   ____)____                 (____   '---
                  ______)               (_____)
               __________)              (_____)
              (____)                     (____)
        ---.__(___)                       (___)__.---
                        Tijera vs Piedra
                           Perdiste :(
              """)
    
    elif respuesta == 2 and respuesta_computadora == 1:
        print("""
            _______                       _______
        ---'   ____)____             ____(____   '----
                  ______)           (______
               __________)         (_______
              (____)                  (_______
        ---.__(___)                       (_________.---
                        Tijera vs Papel
                           Ganaste :)
              """)

opciones = ["Piedra", "Papel", "Tijera"]

respuesta = int(input("Elige 0 para piedra, 1 para papel, 2 para tijera."))
manos(respuesta)
print(f"Elegiste {opciones[respuesta]}.")

respuesta_computadora = int(random.randint(0, 2))
manos(respuesta_computadora)
print(f"La computadora Eligio {opciones[respuesta_computadora]}.")
versus()
