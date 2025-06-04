from django.db import models
from users.models import User


class Ticket(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    student = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, limit_choices_to={'user_type': 'student'}, related_name="%(class)s_tickets")
    date_submitted = models.DateField(auto_now=True, null=False)

    class Meta:
        abstract = True
