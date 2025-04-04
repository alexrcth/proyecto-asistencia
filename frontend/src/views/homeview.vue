<template>
    <div class="home-container">
      <header class="hero">
        <div class="logo-container">
          <!-- Espacio para el logo de la universidad -->
          <div class="uees">
            <img src="/img/uees.png" alt="uees" />
          </div>
        </div>
        
        <div class="hero-content">
          <h1>Sistema de Control de Asistencia</h1>
          <p>Gestión eficiente de asistencia para estudiantes y docentes universitarios</p>
          <div class="cta-buttons">
            <button @click="$router.push('/login')" class="btn-primary">Ingresar</button>
            <button @click="scrollToFeatures" class="btn-secondary">Conoce más</button>
          </div>
        </div>
      </header>
  
      <section id="features" class="features">
        <h2>Características principales</h2>
        
        <div class="feature-grid">
          <div class="feature-card">
            <div class="feature-icon">✓</div>
            <h3>Registro simplificado</h3>
            <p>Toma de asistencia rápida y sencilla para profesores y estudiantes</p>
          </div>
          
          <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Reportes detallados</h3>
            <p>Visualiza estadísticas de asistencia por curso, carrera o facultad</p>
          </div>
          
          <div class="feature-card">
            <div class="feature-icon">📱</div>
            <h3>Acceso móvil</h3>
            <p>Registra asistencia desde cualquier dispositivo, en cualquier momento</p>
          </div>
          
          <div class="feature-card">
            <div class="feature-icon">🔔</div>
            <h3>Notificaciones</h3>
            <p>Alertas automáticas sobre inasistencias y umbrales críticos</p>
          </div>
        </div>
      </section>
  
      <section class="benefits">
        <h2>Beneficios para la comunidad universitaria</h2>
        
        <div class="benefits-container">
          <div class="benefit-column">
            <h3>Para docentes</h3>
            <ul>
              <li>Ahorro de tiempo en tareas administrativas</li>
              <li>Seguimiento automático de la asistencia</li>
              <li>Identificación temprana de estudiantes en riesgo</li>
              <li>Generación de reportes para coordinación académica</li>
            </ul>
          </div>
          
          <div class="benefit-column">
            <h3>Para estudiantes</h3>
            <ul>
              <li>Registro transparente de asistencias</li>
              <li>Consulta de estado de asistencia en tiempo real</li>
              <li>Justificación digital de inasistencias</li>
              <li>Alertas preventivas sobre porcentajes mínimos</li>
            </ul>
          </div>
          
          <div class="benefit-column">
            <h3>Para la institución</h3>
            <ul>
              <li>Reducción de carga administrativa</li>
              <li>Datos precisos para toma de decisiones</li>
              <li>Mayor retención estudiantil</li>
              <li>Optimización de recursos educativos</li>
            </ul>
          </div>
        </div>
      </section>
  
      <footer class="footer">
        <p>&copy; 2025 Sistema de Control de Asistencia Universitaria. Todos los derechos reservados.</p>
      </footer>
    </div>
  </template>
  
  <script>

  export default {
    name: 'HomeView',
    methods: {
      scrollToFeatures() {
        document.getElementById('features').scrollIntoView({ 
          behavior: 'smooth' 
        });
      }
    }
  }
  </script>
  
  <style scoped>
  .home-container {
    color: #f2ae35;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  
  .hero {
    background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
    color: white;
    padding: 60px 20px 100px;
    text-align: center;
    position: relative;
  }
  
  .logo-container {
    margin-bottom: 20;
  }
  
  .university-logo {
    display: inline-block;
    padding: 50px;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  .university-logo img {
    max-height: 100px;
    max-width: 200px;
  }
  
  .hero-content {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .hero h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
  }
  
  .hero p {
    font-size: 1.2rem;
    margin-bottom: 30px;
    opacity: 0.9;
  }
  
  .cta-buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
  }
  
  .btn-primary, .btn-secondary {
    padding: 12px 25px;
    border-radius: 5px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .btn-primary {
    background-color: #f2ae35;
    color: white;
    border: none;
  }
  
  .btn-primary:hover {
    background-color: #f7bb54;
    transform: translateY(-2px);
  }
  
  .btn-secondary {
    background-color: transparent;
    color: white;
    border: 2px solid white;
  }
  
  .btn-secondary:hover {
    background-color: rgba(255, 255, 255, 0.1);
    transform: translateY(-2px);
  }
  
  .features {
    padding: 80px 20px;
    background-color: #f9f9f9;
    text-align: center;
    margin-top: -40px;
  }
  
  .features h2, .benefits h2 {
    font-size: 2rem;
    margin-bottom: 50px;
    color: #333;
  }
  
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .feature-card {
    background-color: white;
    border-radius: 8px;
    padding: 30px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  }
  
  .feature-icon {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: #043e58;
  }
  
  .feature-card h3 {
    font-size: 1.3rem;
    margin-bottom: 15px;
    color: #444;
  }
  
  .benefits {
    padding: 80px 20px;
    text-align: center;
    background-color: white;
  }
  
  .benefits-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    margin-bottom: 50px;
  }
  
  .benefit-column {
    flex: 1;
    min-width: 300px;
    max-width: 400px;
    text-align: left;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 8px;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
  }
  
  .benefit-column h3 {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  
  .benefit-column ul {
    padding-left: 20px;
    line-height: 1.8;
    color: #555;
  }
  
  .benefit-column li {
    margin-bottom: 10px;
  }
  
  .action-section {
    margin-top: 40px;
  }
  
  .footer {
    background-color: #2c3e50;
    padding: 30px;
    text-align: center;
    color: #ecf0f1;
  }
  
  @media (max-width: 768px) {
    .hero h1 {
      font-size: 2rem;
    }
    
    .features h2, .benefits h2 {
      font-size: 1.8rem;
    }
    
    .benefits-container {
      flex-direction: column;
      align-items: center;
    }
    
    .benefit-column {
      width: 100%;
    }
  }
  </style>