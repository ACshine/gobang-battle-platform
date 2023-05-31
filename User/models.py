from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.
class Player(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.URLField(max_length=256,blank=True)
    photo='https://cdn.acwing.com/media/user/profile/photo/152778_lg_96889ae88e.jpg'
    coins=models.DecimalField(default=100.50,max_digits=15, decimal_places=2)
    fanscount=models.IntegerField(default=0)
    is_sign_in=models.BooleanField(default=False)
    sign_in_coins=models.DecimalField(default=0,max_digits=15, decimal_places=2)
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False,
    )


    def __str__(self):#to_string函数
        return str(self.user)+' '+str(self.coins)+' '+str(self.fanscount)

class Post(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE,related_name='posts',default='')
    content=models.TextField(max_length=1000,default='')
    def __str__(self):
        return str(self.content)

    class Meta:
        ordering = ['-id']
