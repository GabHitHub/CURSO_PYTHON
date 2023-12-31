import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombreProducto = entry_nombreProducto.get()
    codigoProducto = entry_codigoProducto.get()
    fechaEntrega = entry_fechaEntrega.get()
    cantidad = entry_cantidad.get()
    
    #Obligatoriedad de datos en campos
    if len(nombreProducto) == 0 or len(codigoProducto)==0 or len(fechaEntrega)==0 or len(cantidad)==0:
         messagebox.showerror("Error", "Faltan Datos")
               
    else :
         if len(nombreProducto) == 1 or len(codigoProducto)==1 or len(fechaEntrega)==1 or len(cantidad)==1:
           messagebox.showinfo("Correcto", f"Guardado: {nombreProducto} - {fechaEntrega} - {codigoProducto} - {cantidad} en el inventario")
    
def limpiar_campos():
    entry_nombreProducto.delete(0, tk.END)
    entry_codigoProducto.delete(0, tk.END)
    entry_fechaEntrega.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

root = tk.Tk()
root.title("CG COMPUTADORAS")

etiqueta_nombreProducto = tk.Label(root, text="Nombre del producto:")
etiqueta_nombreProducto.pack()

entry_nombreProducto = tk.Entry(root)
entry_nombreProducto.pack()

etiqueta_codigoProducto = tk.Label(root, text="Código del producto:")
etiqueta_codigoProducto.pack()

entry_codigoProducto = tk.Entry(root)
entry_codigoProducto.pack()

etiqueta_cantidad = tk.Label(root, text="Cantidad:")
etiqueta_cantidad.pack()

entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

etiqueta_fechaEntrega = tk.Label(root, text="Fecha de Entrega:")
etiqueta_fechaEntrega.pack()

entry_fechaEntrega = tk.Entry(root)
entry_fechaEntrega.pack()

#Verificar el ingreso de datos

boton_guardar = tk.Button(root, text="Guardar", command=guardar_datos)
boton_guardar.pack()

boton_limpiar = tk.Button(root, text="Limpiar Campos", command=limpiar_campos)
boton_limpiar.pack()

root.mainloop()

