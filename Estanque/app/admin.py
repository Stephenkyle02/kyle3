from django.contrib import admin
from .models import Customer, Order, OrderDetail, Category, Product
# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Category)
admin.site.register(Product)
