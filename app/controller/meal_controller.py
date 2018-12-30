from flask import request
from flask.json import jsonify

from app.models.meal import Meal
from app.models.user import User
from attrdict import AttrDict
from mongoengine.errors import DoesNotExist
from mongoengine.queryset import QuerySet
from config import Config
from flask_api import status
from dateutil import tz
from datetime import datetime, timedelta

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

'''
/* Assign Meals to the user 
        - User's food preferences
        - User's Medical Condition
        - User's Timezone/Meal plan reset in 24H period

        - Meal Selection depending on the course - No Logic provided (Pending)
        - Meals limit - Total 15
        - For Vegetarian: Random Selection of Vegan + Vegetarian
        - For Non-Vegetarian - 5 Veg + Vegan (Random Selection) + 10 Non-Vegetarian
    
    */
'''

def getMeals(userId):
    try:
        user = User.objects(id=userId).get()
        newMealsFlag = False
        if user and user['mealExpiry']:
            ''' Check for meal plan expiry'''
            tzinf = tz.tz.tzoffset('TZONE', int(user['timeZone'])/1000)  # creating the user's timezone by
                                                                        # timezone offset
            localCurrentTime = datetime.now(tz=tzinf)  # creating local time

            # Check if meal plan has expired
            if localCurrentTime > user['mealExpiry']:
                newMealsFlag = True
            else:
                try:
                    meals = Meal.objects(id__in=user['mealAssigned'])
                except Exception as e:
                    print(format(e))
                    return jsonify({'stat':'Some error occurred'}),500
        else:
            newMealsFlag = True
        if newMealsFlag:
                    # User's medical condition consideration - Check 2
            usersMedicalCondition = user['medicalCondition']
            # Meal Preference Counts initialize
            foodPref = []
            vegLimit = 15
            nonVegLimit = 0
            if user['foodPreference'] is 'Vegan':
                foodPref = ['Vegan']
            elif user['foodPreference'] is 'Vegetarian':
                foodPref = ['Vegan','Vegetarian']
            else:
                foodPref = ['Vegan','Vegetarian']
                vegLimit = 5
                nonVegLimit = 10

            # Query Array Initialize
            vegQuery = Meal.objects(id__nin=user['mealAssigned'],foodPreference__in=foodPref,
                                    avoidableMedCond__nin=usersMedicalCondition)[:vegLimit]
            if user['foodPreference'] == 'Non-Vegetarian':
                nonVegQuery = Meal.objects(id__nin=user['mealAssigned'],foodPreference__in=['Non-Vegetarian'],
                                           avoidableMedCond__nin=usersMedicalCondition)[:nonVegLimit]
                res = (list(vegQuery) + list(nonVegQuery))
            else:
                res = vegQuery

            ''' Assigning generated plan to the user '''
            tzinf = tz.tz.tzoffset('TZONE', int(user['timeZone'])/1000)
            localCurrentTime = datetime.now(tz=tzinf)
            expiryTime = localCurrentTime + timedelta(days=1)
            user['mealExpiry'] = expiryTime.replace(hour=5, minute=0, second=0, microsecond=0, tzinfo=tzinf)
            user['mealAssigned'] = res
        user.save()
        return jsonify(user['mealAssigned']),200
    except Exception as e:
        return format(e),500



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
