from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment, Category


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'updated_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)


@admin.register(Category)
class Category(SummernoteModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'id')
