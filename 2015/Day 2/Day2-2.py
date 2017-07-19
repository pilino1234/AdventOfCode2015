def orderribbon(filename):
    total = 0
    with open(filename) as file:
        for box in (file.read()).split():
            dims = sorted(map(int, box.split('x')))
            length = 2*dims[0] + 2*dims[1]
            volume = dims[0] * dims[1] * dims[2]
            total += length + volume
    return total
    
print(orderribbon("Day-2-input.txt"))
