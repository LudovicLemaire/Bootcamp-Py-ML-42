from book import Book
from recipe import Recipe
import datetime

salad = Recipe(
    name='Salad', cooking_lvl=1, cooking_time=10,
    ingredients=['salad', 'Tomato', 'Ham'],
    description='A delicious salad.', recipe_type='lunch')
flan = Recipe(
    name='Flan', cooking_lvl=2, cooking_time=30,
    ingredients=['egg', 'milk', 'butter'],
    description='A delicious flan.', recipe_type='dessert')
choco = Recipe(
    name='Flanchoco', cooking_lvl=2, cooking_time=35,
    ingredients=['egg', 'milk', 'butter', 'chocolate'],
    description='A delicious flan au chocolat.', recipe_type='dessert')
Shouldnotwork = 'Shouldnotwork'

rcp_dict = dict.fromkeys(['starter', 'lunch', 'dessert'])
my_book = Book(name="Benji's book", last_update=datetime.datetime.now(),
               creation_date=datetime.datetime.now(), recipes_list=rcp_dict)
my_book.add_recipe(salad)
my_book.add_recipe(flan)
my_book.add_recipe(choco)

nb_recipe = my_book.get_number_of_recipe()
print('There is currently {} recipes. Next one wont work.'.format(nb_recipe))
my_book.add_recipe(Shouldnotwork)
nb_recipe = my_book.get_number_of_recipe()

print('There is currently {} recipes.'.format(nb_recipe))
print()
print('---- Recipe for flan ----')
my_book.get_recipe_by_name(flan)
print('\n---- Recipe for salad ----')
my_book.get_recipe_by_name(salad)

print('\n---- Starter recipes ----')
starter_list = my_book.get_recipes_by_types('starter')
if starter_list is not None:
    if isinstance(starter_list, list):
        for elem in starter_list:
            print("\n" + str(elem))
    else:
        print(str(starter_list))

print('\n---- Lunch recipes ----')
lunch_list = my_book.get_recipes_by_types('lunch')
if lunch_list is not None:
    if isinstance(lunch_list, list):
        for elem in lunch_list:
            print("\n" + str(elem))
    else:
        print(str(lunch_list))

print('\n---- Dessert recipes ----')
dessert_list = my_book.get_recipes_by_types('dessert')
if dessert_list is not None:
    if isinstance(dessert_list, list):
        for elem in dessert_list:
            print("\n" + str(elem))
    else:
        print(str(dessert_list))
