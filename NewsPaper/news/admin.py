from django.contrib import admin

# Register your models here.
from news.models import Post, Author, Category, PostCategory


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)