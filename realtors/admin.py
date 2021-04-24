from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_mvp','phone','email')
    list_display_links=('id','name')
    list_filter=('name',)
    search_fields=('name','phone','email')
    list_per_page=25


admin.site.register(Realtor,RealtorAdmin)

