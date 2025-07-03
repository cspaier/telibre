from django.http import HttpResponseBadRequest, JsonResponse
from wagtail.admin.viewsets.model import ModelViewSet
from .models import Phone, Application
from .forms import PhoneForm

# Wagtail Viewsets
# https://docs.wagtail.org/en/stable/extending/generic_views.html#modelviewset-templates
class PhoneViewSet(ModelViewSet):
    model = Phone
    icon = "mobile-alt"
    add_to_admin_menu = True
    copy_view_enabled = False
    inspect_view_enabled = True

    def get_form_class(self,for_update=False):
        return PhoneForm

phone_viewset = PhoneViewSet("phone")  # defines /admin/phone/ as the base URL

class ApplicationViewSet(ModelViewSet):
    model = Application
    icon = "table"
    add_to_admin_menu = True
    copy_view_enabled = False
    inspect_view_enabled = True

application_viewset = ApplicationViewSet("Application")  

# Other views

def get_gsmarena_data(request):
    """API returning JSON from a gsmarena url
    Expects an `url` GET parameter.
    see Phone.get_gsmarena static method for returned data
    """
    url = request.GET.get('url', None)
    if url is None:
        return HttpResponseBadRequest()
    data = Phone.parse_gsmarena_url(url)
    return JsonResponse(data)