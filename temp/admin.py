from django.contrib import admin
from .models import MyModel
# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    fields = ['item']
    list_display = ['item']


admin.site.register(MyModel, MyModelAdmin)