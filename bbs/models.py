from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User,null=True)
    signature = models.CharField(max_length=128,default='lazy guy,nothing left')
    #photo = models.ImageField(upload_to='upload_imgs/',dufault='upload_imgs/u=1678328676,1216794096&fm=23&gp=0.jpg')
    photo = models.ImageField(upload_to='upload_imgs/',null=True)
    def __unicode__(self):
        return self.user.username

