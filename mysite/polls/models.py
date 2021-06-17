from django.db import models

# Create your models here.
# 用于新建类
class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    info = models.CharField(max_length=20)