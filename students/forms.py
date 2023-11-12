
from django import forms
from courses.models import Course

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'bg-red-900'}))
    subject =forms.CharField(widget=forms.TextInput)
    message = forms.CharField(widget=forms.Textarea)