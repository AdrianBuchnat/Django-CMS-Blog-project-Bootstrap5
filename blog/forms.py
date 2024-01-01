from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog, Article
from ckeditor.widgets import CKEditorWidget


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
    

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('__all__')
        # widgets = {
        #     'user_id': forms.HiddenInput(),
        # }


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('article_name', 'content', 'image_first')
        widgets = {
            'content': CKEditorWidget()
        }
