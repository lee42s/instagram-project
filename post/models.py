from mysite import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    photo = models.ImageField(upload_to='post')

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'


class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments',on_delete=models.CASCADE,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    content = models.TextField()

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'