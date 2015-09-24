from django.db import models

# Create your models here.
class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)

class BBS_user(models.Model):
# fix it
    name = models.CharField(max_length=50)
    signature = models.CharField(max_length=128)
    photo = models.FileField()

