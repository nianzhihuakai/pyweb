from django.contrib import admin

# Register your models here.
from .models import Article

admin.site.register(Article)  #这一行注册后，admin就可以管理数据库中这类对象了