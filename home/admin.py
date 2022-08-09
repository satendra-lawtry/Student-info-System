from django.contrib import admin
from .models import Student,Trainer,Batch,Joined

# Register your models here.
admin.site.register(Student)
admin.site.register(Trainer)
admin.site.register(Batch)
admin.site.register(Joined)
