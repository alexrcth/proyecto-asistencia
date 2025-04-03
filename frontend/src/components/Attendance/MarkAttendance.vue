<template>
    <div class="container mt-5">
      <h2>Marcar Asistencia</h2>
      
      <div v-if="error" class="alert alert-danger">{{ error }}</div>
      <div v-if="message" class="alert alert-success">{{ message }}</div>
      
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label>Seleccionar Curso</label>
          <select 
            class="form-control" 
            v-model="courseId" 
            required
          >
            <option value="">Seleccione un curso</option>
            <option v-for="course in courses" :key="course.id" :value="course.id">
              {{ course.name }}
            </option>
          </select>
        </div>
        
        <div class="form-group">
          <label>Código de Asistencia</label>
          <input 
            type="text" 
            class="form-control" 
            v-model="code" 
            placeholder="Ingrese el código"
            required
          />
        </div>
        
        <button 
          type="submit" 
          class="btn btn-primary"
          :disabled="loading"
        >
          {{ loading ? 'Procesando...' : 'Marcar Asistencia' }}
        </button>
      </form>
    </div>
  </template>
  
  <script>
  import api from '@/services/api';
  
  export default {
  name: 'MarkAttendanceView',
    data() {
      return {
        code: '',
        courseId: '',
        courses: [],
        message: '',
        error: '',
        loading: false
      };
    },
    mounted() {
      this.fetchCourses();
    },
    methods: {
      async fetchCourses() {
        try {
          const response = await api.get('courses/');
          this.courses = response.data;
        } catch (err) {
          this.error = 'Error al cargar cursos';
        }
      },
      async handleSubmit() {
        this.loading = true;
        this.message = '';
        this.error = '';
  
        try {
          navigator.geolocation.getCurrentPosition(
            async (position) => {
              const { latitude, longitude } = position.coords;
              
              try {
                const response = await api.post(`courses/${this.courseId}/mark_attendance/`, {
                  access_code: this.code,
                  latitude,
                  longitude
                });
                
                this.message = response.data.location_valid 
                  ? 'Asistencia registrada exitosamente' 
                  : 'Asistencia registrada pero fuera del área permitida';
                
                this.loading = false;
              } catch (err) {
                this.error = 'Error al registrar asistencia: ' + (err.response?.data?.error || 'Error desconocido');
                this.loading = false;
              }
            },
            (err) => {
              this.error = 'Error al obtener ubicación: ' + err.message;
              this.loading = false;
            },
            { enableHighAccuracy: true }
          );
        } catch (err) {
          this.error = 'Error al procesar la solicitud';
          this.loading = false;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .form-group {
    margin-bottom: 15px;
  }
  .btn {
    margin-top: 10px;
  }
  </style>