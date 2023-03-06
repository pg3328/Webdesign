Introduction
This code implements a simple Flask application to retrieve a recipe based on ingredients entered by the user.
It uses the Spoonacular API to retrieve recipe information and the Nutrition by API Ninjas to retrieve nutritional information about the ingredients.
Further the application uses Number Conversion API to convert the number into words. 

Requirements
Before running the code, make sure you have the following:
A Flask environment setup
A RapidAPI account to access the Nutrition by API Ninjas API
A Spoonacular API key to access the Spoonacular API
Ensure that python is installed in the environment

Running the code
download the code as a zip file
Replace the RapidAPI key and Spoonacular API key in the appropriate places in the code
Run the following command in the terminal/command prompt : python nutrition.py else run the program in an IDE. 
Access the application in your browser at the URL http://127.0.0.1:5000/ 

Note: If the port in your system is blocked please update the port attribute (with the empty port) in app.run() function in driver main. 