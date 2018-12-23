from flask import request
from flask.json import jsonify

from app.models.meal import Meal
from app.models.user import User

from config import Config

from mongoengine import NotUniqueError


def addNewMeal():
    data = AttrDict(request.get_json())

    try:
        newMeal = Meal(
            name=data.name, 
            foodPreference=data.foodPreference,
            cuisine=data.cuisine, 
            dietType=[dt for dt in data.dietType],
            idealMedCond=[imc for imc in data.idealMedCond], 
            avoidableMedCond=[amc for amc in data.avoidableMedCond],
            course = data.course,
            calories = data.calories,
            nutritionInfo = data.nutritionInfo,
            ingredients = data.ingredients,
            directions = data.directions,
            photoURL = data.photoURL
        ).save()

        return jsonify(newMeal)
    except NotUniqueError:
        return 'Meal already exists.'
    except Exception as e:
        return 'Error while saving meal - {}'.format(e), 400

def addMealData():
    pass #todo check with Bala

def getMeals():
    pass #todo check with Bala

def filterMeals():
    pass #todo check with Bala

def getMealsList():
    return jsonify(Meal.objects)

def updateMeal(id):
    data = AttrDict(request.get_json())

    try:
        updatedMeal = Meal.objects(id=id).update_one(
            name=data.name, 
            foodPreference=data.foodPreference,
            cuisine=data.cuisine, 
            dietType=[dt for dt in data.dietType],
            idealMedCond=[imc for imc in data.idealMedCond], 
            avoidableMedCond=[amc for amc in data.avoidableMedCond],
            course = data.course,
            calories = data.calories,
            nutritionInfo = data.nutritionInfo,
            ingredients = data.ingredients,
            directions = data.directions,
            photoURL = data.photoURL
        )

        return updatedMeal
    except Exception as e:
        return 'Unable to update meal - {}'.format(e)
    

def deleteMeal(id):
    try:
        delMeal = Meal.objects(id=id)
        
        if delMeal:
            delMeal = delMeals.delete()
            return jsonify(delMeals)
        else:
            return 'Meals not deleted', 400
    except Exception as e:
        return 'Unable to delete meals - {}'.format(e)


def implicitEndTest():
    pass #todo check with Bala
