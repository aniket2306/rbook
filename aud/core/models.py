from django.db import models

#postgress only field
#from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model


User = get_user_model()
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


class Book(models.Model):

    name=models.CharField(max_length=500, blank=False, null=False, )    
    author=models.CharField(max_length=300, null=False, default='Unknown')
    description=models.TextField(null=False, default="No description added, click edit to add description")
    narrator = models.CharField(max_length=500, blank=True, null=False, default='Unknown')
    

    def __str__(self):
        return self.name



class AudioBookReviewItem(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.TextField(blank=False, null=False, default="!@#")
    add_date = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(choices=SCORE_CHOICES, blank=True, null=True, db_index=True)
    upvotes = models.IntegerField(blank=True, null=False, default=0)
    downvotes = models.IntegerField(blank=True, null=False, default=0)
