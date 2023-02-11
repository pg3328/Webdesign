import requests

url = "https://ai-recipe-generator-from-inputed-available-products.p.rapidapi.com/"

querystring = {"text": "Rice, Chicken"}

headers = {
    "X-RapidAPI-Key": "9352f07c0amsha0c0c3ed26af01ep1bd280jsn231a9a34b6a6",
    "X-RapidAPI-Host": "ai-recipe-generator-from-inputed-available-products.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
phrase_tolist = response.text.split()
starting_index = 0
ending_index = 0
for i in range(len(phrase_tolist)):
    if phrase_tolist[i] == "Ingredients:":
        starting_index = i
    elif phrase_tolist[i] == "Instructions:":
        ending_index = i
        break
    else:
        continue
required_list = phrase_tolist[starting_index+1:ending_index]
ingredients  = ''.join(required_list)
print(ingredients)
