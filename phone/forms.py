from wagtail.admin.forms.models import WagtailAdminModelForm
from django.forms import Script
from django.core.exceptions import ValidationError

from .models import Phone

class PhoneForm(WagtailAdminModelForm):    
    class Meta:
        model = Phone
        
        fields = "__all__" # C'est mal de faire ca!
    
    class Media:
        js = [Script(
                "phoneForm.js",
                **{"defer": True}
        )]

    def clean_gsmarena_url(self):
        if 'www.gsmarena.com/' not in self.cleaned_data["gsmarena_url"]:
            raise ValidationError("L'url ne pointe pas vers www.gsmarena.com")           
        return self.cleaned_data["gsmarena_url"]

        