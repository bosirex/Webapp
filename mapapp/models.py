from django.db import models

class Credential(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    acceleration = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



class Incidents(models.Model):
    UUID = models.CharField(max_length=255, unique=True)  # set as primary key
    UUID_Serial = models.CharField(max_length=250, null=True, blank=True)
    incident_number = models.CharField(max_length=100, unique=True)
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

class needHelp(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    seat = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    category = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



# Assuming needHelp is another model you might have defined elsewhere. If not, you'd have to define it in this models.py as well.
class Assignment(models.Model):
    incident = models.ForeignKey('needHelp', on_delete=models.CASCADE)  # Quoted 'needHelp' in case it's defined later in the file or is imported from elsewhere.
    responder = models.ForeignKey(Credential, on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.incident.username} assigned to {self.responder.username}"

class Message(models.Model):
    sender = models.ForeignKey(Credential, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Credential, related_name='received_messages', on_delete=models.CASCADE)
    message_text = models.CharField(max_length=175)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"
#send message



class VenueName(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    capacity = models.PositiveIntegerField(default=0)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name




