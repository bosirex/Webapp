from django.contrib import admin
from .models import Credential,needHelp,Incidents,Message,Assignment,VenueName

admin.site.register(Credential)
admin.site.register(needHelp)
admin.site.register(Incidents)
admin.site.register(Message)
admin.site.register(Assignment)
admin.site.register(VenueName)
