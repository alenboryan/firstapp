from .models import Addinfo
from django.forms import ModelForm ,TextInput, DateTimeInput
from django import forms

class AddinfoForm(ModelForm):
    class Meta:
        model = Addinfo
        fields = ['title', 'anons', 'date']
        
        widgets = {
            "title":TextInput(attrs={
                'class':'form_control',
                'placeholder':'Name'
            } ),
            "anons":TextInput(attrs={
                'class':'form_control',
                'placeholder':'Info'
            } ),
            "date":DateTimeInput(attrs={
                'class':'form_control',
                'placeholder':'Date'
            } )
        }
