# Generated by Django 4.1.7 on 2023-03-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_comment_author_restaurant_owner_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/user/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to='images/restaurant/'),
        ),
    ]