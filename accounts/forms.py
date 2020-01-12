from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ('first_name',
                  'middle_name',
                  'last_name', 
                  'id_num',
                  'born',
                  'died',
                  'house_num',
                  'street_name',
                  'town',
                  'city',
                  'province',
                  'zip_code',
                  
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'born': forms.NumberInput(attrs={'class': 'form-control'}),
            'died': forms.NumberInput(attrs={'class': 'form-control'}),
            'house_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'street_name': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control'}),
        }
