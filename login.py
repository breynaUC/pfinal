import tkinter as tk
from tkinter import *

def submitact():     
    user = Username.get()
    passw = password.get()  
    logintodb(user, passw)
  
def abrir_ventana_secundaria():
    root.withdraw()
    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)
    center(ventana_secundaria)
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    boton_cerrar = tk.Button(
        ventana_secundaria,
        text="Cerrar ventana", 
        command=ventana_secundaria.destroy
    )
    boton_cerrar.place(x=75, y=75)
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))   
def logintodb(user, passw):
     
    if user=='dreyna' and passw=="123":
        abrir_ventana_secundaria();
    else:
        print("Error de datos...!")
 
root = tk.Tk()
root.geometry("300x150")
root.title("Login")
root.eval('tk::PlaceWindow . center')
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username: ", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 50)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password: ")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 50)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(root, text ="Login",
                      bg ='red', command = submitact, fg='white')
submitbtn.place(x = 150, y = 80, width = 100)
 
root.mainloop()