"""
URL configuration for CMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import HomePageView, ArticleView, BlogsView, BlogView, RegisterView, CreateBlogView, MyBlogView, AddArticleView, EditArticleView, DeleteArticleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', HomePageView.as_view(), name='strona-glowna'),
    path('article/<str:article_name>/', ArticleView.as_view(), name='article'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('blogs/<int:blog_id>/', BlogView.as_view(), name='blog'),
    path('register/', RegisterView.as_view(), name="register"),
    path('my-blog/<user>/', MyBlogView.as_view(), name='my_blog'),
    path('my-blog/<user>/create-blog', CreateBlogView.as_view(), name='create_blog'),
    path('my-blog/<user>/add-article', AddArticleView.as_view(), name='add_article'),
    path('article/edit/<int:pk>/', EditArticleView.as_view(), name='edit_article'),
    path('article/delete/<int:pk>/', DeleteArticleView.as_view(), name='delete_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
