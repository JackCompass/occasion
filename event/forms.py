from django.forms import widgets, ModelForm
from event.models import Events
# Creating a Model form based on Event Model

class EventForm(ModelForm): 
	class Meta:
		model = Events
		fields = '__all__'

		widgets = {
			'event_date' : widgets.DateInput(attrs={'type' : 'date'})
		}