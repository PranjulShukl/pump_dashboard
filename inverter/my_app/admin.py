from django.contrib import admin
from .models import Inverter1Data

# Register your models here.
from django.utils.timezone import localtime
class Inverter1DataAdmin(admin.ModelAdmin):
    list_display = (
        'holding_reg1', 'holding_reg2', 'holding_reg3',
        'holding_reg4', 'holding_reg5', 'holding_reg6',
        'holding_reg7', 'holding_reg8', 'holding_reg9',
        'holding_reg10', 'holding_reg11', 'holding_reg12',
        'formatted_last_updated'
    )

    def formatted_last_updated(self, obj):
        # Convert to local timezone and format
        return obj.last_updated.strftime('%Y-%m-%d %H:%M:%S')  # Includes seconds

    formatted_last_updated.short_description = 'Last Updated'

admin.site.register(Inverter1Data, Inverter1DataAdmin)