import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import Login from './components/Login.vue'
import Home from './components/Home.vue'
import Mision from './components/Mision.vue'
import Donaciones from './components/Donaciones.vue'
import Adopcion from './components/Adopcion.vue'
import Administrador from './components/Administrador.vue'
import Administrador_solicitudes from './components/Administrador_solicitudes.vue'
import Formulario_adopcion from './components/Formulario_adopcion.vue'
import Estado_solicitud from './components/Estado_solicitud.vue'

const routes = [
  {
    path: '/',
    name: 'root',
    component: Home
  },

  {
    path: '/login',
    name: 'Login',
    component: Login
  },

  {
    path: '/home',
    name: 'Home',
    component: Home
  },

  {
    path: '/mision',
    name: 'Mision',
    component: Mision
  },

  {
    path:'/donaciones',
    name:'Donaciones',
    component: Donaciones
  },  

  {
    path:'/adopcion',
    name: 'Adopcion',
    component: Adopcion
  },

  {
    path:'/administrador',
    name: 'Administrador',
    component: Administrador
  },

  {
    path:'/admin_solicitudes',
    name:'Administrador_solicitudes',
    component: Administrador_solicitudes
  },

  {
    path:'/formulario_adopcion',
    name: 'Formulario_adopcion',
    component: Formulario_adopcion
  }, 

  
  {
    path:'/estado_solicitud',
    name: 'Estado_solicitud',
    component: Estado_solicitud
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
