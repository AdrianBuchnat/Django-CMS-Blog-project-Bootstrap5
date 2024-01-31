from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article, Blog, Coments
from .forms import NewUserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Widoki dla niezalogowanych użytkowników

class HomePageView(View):
    def get(self, request):
        articles = Article.objects.all()
        blogs = Blog.objects.all()

        for article in articles:
            article.content = article.content[:256]
        
        ctx = {
            'articles': articles,
            "blogs": blogs
        }

        return render(request, "blog/main.html", ctx)


class RegisterView(View):
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            form = NewUserForm()
            return render(request, template_name="registration/register.html", context={"register_form":form})
	
    def get(self, request):
        form = NewUserForm()
        return render(request, template_name="registration/register.html", context={"register_form":form})


class BlogsView(View):
    def get(self, request):
        blogs = Blog.objects.all()

        ctx = {
            "blogs": blogs
        }

        return render(request, "blog/blogs.html", ctx)


class BlogView(View):
    def get(self, request, blog_id):

        blog = get_object_or_404(Blog, pk = blog_id)
        articles = Article.objects.filter(blog_id = blog)

        for article in articles:
            article.content = article.content[:256]

        ctx = {

            'blog': blog,
            'articles': articles

        }

        return  render(request, "blog/blog.html", ctx)


class ArticleView(View):
    def get(self, request, article_name):
        article = get_object_or_404(Article, article_name = article_name)
        blog = Blog.objects.get(name = article.blog_id)
        coments = Coments.objects.filter(article_id = article.id)

        ctx = {
            'coments': coments,
            'article': article,
            'blog': blog
        }
        return render(request, 'blog/article.html', ctx)
    
    def post(self, request, article_name):
        content = request.POST.get('content')
        user = request.user
        article = get_object_or_404(Article, article_name = article_name)
        Coments.objects.create(content=content, user_id=user, replie_comment=None, article_id=article)
        return HttpResponseRedirect('')



# class AboutMeView(View):
#     #TODO Widok na temat twórcy strony



# class Statue(View):
#     #TODO Widok z regulaminem


# class HowToStartView(View):
#     #TODO Widok z poradnikiem jak zacząć jak zacząć


# #Widoki dla zalogowanych użytkowników bez bloga


# class UserProfilView(View):
#     #TODO: widok profilu użytkownika pod /{user.id}


# class UserProfileSettingsView(View):
#     #TODO Widok z ustawieniami profilu takimi jak zmiana hasła pod /{user.id}/settings 


class CreateBlogView(LoginRequiredMixin, View):
    def get(self, request, user):
        try:
            blog = Blog.objects.get(user_id=request.user.pk)
        except ObjectDoesNotExist:
            return render(request, 'blog/create_blog.html')
        else:
            return HttpResponseRedirect('/')
    
    def post(self, request, user):
        name = request.POST.get('name')
        descroption = request.POST.get('descroption')
        author_name = request.POST.get('author_name')
        blog_img = request.FILES.get('blog_img') 
        userR = request.user
        Blog.objects.create(name=name, descroption=descroption, author_name=author_name, blog_img=blog_img, user_id=userR)
        return HttpResponseRedirect('my-blog')



# #Widok dla użytkownika posaidającego bloga:
class MyBlogView(LoginRequiredMixin, View):
    def get(self, request, user):
        try:
            blog = Blog.objects.get(user_id=request.user.id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('create-blog')
        else:
            articles = Article.objects.filter(blog_id = blog)
            ctx = {
                'blog': blog,
                'articles': articles
            }

        return render(request, 'blog/my_blog.html', ctx)


# class EditBlogView(View):
#     #TODO Widok edycji bloga /{blog.name}/dashboard/settings


class AddArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/add_article.html'
    fields = ['article_name', 'content', 'image_first']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        blog = Blog.objects.get(user_id = self.request.user)
        form.instance.blog_id = blog
        return super().form_valid(form)


class EditArticleView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blog/edit_article.html'
    fields = ['article_name', 'content', 'image_first']


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog/delete_article.html'
    success_url = '/my-blog/<user>/'


    

# #NICE TO HAVE MNIEJ WAŻNE

# class DashboardBlogsView(View):
#     #TODO widok blogów i możliwość zmiany bloga
