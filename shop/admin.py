from django.contrib import admin
from .models import Product, Orders, OrderUpdate
class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'update_desc', 'timestamp')
    list_filter = ['timestamp']

    def has_delete_permission(self, request, obj=None):
        return False
    
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'userId', 'name', 'timestamp')
    list_filter = ['timestamp']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price')
    list_filter = ['category']
    search_fields = ['product_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderUpdate, OrderUpdateAdmin)

admin.site.site_header = "Masterchef"
admin.site.index_title = "The Masterchef Administration"
admin.site.site_title = "The Masterchef Admin"
