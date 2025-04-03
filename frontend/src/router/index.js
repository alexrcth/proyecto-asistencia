import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/homeview.vue'
import LoginView from '../views/LoginView.vue';
import DashboardView from '../views/dashboardview.vue'
import MarkAttendanceView from '../components/Attendance/MarkAttendance.vue';
import GenerateCodeView from '../components/Attendance/GenerateCode.vue';
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView,
    meta: { requiresAuth: true }
  },
  {
    path: '/mark-attendance',
    name: 'mark-attendance',
    component: MarkAttendanceView,
    meta: { requiresAuth: true }
  },
  {
    path: '/generate-code',
    name: 'generate-code',
    component: GenerateCodeView,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Navegación protegida
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token')
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router