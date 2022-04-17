from django.http import HttpResponse
from django.template.loader import render_to_string
from Organizador.models import Home, Note, Meeting, Task
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

def delete_note(request, id):
    if request.method == "POST":
        Note.objects.filter(id = id).delete()

    return redirect(list_notes)

def edit_note(request, id):
    if request.method == "POST":
        note = Note.objects.get(id = id)
        note.title = request.POST.get("title", "New Note")
        note.text = request.POST.get("text", "...")
        note.color = request.POST.get("color", "#FFF")
        note.date = datetime.now()

        note.save()


    return redirect(list_notes)

def list_meetings(request):
    return render(request, 'meetings.html', { 'meetings': Meeting.objects.all() })
    

def new_meeting(request):
    if request.method == "POST":
        meeting = Meeting(
            title = request.POST.get("title", "New Meeting"),
            description = request.POST.get("description", "..."),
            place = request.POST.get("place", "Remote"),
            date = datetime.strptime(request.POST.get("date"), '%Y-%m-%dT%H:%M')
        )
        meeting.save()
        return redirect(list_meetings)


    return render(request,'new_meeting.html')

def delete_meeting(request, id):
    if request.method == "POST":
        Meeting.objects.filter(id = id).delete()

    return redirect(list_meetings)

def edit_meeting(request, id):
    if request.method == "POST":
        meeting = Meeting.objects.get(id = id)
        meeting.title = request.POST.get("title", "New Meeting")
        meeting.description = request.POST.get("description", "...")
        meeting.place = request.POST.get("place", "Remote")
        meeting.date = datetime.strptime(request.POST.get("date"), '%Y-%m-%dT%H:%M')

        meeting.save()


    return redirect(list_meetings)

def list_task(request):
    return render(request, 'task.html', { 'task': Task.objects.all() })
    

def new_task(request):
    if request.method == "POST":
        task = Task(title = request.POST.get("title", "New Task"), text = request.POST.get("text", "..."), color = request.POST.get("color", "#FFF"), date = datetime.now())
        task.save()
        return redirect(list_task)


    return render(request,'new_task.html')

def delete_task(request, id):
    if request.method == "POST":
        Task.objects.filter(id = id).delete()

    return redirect(list_task)

def edit_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id = id)
        task.title = request.POST.get("title", "New Task")
        task.text = request.POST.get("text", "...")
        task.color = request.POST.get("color", "#FFF")
        task.date = datetime.now()

        task.save()


    return redirect(list_task)

def home(request):
    return render(request, 'home.html', { 'home': Home.objects.all() })



