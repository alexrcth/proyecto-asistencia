<!-- src/views/AttendanceView.vue -->
<template>
  <div class="attendance-view">
    <h1>Marcar Asistencia</h1>
    <label for="codigo">Código de acceso:</label>
    <input id="codigo" v-model="codigo" placeholder="Ingrese el código" />

    <label for="curso">ID del Curso:</label>
    <input id="curso" v-model="cursoId" placeholder="Ingrese el ID del curso" />

    <button @click="enviarAsistencia">Enviar</button>

    <div v-if="resultado">
      <p>Presente: {{ resultado.attendance.is_present ? 'Sí' : 'No' }}</p>
      <p>Nueva clave generada: {{ resultado.new_access_code }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { marcarAsistencia } from '@/services/attendance.service';

const codigo = ref('');
const cursoId = ref('');
const resultado = ref(null);

const obtenerUbicacion = () => {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      reject("Geolocalización no disponible");
    }
    navigator.geolocation.getCurrentPosition(
      position => {
        resolve({
          latitude: position.coords.latitude,
          longitude: position.coords.longitude
        });
      },
      err => reject(err.message)
    );
  });
};

const enviarAsistencia = async () => {
  try {
    const { latitude, longitude } = await obtenerUbicacion();
    const data = await marcarAsistencia(cursoId.value, codigo.value, latitude, longitude);
    resultado.value = data;
  } catch (error) {
    alert("Error al marcar asistencia: " + error.message);
  }
};
</script>

<style scoped>
.attendance-view {
  max-width: 400px;
  margin: auto;
}
input {
  display: block;
  margin-bottom: 10px;
}
button {
  margin-top: 10px;
}
</style>
