from django.urls import path
from .views import get_gsmarena_data
app_name = "phone"

urlpatterns = [
    path("get-gsmarena-data/", get_gsmarena_data, name="gsmarena"),
]