from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField("프로필 이미지", upload_to = "users/profile", blank=True)
    short_description = models.TextField("소개글", blank=True)
    
    like_posts = models.ManyToManyField(
        "posts.Post",
        verbose_name="좋아요 누른 'Post'목록",
        related_name="like_users",
        blank=True,
    )

    following = models.ManyToManyField(
        "self",
        verbose_name="팔로우 중인 사람들",
        related_name="followers",
        symmetrical=False,
        through="users.Relationship",
    )

    def __str__(self):
          return self.username
    
    

class Relationship(models.Model):
     from_user = models.ForeignKey(
          'users.User',
          verbose_name="팔로우를 요청한 사용자",
          related_name="following_relationships",
          on_delete=models.CASCADE,
     )
     to_user = models.ForeignKey(
          "users.User",
          verbose_name="팔로우 요청의대상",
          related_name="follower_relationships",
          on_delete=models.CASCADE
     )
     created = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f"관계 ({self.from_user} -> {self.to_user})"