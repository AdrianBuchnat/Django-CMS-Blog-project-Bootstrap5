# Generated by Django 4.2.7 on 2023-12-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_author_name_blog_blog_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_first',
            field=models.ImageField(upload_to='./CMS/static/'),
        ),
    ]
