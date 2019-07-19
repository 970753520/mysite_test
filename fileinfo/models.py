from django.db import models

# Create your models here.
class Fileinfo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    #修改模型
    def __str__(self):
        return "<标题:%s>"%self.title
