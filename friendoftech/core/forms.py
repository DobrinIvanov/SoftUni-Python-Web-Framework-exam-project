from django import forms


class ContactForm(forms.Form):

    full_name = forms.CharField(max_length=50,)
    email_address = forms.EmailField()
    subject = forms.CharField(max_length=30)
    message = forms.Textarea()
