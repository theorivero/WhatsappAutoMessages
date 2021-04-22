from django.shortcuts import render, redirect
from django.http import HttpResponse
from .bot import WhatsBot, ContactRow
from django.forms import inlineformset_factory

from .models import *
from .forms import *

# Create your views here.

def home(request):
	
	form = BotConfigForm()

	if request.method == 'POST':
		form = BotConfigForm(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			messages = template_to_messages(form_data['template'])
			contacts = group_to_contacts(form_data['group'])
			run_bot(messages,contacts)
			return redirect('/')

	context = {'form':form}
	return render(request, 'wam_interface/home.html', context)

# Many Group of Contacts -------------------------------------------------------

def contactsGroupPage(request):
	contactsGroups = ContactsGroup.objects.all()
	contacts = Contact.objects
	context = {
				'contactsGroups': contactsGroups,
				'contacts':contacts
				}

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
	context = {
				'contactsGroup':contactsGroup,
				'contacts':contacts,
		}
	return render(request, 'wam_interface/oneGroup.html', context)


# 1 Contact --------------------------------------------

def createContact(request, pk):
	ContactFormSet = inlineformset_factory(ContactsGroup, Contact, fields=('name','company','phone','var_1','var_2'), extra=1)
	contactsGroup = ContactsGroup.objects.get(id=pk)
	#form = OrderForm(initial = {'customer': customer})
	formset = ContactFormSet(queryset=Contact.objects.none(), instance=contactsGroup)
	if request.method == "POST":
		formset = ContactFormSet(request.POST, instance=contactsGroup)
		if formset.is_valid():
			formset.save()
			return redirect(f'/contacts_group/{pk}')

	context = {'formset': formset}

	return render(request, 'wam_interface/contact_form.html', context)

def deleteContact(request, pk):
	contact = Contact.objects.get(id=pk)
	if request.method == 'POST':
		contact.delete()
		return redirect('/contacts')

	context = {'item': contact}
	return render(request, 'wam_interface/delete.html', context)


# Messages ----------------------------------------------------

def MessageTemplatesHome(request):
	MessageTemplates = MessageTemplate.objects.all()
	context = {
				'MessageTemplates': MessageTemplates
				}

	return render(request, 'wam_interface/message_templates_home.html', context)

def createTemplate(request):
	form = TemplateForm()

	if request.method == 'POST':
		form = TemplateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/templates')

	context = {'form':form}

	return render(request, 'wam_interface/template_form.html', context)

def deleteTemplate(request, pk):
	template = MessageTemplate.objects.get(id=pk)
	if request.method == 'POST':
		template.delete()
		return redirect('/templates')

	context = {'item': template}
	return render(request, 'wam_interface/delete.html', context)


def updateTemplate(request, pk):
	template = MessageTemplate.objects.get(id=pk)
	form = TemplateForm(instance=template)
	if request.method == "POST":
		form = TemplateForm(request.POST, instance=template)
		if form.is_valid():
			form.save()
			return redirect('/templates')

	context = {'form': form}

	return render(request, 'wam_interface/template_form.html', context)

# bot funcs -------------------------------------------

def template_to_messages(template):
	messages = [template.message_1, template.message_2, template.message_3]
	return [message for message in messages if message != '-']

def group_to_contacts(group):
	res_contacts = []
	contacts = Contact.objects.filter(group=group)
	for contact in contacts:
		res_contact = ContactRow(
			contact.name,
			contact.phone,
			contact.company,
			contact.var_1,
			contact.var_2)
		res_contacts.append(res_contact)
	
	return res_contacts

def run_bot(messages, contacts):
	bot = WhatsBot()
	bot.open()

	bot.login()
	for contact in contacts:
		bot.send_message(contact, messages)
	bot.close()