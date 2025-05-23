from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cif = models.CharField(max_length=20, unique=True) # Distancia máxima en metros

    def __str__(self):
        return f"{self.user.username} - {self.cif}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    access_code = models.CharField(max_length=50, default='DEFAULT_CODE')
    classroom_latitude = models.FloatField(null=True, blank=True)
    classroom_longitude = models.FloatField(null=True, blank=True)
    max_distance = models.IntegerField(default=50)  # Distancia máxima en metros
class AccessCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

class Attendance(models.Model):  # <-- Debe estar fuera de Course
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.date}"
