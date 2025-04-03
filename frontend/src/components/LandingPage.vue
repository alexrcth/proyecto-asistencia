<template>
    <div class="landing-container">
      <!-- Header / Hero Section -->
      <section class="hero-section">
        <div class="hero-content">
          <img src="@/assets/logo.png" alt="UEES" class="logo" v-if="false">
          <h1 class="hero-title">Sistema de Control de Asistencia</h1>
          <p class="hero-subtitle">Gestión eficiente de asistencia para estudiantes y docentes universitarios</p>
          <div class="hero-buttons">
            <router-link to="/login" class="btn btn-primary">Iniciar sesión</router-link>
            <router-link to="/about" class="btn btn-secondary">Conoce más</router-link>
          </div>
        </div>
      </section>
  
      <!-- Features Section -->
      <section class="features-section">
        <h2 class="section-title">Características principales</h2>
        
        <div class="features-grid">
          <!-- Feature 1 -->
          <div class="feature-card">
            <div class="feature-icon">
              <i class="feature-check">✓</i>
            </div>
            <h3 class="feature-title">Registro simplificado</h3>
            <p class="feature-description">Toma de asistencia rápida y sencilla para profesores y estudiantes</p>
          </div>
          
          <!-- Feature 2 -->
          <div class="feature-card">
            <div class="feature-icon reports">
              <i class="feature-chart">📊</i>
            </div>
            <h3 class="feature-title">Reportes detallados</h3>
            <p class="feature-description">Visualiza estadísticas de asistencia por curso, carrera o facultad</p>
          </div>
          
          <!-- Feature 3 -->
          <div class="feature-card">
            <div class="feature-icon mobile">
              <i class="feature-phone">📱</i>
            </div>
            <h3 class="feature-title">Acceso móvil</h3>
            <p class="feature-description">Registra asistencia desde cualquier dispositivo, en cualquier momento</p>
          </div>
          
          <!-- Feature 4 -->
          <div class="feature-card">
            <div class="feature-icon notifications">
              <i class="feature-bell">🔔</i>
            </div>
            <h3 class="feature-title">Notificaciones</h3>
            <p class="feature-description">Alertas automáticas sobre inasistencias y umbrales críticos</p>
          </div>
        </div>
      </section>
  
      <!-- Optional: Testimonials or Benefits Section -->
      <section class="benefits-section">
        <div class="benefits-content">
          <h2 class="section-title">Beneficios para tu institución</h2>
          <div class="benefits-grid">
            <div class="benefit-item">
              <h3>Ahorro de tiempo</h3>
              <p>Reduce hasta un 70% el tiempo dedicado a la gestión de asistencia</p>
            </div>
            <div class="benefit-item">
              <h3>Mayor precisión</h3>
              <p>Elimina errores humanos en el registro y cálculo de asistencia</p>
            </div>
            <div class="benefit-item">
              <h3>Mejor seguimiento</h3>
              <p>Identifica tendencias y patrones para mejorar la retención estudiantil</p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Footer -->
      <footer class="landing-footer">
        <div class="footer-content">
          <p>&copy; 2025 Sistema de Control de Asistencia</p>
          <div class="footer-links">
            <a href="#">Términos de servicio</a>
            <a href="#">Política de privacidad</a>
            <a href="#">Contacto</a>
          </div>
        </div>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LandingPage',
    data() {
      return {
        // Datos si son necesarios
      }
    },
    methods: {
      // Métodos si son necesarios
    }
  }
  </script>
  
  <style scoped>
  .landing-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  
  /* Hero Section */
  .hero-section {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 5rem 2rem;
    background-image: linear-gradient(rgba(44, 62, 80, 0.9), rgba(44, 62, 80, 0.9));
    background-size: cover;
    background-position: center;
  }
  
  .logo {
    height: 40px;
    margin-bottom: 1.5rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    font-weight: 700;
  }
  
  .hero-subtitle {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .hero-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
  }
  
  .btn {
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
  }
  
  .btn-primary {
    background-color: #f39c12;
    color: white;
  }
  
  .btn-primary:hover {
    background-color: #e67e22;
  }
  
  .btn-secondary {
    background-color: transparent;
    color: white;
    border: 2px solid white;
  }
  
  .btn-secondary:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
  
  /* Features Section */
  .features-section {
    padding: 5rem 2rem;
    background-color: #f9f9f9;
  }
  
  .section-title {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 3rem;
    color: #333;
  }
  
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .feature-card {
    background-color: white;
    border-radius: 8px;
    padding: 2rem;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    text-align: center;
    transition: transform 0.3s ease;
  }
  
  .feature-card:hover {
    transform: translateY(-5px);
  }
  
  .feature-icon {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #e3f2fd;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    font-size: 1.5rem;
  }
  
  /* Customize icon backgrounds */
  .feature-icon.reports {
    background-color: #e8f5e9;
  }
  
  .feature-icon.mobile {
    background-color: #fff3e0;
  }
  
  .feature-icon.notifications {
    background-color: #fff8e1;
  }
  
  .feature-title {
    font-size: 1.2rem;
    margin-bottom: 1rem;
    color: #333;
  }
  
  .feature-description {
    color: #666;
    line-height: 1.6;
  }
  
  /* Benefits Section */
  .benefits-section {
    padding: 5rem 2rem;
    background-color: white;
  }
  
  .benefits-content {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }
  
  .benefit-item {
    padding: 1.5rem;
    border-left: 4px solid #4a6cf7;
    background-color: #f9f9f9;
  }
  
  .benefit-item h3 {
    margin-top: 0;
    color: #333;
    margin-bottom: 0.5rem;
  }
  
  .benefit-item p {
    color: #666;
    line-height: 1.6;
  }
  
  /* Footer */
  .landing-footer {
    background-color: #2c3e50;
    color: white;
    padding: 2rem;
    margin-top: auto;
  }
  
  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
  }
  
  .footer-links {
    display: flex;
    gap: 1.5rem;
  }
  
  .footer-links a {
    color: #ccc;
    text-decoration: none;
    transition: color 0.3s ease;
  }
  
  .footer-links a:hover {
    color: white;
  }
  
  /* Responsive Adjustments */
  @media (max-width: 768px) {
    .hero-title {
      font-size: 2rem;
    }
    
    .hero-subtitle {
      font-size: 1rem;
    }
    
    .footer-content {
      flex-direction: column;
      text-align: center;
    }
    
    .footer-links {
      margin-top: 1rem;
      justify-content: center;
    }
  }
  </style>