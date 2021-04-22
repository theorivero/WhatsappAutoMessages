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

class MessageTemplate(models.Model):
	name = models.CharField(max_length= 200, null=True)
	message_1 = models.CharField(max_length= 200, null=True)
	message_2 = models.CharField(max_length= 200, null=True)
	message_3 = models.CharField(max_length= 200, null=True)

	def __str__(self):
			return self.name

class BotConfig(models.Model):
	template = models.ForeignKey(MessageTemplate, null=True, on_delete=models.SET_NULL)
	group = models.ForeignKey(ContactsGroup, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return f'{self.template.name} for {self.group.name}'


