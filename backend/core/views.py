from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Attendance
from .serializers import CourseSerializer, AttendanceSerializer
from .utils import is_location_valid
import random
import string

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def generate_unique_access_code(self):
        """Generar código de acceso único"""
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if not Course.objects.filter(access_code=code).exists():
                return code

    def create(self, request):
        """Añadir código de acceso al crear un curso"""
        request.data['access_code'] = self.generate_unique_access_code()
        return super().create(request)

    @action(detail=True, methods=['POST'])
    def mark_attendance(self, request, pk=None):
        """Marcar asistencia para un curso"""
        course = self.get_object()
        student = request.user
        latitude = request.data.get('latitude', 0)
        longitude = request.data.get('longitude', 0)
        access_code = request.data.get('access_code', '')  # Obtener el código de acceso del request

        # Validar código de acceso
        if access_code != course.access_code:
            return Response({'error': 'Código de acceso inválido'}, status=400)

        # Generar nuevo código
        course.access_code = self.generate_unique_access_code()
        course.save()

        # Validar ubicación si el curso tiene coordenadas definidas
        location_valid = True
        if course.classroom_latitude and course.classroom_longitude:
            location_valid = is_location_valid(
                course.classroom_latitude, 
                course.classroom_longitude,
                latitude, 
                longitude,
                course.max_distance
            )

        # Crear registro de asistencia
        attendance = Attendance.objects.create(
            student=student,
            course=course,
            latitude=latitude,
            longitude=longitude,
            is_present=location_valid
        )

        serializer = AttendanceSerializer(attendance)
        return Response({
            'attendance': serializer.data,
            'location_valid': location_valid,
            'new_access_code': course.access_code
        })

    @action(detail=True, methods=['GET'])
    def attendance_report(self, request, pk=None):
        """Generar reporte de asistencia para el curso"""
        course = self.get_object()
        
        # Verificar que es el instructor
        if request.user != course.instructor:
            return Response({'error': 'Acceso denegado'}, status=403)
        
        # Obtener todos los registros de asistencia
        attendances = Attendance.objects.filter(course=course)
        
        # Agrupar por estudiante
        report = {}
        for attendance in attendances:
            student_id = attendance.student.id
            if student_id not in report:
                report[student_id] = {
                    'student': {
                        'id': attendance.student.id,
                        'username': attendance.student.username,
                        'email': attendance.student.email
                    },
                    'attendances': []
                }
            
            report[student_id]['attendances'].append({
                'date': attendance.date,
                'is_present': attendance.is_present
            })
        
        return Response(list(report.values()))

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
