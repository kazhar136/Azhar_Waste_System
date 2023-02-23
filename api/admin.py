from django.contrib import admin
from .models import Waste

@admin.register(Waste)
class WasteAdmin(admin.ModelAdmin):
    list_display = ['id','location','waste_type','waste_weight','added_date']