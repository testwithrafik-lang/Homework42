from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'reminder']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'reminder': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
