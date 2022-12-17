from django import forms

from friendoftech.shop.models import Review


class CheckoutForm(forms.Form):
    names = forms.CharField(
        max_length=60,
    )

    phone_number = forms.CharField(
        max_length=15,
    )

    shipping_address = forms.CharField(
        max_length=100,
    )

    comment = forms.Textarea()


class WriteReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('is_positive', 'comment')
