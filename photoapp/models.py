from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from unicodedata import name
import uuid
from django.db import models
from ckeditor.fields import RichTextField
import uuid

# Create your models here.

class Pictures(models.Model):
    name = models.CharField(max_length=150)
    body = RichTextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    category = models.ManyToManyField('Category')
    image = models.ImageField(upload_to='new_image')
    
    class Meta:
        verbose_name = ('Picture')
        verbose_name_plural = ('Pictures')
        
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Category')
        
    def __str__(self):
        return self.name