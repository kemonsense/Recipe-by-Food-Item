# Create your views here.
from django.shortcuts import render
import requests
from requests import get

from py_edamam import PyEdamam



def home(request, pk):

    e = PyEdamam(
    recipes_appid='87ab3c31',
    recipes_appkey='2a61168bcb042414e63f965bfa63a0be')

    for recipe in e.search_recipe(pk):
        context = {'recipe':recipe, 
        'recipe.calories':recipe.calories, 
        'recipe.cautions':recipe.cautions, 
        'recipe.dietLabels':recipe.dietLabels, 
        'recipe.healthLabels':recipe.healthLabels,
        'recipe.url':recipe.url,
        'recipe.ingredient_quantities':recipe.ingredient_quantities
        }

    return render(request, 'core/home.html', context)