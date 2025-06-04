from django.db import models

# Create your models here.
class FAQs(models.Model):
    question = models.TextField()
    answer = models.TextField()