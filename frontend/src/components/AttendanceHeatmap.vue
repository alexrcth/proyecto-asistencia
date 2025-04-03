<template>
    <div class="heatmap-container">
      <div class="heatmap-header">
        <h3>Mapa de calor de asistencia</h3>
        <div class="filter-controls">
          <select v-model="selectedCourse" class="course-selector">
            <option value="all">Todos los cursos</option>
            <option v-for="course in courses" :key="course.courseId" :value="course.courseId">
              {{ course.courseName }}
            </option>
          </select>
        </div>
      </div>
  
      <div class="legend">
        <div class="legend-item">
          <span class="legend-color" style="background-color: #4caf50;"></span>
          <span>Presente</span>
        </div>
        <div class="legend-item">
          <span class="legend-color" style="background-color: #f44336;"></span>
          <span>Ausente</span>
        </div>
        <div class="legend-item">
          <span class="legend-color" style="background-color: #ff9800;"></span>
          <span>Tardanza</span>
        </div>
        <div class="legend-item">
          <span class="legend-color" style="background-color: #9e9e9e;"></span>
          <span>Justificado</span>
        </div>
      </div>
  
      <div class="heatmap-scroll">
        <table class="heatmap-table">
          <thead>
            <tr>
              <th class="student-name-header">Estudiante</th>
              <th v-for="date in uniqueDates" :key="date">{{ formatDate(date) }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredStudents" :key="student.id">
              <td class="student-name">{{ student.name }}</td>
              <td v-for="date in uniqueDates" :key="date" class="attendance-cell">
                <div :class="getCellClass(student, date)" :title="getCellTitle(student, date)"></div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
  
      <div class="attendance-summary">
        <div class="summary-card">
          <div class="summary-title">Tasa de asistencia</div>
          <div class="summary-value">{{ attendanceRate }}%</div>
        </div>
        <div class="summary-card">
          <div class="summary-title">Ausencias</div>
          <div class="summary-value">{{ absenceRate }}%</div>
        </div>
        <div class="summary-card">
          <div class="summary-title">Tardanzas</div>
          <div class="summary-value">{{ lateRate }}%</div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AttendanceHeatmap',
    props: {
      // Permite que los datos sean pasados como prop o usar los datos internos
      attendanceData: {
        type: Array,
        default: null
      }
    },
    data() {
      return {
        selectedCourse: 'all',
        localAttendanceData: [
          {
            "courseId": "CS101",
            "courseName": "Introducción a la Programación",
            "students": [
              {"id": 1, "name": "Ana García", "attendance": [
                {"date": "2025-04-01", "status": "present"},
                {"date": "2025-04-03", "status": "present"},
                {"date": "2025-04-08", "status": "late"},
                {"date": "2025-04-10", "status": "present"}
              ]},
              {"id": 2, "name": "Carlos Pérez", "attendance": [
                {"date": "2025-04-01", "status": "present"},
                {"date": "2025-04-03", "status": "absent"},
                {"date": "2025-04-08", "status": "justified"},
                {"date": "2025-04-10", "status": "present"}
              ]}
            ]
          },
          {
            "courseId": "MTH205",
            "courseName": "Cálculo Avanzado",
            "students": [
              {"id": 3, "name": "Elena López", "attendance": [
                {"date": "2025-04-02", "status": "present"},
                {"date": "2025-04-04", "status": "present"},
                {"date": "2025-04-09", "status": "present"},
                {"date": "2025-04-11", "status": "late"}
              ]},
              {"id": 4, "name": "Daniel Torres", "attendance": [
                {"date": "2025-04-02", "status": "absent"},
                {"date": "2025-04-04", "status": "justified"},
                {"date": "2025-04-09", "status": "present"},
                {"date": "2025-04-11", "status": "present"}
              ]}
            ]
          }
        ]
      };
    },
    computed: {
      // Usa los datos proporcionados por prop o los datos locales
      courses() {
        const data = this.attendanceData || this.localAttendanceData;
        return data;
      },
      // Filtra estudiantes según el curso seleccionado
      filteredStudents() {
        const data = this.attendanceData || this.localAttendanceData;
        if (this.selectedCourse === 'all') {
          return data.flatMap(course => course.students);
        } else {
          const selectedCourseData = data.find(course => course.courseId === this.selectedCourse);
          return selectedCourseData ? selectedCourseData.students : [];
        }
      },
      // Obtiene todas las fechas únicas de los registros de asistencia
      uniqueDates() {
        const data = this.attendanceData || this.localAttendanceData;
        const allDates = new Set();
        
        data.forEach(course => {
          course.students.forEach(student => {
            student.attendance.forEach(record => {
              allDates.add(record.date);
            });
          });
        });
        
        return [...allDates].sort();
      },
      // Calcula estadísticas de asistencia
      attendanceStats() {
        const data = this.attendanceData || this.localAttendanceData;
        let present = 0;
        let absent = 0;
        let late = 0;
        let justified = 0;
        let total = 0;
        
        // Si hay un curso seleccionado, filtra por ese curso
        if (this.selectedCourse !== 'all') {
          const course = data.find(c => c.courseId === this.selectedCourse);
          if (course) {
            course.students.forEach(student => {
              student.attendance.forEach(record => {
                total++;
                if (record.status === 'present') present++;
                else if (record.status === 'absent') absent++;
                else if (record.status === 'late') late++;
                else if (record.status === 'justified') justified++;
              });
            });
          }
        } else {
          // Si no, cuenta todos
          data.forEach(course => {
            course.students.forEach(student => {
              student.attendance.forEach(record => {
                total++;
                if (record.status === 'present') present++;
                else if (record.status === 'absent') absent++;
                else if (record.status === 'late') late++;
                else if (record.status === 'justified') justified++;
              });
            });
          });
        }
        
        return { present, absent, late, justified, total };
      },
      // Calcula tasas para mostrar en los resúmenes
      attendanceRate() {
        const { present, total } = this.attendanceStats;
        return total > 0 ? Math.round((present / total) * 100) : 0;
      },
      absenceRate() {
        const { absent, justified, total } = this.attendanceStats;
        return total > 0 ? Math.round(((absent + justified) / total) * 100) : 0;
      },
      lateRate() {
        const { late, total } = this.attendanceStats;
        return total > 0 ? Math.round((late / total) * 100) : 0;
      }
    },
    methods: {
      // Formatea la fecha para mostrarla de manera más amigable
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('es-ES', { day: '2-digit', month: '2-digit' });
      },
      // Obtiene la clase CSS para las celdas del mapa de calor
      getCellClass(student, date) {
        const attendanceRecord = this.getAttendanceRecord(student, date);
        if (!attendanceRecord) return 'no-data';
        
        return `status-${attendanceRecord.status}`;
      },
      // Obtiene el título para mostrar al pasar el mouse sobre la celda
      getCellTitle(student, date) {
        const attendanceRecord = this.getAttendanceRecord(student, date);
        if (!attendanceRecord) return 'No hay datos';
        
        const statusMap = {
          'present': 'Presente',
          'absent': 'Ausente',
          'late': 'Tardanza',
          'justified': 'Ausencia justificada'
        };
        
        return `${student.name} - ${this.formatDate(date)}: ${statusMap[attendanceRecord.status]}`;
      },
      // Busca el registro de asistencia para un estudiante en una fecha específica
      getAttendanceRecord(student, date) {
        return student.attendance.find(record => record.date === date);
      }
    }
  };
  </script>
  
  <style scoped>
  .heatmap-container {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  }
  
  .heatmap-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .heatmap-header h3 {
    margin: 0;
    color: #333;
  }
  
  .filter-controls {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .course-selector {
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: white;
  }
  
  .legend {
    display: flex;
    gap: 15px;
    margin-bottom: 15px;
  }
  
  .legend-item {
    display: flex;
    align-items: center;
    font-size: 0.85rem;
  }
  
  .legend-color {
    display: inline-block;
    width: 15px;
    height: 15px;
    margin-right: 5px;
    border-radius: 3px;
  }
  
  .heatmap-scroll {
    overflow-x: auto;
    margin-bottom: 20px;
  }
  
  .heatmap-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 2px;
  }
  
  .heatmap-table th, .heatmap-table td {
    padding: 10px;
    text-align: center;
    white-space: nowrap;
  }
  
  .heatmap-table th {
    background-color: #f5f5f5;
    font-weight: 500;
  }
  
  .student-name-header {
    position: sticky;
    left: 0;
    background-color: #f5f5f5;
    z-index: 1;
    min-width: 150px;
    text-align: left;
  }
  
  .student-name {
    position: sticky;
    left: 0;
    background-color: white;
    z-index: 1;
    font-weight: 500;
    text-align: left;
  }
  
  .attendance-cell {
    padding: 5px;
  }
  
  .attendance-cell div {
    width: 25px;
    height: 25px;
    border-radius: 4px;
    margin: 0 auto;
  }
  
  .status-present {
    background-color: #4caf50;
  }
  
  .status-absent {
    background-color: #f44336;
  }
  
  .status-late {
    background-color: #ff9800;
  }
  
  .status-justified {
    background-color: #9e9e9e;
  }
  
  .no-data {
    background-color: #f5f5f5;
  }
  
  .attendance-summary {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 15px;
    margin-top: 20px;
  }
  
  .summary-card {
    background-color: #f9f9f9;
    border-radius: 6px;
    padding: 15px;
    text-align: center;
  }
  
  .summary-title {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 8px;
  }
  
  .summary-value {
    font-size: 1.8rem;
    font-weight: 600;
    color: #333;
  }
  
  @media (max-width: 768px) {
    .heatmap-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }
    
    .legend {
      flex-wrap: wrap;
    }
    
    .attendance-summary {
      grid-template-columns: 1fr;
    }
  }
  </style>