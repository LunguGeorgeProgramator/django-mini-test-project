from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Masini
from .helper import db_table_exists, validatorPost


def index(request):
    users = {}
    if db_table_exists('auth_user'):
        users = User.objects.all()
    return render(request, 'webapp/index.html', {'users': users})


def show(request):
    masini = Masini.objects.all()
    return render(request, 'webapp/show.html', {'pass_var': "Yep", 'masini': masini})


def edit(request, id):
    masina = Masini.objects.get(id=id)
    return render(request, 'webapp/form.html', {'masina': masina})


def update(request, id):
    masina = Masini.objects.get(id=id)
    error_message, values = validatorPost(request, {
        'marca': 'required|string',
        'pret': 'required|number',
    })
    if error_message:
        return render(request, 'webapp/form.html', {'masina': masina, 'error_message': error_message, 'values': values})
    masina.marca = values['marca']
    masina.pret = values['pret']
    masina.save()
    return redirect('show')


def create(request):
    return render(request, 'webapp/form.html')


def store(request):
    error_message, values = validatorPost(request, {
        'marca': 'required|string',
        'pret': 'required|number',
    })
    if error_message:
        return render(request, 'webapp/form.html', {'error_message': error_message, 'values': values})
    masina = Masini(**values)
    masina.save()
    return redirect('show')


def destroy(request, id):
    instance = Masini.objects.get(id=id)
    instance.delete()
    return redirect('show')
