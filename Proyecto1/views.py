from django.http import HttpResponse
from django.template.loader import render_to_string
from Organizador.models import Note
from datetime import datetime
from django.template import RequestContext
from django.template import *
from django.http import *
from django.template import *
from django.shortcuts import *

def list_notes(request):
    return render(request, 'notes.html', { 'notes': Note.objects.all() })
    

def new_note(request):
    if request.method == "POST":
        note = Note(title = request.POST.get("title", "New Note"), text = request.POST.get("text", "..."), color = request.POST.get("color", "#FFF"), date = datetime.now())
        note.save()
        return redirect(list_notes)


    return render(request,'new_note.html')

def delete_note(request,id):
    if request.method == "POST":
        Note.objects.filter(id=id).delete()

    return redirect(list_notes)