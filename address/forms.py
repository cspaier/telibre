from django import forms
from .models import Address
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Submit, Field
from django.forms import ModelForm, Script
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
"""Formulaire pour les Addresss.
Il faudra je pense faire une template propre mais ca fonctionne.
"""
class AddressForm(ModelForm):
    autocomplete = forms.CharField(label="", required=False)
    phone = PhoneNumberField(region="FR", widget=RegionalPhoneNumberWidget(attrs={"class": "textinput focus:ring input w-full focus:outline-none input-bordered"}))
    
    def __init__(self, *args, **kwargs):
        submit_text = kwargs.pop('submit-text')
        super().__init__(*args, **kwargs)        
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field("autocomplete"),
            Row("first_name", "last_name", css_class="flex flex-row gap-2"),
            Row("house_number", "street", css_class="flex flex-row gap-2"),
            Row("postcode", "city", css_class="flex flex-row gap-2"),
                
            "phone",
            "infos"
        )
        self.helper.add_input(Submit('submit', submit_text))
        
    class Meta:
        model = Address
        fields = ["autocomplete", "first_name", "last_name", "house_number", "street", "postcode", "city", "phone", "infos"]

    class Media:
        js = [
            Script(
                "https://cdn.jsdelivr.net/npm/@tarekraafat/autocomplete.js@10.2.6/dist/autoComplete.min.js",
                **{
                    "defer": True
                }
            ),
            Script(
                "address.js",
                **{
                    "defer": True
                }
            )
        ]
        
        css = {
            "all": ["https://cdn.jsdelivr.net/npm/@tarekraafat/autocomplete.js@10.2.6/dist/css/autoComplete.min.css"]
        }