from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from users.models import User

MODULE_CODE_REGEX = r'ECS[0-9]{3}[A-Z]'

MODULE_CODE_VALIDATOR = RegexValidator(MODULE_CODE_REGEX)

# Create your models here.
class Module(models.Model):
    code = models.CharField(max_length=9, validators=[MODULE_CODE_VALIDATOR], primary_key=True)
    name = models.TextField()



class Enrollment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    module = models.ForeignKey(to=Module, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'module']

    def clean(self):
        if self.user and self.user.user_type != "student":
            raise ValidationError({
                "user": "User must be a student."
            })
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)