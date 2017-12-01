def orderpaper(filename):
    total = 0
    with open(filename) as file:
        for box in (file.read()).split():
            l, w, h = map(int, box.split('x'))
            t = l * w
            f = w * h
            s = l * h
            area = 2 * (t + f + s) + min(t, f, s)
            total += area
    return total

print(orderpaper("Day-2-input.txt"))
