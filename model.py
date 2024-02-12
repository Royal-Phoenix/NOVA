import csv
import sys
import tkinter as tk
import math
import time


class Graph:
    def __init__(self, vertices, canvas, window):
        self.V = vertices
        a, b, c, x, y, z, s, t = 433, 683, 933, 94, 344, 594, 283, 1083
        self.graphCoords = {'Home A': (s, y), 'Temple': (a, x), 'Office': (b, x), 'Theme Park': (c, x), 'Home B': (t, y),
                            'Cinema': (c, z), 'School': (b, z), 'Beach': (a, z), 'Restaurant': (b, y)}
        self.edgesCoords = [('Home A', 'Temple'), ('Home A', 'Beach'), ('Temple', 'Office'), ('Temple', 'Beach'), ('Office', 'Theme Park'), ('Office', 'Cinema'), ('Office', 'Restaurant'),
                            ('Theme Park', 'Home B'), ('Theme Park', 'Cinema'), ('Home B', 'Cinema'), ('Cinema', 'School'), ('School', 'Beach'), ('School', 'Restaurant'), ('Beach', 'Restaurant')]
        self.graph = {'Home A': [25, [['Temple', 4], ['Beach', 8]]], 'Temple': [60, [['Home A', 4], ['Office', 8], ['Beach', 11]]], 'Office': [45, [['Temple', 8], ['Theme Park', 7], ['Cinema', 4], ['Restaurant', 2]]],
                      'Theme Park': [90, [['Office', 7], ['Home B', 9], ['Cinema', 14]]], 'Home B': [125, [['Theme Park', 9], ['Cinema', 10]]], 'Cinema': [35, [['Office', 4], ['Theme Park', 14], ['Home B', 10], ['School', 2]]],
                      'School': [10, [['Cinema', 2], ['Beach', 1], ['Restaurant', 6]]], 'Beach': [75, [['Home A', 8], ['Temple', 11], ['School', 1], ['Restaurant', 7]]], 'Restaurant': [80, [['Office', 2], ['School', 6], ['Beach', 7]]]}
        self.screen = canvas
        self.path = 'assets/sprites/'
        self.win = window
        self.radius = 50
        self.nodes = []
        self.selected = []
        self.edges = []
        self.distCosts = []
        self.timeCosts = []
        self.crowdCosts = []
        self.totCosts = []
        self.paths = []
        self.speed = 2
        self.minCost = sys.maxsize
        for i in self.graph:
            self.graph[i].append(tk.PhotoImage(file=self.path+i+'.png'))
        self.addEdges()
        self.addVertices()

    def Add(self, x):
        self.selected.append(x)

    def addVertices(self):
        r = self.radius
        for i in self.graphCoords:
            m, n = self.graphCoords[i]
            node = tk.Button(self.win, text=i, image=self.graph[i][2], command=lambda s=i: self.Add(s), compound=tk.BOTTOM, fg='red', font=('times', 15, 'bold'))
            node.place(x=m-r, y=n-r)
            self.nodes.append(node)

    def addEdges(self):
        for i in self.edgesCoords:
            s, t = i
            x1, y1 = self.graphCoords[s]
            x2, y2 = self.graphCoords[t]
            line = self.screen.create_line(x1, y1, x2, y2, width=4)
            x = abs((x2-x1)/2) + min(x1, x2)
            y = abs((y2-y1)/2) + min(y1, y2)
            x = x-20 if (y > 0) else x
            y = y-20 if (x > 0) else y
            for j, k in self.graph[s][1]:
                if j == t:
                    data = str(k)
                    break
            self.screen.create_text(x, y, text=data, fill="black", font=('times', 20, 'bold'))
            self.edges.append(line)

    def printPath(self, path):
        arr = [i for i in path]
        return arr

    def All(self, sub, full):
        for i in sub:
            if i not in full:
                return False
        return True

    def printAllPathsUtil(self, u, d, visited, path, records):
        visited.add(u)
        path.append(u)
        if u == d and self.All(self.selected, path):
            dcost, tcost, ccost = 0, 0, 0
            for i in range(len(path) - 1):
                src, dest = path[i], path[i + 1]
                for j, k in self.graph[src][1]:
                    if j == dest:
                        dcost += k
                        if dest in self.selected:
                            tcost += self.graph[dest][0]
                            ccost += int(records[str(dest)])
            p = self.printPath(path)
            self.paths.append(p)
            self.distCosts.append(dcost)
            self.timeCosts.append(tcost)
            self.crowdCosts.append(ccost)
            totCost = (dcost/self.speed)+tcost+ccost
            self.totCosts.append(totCost)
        else:
            for i, w in self.graph[u][1]:
                if i not in visited:
                    self.printAllPathsUtil(i, d, visited, path, records)
        path.pop()
        visited.remove(u)

    def printAllPaths(self, s, d, records):
        self.printAllPathsUtil(s, d, set(), [], records)

    def Move(self, x0, y0, x1, y1):
        if abs(x1-x0) == 0:
            x, y = (0, 1) if (y0 < y1) else (0, -1)
            return x, y
        elif abs(y1-y0) == 0:
            x, y = (1, 0) if (x0 < x1) else (-1, 0)
            return x, y
        else:
            slope = abs(y1-y0)/(x1-x0)
            if x0 < x1:
                x, y = (1, slope) if (y0 < y1) else (1, -slope)
            else :
                x, y = (-1, -slope) if (y0 < y1) else (-1, slope)
            return x, y

    def Travel(self, x, y, path):
        r = 30
        user = self.screen.create_oval(x-r, y-r, x+r, y+r, fill="gold")
        for i in range(1, len(path)):
            dx, dy = self.graphCoords[path[i]]
            slope_x, slope_y = self.Move(x, y, dx, dy)
            dist = abs(x-dx) if (abs(x-dx) > 0) else int(math.sqrt(((x-dx)**2)+((y-dy)**2)))
            for j in range(dist):
                self.screen.move(user, slope_x, slope_y)
                self.win.update()
                time.sleep(0.01)
            x, y = dx, dy

    def travelPath(self):
        ind = self.totCosts.index(min(self.totCosts))
        check = True
        for i in range(len(self.paths[ind])-1):
            x1, y1 = self.graphCoords[self.paths[ind][i]]
            x2, y2 = self.graphCoords[self.paths[ind][i+1]]
            if check:
                self.Travel(x1, y1, self.paths[ind])
                check = False
            self.screen.create_line(x1, y1, x2, y2, fill="red", width=4)

    def Submit(self):
        src, dest = self.selected[0], self.selected[-1]
        self.selected = self.selected[1:-1]
        with open('TTSP5.csv') as data:
            reader = csv.DictReader(data, delimiter=',')
            for row in reader:
                self.printAllPaths(src, dest, row)
                for i in range(len(self.totCosts)):
                    print(self.paths[i], self.distCosts[i], self.timeCosts[i], self.crowdCosts[i], self.totCosts[i])
                print('------------------------')
        ind = self.paths.index(min(self.paths))
        print(self.paths[ind], self.distCosts[ind], self.timeCosts[ind], self.crowdCosts[ind], self.totCosts[ind])
        print(len(self.paths))
        self.travelPath()
