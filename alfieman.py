import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("Editor de texto Alfieman")

text = tk.Text(root)
text.grid()

def abrir():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        file_contents = file.read()
        text.delete('1.0', tk.END)
        text.insert(tk.END, file_contents)

def guardar():
    file_path = filedialog.asksaveasfilename()
    with open(file_path, 'w') as file:
        file_contents = text.get('1.0', tk.END)
        file.write(file_contents)

menu_bar = tk.Menu(root)

archivo_menu = tk.Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Abrir archivo", command=abrir)
archivo_menu.add_command(label="Guardar archivo", command=guardar)
archivo_menu.add_command(label="Salir del editor de texto Alfieman", command=root.quit)

menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

root.config(menu=menu_bar)
root.mainloop()


