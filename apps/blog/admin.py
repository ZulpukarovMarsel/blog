from django.contrib import admin
from .models import Blog, Tag, Like, Comment

class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Названия тега', {
            'fields': ('name',)
        }),
    )

class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Автор блога', {
            'fields': ('user',)
        }),
        ('Видео', {
            'fields': ('video',)
        }),
        ('Основная информация', {
            'fields': ('title', 'description')
        }),
        ('Теги', {
            'fields': ('tags',)
        })
    )
    exclude = ('create_at',)


class LikeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Автор лайка', {
            'fields': ('user',)
        }),
        ('Видео', {
            'fields': ('blog',)
        }),
    )

class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Автор коментарии', {
            'fields': ('user',)
        }),
        ('Видео', {
            'fields': ('blog',)
        }),
        ('Текст комментария', {
            'fields': ('text',)
        }),
    )
    exclude = ('create_at',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
