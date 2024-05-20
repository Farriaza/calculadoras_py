from tkinter import *

root = Tk()
root.configure(background="#333333")
root.title("Calculadora")

ecuacion = StringVar()


def tecla(val):
    ecuacion.set(ecuacion.get() + str(val))


def limpiar():
    ecuacion.set("")


def tecla_igual():
    try:
        resultado = str(eval(ecuacion.get()))
        ecuacion.set(resultado)
    except:
        ecuacion.set("Error")


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

exprecion_entry = Entry(root, textvariable=ecuacion)
exprecion_entry.grid(row=0, columnspan=4, sticky="nswe")

btn7 = Button(root, text="7", background="#666", fg="#fff", command=lambda: tecla(7))
btn7.grid(row=1, column=0, sticky="nswe")
btn8 = Button(root, text="8", background="#666", fg="#fff", command=lambda: tecla(8))
btn8.grid(row=1, column=1, sticky="nswe")
btn9 = Button(root, text="9", background="#666", fg="#fff", command=lambda: tecla(9))
btn9.grid(row=1, column=2, sticky="nswe")

btn4 = Button(root, text="4", background="#666", fg="#fff", command=lambda: tecla(4))
btn4.grid(row=2, column=0, sticky="nswe")
btn5 = Button(root, text="5", background="#666", fg="#fff", command=lambda: tecla(5))
btn5.grid(row=2, column=1, sticky="nswe")
btn6 = Button(root, text="6", background="#666", fg="#fff", command=lambda: tecla(6))
btn6.grid(row=2, column=2, sticky="nswe")

btn1 = Button(root, text="1", background="#666", fg="#fff", command=lambda: tecla(1))
btn1.grid(row=3, column=0, sticky="nswe")
btn2 = Button(root, text="2", background="#666", fg="#fff", command=lambda: tecla(2))
btn2.grid(row=3, column=1, sticky="nswe")
btn3 = Button(root, text="3", background="#666", fg="#fff", command=lambda: tecla(3))
btn3.grid(row=3, column=2, sticky="nswe")

btn0 = Button(root, text="0", background="#666", fg="#fff", command=lambda: tecla(0))
btn0.grid(row=4, column=0, sticky="nswe", columnspan=2)

btn_punto = Button(
    root, text=".", background="#666", fg="#fff", command=lambda: tecla(".")
)
btn_punto.grid(row=4, column=2, sticky="nswe")

btn_suma = Button(
    root, text=" + ", background="#666", fg="#fff", command=lambda: tecla("+")
)
btn_suma.grid(row=1, column=3, sticky="nswe")


btn_resta = Button(
    root, text=" - ", background="#666", fg="#fff", command=lambda: tecla("-")
)
btn_resta.grid(row=2, column=3, sticky="nswe")

btn_mult = Button(
    root, text=" * ", background="#666", fg="#fff", command=lambda: tecla("*")
)
btn_mult.grid(row=3, column=3, sticky="nswe")

btn_div = Button(
    root, text=" / ", background="#666", fg="#fff", command=lambda: tecla("/")
)
btn_div.grid(row=4, column=3, sticky="nswe")

btn_igual = Button(root, text="=", background="#666", fg="#fff", command=tecla_igual)
btn_igual.grid(row=5, column=2, sticky="nswe")

btn_borrar = Button(root, text="clr", background="#666", fg="#fff", command=limpiar)
btn_borrar.grid(row=5, column=3, sticky="nswe")

root.mainloop()
