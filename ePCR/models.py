from django.db import models

class EPCR(models.Model):
    incident_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField(blank=True)
    incident_details = models.TextField()
    responding_unit = models.CharField(max_length=100)
    personnel = models.TextField()
    assessment_findings = models.TextField(blank=True)
    treatments = models.TextField(blank=True)
    outcome = models.TextField(blank=True)
    alcohol_involved = models.BooleanField(default=False)
    overdose_type = models.CharField(max_length=100)
    signature = models.TextField() # base64 encoded image

    def __str__(self):
        return self.incident_number

