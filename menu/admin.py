from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "dollar_price", 'discount', "hot_item" , "best_seller")
    list_filter = ('hot_item', "best_seller",)
    list_editable = ('hot_item', "best_seller",)
    search_fields = ("name", "price", 'after_discount', "hot_item" , "best_seller")
    prepopulated_fields = {'slug': ('name',)}

    def dollar_price(self, obj): #Used to render a $ in front of each price, and add commas in for readability
        return "RM {}".format(obj.price)
    dollar_short_description = 'price'

    def discount(self, obj): #Used to render a $ in front of each price, and add commas in for readability
        if obj.after_discount:
            return "RM {}".format(obj.after_discount)

    discount.short_description = 'after_discount'


admin.site.register(Menu, MenuAdmin)
