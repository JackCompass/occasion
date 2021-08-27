from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
	'''
	Model is used to store the events.
	'''
	event_name = models.CharField(max_length=100, unique=True)
	description = models.TextField()
	image = models.ImageField(upload_to = 'images/', blank = True, null = True, default = 'images/defaultEvent.png')
	location = models.CharField(max_length=50)
	event_date = models.DateField(auto_now_add=False)

	def __str__(self):
		return f'{self.event_name}'


class Like(models.Model):
	'''
		Model is used to keep track of liked event by different users.
	'''

	event = models.OneToOneField(Events, on_delete = models.CASCADE, related_name = "program")
	user = models.ManyToManyField(User)

	def __str__(self):
		return f'{self.event}'