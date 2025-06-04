from django.db import models
from .ticket import Ticket
from users.models import User

LOCATION = (
    ("ITL", "ITL"),
    ("ITS", "ITS"),
    ("MySIS", "MySIS"),
    ("QM+", "QM+"),
)

TECH_FAULT_STATUS = (
    ("Pending", "Pending"),
    ("Resolved", "Resolved")
)

class TechFault(Ticket):
    explanation = models.TextField()
    location = models.CharField(max_length=10, choices=LOCATION, default=LOCATION[0])
    status = models.CharField(max_length=10, choices=TECH_FAULT_STATUS, default=TECH_FAULT_STATUS[0])
    assigned_to = models.ForeignKey(to=User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'tech_fault_handler'})


class TechFaultFileUploads(models.Model):
    ticket = models.ForeignKey(to=TechFault, related_name="files", on_delete=models.CASCADE)
    file = models.FileField(upload_to="tech_fault_evidence/")
    uploaded_at = models.DateField(auto_now_add=True)