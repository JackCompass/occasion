from django.urls import path
from event import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('addevent', views.addEvent, name = 'addevent'),
	path('favourites', views.display, name = 'favourite'),
	path('api', views.api, name = 'api'),
]