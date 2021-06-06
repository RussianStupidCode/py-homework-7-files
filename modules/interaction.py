import modules.constants as const


def get_shop_list(dish_name, recipes):
    shop_list = {}

    for ingredient in recipes[dish_name]:
        ingredient_name = ingredient[const.INGREDIENT_NAME]
        ingredient_info = {
            const.INGREDIENT_MEASURE: ingredient[const.INGREDIENT_MEASURE],
            const.INGREDIENT_QUANTITY: ingredient[const.INGREDIENT_QUANTITY]
        }
        shop_list[ingredient_name] = ingredient_info

    return shop_list


def merge_shop_lists(destination, source):
    for key, value in source.items():
        if key in destination:
            destination[key][const.INGREDIENT_QUANTITY] += source[key][const.INGREDIENT_QUANTITY]
        else:
            destination[key] = source[key]


def shop_calc_for_persons(recipe, person_count):
    for ingredient in recipe:
        recipe[ingredient][const.INGREDIENT_QUANTITY] *= person_count
    return recipe


def get_shop_list_by_dishes(dish_names: list, person_count, recipes):
    result = {}
    for name in dish_names:
        shop_list = get_shop_list(name, recipes)
        merge_shop_lists(result, shop_list)
    return shop_calc_for_persons(result, person_count)


