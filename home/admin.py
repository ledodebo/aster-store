from django.contrib import admin
from .models import catagory,product,CartItem,inc,gust,order,ProductVariation
admin.site.register(catagory)
admin.site.register(CartItem)
admin.site.register(product)
admin.site.register(order)
admin.site.register(gust)
admin.site.register(inc)
admin.site.register(ProductVariation)
