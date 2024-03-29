from django.contrib import admin
from learn_django.models import Product, CustomUser
from learn_django.models import Visitor
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from learn_django.forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
admin.site.register(Product)
admin.site.register(Visitor)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser 
    list_display = ['email', 'username']

admin.site.register(CustomUser,CustomUserAdmin)
    
    


  