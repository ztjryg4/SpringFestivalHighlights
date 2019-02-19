from django.db import models

# Create your models here.

class RawImg(models.Model):
    code = models.CharField(max_length=8,default='code')
    # img_01 = models.ImageField(upload_to='./upload/')
    # img_02 = models.ImageField(upload_to='./upload/')
    # img_03 = models.ImageField(upload_to='./upload/')
    # img_04 = models.ImageField(upload_to='./upload/')
    # img_05 = models.ImageField(upload_to='./upload/')
    # img_06 = models.ImageField(upload_to='./upload/')
    # img_07 = models.ImageField(upload_to='./upload/')
    # img_08 = models.ImageField(upload_to='./upload/')
    # img_09 = models.ImageField(upload_to='./upload/')
    # img_10 = models.ImageField(upload_to='./upload/')
    # img_11 = models.ImageField(upload_to='./upload/')
    # img_12 = models.ImageField(upload_to='./upload/')
    # img_13 = models.ImageField(upload_to='./upload/')
    # img_14 = models.ImageField(upload_to='./upload/')
    # img_15 = models.ImageField(upload_to='./upload/')
    # img_16 = models.ImageField(upload_to='./upload/')
    # img_17 = models.ImageField(upload_to='./upload/')
    # img_18 = models.ImageField(upload_to='./upload/')
    # img_19 = models.ImageField(upload_to='./upload/')
    # img_20 = models.ImageField(upload_to='./upload/')
    # img_21 = models.ImageField(upload_to='./upload/')
    # img_22 = models.ImageField(upload_to='./upload/')
    # img_23 = models.ImageField(upload_to='./upload/')
    # img_24 = models.ImageField(upload_to='./upload/')
    # img_25 = models.ImageField(upload_to='./upload/')
    # img_26 = models.ImageField(upload_to='./upload/')
    # img_27 = models.ImageField(upload_to='./upload/')
    def __str__(self):
        return self.username