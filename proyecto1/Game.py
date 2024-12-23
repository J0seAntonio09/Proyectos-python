import tkinter as tk
import random

root = tk.Tk()
root.title("Juego de Piedra, Papel o Tijera.")

clicks = 0

def Botones(opcion):
    global resultado_texto, opcion_texto,clicks
    if opcion == 0:
        resultado_texto = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """
        opcion_texto = "¡Elegiste Piedra!"
    elif opcion == 1:
        resultado_texto = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
        opcion_texto = "¡Elegiste Papel!"
    elif opcion == 2:
        resultado_texto = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
        opcion_texto = "¡Elegiste Tijera!"
    etiqueta_resutado.config(text=resultado_texto)
    etiqueta_txt.config(text=opcion_texto)

    #Se Ocultarian los botones.
    boton_0.pack_forget()
    boton_1.pack_forget()
    boton_2.pack_forget()
    boton_4.pack(pady=25)
    boton_3.pack(pady=25)

    clicks = 0

def Continuar():
    global clicks
    
    # Incrementar el contador de clics
    clicks += 1
    
    if clicks == 2:  # Si el usuario hace doble clic, continuar
        etiqueta_txt.config(text="¡Juego Continuado!") #Aquí puedes agregar lo que ocurra cuando el usuario da doble clic
        boton_4.forget()
        clicks = 0  # Reiniciar contador después de continuar
    else:
        etiqueta_txt.config(text="Haz doble clic para continuar.")
        #print("Haz doble clic para continuar.")

def regresar():
    #.forget sirve para que no muestre los botones siguientes.
    boton_3.forget()
    boton_4.forget()

    boton_0.pack(pady=25)
    boton_1.pack(pady=25)
    boton_2.pack(pady=25)
    
    #editamos la variable etiqueta_txt con el .config a como estaba antes
    etiqueta_txt.config(text="")
    etiqueta_txt.config(text="Elige piedra, papel, tijera.")

#Se Indica que no queremos hacer que el usuario cambie el tamaño de la ventana.
root.resizable(False, False)
#Se crea la altura y la anchura de la aplicacion.
ancho = 1400
alto = 800

#Se toman las medidas de la pantalla de la computadora.
pantalla_ancho = root.winfo_screenwidth()
pantalla_alta = root.winfo_screenheight()

#Se centra la apertura de la aplicacion.
x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alta // 2) - (alto // 2)

#El root.geometry es para indicar el tamaño de la ventana que se va crear.
root.geometry(f"{ancho}x{alto}+{x}+{y}")

#Se crearia una etiqueta que nos mostraria el texto siguiente para luego seleccionar las opciones siguientes.
etiqueta_txt = tk.Label(root, text="Elige piedra, papel, tijera.")
etiqueta_txt.pack(anchor="center")
etiqueta_txt.config(font=("Arial",24, "bold"))

etiqueta_resutado = tk.Label(root, text="", font=("Courier", 16), justify="center")
etiqueta_resutado.pack(pady=30)


#Se Crearian los botones para seleccionar una opcion.
"""
relief = "groove" (es el formato del bonton el diseño.)
borderwidth = 5 (es la escala del tamaño del borde del bonton con su diseño.)
height=5 (Altura del Boton.)
width=100 (Ancho del Boton.)
"""
boton_0 = tk.Button(root, text="Piedra", relief="groove"  , borderwidth= 5 , height=5 , width=100 , command= lambda: Botones(0))
boton_1 = tk.Button(root, text="Papel", relief="groove"  , borderwidth= 5 , height=5 , width=100 , command= lambda: Botones(1)) 
boton_2 = tk.Button(root, text="Tijera", relief="groove"  , borderwidth= 5 , height=5 , width=100 , command= lambda: Botones(2))
boton_3 = tk.Button(root, text="¿Continuar?", relief="groove", borderwidth=5, height=5, width=100, command=Continuar)
boton_4 = tk.Button(root, text="¿Deseas Regresar?", relief="groove", borderwidth=5, height=5, width=100, command=regresar)
#Se mostraria los botones en la aplicacion.
boton_0.pack (pady=25)
boton_1.pack (pady=25)
boton_2.pack (pady=25)



root.mainloop()