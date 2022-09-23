from django.contrib import admin
from .models import destinations
from .models import profile
# Register your models here.
admin.site.register(destinations)
admin.site.register(profile)