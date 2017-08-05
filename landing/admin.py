from django.contrib import admin
from .models import *
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    search_fields = ['name','email']

    #exclude = ['email']
    #inlines = [FieldMappingInlines]
    #fields = []
    #search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber,SubscriberAdmin )