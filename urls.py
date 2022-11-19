"""my_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import view
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^tasks/([^/]+)$',view.tasks_information),
    url(r'^tasks$', view.list_of_tasks),
    url(r'^marks_as_completed/([^/]+)$', view.marking_as_complete),
    url(r'^completed_tasks$',view.list_of_completed_tasks),
    url(r'^pending_tasks$',view.list_of_pending_tasks)
]
