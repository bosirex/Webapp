from django.db import models



class Incidents(models.Model):
    UUID = models.CharField(max_length=255, unique=True)  # set as primary key
    UUID_Serial = models.CharField(max_length=250, null=True, blank=True)
    incident_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    seating = models.CharField(max_length=100, null=True, blank=True)
    type_incident = models.CharField(max_length=100)  # Assuming a max_length of 100 here too
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    unit_responding = models.CharField(max_length=100, blank=True)  # Assuming a max_length of 100
    response_timestamp = models.DateTimeField(null=True, blank=True)  # Assuming DateTimeField
    on_location_time = models.DateTimeField(null=True, blank=True)  # Assuming DateTimeField
    transport = models.BooleanField(default=False)  # Assuming a boolean, where True means there was transport and False means there wasn't
    additional_resources = models.TextField(null=True, blank=True)  # Assuming a TextField for a larger text area
    age = models.IntegerField(null=True, blank=True,)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)
    injury = models.TextField(null=True, blank=True)  # Assuming a TextField for description of injuries
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    contacts = models.CharField(max_length=150, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)  # Assuming a US-style zipcode

    def __str__(self):
        return f"{self.incident_number}"
