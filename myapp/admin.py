from django.contrib import admin
from myapp.models import Users
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','pwd')
