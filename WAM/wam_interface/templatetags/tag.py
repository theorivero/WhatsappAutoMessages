from django import template

register = template.Library()

@register.simple_tag
def count_contacts_by_group(contacts, group):
    return contacts.filter(group=group).count()

@register.simple_tag
def count_messages(template):
	messages = [template.message_1, template.message_2, template.message_3]
	messages = [message for message in messages if message != '-']
	return len(messages)