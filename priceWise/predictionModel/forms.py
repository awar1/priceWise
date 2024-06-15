from django import forms

class ModelForm(forms.Form):
    rent = forms.IntegerField(label='Czynsz (jeśli nieznany zostawić puste)')
    size = forms.FloatField(label='Rozmiar (m^2)')
    no_of_rooms = forms.IntegerField(label='Liczba pokoi')
    year = forms.IntegerField(label='Rok budowy')
    dist_from_underground = forms.FloatField(label='odległość od metra (w km)')
    longitude = forms.FloatField(label='długość geograficzna')
    lattitude = forms.FloatField(label='szerokość geograficzna')
    height = forms.IntegerField(label='Ile pięter ma budynek (jeśli niewiadomo zostawić puste)')