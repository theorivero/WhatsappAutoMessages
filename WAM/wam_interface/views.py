from django.shortcuts import render, redirect
from django.http import HttpResponse
from .bot import WhatsBot, ContactRow

from .models import *
from .forms import *

# Create your views here.

def home(request):
	context = {}

	if(request.GET.get('bot_btn')):       
		bot = WhatsBot()
		bot.open()
		bot.login()
		contato = ContactRow('Pedro','4899182048' )
		bot.send_message(contato, [f'Boa noite tudo bem? Seu nome é {contato.name}?', 'Você poderia me fazer o favor'])
		bot.close()


	return render(request, 'wam_interface/home.html')

def contactsGroupPage(request):
	contactsGroups = ContactsGroup.objects.all()
	context = {'contactsGroups': contactsGroups}
	print(contactsGroups)

	return render(request, 'wam_interface/contactsGroup.html', context)

def createContactsGroup(request):
	form = ContactsGroupForm()

	if request.method == 'POST':
		form = ContactsGroupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/contacts')

	context = {'form':form}

	return render(request, 'wam_interface/contactsGroup_form.html', context)

def deleteContactsGroup(request, pk):
	contactsGroup = ContactsGroup.objects.get(id=pk)
	if request.method == 'POST':
		contactsGroup.delete()
		return redirect('/contacts')

	context = {'item': contactsGroup}
	return render(request, 'wam_interface/delete.html', context)

def oneGroup(request, pk):
	contactsGroup = ContactsGroup.objects.get(id=pk)
	contacts = Contact.objects.filter(group=contactsGroup)
	print(contacts)
	context = {
				'contactsGroup':contactsGroup,
				'contacts':contacts,
		}
	return render(request, 'wam_interface/oneGroup.html', context)

def createContact(request,pk):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/contacts')

	context = {'form':form}

	return render(request, 'wam_interface/contact_form.html', context)
