<template>
  <div class="login-container">
    <div class="loading-circle"></div> 
    <div class="login-box">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label>CIF</label>
          <input type="cif" v-model="email" required />
        </div>
        <div class="input-group">
          <label>Password</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit" class="login-button">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      cif: "",
      password: "",
    };
  },
  methods: {
    handleLogin() {
      console.log("Iniciar sesión con:", this.email, this.password);
    },
  },
};
</script>

<style scoped>
/* Contenedor general */
.login-container {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #0b1b2e;
}

/* Círculo de carga */
.loading-circle {
  position: absolute;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  border: 8px solid rgba(0, 255, 255, 0.2);
  border-top-color: #00ffff;
  animation: spin 2s linear infinite;
}

/* Cuadro de login */
.login-box {
  position: absolute;
  width: 250px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  backdrop-filter: blur(10px);
  text-align: center;
  color: white;
  box-shadow: 0 0 15px rgba(0, 255, 255, 0.4);
}

/* Estilo de inputs */
.input-group {
  margin-bottom: 15px;
  text-align: left;
}

.input-group label {
  font-size: 14px;
}

.input-group input {
  width: 100%;
  padding: 8px;
  border-radius: 5px;
  border: none;
  outline: none;
  margin-top: 5px;
}

/* Botón de login */
.login-button {
  width: 100%;
  padding: 10px;
  background: #00ffff;
  border: none;
  color: black;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.login-button:hover {
  background: #00cccc;
}

/* Animación del círculo */
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
