import numpy 
 
class OneMillionLights:
    def __init__(self):
        self.grid = numpy.zeros((1000, 1000), bool)

    def __str__(self):
        return str(self.grid)

    def parser(self, text):
        words = text.split()
        command = words[0]
        if command == "turn":
            onoff = {"on": True, "off": False}
            self.switch(words[2], words[-1], onoff[words[1]])
        if command == "toggle":
            self.toggle(words[1], words[-1])

    def toggle(self, start, end):
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        print("[toggle] ({x1},{y1}) ({x2},{y2})".format(x1=x1, y1=y1, x2=x2, y2=y2))
        self.grid[int(x1):int(x2)+1, int(y1):int(y2)+1] = numpy.logical_not(self.grid[int(x1):int(x2)+1, int(y1):int(y2)+1])


    def switch(self, start, end, onoff):
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        print("[switch] ({x1},{y1}) ({x2},{y2}) {onoff}".format(x1=x1, y1=y1, x2=x2, y2=y2, onoff=onoff))
        self.grid[int(x1):int(x2)+1, int(y1):int(y2)+1] = onoff

    def count_on(self):
        return (self.grid == 1).sum()

if __name__ == "__main__":

    lights = OneMillionLights()
    print(lights)

    with open("Day6-input.txt") as file:
        commands = file.read().splitlines()
        for i in commands:
            lights.parser(i)
    
    print(lights)
    print(lights.count_on())
