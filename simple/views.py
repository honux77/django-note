from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Note

def hello(request):
    return render(request, 'simple/hello.html', {})

def note(request):
    notes = Note.objects.all().order_by('-published_date')
    return render(request, 'simple/note.html', {'notes': notes})

class Write(CreateView):
    model = Note
    fields = ['name', 'text']
    success_url = reverse_lazy('note')