from rest_framework import serializers
from .models import Course, Attendance
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'instructor', 'access_code']

class AttendanceSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'course', 'date', 'latitude', 'longitude', 'is_present']