from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
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
            # print(form.cleaned_data)
            # print(form.changed_data.name)
            if form.cleaned_data['name'].lower() == 'robertdek':
                print("not campaign email")
                return JsonResponse({'message': 'Thanks! We will get back to you shortly.'})
            resp = send_telegram_message(json.dumps(form.cleaned_data))
            return JsonResponse({'message': 'Thanks! We will get back to you shortly.'})
        else:
            return JsonResponse({'error': form.errors.as_text()}, status=400)
    else:
        form = ContactForm()
    return render(request, 'main/contact.html',{"form": form})


def service_detail(request, service_slug):
    # Service data - you can replace this with a database model later
    services_data = {
        'custom-web-applications': {
            'title': 'Custom Web Applications',
            'subtitle': 'Scalable Django solutions built for your exact workflow',
            'icon': 'fas fa-laptop-code',
            'description': '''
                We specialize in building custom web applications using Django that are tailored to your specific business needs. 
                Our solutions include robust authentication, payment processing, admin dashboards, and deployment pipelines.
            ''',
            'features': [
                'B2B dashboards & portals',
                'Marketplaces & booking engines',
                'REST & GraphQL APIs',
                'User authentication & authorization',
                'Payment integration',
                'Admin dashboards',
                'Deployment pipelines'
            ],
            'process': [
                {
                    'step': 1,
                    'title': 'Discovery',
                    'description': 'We start by understanding your business requirements and goals.'
                },
                {
                    'step': 2,
                    'title': 'Design',
                    'description': 'Our team creates wireframes and prototypes for your approval.'
                },
                {
                    'step': 3,
                    'title': 'Development',
                    'description': 'We build your application using best practices and modern technologies.'
                },
                {
                    'step': 4,
                    'title': 'Testing',
                    'description': 'Rigorous testing ensures your application is bug-free and secure.'
                },
                {
                    'step': 5,
                    'title': 'Deployment',
                    'description': 'We deploy your application and provide ongoing support.'
                }
            ],
            'technologies': [
                {'name': 'Django', 'icon': 'fab fa-python'},
                {'name': 'PostgreSQL', 'icon': 'fas fa-database'},
                {'name': 'Docker', 'icon': 'fab fa-docker'},
                {'name': 'AWS', 'icon': 'fab fa-aws'},
                {'name': 'React', 'icon': 'fab fa-react'}
            ]
        },
        'desktop-software': {
            'title': 'Desktop Software',
            'subtitle': 'Cross-platform desktop apps that work offline and sync when online',
            'icon': 'fas fa-desktop',
            'description': '''
                We develop cross-platform desktop applications using PySide6, PyQt, and Tkinter that run seamlessly on Windows, macOS, and Linux. 
                Our desktop solutions are perfect for internal tools, client-installed applications, and systems that need to work offline.
            ''',
            'features': [
                'Windows / macOS / Linux installers',
                'Auto-updater & telemetry baked-in',
                'Offline functionality',
                'Data synchronization',
                'Cross-platform compatibility'
            ],
            'process': [
                {
                    'step': 1,
                    'title': 'Requirements Analysis',
                    'description': 'We analyze your specific desktop application needs.'
                },
                {
                    'step': 2,
                    'title': 'UI/UX Design',
                    'description': 'Creating intuitive interfaces for desktop environments.'
                },
                {
                    'step': 3,
                    'title': 'Development',
                    'description': 'Building the application using the best framework for your needs.'
                },
                {
                    'step': 4,
                    'title': 'Packaging',
                    'description': 'Creating installers for all target platforms.'
                },
                {
                    'step': 5,
                    'title': 'Maintenance',
                    'description': 'Providing updates and support for your application.'
                }
            ],
            'technologies': [
                {'name': 'PySide6', 'icon': 'fab fa-python'},
                {'name': 'PyQt', 'icon': 'fab fa-python'},
                {'name': 'Tkinter', 'icon': 'fab fa-python'},
                {'name': 'Electron', 'icon': 'fab fa-electron'}
            ]
        },
        # Add these to the services_data dictionary
        'automation-ai': {
            'title': 'Automation & AI',
            'subtitle': 'Scripts, bots & ML models that save hours every day',
            'icon': 'fas fa-robot',
            'description': '''
                Our automation and AI solutions help businesses streamline operations and gain insights from data. 
                We develop custom scripts, bots, and machine learning models that automate repetitive tasks and 
                provide actionable insights from your data.
            ''',
            'features': [
                'Web scraping & data ingestion',
                'Invoice / receipt OCR',
                'Predictive analytics',
                'Process automation',
                'Data visualization'
            ],
            'process': [
                # Add process steps similar to other services
            ],
            'technologies': [
                {'name': 'Python', 'icon': 'fab fa-python'},
                {'name': 'TensorFlow', 'icon': 'fas fa-brain'},
                {'name': 'Selenium', 'icon': 'fab fa-firefox'},
                {'name': 'Pandas', 'icon': 'fas fa-table'}
            ]
        },
        'data-scraping-mining': {
            'title': 'Data Scraping & Mining',
            'subtitle': 'Desktop apps that scrape, clean, and mine data without coding',
            'icon': 'fas fa-database',
            'description': '''
                We deliver powerful desktop applications that allow you to scrape, clean, and mine web or internal 
                data without writing code or owning servers. Our tools make data collection and processing accessible 
                to everyone in your organization.
            ''',
            'features': [
                'Data cleaning tools',
                'Offline data processing',
                'Automated scheduling',
                'Multiple export formats'
            ],
            'process': [
                # Add process steps similar to other services
            ],
            'technologies': [
                {'name': 'BeautifulSoup', 'icon': 'fas fa-code'},
                {'name': 'Scrapy', 'icon': 'fas fa-spider'},
                {'name': 'Pandas', 'icon': 'fas fa-table'},
                {'name': 'Tkinter', 'icon': 'fab fa-python'}
            ]
        },
        'android-automation': {
            'title': 'Android Automation via ADB',
            'subtitle': 'Lightweight apps that hide ADB behind a clean GUI',
            'icon': 'fas fa-mobile-alt',
            'description': '''
                We develop lightweight applications that hide the complexity of ADB (Android Debug Bridge) behind 
                a clean, user-friendly GUI. Our tools make it easy to automate Android devices without technical expertise.
            ''',
            'features': [
                'Device automation',
                'App testing tools',
                'Data extraction',
                'Bulk operations'
            ],
            'process': [
                # Add process steps similar to other services
            ],
            'technologies': [
                {'name': 'ADB', 'icon': 'fab fa-android'},
                {'name': 'Python', 'icon': 'fab fa-python'},
                {'name': 'PySide6', 'icon': 'fab fa-python'},
                {'name': 'Uiautomator', 'icon': 'fas fa-robot'}
            ]
        },
        'telegram-bots': {
            'title': 'Custom Telegram Bots',
            'subtitle': 'Telegram Bots as per your needs!',
            'icon': 'fas fa-comments',
            'description': '''
                We create custom Telegram bots using the Telegram API to meet your specific requirements. 
                Our bots can handle customer service, notifications, content delivery, and much more.
            ''',
            'features': [
                'Custom bot development',
                'API integration',
                'Interactive commands',
                'Notification systems',
                'Content delivery'
            ],
            'process': [
                # Add process steps similar to other services
            ],
            'technologies': [
                {'name': 'Python', 'icon': 'fab fa-python'},
                {'name': 'Telegram API', 'icon': 'fab fa-telegram'},
                {'name': 'Webhooks', 'icon': 'fas fa-plug'},
                {'name': 'Databases', 'icon': 'fas fa-database'}
            ]
        }
    }
    
    # Get the service data or return 404 if not found
    service = get_object_or_404(services_data, service_slug)
    
    return render(request, 'main/service_detail.html', {
        'service': service,
        'service_slug': service_slug
    })