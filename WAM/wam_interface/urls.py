from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),


	path('contacts', views.contactsGroupPage, name='contacts'),
	path('create_contacts_group', views.createContactsGroup, name='create-group' ),
	path('delete_contacts_group/<str:pk>', views.deleteContactsGroup, name='delete-group' ),
	path('contacts_group/<str:pk>', views.oneGroup, name='group' ),
	path('create_contact/<str:pk>', views.createContact, name='create-contact' ),
]