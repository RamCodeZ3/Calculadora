import tkinter as tk
import math
import re


def clic(numero):
    if re.findall(r'^0', pantalla.get()):
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, numero)

    else:
        pantalla.insert(tk.END, numero)


def calcular():
    operacion = pantalla.get()
    try:
        resultado = eval(operacion)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
       
        if re.findall(r'\.0$', pantalla.get()):
           pantalla.delete(len(pantalla.get())- 2, tk.END)
           
    except: 
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str("ERROR"))

def Raiz():
    numeral = pantalla.get()
    try:
     resultado = math.sqrt(int(numeral))
     pantalla.delete(0, tk.END)
     pantalla.insert(tk.END, str(resultado))
     if re.findall(r'.0$', pantalla.get()):
         pantalla.delete(len(pantalla.get())- 2, tk.END)
         
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str("ERROR"))

def insert_sign():
   if re.findall(r'^\d', pantalla.get()) and not pantalla.get() == "0":
     pantalla.insert(0, "-")
   elif re.findall(r'^-', pantalla.get()):
      pantalla.delete(0)

def clear():
    pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, "0")

def clear2(): 
   if len(pantalla.get()) == 1:
      pantalla.delete(len(pantalla.get())-1, tk.END)
      pantalla.insert(tk.END, "0")
   else:  pantalla.delete(len(pantalla.get())-1, tk.END)


app = tk.Tk()
app.geometry("325x415")
app.configure(background="#212f3c")
app.title("Calculadora")
app.resizable(height=False, width=False)

pantalla = tk.Entry(app, width=50, bg="#154360", border=0, fg="White", font=("Sans", 22))
pantalla.grid(row=0, column=0, columnspan=4,)
pantalla.insert(tk.END, "0")

numeros = [
   "**",
   "7",
   "8",
   "9",
   "/",
   "4",
   "5",
   "6",
   "*",
   "1",
   "2",
   "3",
   "-",
   "0",
   "00",
   ".",
   "+"
]

fila = 1
columna = 3

for numero in numeros:
    boton_numerico = tk.Button(
       app,
       text=numero,
       height=3,
       width=8,
       border=0,
       font=("Sans", 12),
       bg="#31404F",
       fg="white",
       command=lambda num=numero: clic(num)
    )
    
    boton_numerico.grid(row=fila, column=columna, padx=0, pady=2)
    columna += 1

    if columna > 3:
        columna = 0
        fila += 1 

    elif re.findall(r'\d', numero):
       boton_numerico.configure(bg="#34495e")

    elif re.findall(r'\.', numero):
       boton_numerico.configure(bg="#34495e")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)

Result = tk.Button(
   text="=",
   width=20,
   border=0,
   fg="white",
   font=("Sans", 16),
   command= calcular,
   bg="#3EEC30"
)
Result.grid()
Result.place(x=82, y=375)

Delete= tk.Button(
   text="CE",
   width=6,
   height=1,
   bg="#EB0101",
   fg="white",
   border=0,
   font=("Sans", 16),
   command= clear
   )

Delete.grid()
Delete.place(x=2, y=375)

Delete2 = tk.Button(
   app,
   text="X",
   height=3,
   width=8,
   border=0,
   font=("Sans", 12),
   bg="#31404F",
   fg="white",
   command=clear2
   )

Delete2.grid(row=1, column=0)

Sqrt = tk.Button(app,
                 text="√2",
                 height=3,
                 width=8,
                 border=0,
                 font=("Sans", 12),
                 bg="#31404F",
                 fg="white",
                 command=Raiz
)

Sqrt.grid(row=1, column=1)

insert_signN = tk.Button(
   app,
   text="-",
   height=3,
   width=8,
   border=0,
   font=("Sans", 12),
   bg="#31404F",
   fg="white",
   command=insert_sign
)

insert_signN.grid(row=1, column=2)

app.mainloop()
