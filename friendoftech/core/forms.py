from django import forms

from friendoftech.core.models import ClientMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ClientMessage
        fields = '__all__'
