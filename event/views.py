from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from event.forms import EventForm
from event.models import Events, Like
import json

@login_required()
def index(request):
	# Fetching all the events from the database
	events = Events.objects.all()

	# Fetching the spcific post Which user has liked.
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

@login_required()
def display(request):
	if request.method == 'POST':
		# Here again we will handle the queries
		pass
	else:
		events = Events.objects.all()
		liked = Like.objects.filter(user = request.user).values_list('event', flat=True)
		return render(request, 'event/favourite.html', {
			'events' : events,
			'liked' : liked,
		})

@login_required()
def api(request):
	if request.method != 'GET':
		post_data = json.loads(request.body.decode("utf-8"))
		eventid = post_data.get('id')
		event = Events.objects.get(id = eventid)

		# Handling the POST request 
		if request.method == 'POST':
			try :
				obj = Like.objects.get(event = event)
			except:
				obj = Like.objects.create(event = event)
			obj.user.add(request.user)

		# Handling the DELETE request
		elif request.method == 'DELETE':
			try : 
				obj = Like.objects.get(event = event)
			except :
				print("No such event exists")
			else:
				obj.user.remove(request.user)
		# Sending an empty string as a JSON response 
		# Could be used to send SUCCESS message
		return JsonResponse('', safe=False)

	else:
		# Using to test GET request API
		return JsonResponse('Endpoint to test GET request', safe=False)