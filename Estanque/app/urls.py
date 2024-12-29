from django.contrib.admin.templatetags.admin_list import pagination_tag
from django.urls import path
from .views import HomePageView, AboutPageView, LoginPageView, SignupPageView
from .views import(
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupPageView.as_view(), name='signup'),

    path('order/', OrderListView.as_view(), name='order'),    
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('order/', OrderListView.as_view(), name='order_list'),


]