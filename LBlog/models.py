from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=256) #제목
    writer = models.CharField(max_length=50)#작성자
    content = models.TextField() #내용 
    