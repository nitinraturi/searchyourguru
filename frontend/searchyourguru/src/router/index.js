import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Verification from '../views/Verification.vue'
import PasswordReset from '../views/PasswordReset.vue'
import Dashboard from '../views/Dashboard.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login/',
    name: 'login',
    component: Login
  },
  {
    path: '/signup/',
    name: 'signup',
    component: Signup
  },
  {
    path: '/verification/',
    name: 'verification',
    component: Verification
  },
  {
    path: '/password-reset/',
    name: 'password_reset',
    component: PasswordReset
  },
  {
    path: '/dashboard/',
    name: 'dashboard',
    component: Dashboard
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
