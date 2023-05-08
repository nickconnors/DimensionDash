from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATINGS)
    review_text = models.TextField()

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    highscore = models.IntegerField()