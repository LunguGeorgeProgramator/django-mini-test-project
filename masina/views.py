from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Masini
from reprezentanta.models import Reprezentanta
from project01.helper import db_table_exists, validatorPost


def index(request):
    users = {}
    masini = {}
    reprezentante = {}
    if db_table_exists('auth_user'):
        users = User.objects.all()
    if db_table_exists('masina_masini'):
        masini = Masini.objects.all()
    if db_table_exists('reprezentanta_reprezentanta'):
        reprezentante = Reprezentanta.objects.all()
    return render(request, 'masina/masina_index.html', {
        'users': users,
        'masini': masini,
        'reprezentante': reprezentante
    })


def show(request, id):
    masina = Masini.objects.get(id=id)
    return render(request, 'masina/masina_show.html', {'masina': masina})


def edit(request, id):
    masina = Masini.objects.get(id=id)
    return render(request, 'masina/masina_edit_create.html', {'masina': masina, 'method': 'edit'})


def update(request, id):
    masina = Masini.objects.get(id=id)
    error_message, values = validatorPost(request, {
        'marca': 'required|string',
        'pret': 'required|number',
    })
    if error_message:
        return render(request, 'masina/masina_edit_create.html', {'masina': masina, 'error_message': error_message, 'values': values})
    masina.marca = values['marca']
    masina.pret = values['pret']
    masina.save()
    return redirect('show', id=id)


def create(request):
    return render(request, 'masina/masina_edit_create.html', {'method': 'create'})


def store(request):
    error_message, values = validatorPost(request, {
        'marca': 'required|string',
        'pret': 'required|number',
    })
    if error_message:
        return render(request, 'masina/masina_edit_create.html', {'error_message': error_message, 'values': values})
    masina = Masini(**values)
    masina.save()
    return redirect('show', id=masina.id)


def destroy(request, id):
    instance = Masini.objects.get(id=id)
    instance.delete()
    return redirect('index')