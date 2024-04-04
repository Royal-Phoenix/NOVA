import socket
import threading
from new import Graph
import tkinter as tk


window = tk.Tk()
window.title("NOVA")
window.state('zoomed')
canvas = tk.Canvas(window)
canvas.pack(fill="both", expand=True)
class Client:
    def __init__(self, name, func):
        self.HOST = "192.168.147.105"
        self.PORT = 4
        self.client = None
        self.func = func
        self.name = name
        self.data, self.crowd = None, None
        self.connect_to_server()

    def create_display(self):
        pass

    def connect_to_server(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        self.client.send(self.name.encode())
        self.receive_messages()
        #threading.Thread(target=self.receive_messages, daemon=True).start()  # threading._start_new_thread(self.receive_messages, (self.client, ""))
        #self.send_messages()

    def send_messages(self):
        while True:
            msg = str(input('Enter: '))
            self.client.send(msg.encode())

    def receive_messages(self):
        flag = True
        while True:
            data = self.client.recv(30000).decode()
            print(len(data))
            data = eval(data)
            if self.data is None and type(data)==type({}):
                self.data = data
                print(self.data)
            if self.crowd is None and type(data)==type([]):
                self.crowd = data
                print(self.crowd)
            if self.data is not None and self.crowd is not None and flag:
                obj = Graph(canvas, window, self.data, self.crowd, self.func)
                add = tk.Button(window, text='ADD SHOP', command=lambda: obj.addStop(), bg='black', fg='white', activebackground='red', font=('times', 25, 'bold'))
                submit = tk.Button(window, text='SUBMIT', command=lambda: obj.Submit(), bg='black', fg='white', activebackground='red', font=('times', 25, 'bold'))
                add.place(x=1130, y=510)
                submit.place(x=1150, y=600)
                flag = False
                break
        window.mainloop()
