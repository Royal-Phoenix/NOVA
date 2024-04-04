from new import Graph
import tkinter as tk
import json, csv

window = tk.Tk()
window.title("NOVA")
window.geometry('1366x788')
canvas = tk.Canvas(window)
canvas.pack(fill="both", expand=True)


data = json.load(open('data/data.json'))#receive json fully

with open('data/crowd.csv') as csvFile:
    reader = csv.DictReader(csvFile, delimiter=',')
    crowd = [row for row in reader]
obj = Graph(canvas, window, data, crowd)
submit = tk.Button(window, text='SUBMIT', command=lambda: obj.Submit(), bg='cyan', activebackground='green', font=('times', 25, 'bold'))
submit.place(x=1150, y=600)
window.mainloop()
