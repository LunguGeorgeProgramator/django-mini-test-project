from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from recenzie.models import Recenzie


class RecenzieForm(forms.ModelForm):

    masina = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

    autor = forms.CharField(
        required=False,
        max_length=25,
        label='Autor recenzie',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introduce un nume !!!'
            })
    )

    descriere = forms.CharField(
        required=False,
        max_length=255,
        label='Autor recenzie',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introduce o recenzie !!!'
            })
    )

    data_adaugari = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M:%S'],
        widget=forms.DateTimeInput(
            attrs={
            'class': 'form-control datepicker',
            'data-target': '#datetimepicker1'
        })
    )

    def clean_masina(self):
        masina = self.cleaned_data['masina']
        if masina is None or not masina.strip():
            raise ValidationError(_('Campul masina_id nu poate fi gol !!!'))
        return masina

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        if autor is None or not autor.strip():
            raise ValidationError(_('Campul autor nu poate fi gol !!!'))
        return autor

    def clean_descriere(self):
        descriere = self.cleaned_data['descriere']
        if descriere is None or not descriere.strip():
            raise ValidationError(_('Campul descriere nu poate fi gol !!!'))
        return descriere

    def clean_data_adaugari(self):
        data_adaugari = self.cleaned_data['data_adaugari']
        print(data_adaugari, timezone.now())
        if data_adaugari is None or not data_adaugari:
            raise ValidationError(_('Campul data adaugari nu poate fi gol !!!'))
        if data_adaugari > timezone.now():
            raise ValidationError(_('Data adaugari nu poate fi mai mare de azi !!!'))
        return data_adaugari

    class Meta:
        model = Recenzie
        fields = ('autor', 'descriere', 'data_adaugari')
