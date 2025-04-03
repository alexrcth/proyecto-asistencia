<template>
    <div class="attendance-heatmap">
      <div class="controls">
        <div class="filter-group">
          <label for="course-select">Curso:</label>
          <select id="course-select" v-model="selectedCourse">
            <option value="all">Todos los cursos</option>
            <option v-for="course in courses" :key="course.id" :value="course.id">
              {{ course.name }}
            </option>
          </select>
        </div>
        
        <div class="filter-group">
          <label for="month-select">Mes:</label>
          <select id="month-select" v-model="selectedMonth">
            <option value="all">Todo el semestre</option>
            <option value="1">Enero</option>
            <option value="2">Febrero</option>
            <option value="3">Marzo</option>
            <option value="4">Abril</option>
            <option value="5">Mayo</option>
            <option value="6">Junio</option>
            <option value="7">Julio</option>
            <option value="8">Agosto</option>
            <option value="9">Septiembre</option>
            <option value="10">Octubre</option>
            <option value="11">Noviembre</option>
            <option value="12">Diciembre</option>
          </select>
        </div>
        
        <button @click="exportData" class="btn-export">
          Exportar datos
        </button>
      </div>
  
      <div class="heatmap-container">
        <table class="attendance-table">
          <thead>
            <tr>
              <th class="header-cell">Estudiante</th>
              <th v-for="date in displayDates" :key="date.id" class="date-cell">
                {{ formatDate(date) }}
              </th>
              <th class="summary-cell">Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredData" :key="student.id">
              <td class="student-cell">{{ student.name }}</td>
              <td 
                v-for="date in displayDates" 
                :key="`${student.id}-${date.id}`" 
                class="attendance-cell"
                :class="getAttendanceClass(student.attendance[date.id])"
              >
                {{ getAttendanceSymbol(student.attendance[date.id]) }}
              </td>
              <td class="summary-cell">{{ calculateAttendanceRate(student) }}%</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div class="legend">
        <div class="legend-item">
          <span class="legend-color present"></span>
          <span>Presente</span>
        </div>
        <div class="legend-item">
          <span class="legend-color absent"></span>
          <span>Ausente</span>
        </div>
        <div class="legend-item">
          <span class="legend-color late"></span>
          <span>Tardanza</span>
        </div>
        <div class="legend-item">
          <span class="legend-color justified"></span>
          <span>Justificado</span>
        </div>
        <div class="legend-item">
          <span class="legend-color no-class"></span>
          <span>Sin clase</span>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AttendanceHeatmap',
    props: {
      data: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
        selectedCourse: 'all',
        selectedMonth: 'all',
        // Datos de ejemplo - reemplazar con datos reales de la API
        students: [
          {
            id: 1,
            name: "Ana García",
            courseId: "cs101",
            attendance: {
              "2025-04-01": "present",
              "2025-04-03": "present",
              "2025-04-08": "late",
              "2025-04-10": "present",
              "2025-04-15": "present",
              "2025-04-17": "absent",
              "2025-04-22": "justified",
              "2025-04-24": "present",
              "2025-04-29": "present"
            }
          },
          {
            id: 2,
            name: "Carlos López",
            courseId: "cs101",
            attendance: {
              "2025-04-01": "present",
              "2025-04-03": "absent",
              "2025-04-08": "absent",
              "2025-04-10": "present",
              "2025-04-15": "present",
              "2025-04-17": "present",
              "2025-04-22": "present",
              "2025-04-24": "late",
              "2025-04-29": "present"
            }
          },
          {
            id: 3,
            name: "Elena Ramírez",
            courseId: "cs101",
            attendance: {
              "2025-04-01": "present",
              "2025-04-03": "present",
              "2025-04-08": "present",
              "2025-04-10": "present",
              "2025-04-15": "justified",
              "2025-04-17": "justified",
              "2025-04-22": "present",
              "2025-04-24": "present",
              "2025-04-29": "late"
            }
          },
          {
            id: 4,
            name: "Juan Martínez",
            courseId: "math202",
            attendance: {
              "2025-04-02": "present",
              "2025-04-04": "absent",
              "2025-04-09": "present",
              "2025-04-11": "present",
              "2025-04-16": "late",
              "2025-04-18": "present",
              "2025-04-23": "present",
              "2025-04-25": "present",
              "2025-04-30": "present"
            }
          },
          {
            id: 5,
            name: "María Rodríguez",
            courseId: "math202",
            attendance: {
              "2025-04-02": "late",
              "2025-04-04": "present",
              "2025-04-09": "present",
              "2025-04-11": "absent",
              "2025-04-16": "present",
              "2025-04-18": "present",
              "2025-04-23": "justified",
              "2025-04-25": "present",
              "2025-04-30": "present"
            }
          }
        ],
        courses: [
          { id: "cs101", name: "Programación I" },
          { id: "math202", name: "Cálculo Avanzado" }
        ],
        dates: [
          { id: "2025-04-01", month: 4 },
          { id: "2025-04-02", month: 4 },
          { id: "2025-04-03", month: 4 },
          { id: "2025-04-04", month: 4 },
          { id: "2025-04-08", month: 4 },
          { id: "2025-04-09", month: 4 },
          { id: "2025-04-10", month: 4 },
          { id: "2025-04-11", month: 4 },
          { id: "2025-04-15", month: 4 },
          { id: "2025-04-16", month: 4 },
          { id: "2025-04-17", month: 4 },
          { id: "2025-04-18", month: 4 },
          { id: "2025-04-22", month: 4 },
          { id: "2025-04-23", month: 4 },
          { id: "2025-04-24", month: 4 },
          { id: "2025-04-25", month: 4 },
          { id: "2025-04-29", month: 4 },
          { id: "2025-04-30", month: 4 }
        ]
      };
    },
    computed: {
      filteredData() {
        let studentsList = [...this.students];
        
        // Filtrar por curso si se ha seleccionado un curso específico
        if (this.selectedCourse !== 'all') {
          studentsList = studentsList.filter(student => student.courseId === this.selectedCourse);
        }
        
        return studentsList;
      },
      displayDates() {
        let datesList = [...this.dates];
        
        // Filtrar por mes si se ha seleccionado un mes específico
        if (this.selectedMonth !== 'all') {
          datesList = datesList.filter(date => date.month === parseInt(this.selectedMonth));
        }
        
        return datesList;
      }
    },
    methods: {
      formatDate(date) {
        const d = new Date(date.id);
        return d.getDate();
      },
      getAttendanceClass(status) {
        if (!status) return 'no-class';
        return status;
      },
      getAttendanceSymbol(status) {
        switch(status) {
          case 'present': return '✓';
          case 'absent': return '✗';
          case 'late': return 'L';
          case 'justified': return 'J';
          default: return '-';
        }
      },
      calculateAttendanceRate(student) {
        const attendanceValues = Object.values(student.attendance);
        if (attendanceValues.length === 0) return 0;
        
        const present = attendanceValues.filter(status => status === 'present' || status === 'late').length;
        return Math.round((present / attendanceValues.length) * 100);
      },
      exportData() {
        // Aquí implementarías la lógica para exportar los datos
        alert('Exportando datos de asistencia...');
      }
    }
  };
  </script>
  
  <style scoped>
  .attendance-heatmap {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 20px;
    width: 100%;
    overflow-x: auto;
  }
  
  .controls {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }
  
  .filter-group {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  
  .filter-group label {
    font-weight: 500;
    color: #444;
  }
  
  .filter-group select {
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: white;
  }
  
  .btn-export {
    margin-left: auto;
    background-color: #3498db;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
    transition: background-color 0.2s;
  }
  
  .btn-export:hover {
    background-color: #2980b9;
  }
  
  .heatmap-container {
    overflow-x: auto;
    max-width: 100%;
  }
  
  .attendance-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
  }
  
  .header-cell {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: left;
    font-weight: 600;
    border-bottom: 2px solid #ddd;
    position: sticky;
    top: 0;
  }
  
  .date-cell {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
    font-weight: 600;
    min-width: 40px;
    border-bottom: 2px solid #ddd;
  }
  
  .summary-cell {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
    font-weight: 600;
    min-width: 60px;
    border-bottom: 2px solid #ddd;
  }
  
  .student-cell {
    padding: 10px;
    font-weight: 500;
    border-bottom: 1px solid #eee;
    white-space: nowrap;
    background-color: #f9f9f9;
    position: sticky;
    left: 0;
  }
  
  .attendance-cell {
    padding: 10px;
    text-align: center;
    border-bottom: 1px solid #eee;
    font-weight: 500;
  }
  
  /* Colores para los diferentes estados de asistencia */
  .present {
    background-color: rgba(46, 204, 113, 0.2);
    color: #27ae60;
  }
  
  .absent {
    background-color: rgba(231, 76, 60, 0.2);
    color: #c0392b;
  }
  
  .late {
    background-color: rgba(241, 196, 15, 0.2);
    color: #f39c12;
  }
  
  .justified {
    background-color: rgba(52, 152, 219, 0.2);
    color: #2980b9;
  }
  
  .no-class {
    background-color: #f5f5f5;
    color: #bbb;
  }
  
  .legend {
    display: flex;
    gap: 15px;
    margin-top: 20px;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 14px;
  }
  
  .legend-color {
    display: inline-block;
    width: 16px;
    height: 16px;
    border-radius: 4px;
  }
  
  @media (max-width: 768px) {
    .controls {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .btn-export {
      margin-left: 0;
    }
  }
  </style>