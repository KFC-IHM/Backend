from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_moderator = models.BooleanField(default=False)
    is_restaurateur = models.BooleanField(default=False)
    is_consumer = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='images/user/', blank=True, null=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/restaurant/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OpenHoursWeek(models.Model):
    WEEKDAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    day = models.CharField(max_length=100, choices=WEEKDAYS)
    open = models.TimeField()
    close = models.TimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.day


class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
