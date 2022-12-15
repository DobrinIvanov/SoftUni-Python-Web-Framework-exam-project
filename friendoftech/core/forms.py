from django import forms

from friendoftech.core.models import ClientMessage


class ContactForm(forms.ModelForm):

    class Meta:
        # model = Message
        model = ClientMessage
        fields = '__all__'
