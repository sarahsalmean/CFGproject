import requests

# imported the requests library and declared the API's user ID and app key.
# Declared app id and app key variables to be used as API parameters

app_id = 'f8807375'
app_key = 'f60da4fd40fabfac4e4df2fd0aa19016'

add_app_id = "app_id={}".format(app_id)
add_app_key = "app_key={}".format(app_key)

# Declared diet restriction and meal type examples to be used in the search
diet_restrictions_options = ['vegetarian', 'vegan', 'paleo', 'gluten-free', 'fodmap-free']
meal_types_options = ['breakfast', 'lunch', 'snack', 'dinner']

# Welcome message

print('\n')
print('Welcome to our recipe search project! Enter your ingredients below and happy cooking!')


# This function asks the user to enter the chosen ingredients and returns the user's input as a variable.
def ingredients_choice():
    print("Which ingredients would you like to use today?")
    ingredient = input('Add as many as you like, and separate them using spaces, for example "milk eggs cheese":')
    while ingredient == "":
        ingredient = input(f"You must enter at least one ingredient. Try again: ")
    elements = ingredient.split()
    chosen_items = "+".join(elements)
    display_items = " + ".join(elements)

    print("\nYou have chosen: " + display_items)
    add_ingredients = "q={}".format(chosen_items)
    return add_ingredients


# Function to determine if the user has any diet restrictions and return the input as a variable.
def diet_choice():
    diet_restrictions = input(
        f"\nSpecify a diet restriction or type 'N' if you don't mind \n{diet_restrictions_options}")
    while diet_restrictions in diet_restrictions_options:
        add_diet_restrictions = 'health={}'.format(diet_restrictions)
        return add_diet_restrictions
    while (diet_restrictions != "N" and diet_restrictions != "n") and (
            diet_restrictions not in diet_restrictions_options):
        diet_restrictions = input(
            f"\nInvalid response. Try again or type 'N' if you don't mind: \n{diet_restrictions_options}: ")
        while diet_restrictions in diet_restrictions_options:
            add_diet_restrictions = 'health={}'.format(diet_restrictions)
            return add_diet_restrictions
        else:
            print('\nError, try again!')


# Function that asks the meal type of preference (if any).
def meal_choice():
    meal_types = input(
        f"\nChoose a meal type from the options below or type 'N' if you don't mind. \n{meal_types_options}")
    while meal_types in meal_types_options:
        add_meal_types = 'mealType={}'.format(meal_types)
        return add_meal_types
    while (meal_types != "N") and (meal_types not in meal_types_options):
        meal_types = input(
            f"Invalid response. Try again or type 'N' if you don't mind: \n{meal_types_options}: ")
        while meal_types in meal_types_options:
            add_meal_types = 'mealType={}'.format(meal_types)
            return add_meal_types
        else:
            print('\nError, start again!')

# Storing the three functions in variables
ingredients_url = ingredients_choice()
diet_restrictions_url = diet_choice()
meal_types_url = meal_choice()

# print(ingredients_url)
# print(diet_restrictions_url)
# print(meal_types_url)

# Using the variables to construct the API request URL and make the GET request.

url = 'https://api.edamam.com/search?{}&{}&{}&{}&{}'.format(add_app_id, add_app_key, ingredients_url,
                                                            diet_restrictions_url, meal_types_url)

# The resulting recipe data is returned in a JSON format and can be parsed and used as desired.
# Extract the recipes from the API and prints the results
results = requests.get(url)
data = results.json()
results = data['hits']
for result in results:
    recipe = result['recipe']
    print(recipe['label'])
    print(recipe['url'])
    print()

# This allows the user to specific whether they would like to save their recipes list, or start a new search
next_choice = input(
    "If you would like to save these recipes, enter 'save'. To search using other ingredients, enter 'search'")

# This takes the user back to the ingredient input stage
if next_choice == "search":
    ingredients_choice()
    diet_choice()
    meal_choice()
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print()

# This saves the search results ina new file on the user's computer
if next_choice == "save":
    print("Thank you for saving! Your recipe list will appear in your downloads folder.")
    import sys

    with open("recipes_list.txt", 'w') as sys.stdout:
        for result in results:
            recipe = result['recipe']
            print(recipe['label'])
            print(recipe['url'])
            print()

else:
    print("Thank you for searching, enjoy your meal!")
