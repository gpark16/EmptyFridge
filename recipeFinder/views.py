from django.shortcuts import render
from recipeFinder.forms import *
import json, requests

# Create your views here.

def index(request):
    context = {}
    breakpoint()
    if request.method != "POST":
        form = IngredientForm()
    else:
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data["ingredients"].split("\r\n")

            q = json.loads(f'{{"type":"public","app_id":"b6f42d6a","app_key":"78f8ad21c33293f28c088455dff177ae", "q":"{", ".join(ingredients)}"}}')
            response = requests.get("https://api.edamam.com/api/recipes/v2", params=q)

            #have immediately display title, link, and image
            #click to expand containing ingredients, health label, nutritional information
            #how to format expandable data
            #expand data when clicked on for the first time

            context["recipes"] = []
            for hit in response.json()['hits']:
                recipe = {
                    "title": hit["recipe"]["label"], 
                    "link": hit["recipe"]["url"], 
                    "image": hit["recipe"]["image"],
                    "ingredients": '<br>'.join([i['text'] for i in hit['recipe']['ingredients']]),
                    "nuts": "<br>".join([f"{n['label']} {n['quantity']/hit['recipe']['yield']:.1f}{n['unit']}" for n in hit['recipe']['totalNutrients'].values() if n['label'] in ['Energy', 'Total lipid (fat)', 'Carbohydrate, by difference', 'Protein']]),
                }
                context["recipes"].append(recipe)

    context["form"] = form

    return render(request, "recipeFinder/index.html", context)