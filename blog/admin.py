from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment



# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'updated_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
# Register your models here.
admin.site.register(Comment)