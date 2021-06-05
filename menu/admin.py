from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price", 'after_discount', "hot_item" , "best_seller")
    list_filter = ('hot_item', "best_seller",)
    list_editable = ('hot_item', "best_seller",)
    search_fields = ("name", "price", 'after_discount', "hot_item" , "best_seller")

    def dollar_price(self, obj): #Used to render a $ in front of each price, and add commas in for readability
        return "RM {:,}".format(obj.price)
    dollar_price.short_description = 'price'


admin.site.register(Menu, MenuAdmin)
