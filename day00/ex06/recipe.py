import sys

cookbook = {
    'sandwich': {
        'ingredients': ["ham", "bread", "cheese", "tomatoes"],
        'meal': "lunch",
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ["flour", "sugar", "eggs"],
        'meal': "dessert",
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
        'meal': "lunch",
        'prep_time': 15,
    }
}


def isNb(value):
    try:
        int(value)
        return True
    except Exception:
        return False


def printCookbook():
    for recipe, v in cookbook.items():
        getRecipe(recipe)
    main()


def getRecipe(name, end=False):
    print("")
    if name in cookbook:
        print(
            "Recipe for {}:\
            \nIngredients list: {}\
            \nTo be eaten for {}.\
            \nTakes {} minutes of cooking.\
            ".format(
                name, cookbook[name]["ingredients"],
                cookbook[name]["meal"],
                cookbook[name]["prep_time"]))
    else:
        print(name + " doesn't exist.")
    if end is True:
        main()


def delRecipe(name):
    if name in cookbook:
        del cookbook[name]
        print(name + " has been deleted.")
    else:
        print(name + " doesn't exist.")
    main()


def addRecipe(name, ingredients, meal, prep_time):
    newRecipe = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    cookbook[name] = newRecipe
    main()


def main():
    print("\n")
    option = input(
        "Please select an option by typing the corresponding number:\n" +
        "1: Add a recipe\n" +
        "2: Delete a recipe\n" +
        "3: Print the recipe\n" +
        "4: Print the cookbook\n" +
        "5: Quit\n" +
        "Option: ")
    print("")
    if option == "1":
        name = input("What is the Name of the recipe ? ")
        ingredients = input(
            "What is the Ingredients of the recipe ?"
            " (seperate with coma ', ') ")
        meal = input("What is the Meal of the recipe ? ")
        prep_time = input(
            "What is the Preparation Time of the recipe ?"
            " (en chiffre)")
        if (not name or not ingredients or not meal or not prep_time):
            print("A value is empty.")
            main()
        elif isNb(prep_time) is False:
            print("Preparation Time must be an integer.")
            main()
        else:
            ingredients = ingredients.split(", ")
            addRecipe(name, ingredients, meal, prep_time)
    elif option == "2":
        name = input("Please enter the recipe's name you want to delete: ")
        delRecipe(name)
    elif option == "3":
        name = input("Please enter the recipe's name to get its details: ")
        getRecipe(name, True)
    elif option == "4":
        printCookbook()
    elif option == "5":
        print("Cookbook closed.")
        sys.exit()
    else:
        print(
            "This option does not exist, please type "
            "the corresponding number.\nTo exit, enter 5.")
        main()


if __name__ == "__main__":
    main()
