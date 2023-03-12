from django.contrib.auth.models import User
from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    number_of_votes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)


class Comment(models.Model):
    story = models.ForeignKey(Story, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class Vote(models.Model):
    story = models.ForeignKey(Story, related_name='votes', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='story_votes', on_delete=models.CASCADE)