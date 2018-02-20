# Register your models here.
from django.contrib import admin

from blog.models import Client, Comment, Post

admin.site.register(Post)
admin.site.register(Client)
admin.site.register(Comment)
