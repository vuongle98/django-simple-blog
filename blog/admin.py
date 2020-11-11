from django.contrib import admin
from .models import Post, Category
from django.db import models
from django.template.defaultfilters import truncatewords_html
# Register your models here.



        
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'author', 'slug', 'status', 'created_at', 'updated_at')
    list_filter = ('status', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}

    def short_content(self, obj):
        return truncatewords_html(obj.content, 20)
    
    short_content.short_description = 'content'

    class Media:
        js = ('ckeditor.js')
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', )
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)