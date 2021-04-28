from django.contrib import admin

from .models import *

admin.site.register(ContactsGroup)
admin.site.register(Contact)
admin.site.register(MessageTemplate)
admin.site.register(BotConfig)