# -*- coding: utf-8 -*-
RECIPE_NAME_INDEX = 0
INGREDIENTS_START_INDEX = 2
INGREDIENT_NAME_INDEX = 0
INGREDIENT_QUANTITY_INDEX = 1
INGREDIENT_MEASURE_INDEX = 2
INGREDIENT_SEPARATOR = "|"

INGREDIENT_NAME = 'ingredient_name'
INGREDIENT_QUANTITY = 'quantity'
INGREDIENT_MEASURE = 'measure'


def ingredient_index(dish_recipe: dict, ingredient_name: str):
    for index, ingredient in enumerate(dish_recipe):
        if ingredient_name in ingredient:
            return index
    raise LookupError(f'{ingredient_name} not find in {dish_recipe}')


def add_ingredient(dish_recipe: dict, ingredient: str):
    ingredient_info = [item.strip() for item in ingredient.split(INGREDIENT_SEPARATOR)]
    name = ingredient_info[INGREDIENT_NAME_INDEX].capitalize()
    quantity = ingredient_info[INGREDIENT_QUANTITY_INDEX]
    measure = ingredient_info[INGREDIENT_MEASURE_INDEX]

    try:
        index = ingredient_index(dish_recipe, name)
        dish_recipe[index][INGREDIENT_QUANTITY] += quantity
    except LookupError as error:
        new_ingredient = {
            INGREDIENT_NAME: name,
            INGREDIENT_QUANTITY: quantity,
            INGREDIENT_MEASURE: measure
        }
        dish_recipe.append(new_ingredient)


class CookBookParser:
    @staticmethod
    def get_dish_recipe(recipe_in_lines: list):
        dish_name = recipe_in_lines[RECIPE_NAME_INDEX]
        recipe = {dish_name: []}
        dish_recipe = recipe[dish_name]

        for ingredient in recipe_in_lines[INGREDIENTS_START_INDEX:]:
            add_ingredient(dish_recipe, ingredient)

        return recipe

    @staticmethod
    def read_recipes(file_path: str):
        cook_book = {}
        file = open(file_path, 'r', encoding="utf-8")
        recipes = file.read().split("\n\n")

        for recipe in recipes:
            recipe_in_lines = recipe.split("\n")
            cook_book.update(CookBookParser.get_dish_recipe(recipe_in_lines))

        return cook_book



