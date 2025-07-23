from django.shortcuts import render,HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.

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
            form.save()
            return JsonResponse({'message': 'Thanks! We will get back to you shortly.'})
        else:
            return JsonResponse({'error': form.errors.as_text()}, status=400)
    else:
        form = ContactForm()
    return render(request, 'main/contact.html',{"form": form})