import re
from django.shortcuts import render
from .forms import NoteForm
from .models import Note


def Main_Page(request):
    return render(request, "main/Main.html")

def Add_Note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
    form = NoteForm()
    context = {
        'form' : form
    }
    return render(request, "main/AddNote.html", context)

def Check_Note(request):
    notes = Note.objects.all()
    return render(request, "main/Notes.html", {'notes' : notes})