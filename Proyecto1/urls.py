"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import delete_note, list_notes, edit_note, list_meetings, new_meeting, delete_meeting, edit_meeting
from django.conf import settings
from django.conf.urls.static import static
from Proyecto1.views import new_note

urlpatterns = [
    path('admin/', admin.site.urls), 

    path('notes/', list_notes),
    path('notes/new', new_note),
    path('notes/<id>/delete', delete_note),
    path('notes/<id>/edit', edit_note),

    path('meetings/', list_meetings),
    path('meetings/new', new_meeting),
    path('meetings/<id>/delete', delete_meeting),
    path('meetings/<id>/edit', edit_meeting)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

