from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Post, Author, Category, SubscribersUsers


class PostForm(forms.ModelForm):
    post_heading = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'post_heading',
            'post_text',
            'post_cat',
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("post_heading")
        text = cleaned_data.get("post_text")

        if heading == text:
            raise ValidationError(
                "Заголовок не должен быть идентичен тексту статьи."
            )
        return cleaned_data


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = [
            'author_user',
        ]


class CategoryForm(forms.ModelForm):

    class Meta:
        model = SubscribersUsers
        fields = [
            'sub_cat',
            'sub_user',
        ]
