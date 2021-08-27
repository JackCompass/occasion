from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from event.forms import EventForm
from event.models import Events, Like

@login_required()
def index(request):
	# Fetching all the events from the database
	events = Events.objects.all()
	liked = Like.objects.filter(user = request.user).values_list('event', flat=True)

	return render(request, 'event/home.html', {
		'events' : events,
		'liked' : liked,
	})


@login_required()
def addEvent(request):
	# This function will process both the get request as well as the post request 
	if request.method == 'GET':
		form = EventForm()
		return render(request, 'event/addevent.html', {
			'form' : form
		})
	if request.method == 'POST':
		# creating a new form and filling it with the user entered details along with image
		form = EventForm(request.POST, request.FILES)

		# validating the form
		if form.is_valid():
			form.save()
			return redirect(reverse('index'))
		else:
			return render(request, 'event/addevent.html', {
			'form' : form
		})


