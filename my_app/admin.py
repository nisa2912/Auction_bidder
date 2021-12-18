from django.contrib import admin

# Register your models here.

from .models import Post, Bidding

admin.site.register(Post)
admin.site.register(Bidding)