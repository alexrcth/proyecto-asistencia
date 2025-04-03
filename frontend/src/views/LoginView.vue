<template>
  <div class="login-container">
    <div class="login-form-box">
      <div class="login-border-glow"></div>
      <div class="login-form-content">
        <div class="login-header">
          <div class="logo-circle">
            <div class="uees-logo">
              <div class="logo-cross"></div>
              <div class="logo-letters">UEES</div>
            </div>
          </div>
    
          <p>Universidad Evangélica de El Salvador</p>
        </div>

        <form @submit.prevent="handleLogin" class="login-form">
          <div class="form-group">
            <label for="cif">CIF</label>
            <div class="input-wrapper">
              <span class="input-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="user-icon">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </span>
              <input 
                type="text" 
                id="cif" 
                v-model="email" 
                placeholder="Introduce tu CIF" 
                required
                class="form-input"
              >
            </div>
          </div>
          
          <div class="form-group">
            <label for="password">Contraseña</label>
            <div class="input-wrapper">
              <span class="input-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lock-icon">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </span>
              <input 
                :type="showPassword ? 'text' : 'password'" 
                id="password" 
                v-model="password" 
                placeholder="Introduce tu contraseña" 
                required
                class="form-input"
              >
              <button 
                type="button" 
                @click="togglePassword" 
                class="password-toggle"
                tabindex="-1"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="eye-icon">
                  <path v-if="!showPassword" d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle v-if="!showPassword" cx="12" cy="12" r="3"></circle>
                  <path v-if="showPassword" d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                  <line v-if="showPassword" x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
              </button>
            </div>
          </div>
          
          <div class="form-options">
            <div class="remember-me">
              <input type="checkbox" id="remember" v-model="rememberMe">
              <label for="remember">Recordarme</label>
            </div>
            <a href="#" class="forgot-link">¿Olvidaste tu contraseña?</a>
          </div>
          
          <button type="submit" class="btn-login" :class="{ 'is-loading': isLoading }">
            <span class="btn-text">{{ isLoading ? 'Iniciando sesión...' : 'Iniciar sesión' }}</span>
            <span class="btn-loader" v-if="isLoading"></span>
          </button>
          
          <div v-if="errorMessage" class="error-message">
            <span class="error-icon">⚠️</span> {{ errorMessage }}
          </div>
        </form>
        
        <div class="login-footer">
          <p>¿No tienes una cuenta? <a href="#" @click.prevent="contactAdmin">Contacta a tu administrador</a></p>
          <router-link to="/" class="back-link">
            <span class="back-icon"></span> Volver a la página principal
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      rememberMe: false,
      showPassword: false,
      isLoading: false,
      errorMessage: ''
    };
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    async handleLogin() {
      this.isLoading = true;
      this.errorMessage = '';
      
      try {
        // Simulamos un retraso para la demostración
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Demo: acepta cualquier correo con contraseña "demo123"
        if (this.password === 'demo123') {
          // Login exitoso - guardar token/usuario en el store o localStorage
          localStorage.setItem('isAuthenticated', 'true');
          localStorage.setItem('user', JSON.stringify({
            name: 'Usuario Demo',
            email: this.email,
            role: 'admin'
          }));
          
          // Redirigir al dashboard
          this.$router.push('/dashboard');
        } else {
          this.errorMessage = 'Credenciales incorrectas. Intenta nuevamente.';
        }
      } catch (error) {
        this.errorMessage = 'Error al iniciar sesión. Por favor, intenta nuevamente.';
        console.error('Error de login:', error);
      } finally {
        this.isLoading = false;
      }
    },
    contactAdmin() {
      alert('Para solicitar una cuenta, contacta al administrador del sistema en: admin@ejemplo.com');
    }
  }
};
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

/* Formulario con borde neón giratorio */
.login-form-box {
  position: relative;
  width: 420px;
  border-radius: 10px;
  background: #003087; /* Azul UEES */
  overflow: hidden;
  z-index: 10;
}

/* Efecto del borde neón giratorio */
.login-border-glow {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: conic-gradient(
    from var(--angle),
    #21a700,
    #FFD700, /* Dorado/amarillo UEES */
    #FFD700,
    #FFD700,
    #003087
  );
  border-radius: 10px;
  z-index: 1;
  animation: rotate 4s linear infinite;
}

@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@keyframes rotate {
  0% {
    --angle: 0deg;
  }
  100% {
    --angle: 360deg;
  }
}

/* Contenido del formulario */
.login-form-content {
  position: relative;
  background: #003087;
  border-radius: 8px;
  margin: 3px;
  padding: 40px 30px;
  z-index: 2;
  color: rgb(255, 255, 255);
}

.login-header {
  text-align: center;
  margin-bottom: 30px;
}

.logo-circle {
  width: 140px;
  height: 140px;
  background: #FFD700; /* Fondo amarillo del logo */
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  box-shadow: 0 5px 20px rgba(0, 48, 135, 0.4);
  position: relative;
  overflow: hidden;
}

/* Logo UEES */
.uees-logo {
  position: relative;
  width: 100px;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-cross {
  position: absolute;
  width: 50px;
  height: 70px;
  background: transparent;
  border: 4px solid #003087;
  right: 10px;
  top: 15px;
}

.logo-cross::before {
  content: '';
  position: absolute;
  width: 38px;
  height: 4px;
  background-color: #003087;
  top: 25px;
  left: -18px;
}

.logo-letters {
  position: absolute;
  bottom: 20px;
  left: 10px;
  font-size: 24px;
  font-weight: bold;
  color: #003087;
  letter-spacing: -2px;
}

.login-header h2 {
  font-size: 28px;
  margin: 0 0 10px 0;
  color: white;
}

.login-header p {
  font-size: 14px;
  color: #ccc;
  margin: 0;
}

.login-form {
  margin-top: 30px;
}

.form-group {
  margin-bottom: 25px;
}

.form-group label {
  display: block;
  margin-bottom: 10px;
  font-weight: 500;
  color: #ffffff;
  font-size: 14px;
}

.input-wrapper {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #ccc;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-icon, .lock-icon, .eye-icon {
  color: #ccc;
}

.form-input {
  width: 100%;
  padding: 15px 15px 15px 45px;
  background-color: #00246e;
  border: 1px solid #001c54;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.3s;
  color: white;
}

.form-input::placeholder {
  color: #7a8dc6;
}

.form-input:focus {
  border-color: #FFD700;
  outline: none;
  box-shadow: 0 0 0 3px rgba(255, 215, 0, 0.2);
}

.password-toggle {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #ccc;
  cursor: pointer;
  font-size: 16px;
  transition: color 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.password-toggle:hover {
  color: #ffffff;
}

.password-toggle:hover .eye-icon {
  color: #ffffff;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  font-size: 13px;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 8px;
}

.remember-me input[type="checkbox"] {
  accent-color: #FFD700;
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.forgot-link {
  color: #FFD700;
  text-decoration: none;
  transition: color 0.2s;
}

.forgot-link:hover {
  color: #FFC107;
  text-decoration: underline;
}

.btn-login {
  width: 100%;
  padding: 14px;
  background: #FFD700;
  color: #003087;
  border: none;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
  margin-bottom: 20px;
}

.btn-login:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
  background: #FFC107;
}

.btn-login:active {
  transform: translateY(0);
}

.btn-login.is-loading .btn-text {
  opacity: 0.7;
}

.btn-loader {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid rgba(0, 48, 135, 0.3);
  border-radius: 50%;
  border-top-color: #003087;
  animation: spin 1s infinite linear;
  top: 50%;
  left: calc(50% - 30px);
  transform: translateY(-50%);
}

@keyframes spin {
  0% { transform: translateY(-50%) rotate(0deg); }
  100% { transform: translateY(-50%) rotate(360deg); }
}

.error-message {
  padding: 12px;
  background-color: rgba(229, 62, 62, 0.1);
  color: #a01d1d;
  border-left: 3px solid #a01d1d;
  border-radius: 4px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  font-size: 13px;
  animation: shake 0.5s ease-in-out;
}

.error-icon {
  margin-right: 10px;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
  20%, 40%, 60%, 80% { transform: translateX(5px); }
}

.login-footer {
  margin-top: 30px;
  text-align: center;
  color: #ccc;
  font-size: 13px;
}

.login-footer a {
  color: #FFD700;
  text-decoration: none;
  transition: color 0.2s;
}

.login-footer a:hover {
  color: #FFC107;
  text-decoration: underline;
}

.back-link {
  display: inline-flex;
  align-items: center;
  margin-top: 15px;
}

.back-icon {
  margin-right: 5px;
  transition: transform 0.3s;
}

.back-link:hover .back-icon {
  transform: translateX(-3px);
}

.error-message {
  padding: 12px;
  background-color: rgba(229, 62, 62, 0.1);
  color: #ff6b6b;
  border-left: 3px solid #ff6b6b;
  border-radius: 4px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  font-size: 13px;
  animation: shake 0.5s ease-in-out;
}

.error-icon {
  margin-right: 10px;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
  20%, 40%, 60%, 80% { transform: translateX(5px); }
}

.login-footer {
  margin-top: 30px;
  text-align: center;
  color: #ccc;
  font-size: 13px;
}

.login-footer a {
  color: #FFD700;
  text-decoration: none;
  transition: color 0.2s;
}

.login-footer a:hover {
  color: #FFC107;
  text-decoration: underline;
}

.back-link {
  display: inline-flex;
  align-items: center;
  margin-top: 15px;
}

.back-icon {
  margin-right: 5px;
  transition: transform 0.3s;
}

.back-link:hover .back-icon {
  transform: translateX(-3px);
}
</style>