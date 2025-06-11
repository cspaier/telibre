from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Address
from .forms import AddressForm

class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('address:index')

    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['submit-text'] = 'Créer'
        return kwargs
    
    def get_initial(self):
        return {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name
        }
        
        
class AddressUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('address:index')

    
    
    def test_func(self):
        return self.get_object().is_owned_by(self.request.user)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['submit-text'] = 'Modifier'
        return kwargs

class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    
    def get_queryset(self):
        return self.request.user.address_set.all()

class AddressDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('address:index')
     
    def test_func(self):
        return self.get_object().is_owned_by(self.request.user)    