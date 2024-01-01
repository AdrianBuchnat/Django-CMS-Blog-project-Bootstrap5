from django.contrib import admin

# Register your models here.
from .models import Blog, Article, ArticleTag, Coments, Profile

admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(ArticleTag)
admin.site.register(Coments)
admin.site.register(Profile)
