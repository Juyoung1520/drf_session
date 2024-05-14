# accounts의 admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')

# db의 작성일 시간 이상 수정    
