from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", 'thumbnail_preview', "dollar_price",
                    'discount', "hot_item", "best_seller")
    list_filter = ('hot_item', "best_seller",)
    list_editable = ('hot_item', "best_seller",)
    search_fields = ("name", "price", 'after_discount',
                     "hot_item", "best_seller")
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    def dollar_price(self, obj):
        return "RM {}".format(obj.price)
    dollar_short_description = 'price'

    def discount(self, obj):
        if obj.after_discount:
            return "RM {}".format(obj.after_discount)

    discount.short_description = 'after_discount'

    thumbnail_preview.short_description = 'Cupcake Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(Menu, MenuAdmin)
