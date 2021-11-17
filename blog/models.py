from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )
    text = models.TextField(
        max_length=200,
        blank=False,
        null=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        null=False
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_previous_by_pk(self):
        """前のデータを取得する。"""
        return type(self).objects.filter(pk__lt=self.pk).order_by('pk').last()

    def get_next_by_pk(self):
        """次のデータを取得する。"""
        return type(self).objects.filter(pk__gt=self.pk).order_by('pk').first()



class Tag(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
