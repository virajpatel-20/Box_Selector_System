from django.contrib import admin
from .models import Product
from .models import Box
from .models import Order
from .models import OrderItem

admin.site.register(Product)
admin.site.register(Box)
admin.site.register(Order)
admin.site.register(OrderItem)
