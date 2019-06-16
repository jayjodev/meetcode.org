from django.contrib import admin
from .models import first_model, second_model, third_model

admin.site.register(first_model)
admin.site.register(second_model)
admin.site.register(third_model)

# Register your models here.
