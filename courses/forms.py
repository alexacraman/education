
from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module, Content

ModuleFormSet = inlineformset_factory(
    Course, Module, fields=['title', 'description'], extra=2, can_delete=True, 
    widgets={
        'title': forms.TextInput(attrs={
        'class': 'mt-6 px-1 py-1.5 text-base font-normal w-full mx-auto border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
   
    }),
        'description': forms.Textarea(attrs={
        'class': ' px-3 py-1.5 text-base font-normal w-full mx-auto  border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
  
    }),
      
    }
)

# widgets={'name': forms.Textarea(attrs={'cols': 80, 'rows': 20})})