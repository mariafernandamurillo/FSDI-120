from django import forms
from .models import Event
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'time_picker' : TimeInput(), 
            'end_picker' : TimeInput(), 
            'date_picker': DateInput(),
            'thumbnail': forms.ClearableFileInput(attrs={'allow_multiple_selected':True}),
        }
    

