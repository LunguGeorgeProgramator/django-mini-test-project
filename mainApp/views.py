from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from masina.models import Masini
from reprezentanta.models import Reprezentanta
from recenzie.models import Recenzie
from mainApp.helper import db_table_exists, validatorPost


def index(request):
    if request.POST:
        print(request.POST)
    return render(request, 'home.html')