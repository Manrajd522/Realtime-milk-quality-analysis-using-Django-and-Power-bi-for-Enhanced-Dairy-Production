from django.forms import ModelForm
from django import forms
from datetime import date
from .import models


class DatePickerInput(forms.DateInput):
        input_type = 'date'



class UserForm(ModelForm):
    

    class Meta:
        model = models.User
        fields = '__all__'

class RecordForm(ModelForm):
    

    class Meta:
        model =models.Record
        fields = '__all__'
        widgets = {
            'Date' : DatePickerInput(),
            'user_id': forms.TextInput(attrs={'placeholder': 'Enter User ID'}),
        
        }

    