
#postgress only field
#from django.contrib.postgres.fields import ArrayField

#normal fields
from django.db import models
from django.contrib.auth import get_user_model

#custom modules import
from core.models import Book
# Create your models here.

#extra data
User = get_user_model()

STATUS_CHOICES = (
    ('CL','Currently Listening'),
    ('PTL', 'Plan to Listen'),
    ('CMP','Completed'),
    ('DRP','Dropped midway')
)
SCORE_CHOICES = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10)
)

class ProfileData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, null=True, blank=True)
    dateJoined = models.DateField(blank=True, null=True)
    userIsPremium = models.BooleanField(blank=True, null=False, default=False)
    recCount = models.IntegerField(blank=True, null=False, default=0)
    favCount = models.IntegerField(blank=True, null=False, default=0)
    followersCount = models.IntegerField(blank=True, null=False, default=0)
    followingCount = models.IntegerField(blank=True, null=False, default=0)

class BookListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=True, null=False, db_index=True, default= 'CL')
    score = models.IntegerField(choices=SCORE_CHOICES, blank=True, null=True, db_index=True)
    add_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.IntegerField(blank=True, null=False, default=0)
    downvotes = models.IntegerField(blank=True, null=False, default=0)
    isModified = models.BooleanField(default=False)


class RecommendedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    add_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True) 

class FavouritesList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(BookListItem, on_delete = models.CASCADE)
    add_date = models.DateTimeField(blank=True, null=True)

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='concernedUser')
    userFollowing = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followedUser')
    
