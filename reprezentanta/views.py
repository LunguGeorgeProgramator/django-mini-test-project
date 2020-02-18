from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Reprezentanta
from project01.helper import db_table_exists, validatorPost


def index(request):
    users = {}
    if db_table_exists('auth_user'):
        users = User.objects.all()
    reprezentante = Reprezentanta.objects.all()
    return render(request, 'reprezentanta/reprezentanta_index.html', {'users': users, 'reprezentante': reprezentante})


def show(request, id):
    reprezentanta = Reprezentanta.objects.get(id=id)
    return render(request, 'reprezentanta/reprezentanta.html', {'reprezentanta': reprezentanta})


def edit(request, id):
    reprezentanta = Reprezentanta.objects.get(id=id)
    return render(request, 'reprezentanta/reprezentanta_edit_create.html', {'reprezentanta': reprezentanta, 'method': 'edit'})


def update(request, id):
    reprezentanta = Reprezentanta.objects.get(id=id)
    error_message, values = validatorPost(request, {
        'nume': 'required|string',
        'localitate': 'required|string',
    })
    if error_message:
        return render(request, 'masina/reprezentanta_edit_create.html', {'reprezentanta': reprezentanta, 'error_message': error_message, 'values': values})
    reprezentanta.marca = values['nume']
    reprezentanta.pret = values['localitate']
    reprezentanta.save()
    return redirect('show', id=id)


def create(request):
    return render(request, 'reprezentanta/reprezentanta_edit_create.html', {'method': 'create'})


def store(request):
    error_message, values = validatorPost(request, {
        'nume': 'required|string',
        'localitate': 'required|string',
    })
    if error_message:
        return render(request, 'reprezentanta/reprezentanta_edit_create.html', {'error_message': error_message, 'values': values})
    reprezentanta = Reprezentanta(**values)
    reprezentanta.save()
    return redirect('show', id=reprezentanta.id)


def destroy(request, id):
    reprezentanta = Reprezentanta.objects.get(id=id)
    reprezentanta.delete()
    return redirect('index')
