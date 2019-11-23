import numpy 
 
class OneMillionLights:
    def __init__(self):
        self.grid = numpy.zeros((1000, 1000), 'int')

    def __getitem__(self, i):
        return self.grid[i]

    def __str__(self):
        return str(self.grid)

    def parser(self, text):
        words = text.split()
        command = words[0]
        if command == "turn":
            onoff = {"on": 1, "off": -1}
            self.change_brightness(words[2], words[-1], onoff[words[1]])
        if command == "toggle":
            self.change_brightness(words[1], words[-1], 2)

    def change_brightness(self, start, end, amount):
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        print("[change brightness] ({x1},{y1}) ({x2},{y2}) {amount}".format(x1=x1, y1=y1, x2=x2, y2=y2, amount=amount))
        self.grid[int(x1):int(x2)+1, int(y1):int(y2)+1] += amount
        self.grid[self.grid < 0] = 0

    def total_brightness(self):
        return numpy.sum(self.grid)

if __name__ == "__main__":

    lights = OneMillionLights()
    print(lights)
    print(lights[999][938])

    with open("Day6-input.txt") as file:
        commands = file.read().splitlines()
        for i in commands:
            lights.parser(i)
    
    print(lights[999][938])
    print(lights.total_brightness())
