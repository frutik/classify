from item.models import Item
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Item, ItemAdmin)
