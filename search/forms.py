from django import forms
from .models import Sheet

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    mail_contact = forms.EmailField(label="Enter your e-mail adress")
    send_back = forms.BooleanField(help_text="Check if you want to keep a copy of the message.", required=False,)
    image = forms.ImageField()

class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = '__all__'