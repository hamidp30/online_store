from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User,Product,Orders

admin.site.unregister(Group)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','Address', 'ZipCode')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProdictID', 'Number', 'Status', 'UserID', 'TimeOrder')
    list_editable = ('Status',)
    search_fields =('id',)
    # prepopulated_fields= {'Status':('id',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('NameProduct', 'Price', 'Quantity')
    search_fields =('NameProduct',)

# Register your models here.
admin.site.register(User, CustomUserAdmin),
admin.site.register(Product,ProductAdmin),
admin.site.register(Orders, OrdersAdmin)