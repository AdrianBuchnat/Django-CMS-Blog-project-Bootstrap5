# Generated by Django 4.2.7 on 2023-12-12 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_content_alter_blog_blog_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]