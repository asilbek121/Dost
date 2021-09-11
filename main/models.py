from django.db import models

# Create your models here.
class Hero_S(models.Model):
    img = models.ImageField(upload_to='img')
    title = models.CharField(max_length=255)
    p = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class About_S(models.Model):
    title = models.CharField(max_length=255)
    p = models.CharField(max_length=255)
    text_1 = models.CharField(max_length=255)
    text_2 = models.CharField(max_length=255)
    text_3 = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img', blank=True)

    def __str__(self):
        return self.title

class Counts_S(models.Model):
    Obunachilar = models.CharField(max_length=255)
    Musics = models.CharField(max_length=255)
    Homiylar = models.CharField(max_length=255)
    Albomlar = models.CharField(max_length=255)

    def __str__(self):
        return self.Obunachilar

class Features_S(models.Model):
    title = models.CharField(max_length=300)
    text_1 = models.CharField(max_length=255)
    text_2 = models.CharField(max_length=255)
    text_3 = models.CharField(max_length=255)
    text_4 = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Pricing_S(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    text_1 = models.CharField(max_length=255)
    text_2 = models.CharField(max_length=255)
    text_3 = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Questions_S(models.Model):
    title = models.CharField(max_length=255)
    text_1 = models.CharField(max_length=255)
    text_2 = models.CharField(max_length=255)
    text_3 = models.CharField(max_length=255)
    text_4 = models.CharField(max_length=255)
    text_5 = models.CharField(max_length=255)
    text_6 = models.CharField(max_length=255, blank=True)
    text_7 = models.CharField(max_length=255, blank=True)
    text_8 = models.CharField(max_length=255, blank=True)
    text_9 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title




# song model
class Song(models.Model):
    sond_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    tags = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    song = models.FileField(upload_to='img')

    def __str__(self):
        return self.name