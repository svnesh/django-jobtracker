from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Project)
#admin.site.register(ProjectHandle)
admin.site.register(Tracker)