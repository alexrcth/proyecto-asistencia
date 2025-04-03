<template>
  <div class="dashboard-container">
    <header class="dashboard-header">
      <h1>Panel de control</h1>
      <div class="user-section">
        <span class="welcome-text">Bienvenido, {{ user.name }}</span>
        <button @click="logout" class="btn-logout">Cerrar sesión</button>
      </div>
    </header>

    <div class="dashboard-content">
      <aside class="sidebar">
        <nav class="navigation">
          <ul>
            <li @click="activeTab = 'overview'" :class="{ active: activeTab === 'overview' }">
              <span class="icon">📊</span> Resumen general
            </li>
            <li @click="activeTab = 'attendance'" :class="{ active: activeTab === 'attendance' }">
              <span class="icon">📈</span> Asistencia
            </li>
            <li @click="activeTab = 'reports'" :class="{ active: activeTab === 'reports' }">
              <span class="icon">📑</span> Informes
            </li>
            <li @click="activeTab = 'settings'" :class="{ active: activeTab === 'settings' }">
              <span class="icon">⚙️</span> Configuración
            </li>
          </ul>
        </nav>
      </aside>

      <main class="main-content">
        <!-- Sección de filtros y controles generales -->
        <div class="controls-section">
          <div class="date-filter">
            <label>Período:</label>
            <select v-model="selectedPeriod">
              <option value="7days">Últimos 7 días</option>
              <option value="30days">Últimos 30 días</option>
              <option value="90days">Últimos 90 días</option>
              <option value="custom">Personalizado</option>
            </select>
          </div>
          
          <button class="btn-refresh" @click="refreshData">
            Actualizar datos
          </button>
        </div>

        <!-- Componente dinámico según la pestaña activa -->
        <div v-if="activeTab === 'overview'" class="overview-section">
          <h2>Resumen general</h2>
          <div class="metrics-grid">
            <div class="metric-card">
              <h3>Estudiantes activos</h3>
              <div class="metric-value">1,483</div>
              <div class="metric-change positive">+5.2%</div>
            </div>
            <div class="metric-card">
              <h3>Asistencia general</h3>
              <div class="metric-value">88.7%</div>
              <div class="metric-change positive">+1.3%</div>
            </div>
            <div class="metric-card">
              <h3>Cursos activos</h3>
              <div class="metric-value">42</div>
              <div class="metric-change neutral">0%</div>
            </div>
            <div class="metric-card">
              <h3>Ausencias justificadas</h3>
              <div class="metric-value">12.4%</div>
              <div class="metric-change negative">+0.7%</div>
            </div>
          </div>
        </div>

        <div v-else-if="activeTab === 'attendance'" class="attendance-section">
          <h2>Registro de Asistencia</h2>
          
          <!-- Aquí insertamos el componente de mapa de calor de asistencia -->
          <AttendanceHeatmap />
          
          <div class="insights-section">
            <h3>Estadísticas</h3>
            <ul class="insights-list">
              <li>El curso CS101 tiene la mejor tasa de asistencia (92%).</li>
              <li>Los lunes muestran la tasa de asistencia más baja de la semana (82%).</li>
              <li>El 15% de las ausencias están justificadas con documentación médica.</li>
              <li>La asistencia disminuye aproximadamente un 5% después de periodos vacacionales.</li>
            </ul>
          </div>
        </div>

        <div v-else-if="activeTab === 'reports'" class="reports-section">
          <h2>Informes</h2>
          <div class="reports-list">
            <p>Esta sección contendrá los informes generados por el sistema.</p>
          </div>
        </div>

        <div v-else-if="activeTab === 'settings'" class="settings-section">
          <h2>Configuración</h2>
          <div class="settings-form">
            <p>Opciones de configuración del panel</p>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import AttendanceHeatmap from '@/components/AttendanceHeatmap.vue';

export default {
  name: 'DashboardView',
  components: {
    AttendanceHeatmap
  },
  data() {
    return {
      activeTab: 'overview',
      selectedPeriod: '30days',
      user: {
        name: 'Usuario Demo',
        email: 'usuario@ejemplo.com'
      },
      // Podemos mantener estos datos para compatibilidad o eliminarlos si no se usan
      attendanceData: [
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
    }
  },
  methods: {
    logout() {
      // Implementar lógica de cierre de sesión
      // Por ejemplo: this.$store.dispatch('auth/logout');
      this.$router.push('/login');
    },
    refreshData() {
      // Simulación de actualización de datos
      alert('Actualizando datos...');
      // Aquí iría la lógica para obtener nuevos datos
    }
  }
}
</script>

<style scoped>
.dashboard-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f9fafc;
}

.dashboard-header {
  background-color: #4a6cf7;
  color: white;
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dashboard-header h1 {
  font-size: 1.5rem;
  margin: 0;
}

.user-section {
  display: flex;
  align-items: center;
  gap: 15px;
}

.welcome-text {
  font-weight: 500;
}

.btn-logout {
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-logout:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

.dashboard-content {
  flex: 1;
  display: flex;
}

.sidebar {
  width: 240px;
  background-color: white;
  box-shadow: 2px 0 5px rgba(0,0,0,0.05);
}

.navigation ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.navigation li {
  padding: 15px 20px;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: background-color 0.2s;
}

.navigation li:hover {
  background-color: #f5f7ff;
}

.navigation li.active {
  background-color: #eef2ff;
  color: #4a6cf7;
  border-left: 3px solid #4a6cf7;
}

.icon {
  margin-right: 10px;
}

.main-content {
  flex: 1;
  padding: 25px;
  overflow-y: auto;
}

.controls-section {
  display: flex;
  justify-content: space-between;
  margin-bottom: 25px;
  background-color: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.date-filter {
  display: flex;
  align-items: center;
  gap: 10px;
}

.date-filter select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: white;
}

.btn-refresh {
  background-color: #4a6cf7;
  color: white;
  border: none;
  padding: 8px 15px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-refresh:hover {
  background-color: #3a5ce5;
}

h2 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #333;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.metric-card {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.metric-card h3 {
  margin-top: 0;
  margin-bottom: 15px;
  font-size: 1rem;
  color: #666;
}

.metric-value {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 10px;
}

.metric-change {
  font-size: 0.9rem;
  font-weight: 500;
}

.positive {
  color: #4caf50;
}

.negative {
  color: #f44336;
}

.neutral {
  color: #9e9e9e;
}

.attendance-section, .reports-section, .settings-section {
  background-color: white;
  border-radius: 8px;
  padding: 25px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.insights-section {
  margin-top: 30px;
}

.insights-list {
  padding-left: 20px;
  line-height: 1.6;
}

.insights-list li {
  margin-bottom: 8px;
}

@media (max-width: 768px) {
  .dashboard-content {
    flex-direction: column;
  }
  
  .sidebar {
    width: 100%;
  }
  
  .metrics-grid {
    grid-template-columns: 1fr;
  }
}
</style>