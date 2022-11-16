from django.db import models
import review
from user.models import User


class Post(models.Model):
    """Model definition for Post."""

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    POST_TYPE = (
        ('R', 'review'),
        ('C', 'clubpost'),
        ('A', 'advertisement'),
    )

    title = models.CharField(
        max_length=20,
        null=False,
        verbose_name='제목'
    )
    content = models.TextField(
        max_length=2000,
        null=False,
        verbose_name='내용'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='글쓴이',
    )
    type = models.CharField(
        max_length=1,
        choices=POST_TYPE,
        null=True,
        verbose_name='글 종류',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성 일시',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='수정 일시',
    )

    # post 에서 type이 R인 객체 생성시 review table 에도 객체 생성
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.type == "R":
            review.models.Review.objects.create(post_id = self.id)