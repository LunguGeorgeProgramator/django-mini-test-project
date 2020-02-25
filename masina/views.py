from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Masini
from reprezentanta.models import Reprezentanta
from recenzie.models import Recenzie
from mainApp.helper import db_table_exists, validatorPost


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
    return render(request, 'masina/masina_show.html', {
        'masina': masina,
        'recenzii': masina.recenzie_set.all()
    })


def edit(request, id):
    masina = Masini.objects.get(id=id)
    return render(request, 'masina/masina_edit_create.html', {'masina': masina, 'method': 'edit', 'reprezentanta_id': masina.reprezentanta_id})


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
    return redirect('masina_show', id=id)


def create(request, reprezentanta_id=None):
    return render(request, 'masina/masina_edit_create.html', {'method': 'create', 'reprezentanta_id': reprezentanta_id})


def store(request):
    error_message, values = validatorPost(request, {
        'marca': 'required|string',
        'pret': 'required|number',
        # 'reprezentanta_id': 'required|number'
        'reprezentanta_id': ''
    })
    if error_message:
        return render(request, 'masina/masina_edit_create.html', {'error_message': error_message, 'values': values})
    if values['reprezentanta_id'] is not None and values['reprezentanta_id'] != 'None':
        values['reprezentanta'] = Reprezentanta.objects.get(id=values['reprezentanta_id'])
    del values['reprezentanta_id']
    masina = Masini(**values)
    masina.save()
    return redirect('masina_show', id=masina.id)


def destroy(request, id):
    instance = Masini.objects.get(id=id)
    instance.delete()
    return redirect('masina_index')
