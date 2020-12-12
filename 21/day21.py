from typing import List, Dict, Tuple, Generator
from collections import namedtuple
from itertools import product
import copy


Item = namedtuple('Item', ['name', 'cost', 'damage', 'armour'])


class Entity:
    def __init__(self, name: str, hp: int, damage: int, armour: int):
        self.name = name
        self.hp = hp
        self.base_damage = damage
        self.base_armour = armour

        self.damage_bonus = 0
        self.armour_bonus = 0

    @property
    def alive(self):
        return self.hp > 0

    @property
    def damage(self):
        return self.base_damage + self.damage_bonus

    @property
    def armour(self):
        return self.base_armour + self.armour_bonus

    def equip_item(self, item: Item):
        self.damage_bonus += item.damage
        self.armour_bonus += item.armour

    def unequip_all(self):
        self.damage_bonus = 0
        self.armour_bonus = 0

    def __str__(self):
        return f"{self.name} HP: {self.hp} Damage: {self.base_damage} Armour: {self.base_armour}"


def parse_boss(line_data: List[str]) -> Entity:
    return Entity(
        name="Boss",
        hp=int(line_data[0].split(':')[1].strip()),
        damage=int(line_data[1].split(':')[1].strip()),
        armour=int(line_data[2].split(':')[1].strip()),
    )


def parse_equipment(line_data: List[str]) -> Dict[str, List[Item]]:
    items = {}

    category = None
    for line in line_data:
        if not line:
            continue

        if ':' in line:
            category, _, _ = line.partition(':')
            items[category] = []
        else:
            assert category is not None
            name, cost, dmg, arm = line.rsplit(maxsplit=3)
            items[category].append(Item(name, int(cost), int(dmg), int(arm)))

    # Add 'None' equipment
    items['Armor'].append(Item('None', 0, 0, 0))
    items['Rings'].append(Item('Damage +0', 0, 0, 0))
    items['Rings'].append(Item('Defense +0', 0, 0, 0))

    return items


def battle(player: Entity, boss: Entity) -> Entity:
    b = copy.copy(boss)
    p = copy.copy(player)

    player_turn = True

    while b.alive and p.alive:
        if player_turn:
            # player turn
            b.hp -= max(p.damage - b.armour, 1)
        else:
            # boss turn
            p.hp -= max(b.damage - p.armour, 1)
        player_turn = not player_turn

    winner = p if p.alive else b
    return winner


def gear_combinations(gear: Dict[str, List[Item]]) -> Generator[Tuple[Item, ...], None, None]:
    for (wep, arm, ring1, ring2) in product(*gear.values(), gear['Rings']):
        if ring1 != ring2:
            yield wep, arm, ring1, ring2


def find_extreme_gear(player: Entity, boss: Entity, gear: Dict[str, List[Item]], win: bool = True):
    extreme_cost = 1e6 if win else 0

    for gear_setup in gear_combinations(gear):
        for item in gear_setup:
            player.equip_item(item)

        winner = battle(player, boss)
        if (win and winner.name == 'Player') or (not win and winner.name == 'Boss'):
            cost = sum(item.cost for item in gear_setup)
            extreme_cost = min(extreme_cost, cost) if win else max(extreme_cost, cost)

        player.unequip_all()

    return extreme_cost


if __name__ == '__main__':
    with open("input.txt") as file:
        boss = parse_boss([line.strip() for line in file])

    with open("shop.txt") as file:
        equipment = parse_equipment([line.strip() for line in file])

    player = Entity("Player", hp=100, damage=0, armour=0)

    print(f"Part 1: {find_extreme_gear(player, boss, equipment)}")
    print(f"Part 2: {find_extreme_gear(player, boss, equipment, win=False)}")
