from django.urls import path
from .views import AddressCreateView, AddressUpdateView, AddressListView, AddressDeleteView

app_name = "address"

urlpatterns = [
    path("", AddressListView.as_view(), name="index"),
    path("ajouter/", AddressCreateView.as_view(), name="add"),
    path("<int:pk>/", AddressUpdateView.as_view(), name="update"),
    path("supprimer/<int:pk>/", AddressDeleteView.as_view(), name="remove"),
    
]