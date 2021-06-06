# -*- coding: utf-8 -*-
from modules.parser import CookBookParser


if __name__ == "__main__":
    cook_book = CookBookParser.read_recipes('./recipes.txt')
    for key in cook_book:
        print(key, cook_book[key])
