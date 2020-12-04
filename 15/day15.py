from collections import namedtuple
from functools import reduce
from itertools import repeat
from typing import List, Dict, Set, Tuple, Generator

from util import extract_all_numbers

Ingredient = namedtuple('Ingredient', ['name', 'capacity', 'durability', 'flavor', 'texture', 'calories'])


def parse(line_data: List[str]) -> List[Ingredient]:
    parsed = []
    for line in line_data:
        name, properties = line.split(': ')
        parsed.append(Ingredient(name, *extract_all_numbers(properties)))

    return parsed


def recipes(components: int, total: int) -> Generator[List[int], None, None]:
    # Recursive generator for recipes.
    # 4 ingredients/components -> [a, b, c, d], where a+b+c+d = total

    # Base case, if there is only one ingredient it correspond to 100% of total
    if components == 1:
        start = total
    else:
        start = 0

    # Loop through all possible values for this position
    for i in range(start, total + 1):
        # Calculate the remaining capacity of the total, yet to be filled
        remaining = total - i

        # If there are still multiple other components to fill, recurse and generate them
        if components >= 1:
            # Generate all shorter recipes that fill the remaining capacity
            for recipe in recipes(components - 1, remaining):
                yield [i] + recipe
        else:
            # Base case, this is the last component
            yield [i]


def score(ingredient_data: List[Ingredient], recipe: List[int], max_calories: int = None) -> int:
    # Multiply each property by its proportion, collecting intermediate results into [[...], [...], ...]
    multiplied = []
    for ingredient, amount in zip(ingredient_data, recipe):
        multiplied.append([ingredient.capacity * amount,
                           ingredient.durability * amount,
                           ingredient.flavor * amount,
                           ingredient.texture * amount,
                           ingredient.calories * amount])

    # Reduce the nested list to a single list by adding all first values, all second values, etc.
    total_properties = list(reduce(lambda ing1, ing2: map(sum, zip(ing1, ing2)), multiplied))

    # Calories are at the end, and should not be included in the score
    calories = total_properties.pop()

    # Compute the total score by multiplying through the totals, setting negative values to 0
    total_score = reduce(lambda a, b: a*b, (max(0, prop) for prop in total_properties))

    # If there are too many calories, give the recipe a score of 0
    if max_calories and calories > max_calories:
        return 0
    return total_score


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file]

    ingredients = parse(lines)

    # Call score with the same ingredients every time but a new recipe from the generator
    print(f"Part 1: {max(map(score, repeat(ingredients), recipes(len(ingredients), 100)))}")

    # Now also the third argument to score, max_calories, is constant
    print(f"Part 2: {max(map(score, repeat(ingredients), recipes(len(ingredients), 100), repeat(500)))}")

