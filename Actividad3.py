import tkinter as tk

def accion_boton():
    print("¡ El Boton ha sidop presionado!")

ventana =tk.Tk()   
ventana.title("Ventana con Botón")

etiqueta = tk.Label(ventana,text="Presiona el boton")
etiqueta.pack()

boton_accion = tk.Button(ventana,text="presioname", command=accion_boton)
boton_accion.pack()

ventana.mainloop()