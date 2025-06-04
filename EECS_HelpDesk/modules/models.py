from django.db import models
from django.core.validators import RegexValidator


MODULE_CODE_REGEX = r'ECS[0-9]{3}[A-Z]'

MODULE_CODE_VALIDATOR = RegexValidator(MODULE_CODE_REGEX)

# Create your models here.
class Module(models.Model):
    code = models.CharField(max_length=7, validators=[MODULE_CODE_VALIDATOR], primary_key=True)
    name = models.TextField()