from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    descroption = models.TextField() #TODO: Naprawić żeby nie było że jakiś analfabeta pisał 
    author_name = models.CharField(max_length=255)
    blog_img = models.ImageField()
    def __str__(self):
        return self.name
    

class ArticleTag(models.Model):
    tags = models.CharField(max_length=64)
    
    def __str__(self):
        return self.tags
    

class Article(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_name = models.CharField("Tytuł Artykułu", max_length=256)
    data = models.DateTimeField(auto_now=True)
    content = RichTextField('Treść')
    catgories_id = models.ManyToManyField(ArticleTag)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image_first = models.ImageField('Zdjęcie')
    
    def __str__(self):
        return self.article_name
    

class Coments(models.Model):
    content = models.TextField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    replie_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    if replie_comment == None:
        def __str__(self):
            return str(self.user_id) + ' comment to ' + str(self.article_id)
    else:
        def __str__(self):
            return str(self.user_id) + ' replie to ' + str(self.replie_comment) + " " + str(self.article_id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default-pic.jpg')