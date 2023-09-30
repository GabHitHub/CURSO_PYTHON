import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get()
    nombre = entry_nombre.get()
    date = entry_date.get()
    cantidad = entry_cantidad.get()
    # Para guardar los datos 
    messagebox.showinfo("Correcto", f"Guardado: {nombre} - {nombre} - {date} - {cantidad} en el inventario")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

root = tk.Tk()
root.title("CG COMPUTADORAS")

etiqueta_nombre = tk.Label(root, text="Nombre del producto:")
etiqueta_nombre.pack()

entry_nombre = tk.Entry(root)
entry_nombre.pack()

etiqueta_nombre = tk.Label(root, text="Código del producto:")
etiqueta_nombre.pack()

entry_nombre = tk.Entry(root)
entry_nombre.pack()

etiqueta_cantidad = tk.Label(root, text="Cantidad:")
etiqueta_cantidad.pack()

entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

etiqueta_date = tk.Label(root, text="Fecha:")
etiqueta_date.pack()

entry_date = tk.Entry(root)
entry_date.pack()

#Verificar el ingreso de datos

boton_guardar = tk.Button(root, text="Guardar", command=guardar_datos)
boton_guardar.pack()

boton_limpiar = tk.Button(root, text="Limpiar Campos", command=limpiar_campos)
boton_limpiar.pack()

root.mainloop()

