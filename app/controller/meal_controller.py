from flask import request
from flask.json import jsonify

from app.models.meal import Meal
from app.models.user import User
from attrdict import AttrDict
from mongoengine.errors import DoesNotExist
from mongoengine.queryset import QuerySet
from config import Config
from flask_api import status

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
            course=data.course,
            calories=data.calories,
            nutritionInfo=data.nutritionInfo,
            ingredients=data.ingredients,
            directions=data.directions,
            photoURL=Config.s3URL + data.photoURL
        ).save()
        return jsonify(newMeal)
    except NotUniqueError:
        return 'Meal already exists.', status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return 'Error while saving meal - {}'.format(e), status.HTTP_500_INTERNAL_SERVER_ERROR


''' /* Add Meals in bulk '''


def addMealData():
    meals_array = request.get_json()
    queryList = []
    for meal in meals_array:
        try:
            meal = Meal.objects.get(name=meal['name'])
        except DoesNotExist as dne:
            data = AttrDict(meal)
            newMeal = Meal(
                name=data.name,
                foodPreference=data.foodPreference,
                cuisine=data.cuisine,
                dietType=[dt for dt in data.dietType],
                idealMedCond=[imc for imc in data.idealMedCond],
                avoidableMedCond=[amc for amc in data.avoidableMedCond],
                course=data.course,
                calories=data.calories,
                nutritionInfo=data.nutritionInfo,
                ingredients=data.ingredients,
                directions=data.directions,
                photoURL=Config.s3URL + data.photoURL
            )
            queryList.append(newMeal)
    try:
        meals = Meal.objects.insert(queryList, load_bulk=True)
        return jsonify(meals), status.HTTP_200_OK
    except Exception as e:
        print(e.with_traceback())
        return format(e.with_traceback()), status.HTTP_400_BAD_REQUEST


def getMeals():
    pass  # todo check with Bala


def filterMeals():
    pass  # todo check with Bala


def getMealsList():
    return jsonify(Meal.objects)


def updateMeal(meal_id):
    data = AttrDict(request.get_json())

    try:
        updatedMeal = Meal.objects(id=meal_id).update_one(
            name=data.name,
            foodPreference=data.foodPreference,
            cuisine=data.cuisine,
            dietType=[dt for dt in data.dietType],
            idealMedCond=[imc for imc in data.idealMedCond],
            avoidableMedCond=[amc for amc in data.avoidableMedCond],
            course=data.course,
            calories=data.calories,
            nutritionInfo=data.nutritionInfo,
            ingredients=data.ingredients,
            directions=data.directions,
            photoURL=data.photoURL
        )
        return updatedMeal
    except Exception as e:
        return 'Unable to update meal - {}'.format(e), status.HTTP_500_INTERNAL_SERVER_ERROR


def deleteMeal(meal_id):
    try:
        delMeal = Meal.objects(id=meal_id).get()
        delMeal.delete()
        return jsonify({'status':'Meal deleted successfully'}), status.HTTP_200_OK
    except DoesNotExist as dne:
        return 'Meal not found - {}'.format(dne.with_traceback), status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return format(e.with_traceback()), status.HTTP_500_INTERNAL_SERVER_ERROR
