import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Verification from '../views/Verification.vue'
import PasswordReset from '../views/PasswordReset.vue'
import Dashboard from '../views/Dashboard.vue'
import Search from '../views/Search.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    beforeEnter(to, from, next) {
      if (store.getters.is_user_tutor) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/search/',
    name: 'search',
    component: Search,
    beforeEnter(to, from, next) {
      if (store.getters.is_user_tutor) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/login/',
    name: 'login',
    component: Login,
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/signup/',
    name: 'signup',
    component: Signup,
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/verification/',
    name: 'verification',
    component: Verification,
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/password-reset/',
    name: 'password_reset',
    component: PasswordReset,
    beforeEnter(to, from, next) {
      if (store.getters.is_loggedin) next('/dashboard/')
      else next()
    }
  },
  {
    path: '/dashboard/',
    name: 'dashboard',
    component: Dashboard,
    beforeEnter(to, from, next) {
      if (!store.getters.is_loggedin) next('/login/')
      else next()
    }
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
