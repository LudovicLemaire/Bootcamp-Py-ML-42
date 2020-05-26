import sys
import datetime
from recipe import Recipe


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        error = 0
        if isinstance(name, str):
            self.name = name
        else:
            error = "Name must be a string."
        if isinstance(last_update, datetime.datetime):
            self.last_update = last_update
        else:
            error = "Last_update must be a datetime value."
        if isinstance(last_update, datetime.datetime):
            self.creation_date = creation_date
        else:
            error = "Creation_date must be a datetime value."
        test_dict = {'starter': 1, 'lunch': 2, 'dessert': 3}
        if isinstance(recipes_list, dict):
            if test_dict.keys() == recipes_list.keys():
                self.recipes_list = recipes_list
            else:
                error = "Recipes_list must be 'starter', 'lunch' or 'dessert'."
        else:
            error = "Recipes_list must be a Dictionary."

        if error:
            print("\x1b[0;31;40mError:\x1b[0m " + error)

    def get_number_of_recipe(self):
        i = 0
        """Print a recipe with the name `name` and return the instance"""
        for e in self.recipes_list.values():
            i += 1
        return i

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if isinstance(name, Recipe):
            for e in self.recipes_list.values():
                if e and isinstance(e, list):
                    for obj in e:
                        if obj == name:
                            print(obj)
                elif e and name == e:
                    print(e)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list.keys():
            return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            if self.recipes_list[recipe.recipe_type] is None:
                self.recipes_list[recipe.recipe_type] = [recipe]
            else:
                self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print(
                "{} is not an instance of class Recipe! "
                "No update has been done.".format(recipe))
