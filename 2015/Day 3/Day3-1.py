def move(location, direction):
    if direction == '^':
        return location[0], location[1] + 1
    elif direction == 'v':
        return location[0], location[1] - 1
    elif direction == '>':
        return location[0] + 1, location[1]
    elif direction == '<':
        return location[0] - 1, location[1]

def delivered_houses(data):
    houses = set()
    location = 0, 0
    houses.add(location)
    for d in data:
        location = move(location, d)
        houses.add(location)
    return len(houses)

def delivered_houses_with_robot(data):
    houses = set()
    santa_location = robosanta_location = 0, 0
    houses.add(santa_location)
    houses.add(robosanta_location)
    for idx, d in enumerate(data):
        if idx % 2 == 0:
            santa_location = move(santa_location, d)
            location = santa_location
        else:
            robosanta_location = move(robosanta_location, d)
            location = robosanta_location
        houses.add(location)
    return len(houses)

with open("Day3-input.txt") as file:
    data = file.read()
    print(delivered_houses(data))
    print(delivered_houses_with_robot(data))

