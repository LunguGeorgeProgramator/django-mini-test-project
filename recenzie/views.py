from django.shortcuts import render, redirect
from recenzie.forms import RecenzieForm
from django.http import JsonResponse
from recenzie.models import Recenzie
from masina.models import Masini


def index(request):
    data_to_return = []
    for recenzie in Recenzie.objects.all():
        data = {}
        for key in ['autor', 'descriere', 'data_adaugari', 'masina']:
            if key is 'masina':
                data[key] = {
                    'id': recenzie.masina.id,
                    'marca': recenzie.masina.marca
                } if recenzie.masina else {}
            else:
                data[key] = getattr(recenzie, key)
        if data:
            data_to_return.append(data)
    return JsonResponse(list(data_to_return), safe=False)


def create(request, masina_id):
    heading_message = 'Formset Demo'
    if request.method == 'POST':
        form_recenzie = RecenzieForm(request.POST)
        if form_recenzie.is_valid():
            Recenzie(
                masina=Masini.objects.get(id=masina_id),
                autor=form_recenzie.cleaned_data.get('autor'),
                descriere=form_recenzie.cleaned_data.get('descriere'),
                data_adaugari=form_recenzie.cleaned_data.get('data_adaugari'),
            ).save()
            return redirect('masina_show', id=masina_id)
    else:
        form_recenzie = RecenzieForm(request.GET or None, initial={'masina': masina_id})

    return render(request, 'recenzie/recenzie_create.html', {
        'form_recenzie': form_recenzie,
        'method': 'creare',
        'masina_id': masina_id
    })


def edit(request, id):
    heading_message = 'Formset Demo'
    recenzie = Recenzie.objects.get(id=id)
    form_recenzie = RecenzieForm(request.POST or None, instance=Recenzie.objects.get(id=id), initial={
        'masina': recenzie.masina.id,
        'data_adaugari': recenzie.data_adaugari.strftime('%d/%m/%Y %H:%M:%S')
    })
    if form_recenzie.is_valid():
        recenzie.autor = form_recenzie.cleaned_data.get('autor')
        recenzie.descriere = form_recenzie.cleaned_data.get('descriere')
        recenzie.data_adaugari = form_recenzie.cleaned_data.get('data_adaugari')
        recenzie.save()
        return redirect('masina_show', id=recenzie.masina.id)

    return render(request, 'recenzie/recenzie_create.html', {
        'form_recenzie': form_recenzie,
        'method': 'editare',
        'masina_id': recenzie.masina.id
    })


def destroy(request, id, redirect_to=None):
    recenzie = Recenzie.objects.get(id=id)
    recenzie.delete()
    return redirect('masina_show', id=redirect_to)
