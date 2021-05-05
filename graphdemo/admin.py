from django.contrib import admin
from . models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('city','customer_type','unit_price','quantity','payment','profit')

admin.site.register(Purchase,PurchaseAdmin)
