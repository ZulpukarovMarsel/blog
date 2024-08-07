from django.contrib import admin
from .models import Blog, Tag, Like, Comment


admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Comment)
