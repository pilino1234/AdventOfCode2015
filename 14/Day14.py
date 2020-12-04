import re
from collections import namedtuple
from queue import PriorityQueue
from typing import List

Reindeer = namedtuple('Reindeer', ['name', 'speed', 'runtime', 'rest'])


def parse_reindeer(input_lines: List[str]) -> List[Reindeer]:
    parsed_list = []

    regex = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")

    for line in input_lines:
        data = regex.match(line)
        values = [*data.groups()]
        values[1:] = list(map(int, values[1:]))
        parsed_list.append(Reindeer(*values))

    return parsed_list


def race(reindeer_list: List[Reindeer], timeout: int):
    distances = {deer: 0 for deer in reindeer_list}
    reindeer_states = {deer: True for deer in reindeer_list}
    schedule = PriorityQueue(maxsize=len(reindeer_list))

    for deer in reindeer_list:
        schedule.put((0, deer))

    while schedule:
        tick, deer = schedule.get()

        if tick > timeout:
            break

        if reindeer_states[deer]:
            # Deer starts running (stops resting)
            reindeer_states[deer] = False
            distances[deer] += deer.speed * min(deer.runtime, timeout - tick)
            schedule.put((tick + deer.runtime, deer))
        else:
            # Deer starts resting (stops running)
            reindeer_states[deer] = True
            schedule.put((tick + deer.rest, deer))

    return distances


def race2(reindeer_list: List[Reindeer], timeout: int):
    distances = {deer: 0 for deer in reindeer_list}
    points = {deer: 0 for deer in reindeer_list}
    reindeer_running = {deer: True for deer in reindeer_list}
    reindeer_times = {deer: deer.runtime for deer in reindeer_list}

    for tick in range(timeout):
        for deer in reindeer_list:
            if reindeer_running[deer]:
                distances[deer] += deer.speed

            reindeer_times[deer] -= 1
            if reindeer_times[deer] == 0:
                if reindeer_running[deer]:
                    reindeer_times[deer] = deer.rest
                else:
                    reindeer_times[deer] = deer.runtime
                reindeer_running[deer] = not reindeer_running[deer]

        leading_distance = max(distances.values())
        for deer in reindeer_list:
            if distances[deer] == leading_distance:
                points[deer] += 1

    return points


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file]

    reindeer = parse_reindeer(lines)

    results = race(reindeer, timeout=2503)
    print(max(results.values()))

    results2 = race2(reindeer, timeout=2503)
    print(max(results2.values()))
