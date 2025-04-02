from django.contrib import admin
from .models import Course, Attendance, AccessCode
from .models import AccessCode

admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(AccessCode)


