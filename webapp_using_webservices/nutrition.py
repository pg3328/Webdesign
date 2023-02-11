import requests


def recipe(available_ingredients):
    url = "https://ai-recipe-generator-from-inputed-available-products.p.rapidapi.com/"

    querystring = {"text": available_ingredients}

    headers = {
        "X-RapidAPI-Key": "9352f07c0amsha0c0c3ed26af01ep1bd280jsn231a9a34b6a6",
        "X-RapidAPI-Host": "ai-recipe-generator-from-inputed-available-products.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def nutrition(ingredients):
    url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
    querystring = {"query": ingredients}
    headers = {
        "X-RapidAPI-Key": "ec55b003camshd61dfb0aac9f0b2p1b50a3jsn47d6d4860adf",
        "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def count_calories(list_of_calories):
    calories = 0
    for i in list_of_calories:
        calories += i["calories"]
    print(calories)


def getIngredients(recipe):
    phrase_to_list = recipe.split()
    starting_index = 0
    ending_index = 0
    for i in range(len(phrase_to_list)):
        if phrase_to_list[i] == "Ingredients:":
            starting_index = i
        elif phrase_to_list[i] == "Instructions:":
            ending_index = i
            break
        else:
            continue
    required_list = phrase_to_list[starting_index + 1:ending_index]
    ingredients = ' '.join(required_list)
    return ingredients


def main():
    recipes = """Chicken Fried Rice

Ingredients:

1 cup white rice

1 chicken breast, cooked and shredded

1/2 onion, chopped

1/2 green bell pepper, chopped

1/4 cup soy sauce

1/4 cup vegetable oil

2 eggs, beaten

Instructions:

1. Cook rice according to package instructions.

2. In a large skillet, heat oil over medium-high heat.

3. Add onion and bell pepper, and cook until softened, about 5 minutes.

4. Add chicken and cook for 5 more minutes.

5. Add cooked rice and soy sauce, and stir to combine.

6. Make a well in the center of the rice mixture, and add beaten eggs.

7. Cook, stirring constantly, until eggs are cooked through.

8. Serve immediately."""
    lists = [
        {"name": "white rice", "calories": 208.5, "serving_size_g": 158.0, "fat_total_g": 0.4, "fat_saturated_g": 0.1,
         "protein_g": 4.3, "sodium_mg": 1, "potassium_mg": 69, "cholesterol_mg": 0, "carbohydrates_total_g": 45.1,
         "fiber_g": 0.6, "sugar_g": 0.1},
        {"name": "chicken breast", "calories": 199.5, "serving_size_g": 120.0, "fat_total_g": 4.3,
         "fat_saturated_g": 1.2, "protein_g": 37.2, "sodium_mg": 87, "potassium_mg": 272, "cholesterol_mg": 102,
         "carbohydrates_total_g": 0.0, "fiber_g": 0.0, "sugar_g": 0.0},
        {"name": "onion", "calories": 44.7, "serving_size_g": 100.0, "fat_total_g": 0.2, "fat_saturated_g": 0.0,
         "protein_g": 1.4, "sodium_mg": 2, "potassium_mg": 35, "cholesterol_mg": 0, "carbohydrates_total_g": 10.1,
         "fiber_g": 1.4, "sugar_g": 4.7},
        {"name": "green bell pepper", "calories": 27.3, "serving_size_g": 100.0, "fat_total_g": 0.2,
         "fat_saturated_g": 0.0, "protein_g": 0.9, "sodium_mg": 1, "potassium_mg": 17, "cholesterol_mg": 0,
         "carbohydrates_total_g": 6.6, "fiber_g": 1.2, "sugar_g": 3.2},
        {"name": "soy sauce", "calories": 53.0, "serving_size_g": 100.0, "fat_total_g": 0.6, "fat_saturated_g": 0.1,
         "protein_g": 8.1, "sodium_mg": 5415, "potassium_mg": 167, "cholesterol_mg": 0, "carbohydrates_total_g": 4.8,
         "fiber_g": 0.8, "sugar_g": 0.4},
        {"name": "vegetable oil", "calories": 877.4, "serving_size_g": 100.0, "fat_total_g": 98.7,
         "fat_saturated_g": 7.4, "protein_g": 0.0, "sodium_mg": 0, "potassium_mg": 0, "cholesterol_mg": 0,
         "carbohydrates_total_g": 0.0, "fiber_g": 0.0, "sugar_g": 0.0},
        {"name": "eggs", "calories": 144.3, "serving_size_g": 100.0, "fat_total_g": 9.4, "fat_saturated_g": 3.1,
         "protein_g": 12.6, "sodium_mg": 143, "potassium_mg": 200, "cholesterol_mg": 373, "carbohydrates_total_g": 0.7,
         "fiber_g": 0.0, "sugar_g": 0.4}]
    count_calories(lists)
    # ingredients = getIngredients(recipes)
    # print(nutrition(ingredients))


#	ingredients = getIngredients(response)
#	nutrition()


if __name__ == '__main__':
    main()
