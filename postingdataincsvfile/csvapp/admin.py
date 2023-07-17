from django.contrib import admin

# Register your models here.
from csvapp import models
admin.site.register(models.Item)