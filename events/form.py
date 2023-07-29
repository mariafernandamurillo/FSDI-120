from django import forms
from .models import Event, Profile
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
            'start_time' : TimeInput(), 
            'end_time' : TimeInput(), 
            'date_picker': DateInput(),
            'thumbnail': forms.ClearableFileInput(attrs={'allow_multiple_selected':True}),
        }

# class UserForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         widgets = {
#             'profile': forms.ClearableFileInput(attrs={'allow_multiple_selected':True}),
#         }    

