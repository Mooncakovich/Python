from .models import Note
from django.forms import ModelForm, TextInput, Textarea



class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "description"]
        widgets = {"title": TextInput(attrs={
            'class': 'note_input',
            'placeholder' : 'Enter note title'
        }),
        "description": Textarea(attrs={
            'class': 'note_input',
            'placeholder' : 'Enter note content'
        })
        }