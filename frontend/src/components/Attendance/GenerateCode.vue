<template>
    <div class="container mt-5">
      <h2>Generar Código de Asistencia</h2>
      
      <div v-if="error" class="alert alert-danger">{{ error }}</div>
      
      <div class="form-group">
        <label>Seleccionar Curso</label>
        <select 
          class="form-control" 
          v-model="selectedCourse"
        >
          <option value="">Seleccione un curso</option>
          <option v-for="course in courses" :key="course.id" :value="course.id">
            {{ course.name }}
          </option>
        </select>
      </div>
      
      <button 
        class="btn btn-primary mb-4" 
        @click="generateNewCode"
        :disabled="loading || !selectedCourse"
      >
        {{ loading ? 'Generando...' : 'Generar Código' }}
      </button>
      
      <div v-if="code" class="code-display">
        <h3>Código Generado:</h3>
        <div class="code-box">{{ code }}</div>
        <p class="text-muted">Este código es temporal y válido por 15 minutos.</p>
      </div>
    </div>
  </template>
  
  <script>
  import api from '@/services/api';
  
  export default {
    name: 'GenerateCode',
    data() {
      return {
        courses: [],
        selectedCourse: '',
        code: '',
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
          const response = await api.get('courses/?instructor=me');
          this.courses = response.data;
        } catch (err) {
          this.error = 'Error al cargar cursos';
        }
      },
      async generateNewCode() {
        if (!this.selectedCourse) {
          this.error = 'Por favor seleccione un curso';
          return;
        }
  
        this.loading = true;
        try {
          const response = await api.post(`courses/${this.selectedCourse}/generate_code/`);
          this.code = response.data.access_code;
          this.error = '';
        } catch (err) {
          this.error = 'Error al generar código';
        } finally {
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
  .code-display {
    margin-top: 20px;
    text-align: center;
  }
  .code-box {
    font-size: 40px;
    font-weight: bold;
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 5px;
    margin: 15px 0;
    letter-spacing: 5px;
  }
  </style>