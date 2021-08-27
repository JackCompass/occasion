from django.urls import path

from event import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('addevent', views.addEvent, name = 'addevent'),
]