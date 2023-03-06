from flask import Flask, request, render_template

"""
    Flask imports to use flask framework for connecting front end to the back end
"""
import requests

"""
    Library to connect to the API 's
"""

import xml.etree.ElementTree as ET

"""
    Library used to update the payload as per the passed attribute.
"""

app = Flask(__name__)
"""
    Ensures that the flask is activated 
"""
"""
    Program that takes the input of raw material available and provides the information about the nearest possible 
    recipe that can be made using the ingredients mentioned. 
    @author : Pradeep Kumar Gontla. 
"""

@app.route("/recipe")
def recipe(available_ingredients):
    """
    generates the recipe based on ingredients passed. Used spoonacular api for recipe generation
    :param available_ingredients: ingredients retrieved from User Interface
    :return: the required display attributes in the form of a dictionary.
    """
    available_ingredients = available_ingredients.split(',')
    url = "https://api.spoonacular.com/recipes/findByIngredients"

    params = {
        "ingredients": available_ingredients,
        "number": 1,
        "apiKey": "5ef7a6bc2e324aaf87b6e27923c0594a"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            reci = data[0]
            title = reci.get("title")
            image = reci.get("image")
            usedIngredientCount = reci.get("usedIngredientCount")
            missedIngredientCount = reci.get("missedIngredientCount")
            missedIngredients = [ingredient.get("name") for ingredient in reci.get("missedIngredients", [])]
            calorie = nutrition(available_ingredients + missedIngredients)

            result = {"title": title, "image": image, "calories": calorie,
                      "calorie_in_words": convert_number_to_words(calorie),
                      "used_ingredient_Count": usedIngredientCount, "missed_ingredients_count": missedIngredientCount,
                      "missed_ingredients": missedIngredients}
            return result


def nutrition(ingredients):
    """
        Calculates the nutrition in the given food material uses nutrition API for nutritional information
    :param ingredients: list of ingredients for which the nutrition is calculated
    :return:overall calorie count in given ingredients

    """
    url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
    querystring = {"query": ingredients}
    headers = {
        "X-RapidAPI-Key": "ec55b003camshd61dfb0aac9f0b2p1b50a3jsn47d6d4860adf",
        "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Extract the calorie information from the response data
    response_data = response.json()
    calorie_list = [nutrient["calories"] for nutrient in response_data]

    # Calculate the sum of calories
    calorie_sum = sum(calorie_list)
    return calorie_sum


def convert_number_to_words(number):
    """
        Given a number the function calls in a SOAP API and returns the number in words.
    :param number: number for which the wording is needed.
    :return: Given number in words.
    """
    url = "https://number-conversion-service.p.rapidapi.com/webservicesserver/NumberConversion.wso"

    payload = f"""<?xml version='1.0' encoding='utf-8'?>
    <soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
      <soap:Body>
        <NumberToWords xmlns='http://www.dataaccess.com/webservicesserver/'>
          <ubiNum>{str(number)}</ubiNum>
        </NumberToWords>
      </soap:Body>
    </soap:Envelope>"""
    headers = {
        "content-type": "application/xml",
        "X-RapidAPI-Key": "ec55b003camshd61dfb0aac9f0b2p1b50a3jsn47d6d4860adf",
        "X-RapidAPI-Host": "number-conversion-service.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers).text
    root = ET.fromstring(response)
    result = root.find('.//{http://www.dataaccess.com/webservicesserver/}NumberToWordsResult').text
    return result


@app.route("/", methods=["GET", "POST"])
def home():
    """
        Starter function that calls the index html page which is then used to take the input.
    :return: renders the home html page.
    """
    if request.method == "POST":
        ingredients = request.form.get("ingredients")
        result = recipe(ingredients)
        return render_template("index.html", result=result)
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    """
        renders the html page that display the information about recipe.
    :return:  recipe page that displays the information.
    """
    ingredients = request.form.get("ingredients")
    res = recipe(ingredients)
    return render_template("recipe.html", result=res)


if __name__ == "__main__":
    """
        Driver for the program that starts the code. Port used is set to default port 5000
    """
    app.run(debug=True)
