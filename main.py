from model import Graph
import tkinter as tk


window = tk.Tk()
window.title("N.O.V.A.")
window.geometry('1366x788')
canvas = tk.Canvas(window)
canvas.pack(fill="both", expand=True)
obj = Graph(9, canvas, window)
submit = tk.Button(window, text='SUBMIT', command=lambda: obj.Submit(), bg='cyan', activebackground='green', font=('times', 25, 'bold'))
submit.place(x=1150, y=600)
window.mainloop()
