from django.shortcuts import render,HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse
from django.http import JsonResponse
import requests
import json

def send_telegram_message(message):
    bot_token = '6391769840:AAHGMZ5fl7xQUpFVsANpIsTXD9fPCQ9dw6U'
    chat_id = '291876635'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # form.save()
            resp = send_telegram_message(json.dumps(form.cleaned_data))
            return JsonResponse({'message': 'Thanks! We will get back to you shortly.'})
        else:
            return JsonResponse({'error': form.errors.as_text()}, status=400)
    else:
        form = ContactForm()
    return render(request, 'main/contact.html',{"form": form})