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