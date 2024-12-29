from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Order


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

class SignupPageView(TemplateView):
    template_name = 'app/signup.html'

class OrderListView(ListView):
    model = Order
    context_object_name = 'order'
    template_name = 'app/order_list.html'

class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'app/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['customer', 'status']
    template_name = 'app/order_create.html'

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['customer', 'status']
    template_name = 'app/order_update.html'

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'app/order_delete.html'
    success_url = reverse_lazy('order_list')

































