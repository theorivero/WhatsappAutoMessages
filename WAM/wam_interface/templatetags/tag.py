from django import template

register = template.Library()

@register.simple_tag
def count_contacts_by_group(contacts, group):
    return contacts.filter(group=group).count()