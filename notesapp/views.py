from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_detail.html', {'form': form, 'note': note})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('home')
