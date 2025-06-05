from django.contrib import admin
from .models import EC, ECFileUploads, TechFault, TechFaultFileUploads

# Register your models here.
admin.site.register(EC)
admin.site.register(ECFileUploads)
admin.site.register(TechFault)
admin.site.register(TechFaultFileUploads)