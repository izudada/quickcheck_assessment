from django.contrib import admin
from .models import Comment, News


class CommentrInline(admin.TabularInline):
    model = Comment

class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentrInline]

admin.site.register(News, CommentAdmin)