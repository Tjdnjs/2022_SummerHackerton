from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .validators import validate_no_special_characters

# # Create your models here.

# class User(AbstractUser):
#     nickname = models.CharField(
#         max_length=15,
#         unique=True,
#         null=True,
#         validators=[validate_no_special_characters],
#         error_messages={"unique": "이미 사용 중인 닉네임입니다."},
#     )

#     def __str__(self):
#         return self.email


# class Review(models.Model):
#     title = models.CharField(max_length=30)
#     travel_place = models.CharField(max_length=20)


#     RATING_CHOICES = [
#         (1, 1),
#         (2, 2),
#         (3, 3),
#         (4, 4),
#         (5, 5),


#     ]
#     rating = models.IntegerField(choices=RATING_CHOICES)
#     # travel 하는 곳에 대한 정보 url
#     image1 = models.ImageField(upload_to="review_pics")
#     image2 = models.ImageField(upload_to="review_pics",blank=True)
#     image3 = models.ImageField(upload_to="review_pics", blank=True)
#     content = models.TextField()
#     dt_created = models.DateTimeField(auto_now_add=True)
#     dt_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
