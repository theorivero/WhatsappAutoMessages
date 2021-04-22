from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),


	path('contacts', views.contactsGroupPage, name='contacts'),
	path('create_contacts_group', views.createContactsGroup, name='create-group' ),
	path('delete_contacts_group/<str:pk>', views.deleteContactsGroup, name='delete-group' ),
	path('contacts_group/<str:pk>', views.oneGroup, name='group' ),

	path('create_contact/<str:pk>', views.createContact, name='create-contact' ),
	path('delete_contact/<str:pk>', views.deleteContact, name='delete-contact' ),

	path('templates', views.MessageTemplatesHome, name='templates-home' ),
	path('create_template', views.createTemplate, name='create-template' ),
	path('delete_template/<str:pk>', views.deleteTemplate, name='delete-template' ),
	path('update_template/<str:pk>', views.updateTemplate, name='update-template' ),

]