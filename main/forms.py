from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your message here...'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'company': 'Company (optional)',
            'message': 'Message',
        }