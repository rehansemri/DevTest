from django import forms

class CsvFileForm(forms.Form):
    file = forms.FileField()
