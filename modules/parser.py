# -*- coding: utf-8 -*-
import modules.constants as const

RECIPE_NAME_INDEX = 0
INGREDIENTS_START_INDEX = 2
INGREDIENT_NAME_INDEX = 0
INGREDIENT_QUANTITY_INDEX = 1
INGREDIENT_MEASURE_INDEX = 2
INGREDIENT_SEPARATOR = "|"


def add_ingredient(dish_recipe: dict, ingredient: str):
    ingredient_info = [item.strip() for item in ingredient.split(INGREDIENT_SEPARATOR)]
    name = ingredient_info[INGREDIENT_NAME_INDEX].capitalize()
    quantity = ingredient_info[INGREDIENT_QUANTITY_INDEX]
    measure = ingredient_info[INGREDIENT_MEASURE_INDEX]

    new_ingredient = {
            const.INGREDIENT_NAME: name,
            const.INGREDIENT_QUANTITY: float(quantity),
            const.INGREDIENT_MEASURE: measure
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
        with open(file_path, 'r', encoding="utf-8") as file:
            recipes = file.read().split("\n\n")

            for recipe in recipes:
                recipe_in_lines = recipe.split("\n")
                cook_book.update(CookBookParser.get_dish_recipe(recipe_in_lines))

        return cook_book



