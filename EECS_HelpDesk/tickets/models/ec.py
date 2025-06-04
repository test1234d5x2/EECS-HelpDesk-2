from django.db import models
from .ticket import Ticket
from users.models import User
from modules.models import Module


EC_STATUS = (
    ("Pending", "Pending"),
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected")
)

NATURE_OF_CIRCUMSTANCE = (
    ("Bereavement", "Bereavement"),
    ("Crime", "Crime"),
    ("Major unforseeable travel disruption", "Major unforseeable travel disruption"),
    ("Mental Health: acute episode", "Mental Health: acute episode"),
    ("Mental Health: long-term condition", "Mental Health: long-term condition"),
    ("Minor illness/medical reasons", "Minor illness/medical reasons"),
    ("Physical Health: long-term condition", "Physical Health: long-term condition"),
    ("Severe illness/medical reasons: acute episode", "Severe illness/medical reasons: acute episode"),
    ("Other", "Other")
)


REQUESTED_OUTCOME = (
    ("Non-Submission", "Non-Submission"),
    ("Non-Attendance", "Non-Attendance"),
)


ASSESSMENT_TYPE = (
    ("Demontrastion", "Demontrastion"),
    ("In-Module Examination", "In-Module Examination"),
    ("Coursework Submission", "Coursework Submission"),
    ("Examination", "Examination")
)

class EC(Ticket):
    assigned_to = models.ForeignKey(to=User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'ec_handler'})
    nature_of_circumstance = models.CharField(max_length=50, choices=NATURE_OF_CIRCUMSTANCE, default=NATURE_OF_CIRCUMSTANCE[-1])
    further_explanation = models.TextField()
    module_code = models.ForeignKey(to=Module, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=25, choices=ASSESSMENT_TYPE, default=ASSESSMENT_TYPE[0])
    assessment_submission_date = models.DateField()
    requested_outcome = models.CharField(max_length=20, choices=REQUESTED_OUTCOME, default=REQUESTED_OUTCOME[0])
    requested_extended_deadline_date = models.DateField()
    status = models.CharField(max_length=10, choices=EC_STATUS, default=EC_STATUS[0])


class ECFileUploads(models.Model):
    ticket = models.ForeignKey(to=EC, related_name="files", on_delete=models.CASCADE)
    file = models.FileField(upload_to="ec_evidence/")
    uploaded_at = models.DateField(auto_now_add=True)