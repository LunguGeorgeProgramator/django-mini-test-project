from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Reprezentanta
from masina.models import Masini
from project01.helper import db_table_exists, validatorPost


def index(request):
    return render(request, 'reprezentanta/reprezentanta_index.html', {
        'reprezentante': Reprezentanta.objects.all()
    })


def show(request, id):
    reprezentanta = Reprezentanta.objects.get(id=id)
    return render(request, 'reprezentanta/reprezentanta_show.html', {
        'reprezentanta': reprezentanta,
        'masini': reprezentanta.masini_set.all()
    })


def edit(request, id):
    return render(request, 'reprezentanta/reprezentanta_edit_create.html', {
        'reprezentanta': Reprezentanta.objects.get(id=id),
        'method': 'edit',
        'masini': Masini.objects.filter(reprezentanta_id__isnull=True)
    })


def update(request, id):
    reprezentanta = Reprezentanta.objects.get(id=id)
    error_message, values = validatorPost(request, {
        'nume': 'required|string',
        'localitate': 'required|string',
    })
    if error_message:
        return render(request, 'reprezentanta/reprezentanta_edit_create.html', {
            'reprezentanta': reprezentanta,
            'error_message': error_message,
            'values': values
        })
    reprezentanta.nume = values['nume']
    reprezentanta.localitate = values['localitate']
    reprezentanta.save()
    for masina_id in request.POST.getlist('masini'):
        m = Masini.objects.get(id=masina_id)
        m.reprezentanta = reprezentanta
        m.save()
    if 'sterge_masinile' in request.POST and 'true' in request.POST['sterge_masinile']:
        reprezentanta.masini_set.all().delete()

    return redirect('reprezentanta_show', id=reprezentanta.id)


def create(request):
    return render(request, 'reprezentanta/reprezentanta_edit_create.html', {
        'method': 'create'
    })


def store(request):
    error_message, values = validatorPost(request, {
        'nume': 'required|string',
        'localitate': 'required|string',
    })
    if error_message:
        return render(request, 'reprezentanta/reprezentanta_edit_create.html', {
            'error_message': error_message,
            'values': values
        })
    reprezentanta = Reprezentanta(**values)
    reprezentanta.save()
    return redirect('reprezentanta_show', id=reprezentanta.id)


def destroy(request, id, masini_true=None):
    reprezentanta = Reprezentanta.objects.get(id=id)
    reprezentanta.delete()
    return redirect('reprezentanta_index')
