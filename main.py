# -*- coding: utf-8 -*-
from modules.parser import CookBookParser
from modules.interaction import get_shop_list_by_dishes
from modules.filesmerge import files_merge


if __name__ == "__main__":
    cook_book = CookBookParser.read_recipes('./recipes.txt')
    for key in cook_book:
        print(key)
        for ingredient in cook_book[key]:
            print(f'\t{ingredient}')

    print()

    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
    for key in shop_list:
        print(key, shop_list[key])

    files_merge('./files', './result_file.txt')
