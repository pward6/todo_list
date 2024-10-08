from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['task', 'completed', 'notes', 'goal']
        widgets = {
            'goal': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
