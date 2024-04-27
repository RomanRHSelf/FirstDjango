from django.contrib import admin
from MainApp.models import Item, Color

# Register your models here.
#admin.site.register((Item, Color))
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "count", "description", "display_colors") 
    list_filter = ("name", "count")

admin.site.register(Item, ItemAdmin)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_filter = ('name',)
