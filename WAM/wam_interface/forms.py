from django.forms import ModelForm
from django import forms

from .models import *

class ContactsGroupForm(ModelForm):
	class Meta:
		model = ContactsGroup
		fields = '__all__'

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

class TemplateForm(ModelForm):
	class Meta:
		model = MessageTemplate
		fields = '__all__'

class BotConfigForm(ModelForm):
	class Meta:
		model = BotConfig
		fields = '__all__'