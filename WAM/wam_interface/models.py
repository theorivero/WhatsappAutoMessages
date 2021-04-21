from django.db import models

# Create your models here.

class ContactsGroup(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField(max_length= 200, null=True)
	company = models.CharField(max_length= 200, null=True)
	phone = models.CharField(max_length= 200, null=True)
	var_1 = models.CharField(max_length= 200, null=True)
	var_2 = models.CharField(max_length= 200, null=True)
	group = models.ForeignKey(ContactsGroup, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

