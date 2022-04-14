from django.contrib import admin
from .models import Rent

# Register your models here.


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'author', 'borrowed_on']
    list_filter = ['borrowed_on', 'author']
