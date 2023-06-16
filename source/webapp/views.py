from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import randint

from webapp.cat_db import CatsDb

cat = CatsDb()


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        cat.name = request.POST.get('catname')
        return HttpResponseRedirect('/cat_stats')


def check_number():
    if cat.happiness > 100:
        cat.happiness = 100
    elif cat.happiness < 0:
        cat.happiness = 0

    if cat.satiety > 100:
        cat.satiety = 100
        cat.happiness -= 30
        if cat.happiness < 0:
            cat.happiness = 0
    elif cat.satiety < 0:
        cat.satiety = 0


def play():
    if cat.cat_state == 'sleep':
        cat.cat_state = 'awake'
        cat.happiness -= 5
        check_number()
    elif cat.cat_state == 'awake':
        fate_choice = randint(1, 3)
        if fate_choice != 2:
            cat.happiness += 15
            cat.satiety -= 10
            check_number()
        elif fate_choice == 2:
            cat.happiness = 0


def feed():
    if cat.cat_state == 'sleep':
        pass
    elif cat.cat_state == 'awake':
        cat.happiness += 5
        cat.satiety += 15
        check_number()


def change_cat_info(action):
    match action:
        case 'play':
            play()
        case 'feed':
            feed()
        case 'sleep':
            cat.cat_state = 'sleep'
    cat.get_img_path()


def cat_stats(request):
    if request.method == 'GET':
        cat_info = {
            'name': cat.name,
            'age': cat.age,
            'happiness': cat.happiness,
            'satiety': cat.satiety,
            'img': cat.img_path
        }
        return render(request, 'cat_stats.html', cat_info)
    elif request.method == 'POST':
        user_action = request.POST.get('action')
        change_cat_info(user_action)
        cat_info = {
            'name': cat.name,
            'age': cat.age,
            'happiness': cat.happiness,
            'satiety': cat.satiety,
            'img': cat.img_path
        }
        return render(request, 'cat_stats.html', cat_info)
