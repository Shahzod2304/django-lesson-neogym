from pyclbr import Class
from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length = 50)
    disc = models.CharField(max_length = 255)

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Home carusel"
        verbose_name_plural = "Home carusel"
    
class Why(models.Model):
    icon_select = (
        ('gantel','Гантель'),
        ('banka', 'Банка'),
        ('bike','Велик'),
        ('timer','Таймер')        
    )
    title = models.CharField(max_length = 50)
    disc = models.TextField()
    icon = models.CharField(choices=icon_select, max_length = 50)

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Why"
        verbose_name_plural = "Why"
    
class HomeContent(models.Model):
    title = models.CharField(max_length = 50)
    disc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Home content"
        verbose_name_plural = "Home content"

class Trainer(models.Model):
    full_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/trainer', default = '/static/images/defoult-avatar-icon', blank = True, null = True)
    facebook = models.URLField(blank = True, null = True)
    twitter = models.URLField(blank = True, null = True)
    instagram = models.URLField(blank = True, null = True)

    def __str__(self):
        return self.full_name
    
class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

class Footer(models.Model):
    location = models.URLField()
    phone_number = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 50)
    footer_text = models.CharField(max_length=100)

    def __str__(self):
        return "Нижняя часть сайта"
    
    class Meta():
        verbose_name = "Footer data"
        verbose_name_plural = "Footer data"