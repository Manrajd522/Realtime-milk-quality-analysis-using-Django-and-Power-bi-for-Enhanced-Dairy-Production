from django.contrib import admin

# Register your models here.
from .models import User, Record

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('User_id', 'Name','Address','Phone_No',)
# admin.site.register(User)
# admin.site.register(Record)
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'Date','Quantity','Fat','SNF','Amount')