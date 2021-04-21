from django.shortcuts import render
from django.http import HttpResponse
from .bot import WhatsBot, ContactRow


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
