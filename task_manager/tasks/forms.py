from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from django.contrib.auth.forms import AuthenticationForm as DefaultAuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'importance']
        widgets = {
            'title': forms.TextInput(attrs={'autocomplete': 'off', 'autofocus': 'true'}),
            'description': forms.Textarea(attrs={'autocomplete': 'off'}),
        }
        
class UserCreationForm(DefaultUserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'autofocus': 'true'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    
class AuthenticationForm(DefaultAuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'autofocus': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    
