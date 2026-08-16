from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'salary']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description', 'rows': 5}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary', 'step': '0.01'}),
        }