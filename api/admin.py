from django.contrib import admin
from .models import User, Customer, Merchant
from products.models import Product
from orders.models import Order

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Merchant)
admin.site.register(Product)
admin.site.register(Order)