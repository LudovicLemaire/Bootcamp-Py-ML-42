import sys


def isNb(value):
    try:
        int(value)
        return True
    except Exception:
        return False


class Recipe:
    def __init__(
            self,
            name,
            cooking_lvl,
            cooking_time,
            ingredients,
            description,
            recipe_type):
        error = 0
        if not name:
            error = "Name can't be empty."
        if isNb(cooking_lvl) is False:
            error = "Level must be an integer."
        cooking_lvl = int(cooking_lvl)
        if cooking_lvl < 1 or cooking_lvl > 5:
            error = "Level must be between 1 and 5."
        if isNb(cooking_time) is False:
            error = "Time must be an integer."
        cooking_time = int(cooking_time)
        if cooking_time < 0:
            error = "Time must be positive."
        if not ingredients:
            error = "There must be at least one ingredient."
        if recipe_type == "starter" or recipe_type == "lunch"\
                or recipe_type == "dessert":
            pass
        else:
            error = "Type must be 'starter', 'lunch' or 'dessert'."

        if error:
            print("\x1b[0;31;40mError:\x1b[0m " + error)
            sys.exit()

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return(
            "\x1b[0;36;40mRecipe name:\x1b[0m {}\n"
            "\x1b[0;36;40mLevel:\x1b[0m {}\n"
            "\x1b[0;36;40mTime:\x1b[0m {}\n"
            "\x1b[0;36;40mIngredients:\x1b[0m {}\n"
            "\x1b[0;36;40mDescription:\x1b[0m {}\n"
            "\x1b[0;36;40mType:\x1b[0m {}".format(
                self.name,
                self.cooking_lvl,
                self.cooking_time,
                ', '.join(self.ingredients),
                self.description,
                self.recipe_type))
