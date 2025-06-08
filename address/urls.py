from django.urls import path
from .views import AddressCreateView, AddressUpdateView, AddressListView, AddressDeleteView

urlpatterns = [
    path("", AddressListView.as_view()),
    path("ajouter/", AddressCreateView.as_view()),
    path("<int:pk>/", AddressUpdateView.as_view()),
    path("supprimer/<int:pk>/", AddressDeleteView.as_view()),
    
]