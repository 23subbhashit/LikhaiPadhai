from django.contrib import admin

# Register your models here.

from .models import GEO_TAGGING,Admin
admin.site.register(GEO_TAGGING)
admin.site.register(Admin)