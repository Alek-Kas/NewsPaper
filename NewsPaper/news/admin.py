from django.contrib import admin
from modeltranslation.admin import TranslationAdmin  # импортируем модель амдинки

# Register your models here.
from news.models import Post, Author, Category, PostCategory


# Регистрируем модели для перевода в админке
class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
