from django.contrib import admin
from posts.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','post_view']
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
