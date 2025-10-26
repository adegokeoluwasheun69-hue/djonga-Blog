from django.contrib import admin
from.models import Blog
from .models import Service, Product


# Register your models here.
admin.site.register(Blog)


admin.site.register(Service)
admin.site.register(Product)
