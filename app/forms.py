from django import forms
from .models import UserInput


class InputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ('height', 'weight', 'age', 'position', 'attributes')
        widgets = {
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'attributes': forms.TextInput(attrs={'class': 'form-control'}),
        }