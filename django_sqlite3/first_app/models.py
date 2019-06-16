from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class first_model(models.Model):
    title =models.CharField(max_length=100)
    content =models.TextField()
    date_posted =models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class second_model(models.Model):
    title_2 =models.CharField(max_length=100)
    content_2 =models.TextField()
    date_posted_2 =models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_2

class third_model(models.Model):
    title_3 =models.CharField(max_length=100)
    content_3 =models.TextField()
    date_posted_3 =models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_3

