from django.forms import ModelForm
from .models import Product, Box
from django import forms

class ProductForm(forms.ModelForm):

    quantity = forms.IntegerField(
        min_value=1,
        initial=1
    )

    class Meta:
        model = Product
        fields = [
            "name",
            "length_cm",
            "width_cm",
            "height_cm",
            "weight_kg",
        ]


class BoxForm(ModelForm):

    class Meta:
        model = Box
        fields = "__all__"