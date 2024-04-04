import socket
import threading
import csv
import time
with open('F:/nodeCrowd.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    data = [row for row in reader]
with open('G:/new NOVA/data/data.json') as file:
    reader = csv.DictReader(file, delimiter=',')
    route = [row for row in reader]
# print(route)
class Server:
    def __init__(self, name):
        self.HOST = "192.168.147.105"
        self.PORT = 4
        self.server = None
        self.name = name
        self.clients = []
        self.client_name = ""
        self.client_names = []
        self.start_server()

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen(5)
        self.accept_clients()

    def stop_server(self):
        self.server.close()

    def accept_clients(self):
        while True:
            if len(self.clients) < 10:
                client, addr = self.server.accept()
                self.clients.append(client)
                threading.Thread(target=self.send_receive_messages, args=(client,), daemon=True).start()  # threading._start_new_thread(self.send_receive_messages, (client, addr))

    def send_receive_messages(self, client):
        self.client_name = client.recv(4096).decode()
        self.client_names.append(self.client_name)
        print(self.client_name+" joined "+self.name)
        for j in range(len(self.clients)):
                self.clients[j].send(str(route).encode())
        
        for item in data: # Introduce a delay of 1 second before printing each item
            for j in range(len(self.clients)):
                self.clients[j].send(str(item).encode())
                # print(item, 'is sent to', self.client_names[j])
            time.sleep(3) 
        
        # while True:
        #     data = client.recv(4096).decode()
        #     if not data:
        #         break
        #     msg = {"message": data, "socket": client}
        #     ind = 0#int(not bool(self.clients.index(msg.get('socket'))))
        #     self.clients[ind].send(msg.get('message').encode())
        #     print(msg.get('message'), 'is sent to', self.client_names[ind])
        ind = self.clients.index(client)
        del self.client_names[ind]
        del self.clients[ind]
        client.close()


obj = Server('a')  # str(input('Enter the Server Name: ')))
