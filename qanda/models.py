""""
class Category(models.Model):
    name = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.name
"""

from django.db import models
from account.models import MyUser
# Create your models here.



class Question(models.Model):
    question = models.TextField()
    created_by = models.ForeignKey(MyUser)
    created_on = models.DateTimeField(auto_now_add=True)
    #category = models.ManyToManyField(Category)

    def __str__(self):
        return self.question
	


class Answer(models.Model):
    question = models.ForeignKey(Question)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(MyUser)
    text = models.TextField()

    def __str__(self):
        return self.text
