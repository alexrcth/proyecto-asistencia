// src/services/attendance.service.js
import api from './api';

export const marcarAsistencia = async (courseId, accessCode, latitude, longitude) => {
  const response = await api.post(`courses/${courseId}/mark_attendance/`, {
    access_code: accessCode,
    latitude,
    longitude
  });
  return response.data;
};

export const obtenerReporteAsistencia = async (courseId) => {
  const response = await api.get(`courses/${courseId}/attendance_report/`);
  return response.data;
};
